from abc import ABC, abstractmethod

from banking.model import AccountID, BankAccount


class AbstractBankAccountRepository(ABC):
    @abstractmethod
    def save(self, account: BankAccount) -> None:
        raise NotImplementedError()

    @abstractmethod
    def load(self, account_id: AccountID) -> BankAccount:
        raise NotImplementedError()
