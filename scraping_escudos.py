from selenium import webdriver
import time, json
from urllib.request import urlopen, Request

data = {}

driver = webdriver.Chrome()

url = 'https://globoesporte.globo.com/futebol/brasileirao-serie-a/'

driver.get(url)

for partida in driver.find_elements_by_class_name('lista-jogos__jogo'):

	# No Ge, se uma partida ja foi jogada ela recebe um link ao inves de uma div
	try:
		time_mandante = partida.find_element_by_xpath('.//div[1]//a[1]//div[1]//div[2]//div[1]')
		time_visitante = partida.find_element_by_xpath('.//div[1]//a[1]//div[1]//div[2]//div[3]')
	except:
		time_mandante = partida.find_element_by_xpath('.//div[1]//div[1]//div[1]//div[2]//div[1]')
		time_visitante = partida.find_element_by_xpath('.//div[1]//div[1]//div[1]//div[2]//div[3]')

	time.sleep(1)

	with open('./escudos/' + time_mandante.find_element_by_xpath('.//span[1]').get_attribute("title")+'.svg','wb') as f:
		f.write(urlopen(time_mandante.find_element_by_xpath('.//img[1]').get_attribute("src")).read())

	with open('./escudos/' + time_visitante.find_element_by_xpath('.//span[1]').get_attribute("title")+'.svg','wb') as f:
		f.write(urlopen(time_visitante.find_element_by_xpath('.//img[1]').get_attribute("src")).read())

driver.close()


