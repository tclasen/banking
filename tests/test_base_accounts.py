import pytest

from banking import BankAccountService
from banking.exceptions import AccountAlreadyDisabled, AccountAlreadyEnabled


def test_users_must_be_able_to_create_new_accounts(service: BankAccountService) -> None:
    assert service.get_balance() == 0


def test_users_must_be_able_to_disable_a_previously_enabled_account(
    service: BankAccountService,
) -> None:
    service.disable_account()
    assert not service.is_enabled()


def test_users_must_be_able_to_enable_a_previously_disabled_account(
    service_with_disabled_account: BankAccountService,
) -> None:
    service_with_disabled_account.enabled_account()
    assert service_with_disabled_account.is_enabled


def test_users_must_not_be_able_to_enable_an_already_enabled_account(
    service: BankAccountService,
) -> None:
    with pytest.raises(AccountAlreadyEnabled):
        service.enabled_account()


def test_users_must_not_be_able_to_disable_an_already_disabled_account(
    service_with_disabled_account: BankAccountService,
) -> None:
    with pytest.raises(AccountAlreadyDisabled):
        service_with_disabled_account.disable_account()
