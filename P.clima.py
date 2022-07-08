import requests
import json
import pprint
import fivedias as fv
import coordenadas2 as C2
accuweatherapikey = 'kGnMMlfUARcaZRgLqnErqP7HQlKziod6'

def pegarcoordenadas():
    r = requests.get('http://www.geoplugin.net/json.gp?ip=xx.xx.xx.xx')
    if (r.status_code!=200):
        print('localização não encontrada')
        return None
    else:
        try:  
            localização = json.loads(r.text)
            coordenadas = {}
            coordenadas['lat'] = localização['geoplugin_latitude']
            coordenadas['long'] = localização['geoplugin_longitude']
            return coordenadas
        except:
            return None

def codlocal(lat,long):
    locationapiurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" +accuweatherapikey+ "&q=" +lat+ "%2C%20"+long+"&language=pt-br"
   
    r = requests.get(locationapiurl)
    if (r.status_code!=200):
        print('localização não encontrada')
        return None
    else:
        try:
            locationresponse = json.loads(r.text)
            
            infolocal = {}
            infolocal['nomelocal'] = locationresponse['LocalizedName'] + ", " + locationresponse['AdministrativeArea']['LocalizedName'] + " - " + locationresponse['Country']['LocalizedName']
            infolocal['codigolocal'] = locationresponse['Key']
            return infolocal
        except:

            return None

def pegarclima(codigolocal,nomelocal):
    CurrentConditionsapiurl= "http://dataservice.accuweather.com/currentconditions/v1/" + codigolocal + "?apikey=" +accuweatherapikey + "+&language=pt-br"
    r = requests.get( CurrentConditionsapiurl)
    if (r.status_code!=200):
        
        print('localização não encontrada')
        return None
    else:
        try:     
            CurrentConditionsresponse = json.loads(r.text)
                  
            clima = {}
            clima['textoclima'] = CurrentConditionsresponse[0]['WeatherText']
            clima['temperatura'] = CurrentConditionsresponse[0]['Temperature']['Metric']['Value']
            clima['hora'] = CurrentConditionsresponse[0]['LocalObservationDateTime']
            return clima
        except:
            return None        

##inicio do programa

try:
    coordenadas = pegarcoordenadas()
    local = codlocal(coordenadas['lat'],coordenadas['long'])
    
    climaatual = pegarclima(local['codigolocal'],local['nomelocal'])
  
    
    print ('Clima Atual em: ', local['nomelocal'], climaatual['hora'])
    print (climaatual['textoclima'])
    print ('Temperatura em: ' + str(climaatual['temperatura']) + "\xb0" + "C")
    repete2 = True
    while repete2 == True:
        consulta = input('deseja ver a previsão para os proximos dias?(s ou n): ')
        if consulta == 's' or consulta == 'n':
            if consulta == 's':
                codigolocal = '44127'
                fv.fivedias(codigolocal)
                coord2 = C2.coordenadas2()
                if coord2 == False:
                    repete2 = False
                else:
                    local = codlocal(coord2['lat'],coord2['long'])        
                    climaatual = pegarclima(local['codigolocal'],local['nomelocal'])
                              
                    print ('Clima Atual em: ', local['nomelocal'], climaatual['hora'])
                    print (climaatual['textoclima'])
                    print ('Temperatura em: ' + str(climaatual['temperatura']) + "\xb0" + "C")
                    repete2 = True                       
            else:
                coord2 = C2.coordenadas2()
                if coord2 == False:
                    repete2 = False
                else:
                    local = codlocal(coord2['lat'],coord2['long'])        
                    climaatual = pegarclima(local['codigolocal'],local['nomelocal'])
                              
                    print ('Clima Atual em: ', local['nomelocal'], climaatual['hora'])
                    print (climaatual['textoclima'])
                    print ('Temperatura em: ' + str(climaatual['temperatura']) + "\xb0" + "C")              
                    repete2 = True
        else:
            print('digite s pra sim ou n pra não')
            valid = True                
except:
    print('erro ao rodar o programa')
