Feature: Persistence of Accounts

    Scenario: Users must be able to save an account
        Given an account with a few transactions
        When the user saves the account
        And the user loads the account
        Then the state of the account and the loaded account should match

    Scenario: Users must not be able to save an invalid account
        Given an account with a few transactions
        When the user performs an invalid action
        And the user saves the account
        Then the operation should fail
