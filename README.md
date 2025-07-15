# ✈️ Southwest Airlines Selenium Automation Project

## 📌 Project Overview

This project automates the flight booking flow on [Southwest.com](https://www.southwest.com) using **Selenium WebDriver with Python**.

It covers real-world challenges including:
- React-based input fields
- Dynamic dropdown suggestion lists
- Passenger quantity spinners
- A complex calendar widget
- Accessibility-driven selectors (e.g. `aria-label`)

---

## 🚀 Tech Stack

- **Language:** Python 3.11+
- **Automation Library:** Selenium 4.x
- **Browser:** Chrome (via ChromeDriver)
- **Tools:** PyCharm / VS Code, Chrome DevTools

---

## ✅ Features Automated

| Feature | Description |
|--------|-------------|
| ✈️ Airport Selection | Custom React autocomplete fields |
| 👤 Passenger Count | Dynamic increase/decrease buttons |
| 🗓️ Date Picker | Multi-month calendar UI navigation |
| 🧠 Accessibility Selectors | Used `aria-label`, `aria-labelledby`, `role`, etc. |
| 🧼 Field Clearing | Keyboard simulation to clear React-bound inputs |

---

## 🧠 Key Implementation Details

### 🔹 Clear Input Fields (React-safe)
```python
input_field.send_keys(Keys.CONTROL + "a")
input_field.send_keys(Keys.BACKSPACE)



🔹 Select from Dropdown by Text
python
Copy
Edit
wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "[aria-labelledby*='Phoenix']")
)).click()



🔹 Adjust Passenger Count (Adults, Teens, Children)
python
Copy
Edit
def increase_passenger_count(label_text, times):
    label = driver.find_element(By.XPATH, f"//div[text()='{label_text}']")
    spinner_id = label.get_attribute("for")
    for _ in range(times):
        btn = driver.find_element(By.XPATH,
            f'//div[@id="{spinner_id}"]//button[@aria-label="inc"]')
        btn.click()


🔹 Click Dynamic Calendar Date (e.g. August 15)
python
Copy
Edit
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[text()='August']/following::div[text()='15'][1]")
)).click()



📌 Challenges Solved
🌀 React UI doesn't expose traditional input behaviors → Used keyboard simulation

🎯 Dynamic IDs & suggestion boxes → Targeted aria-labelledby and text patterns

🔄 Live calendar rendering → Indexed through relative XPath and month labels

♿️ Accessibility-first attributes → Made locators stable and semantic


👨‍💻 Author
Nicholas Olumese
Built with 💻 & ✈️ using Python + Selenium
GitHub | LinkedIn



