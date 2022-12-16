from pydantic import BaseModel, Field


class EventsRequest(BaseModel):
    """Параметры запроса для получения событий из блока."""

    block_number: str = Field(
        ...,
        description='Номер блока для расчета',
        example='latest',
    )


class EventModel(BaseModel):
    """Модель события, полученного из блока."""

    anonymous: bool = Field(
        ...,
    )

    inputs: list[dict] = Field(  # модель для inputs не описана, так как смысл полей не совсем понятен:)
        ...,
    )

    name: str = Field(
        ...,
    )


class EventsResponse(BaseModel):
    """Модель ответа, которая содержит в себе набор событий."""

    events: list[EventModel] = Field(
        ...,
        description='Номер блока для расчета',
    )


