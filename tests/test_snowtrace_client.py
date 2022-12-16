from unittest.mock import AsyncMock

from src.clients.snowtrace import SnowtraceClient


class MockClientSession:

    @property
    def closed(self):
        return True


async def test_snowtrace_client(monkeypatch):
    monkeypatch.setenv('SNOWTRACE_TOKEN', 'test')
    client = SnowtraceClient(MockClientSession())
    with monkeypatch.context() as m:
        m.setattr(
            client,
            '_get_raw_abi',
            AsyncMock(return_value={'result': '[{}]'}),
        )
        assert await client.get_events('block_number') == []
