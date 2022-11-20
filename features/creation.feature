Feature: Creation, Enabling, and Disabling of Accounts

    Scenario: Users must be able to create new accounts
        When the User creates a new account
        Then an account should exist
        And the account should be enabled
        And the account balance should be zero

    Scenario: Users must be able to disable a previously enabled account
        Given a new account
        When the User disables the account
        Then the account should show as being disabled

    Scenario: Users must be able to enable a previously disabled account
        Given a previously disabled account
        When the User enables the account
        Then the account should show as being enabled

    Scenario: Users must not be able to enable an already enabled account
        Given a new account
        When the User enables the account
        Then the operation should fail

    Scenario: Users must not be able to disable an already disabled account
        Given a previously disabled account
        When the User disables the account
        Then the operation should fail
