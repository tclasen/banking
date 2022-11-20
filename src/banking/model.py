from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import NewType
from uuid import UUID

AccountID = NewType("AccountID", UUID)


@dataclass(frozen=True)
class BankAccount:
    account_id: AccountID | None = field(default=None)
    balance: int = field(default=0)
    enabled: bool = field(default=True)

    def disable_account(self) -> BankAccount:
        return replace(self, enabled=False)

    def enabled_account(self) -> BankAccount:
        return replace(self, enabled=True)

    def deposit(self, amount: int) -> BankAccount:
        return replace(self, balance=self.balance + amount)

    def withdraw(self, amount: int) -> BankAccount:
        return replace(self, balance=self.balance - amount)
