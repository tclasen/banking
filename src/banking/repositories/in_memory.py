from functools import reduce

from banking.events import AccountCreated, Events
from banking.model import UUID, BankAccount
from banking.repository import AbstractBankAccountRepository


class InMemoryBankAccountRepository(AbstractBankAccountRepository):
    def __init__(self) -> None:
        self._accounts: dict[UUID, tuple[Events, ...]] = {}

    def save(self, account_id: UUID, events: tuple[Events, ...]) -> None:
        self._accounts[account_id] += events

    def load(self, account_id: UUID) -> BankAccount:
        root = BankAccount()
        if not account_id in self._accounts:
            self._accounts[account_id] = (AccountCreated(account_id=account_id),)
        events = self._accounts[account_id]
        return reduce(BankAccount.handle_event, events, root)
