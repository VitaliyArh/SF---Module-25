# ТЕСТ --- Присутствуют все питомцы

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(go_to_my_pets):
   '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную statistic элементы статистики
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
      #EC.presence_of_element_located((By.CSS_SELECTOR, "div#all_my_pets > table > tbody > tr")))

   # Сохраняем в переменную pets элементы карточек питомцев
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")
   #pets = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Получаем количество карточек питомцев
   number_of_pets = len(pets)

   # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number == number_of_pets



# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe tests/1-test_all_pets_are_present.py
# pytest -v --driver Chrome --driver-path с:/chromedriver/chromedriver.exe
# div#all_my_pets > table > tbody > tr > th > img
# //*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/th[1]/img[1]
