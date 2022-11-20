import pytest

from banking import BankAccountService
from banking.exceptions import AccountDisabled, InvalidTransactionAmount


def test_users_must_be_able_to_withdraw_money_from_an_existing_account(
    service: BankAccountService,
) -> None:
    service.withdraw(100)
    assert service.get_balance() == -100


def test_users_must_not_be_able_to_withdraw_zero_into_an_existing_account(
    service: BankAccountService,
) -> None:
    with pytest.raises(InvalidTransactionAmount):
        service.withdraw(0)


def test_users_must_not_be_able_to_withdraw_negative_amount_into_an_existing_account(
    service: BankAccountService,
) -> None:
    with pytest.raises(InvalidTransactionAmount):
        service.withdraw(-100)


def test_users_must_not_be_able_to_withdraw_from_a_disable_account(
    service_with_disabled_account: BankAccountService,
) -> None:
    with pytest.raises(AccountDisabled):
        service_with_disabled_account.withdraw(100)
