import os
import signal
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)


def handler(*args):
    driver.close()
    sys.exit(0)


signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

wait = WebDriverWait(driver, 5)


def main():
    info = {}
    for key in (
        "LICENSE_NUMBER",
        "EXPIRY_DATE",
        "FIRST_NAME",
        "LAST_NAME",
        "DATE_OF_BIRTH",
    ):
        breakpoint()
        info[key] = os.getenv(key)

    driver.get("https://online.transport.wa.gov.au/pdabooking/manage/?0")

    driver.find_element(By.NAME, "clientDetailsPanel:licenceNumber").send_keys(
        info["LICENSE_NUMBER"]
    )

    driver.find_element(By.NAME, "clientDetailsPanel:licenceExpiryDate").send_keys(
        info["EXPIRY_DATE"]
    )

    driver.find_element(By.NAME, "clientDetailsPanel:firstName").send_keys(
        info["FIRST_NAME"]
    )

    driver.find_element(By.NAME, "clientDetailsPanel:lastName").send_keys(
        info["LAST_NAME"]
    )

    driver.find_element(By.NAME, "clientDetailsPanel:dateOfBirth").send_keys(
        info["DATE_OF_BIRTH"]
    )

    wait.until(ec.element_to_be_clickable((By.ID, "id5"))).click()

    sleep(2)

    try:
        wait.until(
            ec.element_to_be_clickable((By.NAME, "manageBookingContainer:search"))
        ).click()
    except TimeoutException:
        wait.until(
            ec.element_to_be_clickable(
                (
                    By.NAME,
                    "manageBookingContainer:currentBookingsTable:listView:0:listViewPanel:change",
                )
            )
        ).click()

    locations = (
        "West Perth",
        "Midland",
        "Mandurah",
    )

    for location in locations:
        select = Select(
            wait.until(
                ec.element_to_be_clickable((By.NAME, "searchBookingContainer:siteCode"))
            )
        )
        select.select_by_visible_text(location)
        wait.until(
            ec.element_to_be_clickable((By.NAME, "searchBookingContainer:search"))
        ).click()

        sleep(1)
        try:
            driver.find_element(By.ID, "searchResultRadio0")
            print(f"Booking available at: {location}")
        except NoSuchElementException:
            pass

    driver.close()


main()
