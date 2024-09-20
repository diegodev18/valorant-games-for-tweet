from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_code(authorization_url, user, passw):
    driver = webdriver.Firefox()

    driver.get(authorization_url)

    driver.find_element(By.ID, 'username_or_email').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(passw)
    driver.find_element(By.ID, 'allow').click()

    code = driver.find_element(By.ID, 'oauth_pin').text.split('\n')[1]

    sleep(5)

    driver.quit()

    return code


def get_tw_code_main(authorization_url, user, passw):
    try:
        return get_code(authorization_url, user, passw)
    except Exception as e:
        print('\nError:', e)
        return None


if __name__ == '__main__':
    pass
