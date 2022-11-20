from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from banking.messages import Message


@dataclass(frozen=True, kw_only=True)
class Command(Message):
    account_id: UUID


@dataclass(frozen=True, kw_only=True)
class EnableAccount(Command):
    pass


@dataclass(frozen=True, kw_only=True)
class DisableAccount(Command):
    pass


@dataclass(frozen=True, kw_only=True)
class DepositMoney(Command):
    amount: int


@dataclass(frozen=True, kw_only=True)
class WithdrawMoney(Command):
    amount: int


Commands = EnableAccount | DisableAccount | DepositMoney | WithdrawMoney
