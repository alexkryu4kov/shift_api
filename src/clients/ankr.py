from web3 import Web3, AsyncHTTPProvider
from web3.eth import AsyncEth


class AnkrClient:

    def __init__(self, blockchain_type='avalanche'):
        self.web3_client = Web3(
            AsyncHTTPProvider(
                f'https://rpc.ankr.com/{blockchain_type}'
            ),
            modules={'eth': (AsyncEth,)},
            middlewares=[],
        )

    async def get_balance(self, address: str, block_number: str) -> int:
        return await self.web3_client.eth.get_balance(address, block_number)
