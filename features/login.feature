Feature: User Login
  As a user
  I want to login to the application
  So that I can access my account

  Background:
    Given I am on the login page

  @smoke @login
  Scenario: Successful login with valid credentials
    When I login with username "testuser" and password "password123"
    Then I should be redirected to the home page
    And I should see the welcome message

  @negative @login
  Scenario: Login with invalid credentials
    When I login with username "invalid" and password "wrongpass"
    Then I should see the error message
    And the error message should contain "invalid credentials"

  @negative @login
  Scenario: Login with empty username
    When I enter username ""
    And I enter password "password123"
    And I click the login button
    Then I should see the error message
    And the error message should contain "username"

  @negative @login
  Scenario: Login with empty password
    When I enter username "testuser"
    And I enter password ""
    And I click the login button
    Then I should see the error message
    And the error message should contain "password"

  @login
  Scenario Outline: Login with different invalid credentials
    When I login with username "<username>" and password "<password>"
    Then I should see the error message

    Examples:
      | username    | password    |
      | invalid     | pass123     |
      | user123     | wrongpass   |
      | testuser    | wrongpass   |
      | wronguser   | password123 |
"""