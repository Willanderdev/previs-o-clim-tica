from datetime import date
import requests
import json
accuweatherapikey = 'kGnMMlfUARcaZRgLqnErqP7HQlKziod6'
codigolocal = '44127'
def fivedias(codigolocal):
       CurrentConditionsapiurl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + codigolocal +"?apikey="+accuweatherapikey +"&language=pt-br&metric=true"
       r = requests.get(CurrentConditionsapiurl)
       if (r.status_code!=200):
              print('localização não encontrada')      
              return None
       else:
              try:
                     textoclima = json.loads(r.text)
                     repete = 0
                     while repete<5:

                            D = textoclima['DailyForecasts'][repete]['Date']
                            Date = D[0:10]
                            Date = Date.replace("-","")
                            #Date = int(Date)
                            Ano = Date[0:4]
                            year = int(Ano)
                            mes = Date[4:6]
                            month = int(mes)
                            dia = Date[6:8]
                            day = int(dia)

                            DIAS = ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-Feira','Sexta-feira','Sábado','Domingo']
                            data = date(year, month, day)
                            indice_da_semana = data.weekday()

                            if repete == 0:

                                   cabeçalho = "Previsao Climatica"
                                   print(cabeçalho.center(60, ' '))
                                   DIAS[indice_da_semana] = "Hoje"
                                   dia_da_semana = DIAS[indice_da_semana]
                                   print('')   
                                   print(dia_da_semana)
                                   print('Mínima: ', textoclima['DailyForecasts'][repete]['Temperature']['Minimum']['Value'])
                                   print('Maxima: ', textoclima['DailyForecasts'][repete]['Temperature']['Maximum']['Value'])
                                   print('Clima pela manhã: ', textoclima['DailyForecasts'][repete]['Day']['IconPhrase'])
                                   print('Clima pela noite: ', textoclima['DailyForecasts'][repete]['Night']['IconPhrase'])
                                   print('')
                                   repete = repete+1
                            else:

                                   dia_da_semana = DIAS[indice_da_semana]
                                   print('')   
                                   print(dia_da_semana)
                                   print('Mínima: ', textoclima['DailyForecasts'][repete]['Temperature']['Minimum']['Value'])
                                   print('Maxima: ', textoclima['DailyForecasts'][repete]['Temperature']['Maximum']['Value'])
                                   print('Clima pela manhã: ', textoclima['DailyForecasts'][repete]['Day']['IconPhrase'])
                                   print('Clima pela noite: ', textoclima['DailyForecasts'][repete]['Night']['IconPhrase'])
                                   print('')
                                   repete = repete+1

              except:
                     return None
