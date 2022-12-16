from unittest.mock import AsyncMock

from src.clients.ankr import AnkrClient


async def test_ankr_client(monkeypatch):
    client = AnkrClient()
    with monkeypatch.context() as m:
        m.setattr(
            client.web3_client.eth,
            'get_balance',
            AsyncMock(return_value=0),
        )
        assert await client.get_balance('address', 'block_number') == 0
