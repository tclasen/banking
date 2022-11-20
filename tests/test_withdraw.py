from uuid import UUID

import pytest

from banking import MessageBus, ViewModel
from banking.commands import WithdrawMoney
from banking.exceptions import AccountIsDisabled, InvalidTransactionAmount


def test_users_must_be_able_to_withdraw_money_from_an_existing_account(
    view: ViewModel, bus: MessageBus, account_id: UUID
) -> None:
    bus.handle(WithdrawMoney(account_id=account_id, amount=100))
    assert view.get_balance(account_id) == -100


def test_users_must_not_be_able_to_withdraw_zero_into_an_existing_account(
    bus: MessageBus, account_id: UUID
) -> None:
    with pytest.raises(InvalidTransactionAmount):
        bus.handle(WithdrawMoney(account_id=account_id, amount=0))


def test_users_must_not_be_able_to_withdraw_negative_amount_into_an_existing_account(
    bus: MessageBus, account_id: UUID
) -> None:
    with pytest.raises(InvalidTransactionAmount):
        bus.handle(WithdrawMoney(account_id=account_id, amount=-100))


def test_users_must_not_be_able_to_withdraw_from_a_disable_account(
    bus_with_disabled_account: MessageBus, account_id: UUID
) -> None:
    with pytest.raises(AccountIsDisabled):
        bus_with_disabled_account.handle(WithdrawMoney(account_id=account_id, amount=100))
