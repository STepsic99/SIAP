from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

tail_number_array = []
type_array = []
flight_date_array = []
df1 = pd.read_csv('trimmed_merged_file.csv', encoding="ISO-8859-1")

options = FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

driver1 = webdriver.Firefox(options=options)


for index, row in df1.iterrows():
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    my_url = "https://flightaware.com/live/flight/"+row['TAIL_NUMBER']
    my_url1 = "https://flightaware.com/resources/registration/"+row['TAIL_NUMBER']
    tail_number_array.append(row['TAIL_NUMBER'])

    driver.get(my_url)

    driver1.get(my_url1)

    flight_date_data = driver.find_elements(By.XPATH, "//*[contains(text(),'Aircraft Type')]/following-sibling::div[1]")
    if len(flight_date_data) == 0 or len(flight_date_data) == 1:
        flight_date_array.append('')

    else:
        for data in flight_date_data:
            # print(data.text)
            data_split = data.text.split('(')[0].strip()
            print(data_split)
            flight_date_array.append(data_split)
            break

    type_data = driver1.find_elements(By.XPATH, "//*[contains(text(),'Airworthiness Date')]/following-sibling::div")

    if len(type_data) == 0:
        type_array.append('')

    else:
        for data in type_data:
            print(data.text)
            type_array.append(data.text)


driver.close()
driver1.close()


data_to_be_written = {
    'TAIL_NUMBER': tail_number_array,
    'TYPE': type_array,
    'FIRST_FLIGHT': flight_date_array,
}
df = pd.DataFrame(data_to_be_written)
df.to_csv("trimmed_merged_file_scrapped.csv", index=False)