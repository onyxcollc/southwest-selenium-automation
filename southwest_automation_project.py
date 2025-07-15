from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#Build Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver,10)
driver.maximize_window()


#Open Southwest url
driver.get("https://www.southwest.com/")
driver.save_screenshot("screenshots/01_homepage.png")


#Click third party cookies Dismiss button
dismiss_btn = wait.until(EC.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler")))
dismiss_btn.click()
driver.save_screenshot("screenshots/02_dismiss.png")

#Click trip type dropdown
# round_trip_dd = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-label*='Trip type']")))
# round_trip_dd.click()

#Type LAX in depart field
depart_field = wait.until(EC.element_to_be_clickable((By.ID,"originationAirportCode")))
depart_field.send_keys(Keys.CONTROL + "a")
depart_field.send_keys(Keys.BACKSPACE)
depart_field.send_keys("LAX")
assert "LAX" in depart_field.get_attribute("value"), "Depart field did not populate with LAX."
driver.save_screenshot("screenshots/03_losangeles_selected.png")

#Type BWI in Arrive field
arrive_field = wait.until(EC.element_to_be_clickable((By.ID,"destinationAirportCode")))
arrive_field.send_keys("BWI")
bwi = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-labelledby*='Baltimore']")))
assert bwi.is_displayed(), "Baltimore suggestions not visible"
bwi.click()
arrive_field.send_keys(Keys.TAB)
driver.save_screenshot("screenshots/04_baltimore_selected.png")

#Type depart date
dep_date_input = wait.until(EC.element_to_be_clickable((By.ID,"departureDate")))
dep_date_input.click()

wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='Select your travel dates']")))

aug_15 = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='August']/following::div[text()='15'][1]")))
aug_15.click()
driver.save_screenshot("screenshots/05_depart_date.png")

#Type return date
dep_date_input = wait.until(EC.element_to_be_clickable((By.ID,"returnDate")))
dep_date_input.click()

wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='Select your travel dates']")))

aug_22 = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='August']/following::div[text()='22'][1]")))
aug_22.click()
driver.save_screenshot("screenshots/06_return_date.png")

#Pick 4 Passengers
passenger_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-label='Passenger Selector']")))
passenger_field.click()

adults_label = driver.find_element(By.XPATH,"//div[text()='Adults']")
spinner_id = adults_label.get_attribute("for")
spinner_xpath = f"//div[@id='{spinner_id}']"

for _ in range(3):
    increased_button = driver.find_element(By.XPATH, f"{spinner_xpath}//button[@aria-label='inc']")
    increased_button.click()

spinner = driver.find_element(By.ID, spinner_id)
assert spinner.get_attribute("aria-valuenow") == "4", "Passenger count is not 4"

#Click Apply Button
apply_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Apply']")))
apply_btn.click()
driver.save_screenshot("screenshots/07_passenger_popup.png")

#Click search for flights
search_flight = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='container__F2xqj']")))
search_flight.click()
driver.save_screenshot("screenshots/08_search_button.png")
sleep(10)


