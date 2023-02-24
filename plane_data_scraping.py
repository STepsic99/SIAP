from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

for i in range(0, 100):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    my_url = "https://www.airfleets.net/recherche/?key=VH-UJK"

    options = FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    driver1 = webdriver.Firefox(options=options)

    driver.get(my_url)

    for data in driver.find_elements(By.CLASS_NAME, "lien"):
        if(data.get_attribute("href").__contains__("ficheapp")):
            driver1.get(data.get_attribute("href"))
            break

    for data in driver1.find_elements(By.CLASS_NAME, "texten"):
        if(data.text.__contains__("years")):
            print(data.text)
            print(i)
    driver.close()
    driver1.close()