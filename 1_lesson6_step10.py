from selenium import webdriver
import time 

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
  browser = webdriver.Chrome()

  # Поменять link1 на link2 для смены ссылки и получения ошибки
  browser.get(link2)

  # Ваш код, который заполняет обязательные поля
  first_name = browser.find_element_by_css_selector(".first_block input.first")
  first_name.send_keys("Ivan")

  last_name = browser.find_element_by_css_selector(".first_block input.second")
  last_name.send_keys("Petrov")

  email = browser.find_element_by_css_selector(".first_block input.third")
  email.send_keys("qwe@dfg.ru")

  # Отправляем заполненную форму
  button = browser.find_element_by_css_selector("button.btn")
  button.click()

  # Проверяем, что смогли зарегистрироваться
  # ждем загрузки страницы
  time.sleep(1)

  # находим элемент, содержащий текст
  welcome_text_elt = browser.find_element_by_tag_name("h1")
  # записываем в переменную welcome_text текст из элемента welcome_text_elt
  welcome_text = welcome_text_elt.text

  # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
  assert "Congratulations! You have successfully registered!" == welcome_text

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()
