from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

i = 0

user = str(input("Digite o seu usuário do Instagram: "))

password = str(input("Digite a sua senha do Instagram: "))

perfil = str(input("Digite o perfil que você deseja visitar: @"))

browser = webdriver.Firefox()

try:

	browser.get('https://www.instagram.com/'+perfil+'/')

	browser.maximize_window()

	login = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button")

	login.click()

	sleep(5)

	usuario = browser.find_element_by_name("username")
	usuario.send_keys(user)

	senha = browser.find_element_by_name("password")
	senha.send_keys(password)
	senha.send_keys(Keys.RETURN)

	sleep(8)

	publicacoes = browser.find_element_by_class_name("g47SY")

	p = int(publicacoes.text)

	print("O Perfil tem : " + publicacoes.text + " publicações")

	foto = browser.find_element_by_xpath("/html/body/div/section/main/div/div/article/div/div/div/div")

	foto.click()

	sleep(5)

	curtidas = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span")

	data = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time")

	print("A FOTO FOI POSTADA: " + data.text + "    QUANTIDADE DE CURTIDAS: " + curtidas.text)

	proximo = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")

	proximo.click()

	sleep(4)

	while i < p:

		try:

			curtidas = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span")
			proximo = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")

			data = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time")

			print("A FOTO FOI POSTADA: " + data.text + "    QUANTIDADE DE CURTIDAS: " + curtidas.text)

			i = i + 1

			proximo.click()

			sleep(4)

		except:

			data = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time")

			print("A FOTO FOI POSTADA: " + data.text + "      A POSTAGEM É UM VÍDEO, NÃO É POSSÍVEL MOSTRAR AS CURTIDAS")

			i = i + 1

			proximo = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")

			proximo.click()

			sleep(4)
	
except:

	print("Ocorreu algum erro!")

	print("1- Verfique se o usuário e senha digitados estão corretos")

	print("2- O perfil digitado pode estar incorreto")

	print("3- O perfil digitado pode ser privado")
