from pydantic import BaseModel, Field


class BalanceRequest(BaseModel):
    """Запрос баланса для нужного кошелька."""

    address: str = Field(
        ...,
        description='Адрес кошелька',
        regex='^(0x)[a-zA-Z0-9]{40}$',
        example='0x66357dCaCe80431aee0A7507e2E361B7e2402370',
    )

    block_number: str = Field(
        ...,
        description='Номер блока для расчета',
        example='latest',
    )


class BalanceResponse(BaseModel):
    """Ответ на запрос баланса из кошелька."""

    balance: int = Field(
        ...,
        description='Баланс на запрошенном кошельке',
    )
