from banking.model import AccountID, BankAccount
from banking.repository import AbstractBankAccountRepository


class InMemoryBankAccountRepository(AbstractBankAccountRepository):
    def __init__(self) -> None:
        self._accounts: dict[AccountID, BankAccount] = {}

    def save(self, account: BankAccount) -> None:
        self._accounts[account.account_id] = account

    def load(self, account_id: AccountID) -> BankAccount:
        return self._accounts.get(account_id, BankAccount(account_id))
