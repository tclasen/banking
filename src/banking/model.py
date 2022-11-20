from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any, Callable, ClassVar, Type
from uuid import UUID

from banking import commands, events, exceptions


def _handle_create_account_event(
    account: BankAccount, event: events.AccountCreated
) -> BankAccount:
    return replace(account, account_id=event.account_id)


def _handle_disable_account_event(account: BankAccount, _: events.AccountDisabled) -> BankAccount:
    return replace(account, enabled=False)


def _handle_enabled_account_event(account: BankAccount, _: events.AccountEnabled) -> BankAccount:
    return replace(account, enabled=True)


def _handle_deposit_event(account: BankAccount, event: events.MoneyDeposited) -> BankAccount:
    return replace(account, balance=account.balance + event.amount)


def _handle_withdraw_event(account: BankAccount, event: events.MoneyWithdrawn) -> BankAccount:
    return replace(account, balance=account.balance - event.amount)


def _handle_enabled_account_command(
    account: BankAccount, _: commands.EnableAccount
) -> tuple[events.Events, ...]:
    if account.enabled:
        raise exceptions.AccountAlreadyEnabled()
    return (events.AccountEnabled(),)


def _handle_disable_account_command(
    account: BankAccount, _: commands.DisableAccount
) -> tuple[events.Events, ...]:
    if not account.enabled:
        raise exceptions.AccountAlreadyDisabled()
    return (events.AccountDisabled(),)


def _handle_deposit_command(
    account: BankAccount, command: commands.DepositMoney
) -> tuple[events.Events, ...]:
    if not account.enabled:
        raise exceptions.AccountIsDisabled()
    if command.amount <= 0:
        raise exceptions.InvalidTransactionAmount()
    return (events.MoneyDeposited(amount=command.amount),)


def _handle_withdraw_command(
    account: BankAccount, command: commands.WithdrawMoney
) -> tuple[events.Events, ...]:
    if not account.enabled:
        raise exceptions.AccountIsDisabled()
    if command.amount <= 0:
        raise exceptions.InvalidTransactionAmount()
    return (events.MoneyWithdrawn(amount=command.amount),)


@dataclass(frozen=True)
class BankAccount:
    account_id: UUID | None = field(default=None)
    balance: int = field(default=0)
    enabled: bool = field(default=True)

    _command_handlers: ClassVar[
        dict[Type[commands.Commands], Callable[[BankAccount, Any], tuple[events.Events, ...]]]
    ] = {
        commands.EnableAccount: _handle_enabled_account_command,
        commands.DisableAccount: _handle_disable_account_command,
        commands.DepositMoney: _handle_deposit_command,
        commands.WithdrawMoney: _handle_withdraw_command,
    }

    _event_handlers: ClassVar[
        dict[Type[events.Events], Callable[[BankAccount, Any], BankAccount]]
    ] = {
        events.AccountCreated: _handle_create_account_event,
        events.AccountDisabled: _handle_disable_account_event,
        events.AccountEnabled: _handle_enabled_account_event,
        events.MoneyDeposited: _handle_deposit_event,
        events.MoneyWithdrawn: _handle_withdraw_event,
    }

    def handle_event(self, event: events.Events) -> BankAccount:
        handler = self._event_handlers[type(event)]
        return handler(self, event)

    def handle_command(self, command: commands.Commands) -> tuple[events.Events, ...]:
        handler = self._command_handlers[type(command)]
        return handler(self, command)
