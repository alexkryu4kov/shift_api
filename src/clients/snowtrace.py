import asyncio
import json
import logging
import os

from aiohttp import ClientSession


class NoSnowtraceTokenException(Exception):
    """Исключение, которое вызывается в случае если АПИ токен не добавлен в переменные окружения."""


class SnowtraceClient:

    def __init__(self, session: ClientSession):
        try:
            self._token = os.environ['SNOWTRACE_TOKEN']
        except KeyError:
            logging.error('No snowtrace api token set up!')
            raise NoSnowtraceTokenException('No snowtrace api token set up!')
        self._session = session

    async def get_events(self, block_number: str) -> list[dict]:
        raw_abi = await self._get_raw_abi(block_number)
        logging.info(f'raw_abi: {raw_abi}')
        abi = json.loads(raw_abi['result'])
        return [ans for ans in abi if ans.get('type') == 'event']

    async def _get_raw_abi(self, block_number: str) -> dict:
        resp = await self._session.get(
            f'https://api.snowtrace.io/api?module=contract&action=getabi&address={block_number}&apikey={self._token}',
        )
        return await resp.json()

    def __del__(self):
        """Переопределение магического метода для закрытия aiohttp сессии."""
        try:
            asyncio.create_task(self._close_session())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(self._close_session())

    async def _close_session(self):
        if not self._session.closed:
            await self._session.close()
