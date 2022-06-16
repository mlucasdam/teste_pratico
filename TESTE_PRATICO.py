# RESOLUÇÃO EXERCICIO 1:

# indice = 13
# soma = 0
# K = 0

# while (K < indice):
#         K += 1
#         soma = soma + K

# print (soma)
# RESULTADO = 91


# RESOLUÇÃO EXERCICIO 2:

# lista = ['1', '1']
# for contador in range(2,100):
#     lista.append(int(lista[len(lista) - 2]) + int(lista[len(lista) - 1]))

# chute = int(input("Qual termo quer encontrar: "))

# if chute in lista :
#     print("Você tem razão {} faz parte da sequencia de fibonatti".format(chute))
# else:
#     print("Não {} não faz parte da sequencia de fibonatti".format(chute))
# print ("FIM!")

# RESOLUÇÃO EXECICIO 3:

# a)1,3,5,7,...
# Após o primeiro termo, os termo seguintes são gerados somando 2 ao numero anterior, 
# concluindo que é uma progreção aritmética de razão = 2, portanto os proximo número serão: 9, 11, 13, 15,... 

# b)2,4,8,16,32,64,...
# Após o primeiro termo, os termo seguintes são gerados multiplicando 2 ao numero anterior, 
# concluindo que é uma progreção geométrica de razão = 2, portanto os proximo número serão: 128, 256, 512, 1024,...

# c)0,1,4,9,16,25,36,...
# Após o primeiro termo, os termo seguintes são gerados somando números impares ao numero anterior, 
# portanto: 
#           0   1    4    9    16     25    36 
#           0  0+1  1+3  4+5   9+7   16+9  25+11            
#logo os proximos termos serão: 49, 64, 81, 100,...

# d)4,16,36,64,...
# Esta sequencia de termos é uma progressão aritimética, sendo que sua razão r = 8 +razão anterior
# observando que, 4 para 16 foram somadas 12 unidades (r = 4+8), de 16 para 36 somadas 20 unidades(r = 12+8) e de 36 para 64 foram somadas 28 unidades (r = 20 + 8)
# portanto, os proximo números serão: 100, 144 ,196,...
#   r = 28 + 8 = 36 
#       36 + 64 = 100;
#
#   r = 36 + 8  = 44
#       44 + 100 = 144;
#
#   r = 44 + 8 = 52
#       52 + 144 = 196;


# e)1,1,2,3,5,8,...
# Esta sequencia de numeros é uma sequencia de fibonacci, portanto os proximos números serão: 13, 21, 34, 55...

# f)2,10,12,16,17,18,19,...
# Todos os termos desta sequencia de números começa com a letra "D", portando o proximo numero desta sequencia é o 200 (DUZENTOS)


# RESOLUÇÃO EXERCICIO 4: 

#a                100km                b             
#|-------------------------------------|
#-> 110km/hr                   80km/hr<-
 
# primeiro é necessario calcular o tempo em que os 2 se encontram, portanto:
# S = So + Vo * T + ((a * T²)/2)
# 100 = 0 + 80T + 110T²/2
# 0 = 40T + 110T² - 100 (EQUAÇÃO DO 2º GRAU)

# DELTA = (40*40) + (4 * 110  * 100)  
# print(DELTA ) RESULTADO 45600
# Baskhara:
#  x = -40 - √45600 / 2 * 110
#  x aproximadamente  = 1.15 horas


# Calculando o ponto de encontro: (do caminhão em relação a ribeirão preto)
# S = So + V * T
# S = 100 -80 * 1.25 (+10 minutos pelos pedagios)
# S = 0 km

# Calculando o ponto de encontro: (do carro em relação a franca)
# S = So + V * T
# S = 100 -110 * 1.05 (-10 minutos pelo sem parar)
# S = 15 km 

# O caminhão estará mais proximo pois ja vai ter chegado a ribeirão preto


# RESOLVENDO EXERCICIO 5: 

# txt  = "texto invertido" [::-1]
# print (txt)



