from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os


EXTENSION_PATH = os.getenv("EXTENSION_PATH")
EXTENSION_ID = os.getenv('EXTENSION_ID')
print(EXTENSION_ID)


opt = webdriver.ChromeOptions()

opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(options=opt)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


driver.get(f"chrome-extension://{EXTENSION_ID}/home.html#onboarding/welcome")
driver.save_screenshot('screenshot.png')

driver.implicitly_wait(10)

checkbox = driver.find_element(By.ID, "onboarding__terms-checkbox")

if checkbox.is_displayed() and checkbox.is_enabled():
    if not checkbox.is_selected():
        print(checkbox.is_selected())
        checkbox.click()
        WebDriverWait(driver, 10).until(EC.element_located_to_be_selected((By.ID, "onboarding__terms-checkbox")))
        print(checkbox.is_selected())

button = driver.find_element(By.CSS_SELECTOR, '[data-testid="onboarding-import-wallet"]')
driver.execute_script("arguments[0].removeAttribute('disabled')", button)
button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

driver.get(f"chrome-extension://{EXTENSION_ID}/home.html#onboarding/metametrics")
driver.save_screenshot('screenshot1.png')


acess = driver.find_element(By.CSS_SELECTOR, '[data-testid="metametrics-i-agree"]')
acess.click()

driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/import-with-recovery-phrase")
driver.save_screenshot('screenshot2.png')

seed_words = [
    "chat",
    "village",
    "motor",
    "mixed",
    "midnight",
    "dream",
    "morning",
    "pulse",
    "heavy",
    "right",
    "slow",
]

brute_force_list = [
    'teste',
    'teste',
    'end',
]

def clear_input():
    for x in range(12):
        element = driver.find_element(By.ID, f"import-srp__srp-word-{x}")
        element.clear()

def check_by_pass(seed_words, brute_force_list):
    for seed in brute_force_list:
        seed_words.append(seed)
        driver.execute_script("window.location.reload();")
        for x in range(12):
            element = driver.find_element(By.ID, f"import-srp__srp-word-{x}")
            element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, f"import-srp__srp-word-{x}")))
            element.send_keys(seed_words[x])
        by_pass = driver.find_element(By.CSS_SELECTOR, '[data-testid="import-srp-confirm"]')

        if by_pass.is_enabled():
            return True

        seed_words.pop()


print(check_by_pass(seed_words, brute_force_list), "result by pass")

print(driver.current_url)

sleep(15)
driver.quit()

