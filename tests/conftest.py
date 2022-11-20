from uuid import UUID

import pytest

from banking import (
    AbstractBankAccountRepository,
    InMemoryBankAccountRepository,
    MessageBus,
    ViewModel,
)
from banking.commands import DisableAccount


@pytest.fixture  # type: ignore
def account_id() -> UUID:
    return UUID("812E217B-F235-42D2-98F2-92439208A643")


@pytest.fixture(params=[InMemoryBankAccountRepository])  # type: ignore
def repo(request: pytest.FixtureRequest) -> AbstractBankAccountRepository:
    return request.param()


@pytest.fixture  # type: ignore
def bus(repo: AbstractBankAccountRepository) -> MessageBus:
    MessageBus.repo = repo
    return MessageBus()


@pytest.fixture  # type: ignore
def view(repo: AbstractBankAccountRepository) -> ViewModel:
    ViewModel.repo = repo
    return ViewModel()


@pytest.fixture  # type: ignore
def bus_with_disabled_account(bus: MessageBus, account_id: UUID) -> MessageBus:
    bus.handle(DisableAccount(account_id=account_id))
    return bus
