# Selenium Test Framework

UI test automation project built with **Python, Pytest, Selenium WebDriver** and **Page Object Model**.

## About

This project demonstrates a structured approach to web UI test automation for an e-commerce application.

It covers:

- Page Object Model architecture
- reusable page methods
- centralized locators
- fixtures and custom pytest options
- parametrized tests
- positive and negative scenarios
- guest and authorized user flows
- basket validation scenarios
- multilingual test execution

The framework is designed as a portfolio project to showcase practical QA Automation skills: clean test architecture and maintainable Selenium code.

## Stack

- Python
- Pytest
- Selenium WebDriver
- Page Object Model (POM)

## Project Structure

```text
pages/
  base_page.py        # Base page with shared methods and assertions
  basket_page.py      # Basket page actions and checks
  locators.py         # Centralized locators
  login_page.py       # Login/registration page object
  main_page.py        # Main page object
  product_page.py     # Product page object

tests/
  test_main_page.py
  test_product_page.py

conftest.py           # Fixtures and custom CLI options
pytest.ini            # Pytest configuration
requirements.txt      # Project dependencies
