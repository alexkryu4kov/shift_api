import pytest

from pydantic.error_wrappers import ValidationError
from src.models.balance import BalanceRequest


def test_address_number_balance_request():
    address = '0x66357dCaCe80431aee0A7507e2E361B7e2402370'
    BalanceRequest(address=address, block_number='block_number')


def test_wrong_address_number_balance_request():
    wrong_address = '066357dCaCe80431aee0A7507e2E361B7e2402370'
    with pytest.raises(ValidationError):
        BalanceRequest(address=wrong_address, block_number='block_number')

