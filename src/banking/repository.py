from abc import ABC, abstractmethod
from uuid import UUID

from banking.events import Events
from banking.model import BankAccount


class AbstractBankAccountRepository(ABC):
    @abstractmethod
    def save(self, account_id: UUID, events: tuple[Events, ...]) -> None:
        raise NotImplementedError()

    @abstractmethod
    def load(self, account_id: UUID) -> BankAccount:
        raise NotImplementedError()
