import json
import requests
from bs4 import BeautifulSoup
import time
#import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome WebDriver with Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
service = Service("path/to/chromedriver")  # Replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_menu(url):
    try:
        # Load the webpage with Selenium
        driver.get(url)
        time.sleep(5)  # Give the page time to load (adjust as needed)

        # Find all menu categories
        categories = driver.find_elements(By.CLASS_NAME, "entry-title")

        menu_data = {}

        # Loop through categories and extract items
        for category in categories:
            category_name = category.text.strip()
            items = []

            # Find items within each category
            category_container = category.find_element(By.XPATH, "..").find_element(By.XPATH, "following-sibling::div")
            item_elements = category_container.find_elements(By.CLASS_NAME, "menu-item")

            for item_element in item_elements:
                item_name = item_element.find_element(By.CLASS_NAME, "menu-item-title").text.strip()
                item_description = item_element.find_element(By.CLASS_NAME, "menu-item-description").text.strip()
                item_price = item_element.find_element(By.CLASS_NAME, "menu-item-price").text.strip()

                item = {
                    "name": item_name,
                    "description": item_description,
                    "price": item_price,
                }
                items.append(item)

            menu_data[category_name] = items

        # Check if any data was extracted
        if menu_data:
            # Save the data as a JSON file
            with open("menu.json", "w", encoding="utf-8") as json_file:
                json.dump(menu_data, json_file, ensure_ascii=False, indent=4)

            print("Menu data has been successfully scraped and saved as 'menu.json'.")
        else:
            print("No menu data found on the website.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()  # Close the WebDriver

# Specify the URL of the menu page
menu_url = "https://fieramoscatoronto.ca/menu/"

# Call the scraping function
scrape_menu(menu_url)
