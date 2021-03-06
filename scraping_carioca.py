from selenium import webdriver
import time, json

data = {}
equipes = {}
partidas = {}
countTimes = 1

driver = webdriver.Chrome()

url = 'https://globoesporte.globo.com/futebol/brasileirao-serie-a/'

driver.get(url)
setaDireta = driver.find_element_by_class_name('lista-jogos__navegacao--seta-direita')

for listaRodadas in range(0,38):
	print(" --> PROCESSANDO RODADA Nº " + str(listaRodadas+1))
	for partida in driver.find_elements_by_class_name('lista-jogos__jogo'):
		time_mandante = partida.find_element_by_xpath('.//div[1]//div[1]//div[1]//div[2]//div[1]//span[1]')
		time_visitante = partida.find_element_by_xpath('.//div[1]//div[1]//div[1]//div[2]//div[3]//span[1]')

		# Processamento de todos os times. Apenas na primeira rodada ja conseguimos todos os dados
		if(listaRodadas == 0):
			equipes[time_mandante.text] = {'id': countTimes, 'sigla': time_mandante.text, 
				"nome": time_mandante.get_attribute("title")}

			countTimes = countTimes + 1

			equipes[time_visitante.text] = {'id': countTimes, 'sigla': time_visitante.text, 
				"nome": time_visitante.get_attribute("title")}

			countTimes = countTimes + 1

			time.sleep(2)

		# Processamento das partidas
		partidas[listaRodadas] = {'id': listaRodadas+1, 'time_mandante': time_mandante.text,
			'time_visitante': time_visitante.text}

		time.sleep(1)

	setaDireta.click()
	time.sleep(2)


driver.close()

data['equipes'] = equipes
data['partidas'] = partidas

# Escrevendo json em arquivo
json_data = json.dumps(data)
with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

