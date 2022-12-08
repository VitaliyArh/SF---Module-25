# ТЕСТ --- Хотя бы у половины питомцев есть фото

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_photo_availability(go_to_my_pets):
   '''Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную ststistic элементы статистики
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   # Сохраняем в переменную images элементы с атрибутом img
   #images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Находим половину от количества питомцев
   half = number // 2

   # Находим количество питомцев с фотографией
   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   assert number_а_photos >= half
   print(f'количество фото: {number_а_photos}')
   print(f'Половина от числа питомцев: {half}')

# python -m pytest -v --driver Chrome --driver-path C:/chromedriver/chromedriver.exe tests/2-test_photo_availability.py
# div#all_my_pets > table > tbody > tr > th > img
# //*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/th[1]/img[1]
