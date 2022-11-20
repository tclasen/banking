from uuid import UUID

import pytest

from banking import MessageBus, ViewModel, commands
from banking.exceptions import AccountAlreadyDisabled, AccountAlreadyEnabled


def test_users_must_be_able_to_create_new_accounts(view: ViewModel, account_id: UUID) -> None:
    assert view.get_balance(account_id) == 0


def test_users_must_be_able_to_disable_a_previously_enabled_account(
    view: ViewModel, bus: MessageBus, account_id: UUID
) -> None:
    bus.handle(commands.DisableAccount(account_id=account_id))
    assert not view.is_enabled(account_id)


def test_users_must_be_able_to_enable_a_previously_disabled_account(
    view: ViewModel, bus_with_disabled_account: MessageBus, account_id: UUID
) -> None:
    assert not view.is_enabled(account_id)
    bus_with_disabled_account.handle(commands.EnableAccount(account_id=account_id))
    assert view.is_enabled(account_id)


def test_users_must_not_be_able_to_enable_an_already_enabled_account(
    bus: MessageBus, account_id: UUID
) -> None:
    with pytest.raises(AccountAlreadyEnabled):
        bus.handle(commands.EnableAccount(account_id=account_id))


def test_users_must_not_be_able_to_disable_an_already_disabled_account(
    bus_with_disabled_account: MessageBus, account_id: UUID
) -> None:
    with pytest.raises(AccountAlreadyDisabled):
        bus_with_disabled_account.handle(commands.DisableAccount(account_id=account_id))
