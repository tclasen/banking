from uuid import UUID

import pytest

from banking import (
    AbstractBankAccountRepository,
    BankAccountService,
    InMemoryBankAccountRepository,
)


@pytest.fixture
def account_id() -> UUID:
    return UUID("812E217B-F235-42D2-98F2-92439208A643")


@pytest.fixture(params=[InMemoryBankAccountRepository])
def repo(request: pytest.FixtureRequest) -> AbstractBankAccountRepository:
    return request.param()


@pytest.fixture
def service(repo: AbstractBankAccountRepository, account_id: UUID) -> BankAccountService:
    BankAccountService.repo = repo
    return BankAccountService(account_id)


@pytest.fixture
def service2(repo: AbstractBankAccountRepository, account_id: UUID) -> BankAccountService:
    BankAccountService.repo = repo
    return BankAccountService(account_id)


@pytest.fixture
def service_with_disabled_account(service: BankAccountService) -> BankAccountService:
    service.disable_account()
    return service
