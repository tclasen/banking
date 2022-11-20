from __future__ import annotations

from uuid import UUID

from banking.model import BankAccount
from banking.repository import AbstractBankAccountRepository


class ViewModel:
    repo: AbstractBankAccountRepository

    def is_enabled(self, account_id: UUID) -> bool:
        account = self._load(account_id)
        return account.enabled

    def get_balance(self, account_id: UUID) -> int:
        account = self._load(account_id)
        return account.balance

    def _load(self, account_id: UUID) -> BankAccount:
        return self.repo.load(account_id)
