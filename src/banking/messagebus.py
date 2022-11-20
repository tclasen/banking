from __future__ import annotations

from uuid import UUID

from banking import commands
from banking.model import BankAccount
from banking.repository import AbstractBankAccountRepository


class MessageBus:
    repo: AbstractBankAccountRepository

    def handle(self, command: commands.Commands) -> None:
        account = self._load(command.account_id)
        events = account.handle_command(command)
        self.repo.save(command.account_id, events)

    def _load(self, account_id: UUID) -> BankAccount:
        return self.repo.load(account_id)
