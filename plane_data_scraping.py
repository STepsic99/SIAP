from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

for i in range(0, 100):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    my_url = "https://www.airfleets.net/recherche/?key=N407AS"

    options = FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    driver1 = webdriver.Firefox(options=options)

    driver.get(my_url)

    for data in driver.find_elements(By.CLASS_NAME, "lien"):
        if data.get_attribute("href").__contains__("ficheapp"):
            driver1.get(data.get_attribute("href"))
            break


    try:
        myElem = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'boxhome')))
        for text in myElem.text.split("\n"):
            if text.__contains__("First flight date"):
                print(text.split("date")[1].trim())
            if text.__contains__("Type"):
                print(text.split(" ")[1].trim())
    except Exception:
        print("Loading took too much time!")

    driver.close()
    driver1.close()