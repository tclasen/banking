from uuid import UUID

from banking import MessageBus, ViewModel
from banking.commands import DepositMoney, WithdrawMoney


def test_users_must_be_able_to_save_an_account(
    bus: MessageBus, view: ViewModel, account_id: UUID
) -> None:
    bus.handle(DepositMoney(account_id=account_id, amount=100))
    bus.handle(WithdrawMoney(account_id=account_id, amount=80))
    assert view.get_balance(account_id) == 20
