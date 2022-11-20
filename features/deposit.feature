Feature: Depositing money into Accounts

    Scenario: Users must be able to deposit money into an existing account
        Given a new account
        When the user deposits 100
        Then the account balance should be 100

    Scenario: Users must not be able to deposit zero into an existing account
        Given a new account
        When the user deposit 0
        Then the operation should fail

    Scenario: Users must not be able to deposit a negative amount into an existing account
        Given a new account
        When the user deposit -100
        Then the operation should fail

    Scenario: Users must not be able to deposit into a disabled account
        Given a previously disabled account
        When the user deposits 100
        Then the operation should fail
