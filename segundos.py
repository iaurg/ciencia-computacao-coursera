entrada = input("Por favor, entre com o número de segundos que deseja converter: ")

totalSegundos = int(entrada)

dias = totalSegundos // 86400
dia_sobra = totalSegundos % 86400

hora = dia_sobra // 3600
hora_sobra = dia_sobra % 3600

minutos = hora_sobra // 60
minutos_sobra = hora_sobra % 60

segundos = minutos_sobra // 60
segundosFinal = minutos_sobra % 60

print(dias, "dias,", hora, "horas,", minutos, "minutos e", segundosFinal, "segundos.")