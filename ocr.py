# Coordenadas de cada número
NUMEROS = {0: (),
           1: (),
           2: (),
           3: (),
           4: (),
           5: (),
           6: (),
           7: (),
           8: (),
           9: ()}

# Importando bibliotecas
import sys

# Função que recebe as coordenadas do usuário e retorna uma lista
def recebe_lista_usuario():
    print("Informe a seguir as coordenadas do seu número!")
    contador = 0
    coordenadas_usuario = []
    while (contador < 8):
        contador += 1
        print("Digite o número", contador)
        numero = float(input("=> \t"))
        coordenadas_usuario.append(numero)
    return coordenadas_usuario


#Função que calcula a distância entre as coordenadas do usuario e as coordenadas de cada NUMERO
def calcula_distancias(lista):
    d0 = ((NUMEROS[0][0] - lista[0])**2 + (NUMEROS[0][1] - lista[1])**2 + (NUMEROS[0][2] - lista[2])**2 + (NUMEROS[0][3] - lista[3])**2 + (NUMEROS[0][4] - lista[4])**2 + (NUMEROS[0][5] - lista[5])**2 + (NUMEROS[0][6] - lista[6])**2 + (NUMEROS[0][7] - lista[7])**2) ** (1/2)
    d1 = ((NUMEROS[1][0] - lista[0])**2 + (NUMEROS[1][1] - lista[1])**2 + (NUMEROS[1][2] - lista[2])**2 + (NUMEROS[1][3] - lista[3])**2 + (NUMEROS[1][4] - lista[4])**2 + (NUMEROS[1][5] - lista[5])**2 + (NUMEROS[1][6] - lista[6])**2 + (NUMEROS[1][7] - lista[7])**2) ** (1/2)
    d2 = ((NUMEROS[2][0] - lista[0])**2 + (NUMEROS[2][1] - lista[1])**2 + (NUMEROS[2][2] - lista[2])**2 + (NUMEROS[2][3] - lista[3])**2 + (NUMEROS[2][4] - lista[4])**2 + (NUMEROS[2][5] - lista[5])**2 + (NUMEROS[2][6] - lista[6])**2 + (NUMEROS[2][7] - lista[7])**2) ** (1/2)
    d3 = ((NUMEROS[3][0] - lista[0])**2 + (NUMEROS[3][1] - lista[1])**2 + (NUMEROS[3][2] - lista[2])**2 + (NUMEROS[3][3] - lista[3])**2 + (NUMEROS[3][4] - lista[4])**2 + (NUMEROS[3][5] - lista[5])**2 + (NUMEROS[3][6] - lista[6])**2 + (NUMEROS[3][7] - lista[7])**2) ** (1/2)
    d4 = ((NUMEROS[4][0] - lista[0])**2 + (NUMEROS[4][1] - lista[1])**2 + (NUMEROS[4][2] - lista[2])**2 + (NUMEROS[4][3] - lista[3])**2 + (NUMEROS[4][4] - lista[4])**2 + (NUMEROS[4][5] - lista[5])**2 + (NUMEROS[4][6] - lista[6])**2 + (NUMEROS[4][7] - lista[7])**2) ** (1/2)
    d5 = ((NUMEROS[5][0] - lista[0])**2 + (NUMEROS[5][1] - lista[1])**2 + (NUMEROS[5][2] - lista[2])**2 + (NUMEROS[5][3] - lista[3])**2 + (NUMEROS[5][4] - lista[4])**2 + (NUMEROS[5][5] - lista[5])**2 + (NUMEROS[5][6] - lista[6])**2 + (NUMEROS[5][7] - lista[7])**2) ** (1/2)
    d6 = ((NUMEROS[6][0] - lista[0])**2 + (NUMEROS[6][1] - lista[1])**2 + (NUMEROS[6][2] - lista[2])**2 + (NUMEROS[6][3] - lista[3])**2 + (NUMEROS[6][4] - lista[4])**2 + (NUMEROS[6][5] - lista[5])**2 + (NUMEROS[6][6] - lista[6])**2 + (NUMEROS[6][7] - lista[7])**2) ** (1/2)
    d7 = ((NUMEROS[7][0] - lista[0])**2 + (NUMEROS[7][1] - lista[1])**2 + (NUMEROS[7][2] - lista[2])**2 + (NUMEROS[7][3] - lista[3])**2 + (NUMEROS[7][4] - lista[4])**2 + (NUMEROS[7][5] - lista[5])**2 + (NUMEROS[7][6] - lista[6])**2 + (NUMEROS[7][7] - lista[7])**2) ** (1/2)
    d8 = ((NUMEROS[8][0] - lista[0])**2 + (NUMEROS[7][1] - lista[1])**2 + (NUMEROS[8][2] - lista[2])**2 + (NUMEROS[8][3] - lista[3])**2 + (NUMEROS[8][4] - lista[4])**2 + (NUMEROS[8][5] - lista[5])**2 + (NUMEROS[8][6] - lista[6])**2 + (NUMEROS[8][7] - lista[7])**2) ** (1/2)
    d9 = ((NUMEROS[9][0] - lista[0])**2 + (NUMEROS[7][1] - lista[1])**2 + (NUMEROS[9][2] - lista[2])**2 + (NUMEROS[9][3] - lista[3])**2 + (NUMEROS[9][4] - lista[4])**2 + (NUMEROS[9][5] - lista[5])**2 + (NUMEROS[9][6] - lista[6])**2 + (NUMEROS[9][7] - lista[7])**2) ** (1/2)

    return {0:d0, 1:d1, 2:d2, 3:d3, 4:d4, 5:d5, 6:d6, 7:d7, 8:d8, 9:d9}
    
#Função recebe um dicionário e retorna qual tem o menor valor
def calcula_menor(dicionario_distancias):
	menor: float = sys.maxsize
	resultado = 0
	for num, distancia in dicionario_distancias.items():
		if(distancia < menor):
			menor = distancia
			resultado = num
	return resultado
# Função principal
def main():
    distancias = calcula_distancias(recebe_lista_usuario())
    print("Suas coordenadas correspondem ao número:", calcula_menor(distancias))

main()