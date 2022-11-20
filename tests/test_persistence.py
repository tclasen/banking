from banking import BankAccountService


def test_users_must_be_able_to_save_an_account(
    service: BankAccountService, service2: BankAccountService
) -> None:
    service.deposit(100)
    service.withdraw(80)
    assert service2.get_balance() == 0

    service2.refresh()
    assert service2.get_balance() == 20
