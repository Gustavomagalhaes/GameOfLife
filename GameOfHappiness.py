#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from random import randint
import math
clear = lambda: os.system('clear')

def montarMatrix():
    global matrixSize
    while True:    
        # value = raw_input("\nDefina o tamanho da matrix: ")
        value = "15"
        if value.isdigit():
            matrixSize = int(float(value))
            break
        print ("     Apenas números inteiro são aceitos")
    
    # global matrix
    # matrix = []
    # for i in range(matrixSize+2):                    
    #     tmp = []                                    
    #     for j in range(matrixSize+2):              
    #         tmp.append('.')                      
    #     matrix.append(tmp)                        

    global happiness
    happiness = []
    for i in range(matrixSize+2):                    
        tmp = []                                    
        for j in range(matrixSize+2):
            # tmp.append(".")
            tmp.append(str(randint(0,9)))
        # matrix.append(tmp)
        happiness.append(tmp)  

def printMatrix():
    clear()
    
    # Define label X AXIS
    # global labelX
    labelX = "    "                                 
    for m in range(1,matrixSize+1):                    
        labelX = labelX+" "+"{0:3d}".format(m)      
    labelX = "\n"+labelX+"\n"
    print (labelX)
    
    # Define label Y AXIS
    for i in range(1,matrixSize+1):
        labelY = ''
        for j in range(1,matrixSize+1):
            # labelY = labelY + '   ' + matrix[i][j]
            labelY = labelY + '   ' + happiness[i][j]
        print ("{0:3d}".format(i) + " " + labelY + "\n")

# def definirCelulasVivas():
#     while True:
#         printMatrix()
#         lista = []
#         value = raw_input("\nDefina a celula viva. 'x,y' (ENTER to start) ")
#         if value == '':
#             break
#         try:
#             a,b = value.split(',')
#             if (a.isdigit() and b.isdigit()):
#                 if (((int(a) < matrixSize+1) and (int(a) > 0)) and
#                     ((int(b) < matrixSize+1) and (int(b) > 0))):
#                     matrix[int(a)][int(b)] = 'O'
#                     lista.append(value)
#                 else:
#                     printMatrix()
#                     raw_input("\n     As células devem estar no intervalo de 1 à {0}!".format(matrixSize)+" << ENTER TO CONTINUE >>" )
#             else:
#                 print ("     Somente números!")
#         except ValueError:
#             printMatrix()
#             raw_input("\n     Insira as células neste formato: 'x,y' << ENTER TO CONTINUE >>")
                
# def run():
#     while True:
#         printMatrix()
#         matrixTemp = []
#         for i in range(matrixSize+2):
#             temp = []
#             for j in range(matrixSize+2):
#                 temp.append(matrix[i][j])
#             matrixTemp.append(temp)    
    
#         for i in range(1,matrixSize+1):
#             for j in range(1,matrixSize+1):
#                 vivos = 0
#                 if (matrix[i-1][j] == 'O'):
#                     vivos = vivos + 1
#                 if (matrix[i+1][j] == 'O'):
#                     vivos = vivos + 1
#                 if (matrix[i][j-1] == 'O'):
#                     vivos = vivos + 1
#                 if (matrix[i][j+1] == 'O'):
#                     vivos = vivos + 1
#                 if (matrix[i-1][j+1] == 'O'):
#                     vivos = vivos + 1
#                 if (matrix[i-1][j-1] == 'O'):
#                     vivos = vivos + 1
#                 if (matrix[i+1][j+1] == 'O'):
#                     vivos = vivos + 1
#                 if (matrix[i+1][j-1] == 'O'):
#                     vivos = vivos + 1
    
#                 if ((matrix[i][j] == 'O') and ((vivos > 3) or (vivos < 2))):
#                     matrixTemp[i][j] = '.'                                       # DEATH
                
#                 if ((matrix[i][j] == '.') and (vivos == 3)):
#                     matrixTemp[i][j] = 'O'                                       # LIVE

#         # Checar se a simulação está parada    
#         if (matrixTemp == matrix):
#             print "\n     A simulação acabou!"
#             break
    
#         # Clonando as matrizez   
#         for i in range(matrixSize+2):
#             temp = []
#             for j in range(matrixSize+2):
#                 temp.append(matrixTemp[i][j])
#             matrix[i] = temp
    
#         time.sleep(1)

def runHappiness():
    while True:
        printMatrix()
        matrixTemp = []
        for i in range(matrixSize+2):
            temp = []
            for j in range(matrixSize+2):
                temp.append(happiness[i][j])
            matrixTemp.append(temp)    
    
        for i in range(1,matrixSize+1):
            for j in range(1,matrixSize+1):
                
                averageHappiness = (\
                int(happiness[i-1][j]) + \
                int(happiness[i+1][j]) + \
                int(happiness[i][j-1]) + \
                int(happiness[i][j+1]) + \
                int(happiness[i-1][j+1]) + \
                int(happiness[i-1][j-1]) + \
                int(happiness[i+1][j+1]) + \
                int(happiness[i+1][j-1]))/8
                
                happyPeople = 0
                
                if (int(happiness[i-1][j]) >= 5):
                    happyPeople = happyPeople + 1
                if (int(happiness[i+1][j]) >= 5):
                    happyPeople = happyPeople + 1
                if (int(happiness[i][j-1]) >= 5):
                    happyPeople = happyPeople + 1
                if (int(happiness[i][j+1]) >= 5):
                    happyPeople = happyPeople + 1
                if (int(happiness[i-1][j+1]) >= 5):
                    happyPeople = happyPeople + 1
                if (int(happiness[i-1][j-1]) >= 5):
                    happyPeople = happyPeople + 1
                if (int(happiness[i+1][j+1]) >= 5):
                    happyPeople = happyPeople + 1
                if (int(happiness[i+1][j-1]) >= 5):
                    happyPeople = happyPeople + 1
    
                # HAPPIER
                if ((averageHappiness >= 4) or (happyPeople >= 4)) and matrixTemp[i][j] != "9":
                    matrixTemp[i][j] = str(int(matrixTemp[i][j]) + 1)       

                # SADDER
                if ((averageHappiness < 4) or (happyPeople < 4)) and matrixTemp[i][j] != "0":
                    matrixTemp[i][j] = str(int(matrixTemp[i][j]) - 1)         

        # Checar se a simulação está parada    
        if (matrixTemp == happiness):
            print "\n     A simulação acabou!"
            break
    
        # Clonando as matrizez   
        for i in range(matrixSize+2):
            temp = []
            for j in range(matrixSize+2):
                temp.append(matrixTemp[i][j])
            happiness[i] = temp
        time.sleep(2)

montarMatrix()
# definirCelulasVivas()
runHappiness()


