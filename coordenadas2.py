import requests
import json
import pprint
def coordenadas2():
	valid = True
	while valid == True:
		consulta2 = input("deseja consultar a previsão de outro local (s ou n)? ").lower()
		if consulta2 == 's' or consulta2 == 'n':
			if consulta2 == "s":
				consulta3 = input("digite a cidade e o estado (ex: sao paulo, sao paulo): ")
				x=0
				for i in consulta3:
					if i == ',':
						cidade = consulta3[0:x]
						estado = consulta3[x+2:]
						local = cidade.replace(' ', '%20')+"%2C%20"+estado.replace(' ', '%20')
						#usando a api do geoaify pra pegar as coordenadas
						chaveapi = "2af874efa45341a59015fd926bc97a72"
						r = requests.get("https://api.geoapify.com/v1/geocode/search?text="+local+"&format=json&apiKey="+chaveapi+"")
						coord = json.loads(r.text)
						coordenadas = {}
						coordenadas['lat']= str(coord['results'][0]['lat'])
						coordenadas['long']= str(coord['results'][0]['lon'])
						return coordenadas
						break
					else:
						x=x+1
						continue
					valid = False
			else:
				return False
				valid = False				
		else:
			print('digite s pra sim ou n pra não')
			valid = True	

