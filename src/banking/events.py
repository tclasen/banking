from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from banking.messages import Message


@dataclass(frozen=True, kw_only=True)
class Event(Message):
    pass


@dataclass(frozen=True, kw_only=True)
class AccountCreated(Event):
    account_id: UUID


@dataclass(frozen=True, kw_only=True)
class AccountEnabled(Event):
    pass


@dataclass(frozen=True, kw_only=True)
class AccountDisabled(Event):
    pass


@dataclass(frozen=True, kw_only=True)
class MoneyDeposited(Event):
    amount: int


@dataclass(frozen=True, kw_only=True)
class MoneyWithdrawn(Event):
    amount: int


Events = AccountCreated | AccountEnabled | AccountDisabled | MoneyDeposited | MoneyWithdrawn
