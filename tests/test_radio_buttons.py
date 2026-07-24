from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_only_one_radio_button_can_be_selected():
    """
    Verify that only one radio button can be selected at any given time.
    """

    # Launch the Chrome browser.
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the test web page.
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        # Wait until all radio buttons are present.
        WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.NAME, "my-radio"))
        )

        # Locate all radio buttons.
        radio_buttons = driver.find_elements(By.NAME, "my-radio")

        # Verify that exactly two radio buttons exist.
        assert len(radio_buttons) == 2

        # Assign radio buttons to descriptive variables.
        first_radio = radio_buttons[0]
        second_radio = radio_buttons[1]

        # Select the first radio button.
        first_radio.click()

        # Verify the first radio button is selected.
        assert first_radio.is_selected()

        # Verify the second radio button is not selected.
        assert not second_radio.is_selected()

        # Select the second radio button.
        second_radio.click()

        # Verify the second radio button is selected.
        assert second_radio.is_selected()

        # Verify the first radio button is no longer selected.
        assert not first_radio.is_selected()

    finally:
        # Close the browser.
        driver.quit()