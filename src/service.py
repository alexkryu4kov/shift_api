import logging

from aiohttp import ClientSession
from fastapi import FastAPI
import uvicorn

from src.clients.ankr import AnkrClient
from src.clients.snowtrace import SnowtraceClient
from src.models.balance import BalanceRequest, BalanceResponse
from src.models.events import EventModel, EventsRequest, EventsResponse

logger = logging.getLogger('app')

app = FastAPI()

ankr_client = AnkrClient(blockchain_type='avalanche')

session = ClientSession()
snowtrace_client = SnowtraceClient(session)


@app.post('/balance')
async def test_balance_handler(request: BalanceRequest):
    return BalanceResponse(
        balance=await ankr_client.get_balance(
            address=request.address,
            block_number=request.block_number,
        ),
    )


@app.post('/events')
async def test_events_handler(request: EventsRequest):
    events = await snowtrace_client.get_events(request.block_number)
    logging.info(f'raw events: {events}')
    return EventsResponse(
        events=[
            EventModel(
                anonymous=event.get('anonymous', False),
                inputs=event.get('inputs'),
                name=event.get('name', ''),
            )
            for event
            in events
        ]
    )


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
