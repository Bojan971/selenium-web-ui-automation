# Selenium Web UI Automation

Python | Selenium | PyTest | Git | GitHub

A practical UI test automation project demonstrating Selenium WebDriver and PyTest best practices.

## Project Overview

This project demonstrates automated UI testing using Selenium WebDriver and PyTest. The automated test validates the behavior of radio buttons on the Selenium Web Test Page, ensuring that only one radio button can be selected at any given time.

The project was developed as part of my Software QA portfolio to demonstrate practical experience in UI test automation, functional validation and Python-based test development.

---

## Recruiter Notes

This repository is part of my comprehensive Software QA Portfolio, which consists of six practical case studies covering different areas of software testing.

The complete portfolio demonstrates hands-on experience in UI Test Automation, API Testing, Performance Testing, Manual Testing, SQL Testing and Test Management using industry-standard tools and best practices.

---

## Repository Status

**Status:** Completed

**Project Type:** Portfolio Project

**Testing Level:** UI Functional Testing

**Last Updated:** July 2026

---

## Project Objectives

- Automate UI testing using Selenium WebDriver
- Validate radio button selection behavior
- Verify that only one radio button can be selected at any time
- Apply explicit waits for reliable synchronization
- Implement automated assertions using PyTest
- Demonstrate clean and maintainable test automation code

---

## Technologies Used

| Category             | Technology         |
|----------------------|--------------------|
| Programming Language | Python             |
| Test Framework       | PyTest             |
| UI Automation        | Selenium WebDriver |
| Browser              | Google Chrome      |
| Driver Management    | WebDriver Manager  |
| IDE                  | Visual Studio Code |
| Version Control      | Git & GitHub       |

---

## Project Structure

```text
selenium-web-ui-automation/

│
├── README.md
├── requirements.txt
├── .gitignore
│
├── tests/
│ └── test_radio_buttons.py
│
├── documentation/
│
├── screenshots/
│
├── test-data/
│
└── assets/
```

---

## Test Scenario

The automated test performs the following validation steps:

1. Launches the Chrome browser.
2. Opens the Selenium Web Form test page.
3. Waits until all radio buttons become available.
4. Verifies that exactly two radio buttons exist.
5. Selects the first radio button.
6. Verifies that the first radio button is selected.
7. Verifies that the second radio button remains unselected.
8. Selects the second radio button.
9. Verifies that the second radio button is selected.
10. Verifies that the first radio button becomes unselected.
11. Closes the browser.

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Bojan971/selenium-web-ui-automation.git
```

### 2. Navigate to the project directory

```bash
cd selenium-web-ui-automation
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Execute the test

```bash
pytest
```

---

## Expected Result

The automated test should complete successfully, confirming that:

- Exactly two radio buttons are present.
- Only one radio button can be selected at any given time.
- All assertions pass successfully.

---

## Project Screenshots

The following screenshots illustrate the project execution:

- Project structure
- Selenium browser execution
- Successful PyTest execution
- Test results

---

## Key Skills Demonstrated

- UI Test Automation
- Selenium WebDriver
- Python Programming
- PyTest
- Functional Testing
- Assertions
- Explicit Waits
- Test Design
- Git
- GitHub

---

## Lessons Learned

During this project I strengthened my understanding of:

- Selenium WebDriver fundamentals
- UI element identification strategies
- Explicit Wait implementation
- Automated validation using assertions
- Writing clean and maintainable automation code
- Organizing a small automation project using Git

---

## Future Improvements

Possible future enhancements include:

- Page Object Model (POM) implementation
- Cross-browser execution
- HTML reporting
- Data-driven testing
- CI/CD integration using GitHub Actions

---

## Author

**Bojan Djordjevic**

Software QA Engineer

LinkedIn:
https://www.linkedin.com/in/bojan-djordjevic-5403bb67/

GitHub:
https://github.com/Bojan971