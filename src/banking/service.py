from banking.exceptions import (
    AccountAlreadyDisabled,
    AccountAlreadyEnabled,
    AccountDisabled,
    InvalidTransactionAmount,
)
from banking.model import AccountID
from banking.repository import AbstractBankAccountRepository


class BankAccountService:
    repo: AbstractBankAccountRepository

    def __init__(self, account_id: AccountID) -> None:
        self._account_id = account_id
        self.refresh()

    def refresh(self) -> None:
        self._account = self.repo.load(self._account_id)

    def is_enabled(self) -> bool:
        return self._account.enabled

    def get_balance(self) -> int:
        return self._account.balance

    def disable_account(self) -> None:
        if not self._account.enabled:
            raise AccountAlreadyDisabled()
        self._account = self._account.disable_account()
        self.repo.save(self._account)

    def enabled_account(self) -> None:
        if self._account.enabled:
            raise AccountAlreadyEnabled()
        self._account = self._account.enabled_account()
        self.repo.save(self._account)

    def deposit(self, amount: int) -> None:
        if not self._account.enabled:
            raise AccountDisabled()
        if amount <= 0:
            raise InvalidTransactionAmount()
        self._account = self._account.deposit(amount)
        self.repo.save(self._account)

    def withdraw(self, amount: int) -> None:
        if not self._account.enabled:
            raise AccountDisabled()
        if amount <= 0:
            raise InvalidTransactionAmount()
        self._account = self._account.withdraw(amount)
        self.repo.save(self._account)
