Feature: Withdrawing money from Accounts

    Scenario: Users must be able to withdraw money from an existing account
        Given a new account
        When the user withdraws 100
        Then the account balance should be -100

    Scenario: Users must not be able to withdraw zero into an existing account
        Given a new account
        When the user withdraws 0
        Then the operation should fail

    Scenario: Users must not be able to withdraw negative amount into an existing account
        Given a new account
        When the user withdraws -100
        Then the operation should fail

    Scenario: Users must not be able to withdraw from a disable account
        Given a previously disabled account
        When the user withdraws 100
        Then the operation should fail
