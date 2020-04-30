from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/lucianodolenc/')

publicacoes = int(browser.find_element_by_class_name("g47SY"))

browser.maximize_window()

browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")



print("O Perfil tem : " + publicacoes.text + " publicações")

foto = len(browser.find_elements_by_xpath("/html/body/div/section/main/div/div/article/div/div/div/div/a"))

print(foto)

