import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException


def login(driver, email, password):
    driver.get('https://sis.galvanize.com/')
    
    sso_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Use Galvanize Single Sign-On')]"))
    )
    sso_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://auth.galvanize.com/sign_in')
    )
    
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'user_email'))
    )
    email_input.send_keys(email)
    
    password_input = driver.find_element(By.ID, 'user_password')
    password_input.send_keys(password)

    login_button = driver.find_element(By.NAME, 'commit')
    login_button.click()

def navigate_to_attendance_page(driver):
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://sis.galvanize.com/dashboards/students/143/')
    )

    attendance_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/cohorts/143/attendance/mine/'][@class='has-text-weight-bold']"))
    )
    attendance_link.click()

    
def check_for_code(driver):
    driver.refresh()
    try:
        code_element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='tag is-danger is-size-6']"))
        )
        return code_element.text
    except TimeoutException:
        return None

def input_code(driver, code):
    code_input = driver.find_element(By.ID, 'form-token')
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), \"I'm here!\")]")
    
    code_input.send_keys(code)
    submit_button.click()

def main():
    email = 'yourEmailAddress@gmail.com'
    password = 'YourPassword'

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        login(driver, email, password)
        navigate_to_attendance_page(driver)
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'form-token'))
        )

        while True:
            code = check_for_code(driver)
            if code and len(code) == 4:
                input_code(driver, code)
                print(f'Code {code} submitted successfully!')
                break
            time.sleep(1)
            driver.refresh()
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
