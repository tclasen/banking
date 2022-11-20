import pytest

from banking import BankAccountService
from banking.exceptions import AccountDisabled, InvalidTransactionAmount


def test_users_must_be_able_to_deposit_money_into_an_existing_account(
    service: BankAccountService,
) -> None:
    service.deposit(100)
    assert service.get_balance() == 100


def test_users_must_not_be_able_to_deposit_zero_into_an_existing_account(
    service: BankAccountService,
) -> None:
    with pytest.raises(InvalidTransactionAmount):
        service.deposit(0)


def test_users_must_not_be_able_to_deposit_a_negative_amount_into_an_existing_account(
    service: BankAccountService,
) -> None:
    with pytest.raises(InvalidTransactionAmount):
        service.deposit(-100)


def test_users_must_not_be_able_to_deposit_into_a_disabled_account(
    service_with_disabled_account: BankAccountService,
) -> None:
    with pytest.raises(AccountDisabled):
        service_with_disabled_account.deposit(100)
