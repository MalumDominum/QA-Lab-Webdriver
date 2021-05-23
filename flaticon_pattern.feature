Feature: Generate patterns from icons
  Scenario: Open non-premium icon pack
    Given I'm on Flaticon main page
    When I click on first non-premium icon pack
    Then The icon pack page opens
  Scenario: Open create pattern window in same tab
    Given I'm on icon pack page
    When I change the button's target attribute on "_blank"
    And Click on it
    Then Page for creating patterns is opened in same tab
  Scenario: Generate 10 patterns and take screenshots
    Given I'm on creating pattern page
    When I click on "Random pattern" button
    Then Page generate random pattern using icons from opened pack and set random background
    And I screenshot this pattern
    And I save my screenshot in the root folder
    And I return to the "When" stage until the moment when I click and screenshot 10 times
  Scenario: Swap to "Background" menu
    Given I'm on creating pattern page
    When I click on "Background" button
    Then Icons menu changing to the menu with color picker
  Scenario: Changing background color on random 10 times
    Given I'm on creating pattern page
    And Background changing menu opened
    When I input random hex number in field (overwriting last)
    Then Pattern's background is changed to that color
    And Pointer on canvas is changing position to the entered color
  Scenario: Clear pattern
    Given I'm on creating pattern page
    When I click on "CLear" button
    Then All icon from pattern canvas was deleted
    And Pattern's background is changed default (#fff)
  Scenario: Click on first 20 icons
    Given I'm on creating pattern page
    When I click on first 20 icons alternately
    Then On pattern canvas on random place appears clicked icons with the same size