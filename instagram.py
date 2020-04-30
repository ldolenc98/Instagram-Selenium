from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

i = 0

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/artneversleeps/')

browser.maximize_window()

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

try:

	botao = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/div[1]/div/button/div/div")

	botao.click()

except:
 	
 	""


while i < 4:
	
		browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

		sleep(2.3)

		i = i + 1

i = 0

usuario = browser.find_element_by_name("username")
usuario.send_keys("lucianodolenc")

senha = browser.find_element_by_name("password")
senha.send_keys("?????")
senha.send_keys(Keys.RETURN)

sleep(5)

publicacoes = browser.find_element_by_class_name("g47SY")

p = int(publicacoes.text)

while i < p/11:

	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

	sleep(2.3)

	i = i + 1

print("O Perfil tem : " + publicacoes.text + " publicações")

#foto = len(browser.find_elements_by_xpath("/html/body/div/section/main/div/div/article/div/div/div/div/a"))

#print(foto)
