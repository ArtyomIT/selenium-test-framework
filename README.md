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
```
## Setup

```bash
# Clone repository
git clone https://github.com/ArtyomIT/selenium-test-framework.git
cd selenium-test-framework

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
## Run Tests
```bash
# Run all tests
pytest -v -s 

# Run all tests in another language
pytest -v -s --language=en

# Run marked tests
pytest -v -s --language=en -m need_review
```

## Goal
This repository was created as part of my QA Automation portfolio to demonstrate:

- UI test automation with Selenium and Pytest

- framework design based on Page Object Model

- maintainable test architecture

- test scenario decomposition

- practical work with locators, assertions, and browser fixtures
