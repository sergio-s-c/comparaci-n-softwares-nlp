import os
import nltk
from nltk.corpus import brown

from nltk.corpus import treebank
import webbrowser
import time
from nltk.corpus.reader.dependency import DependencyCorpusView
from nltk.grammar import DependencyGrammar
from nltk.parse import dependencygraph

from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer


    
   
    
entradaOpc =""
entrada= 0

while (entrada != 4):
    entradaOpc=""
    print("1) Clasificación de palabras")
    print("2) Clasificación de dependencias")
    print("3) Reconocimiento de entidades")
    print("4) Cerrar")
    try:
        entrada= int(input())
    except:
        print("Introduzca un valor numérico comprendido entre el 1 y el 4 para seleccionar una opción")

    os.system('cls')

    if(entrada == 1):
        
        while entradaOpc != "no":
            #Frase de ejemplo:The dog runs after the red ball while I eat a chocolate ice cream in the Europa park
            frase= input("Introduzca una frase en inglés: ")

           #Para calcular el tiempo de ejecución descomentar la linea siguiente 
           #start_time = time()

            
            tokens=nltk.word_tokenize(frase)    #Tokenizamos la frase dividiéndola en palabras
            tagged=nltk.pos_tag(tokens)     #Se le asigna a cada palabra su categoría gramatical
           
            print(tagged)
            print("")

            entradaOpc= input("¿Desea repetir?: (Si/No) ") 
            entradaOpc= entradaOpc.lower()
            os.system('cls')  

    elif (entrada == 2):
        while entradaOpc != "no":
            #Frase de ejemplo: Peter runs after the ball and Sarah looks at the sky
            frase= input("Introduzca una frase en inglés: ")
            #Para calcular el tiempo de ejecución descomentar la linea siguiente 
            #start_time = time()

            tokens=nltk.word_tokenize(frase)
            tagged=nltk.pos_tag(tokens)

            chunkGram= r"""Chunk: {<NN.?>*<VB.?|IN|DT|TO>*<NN.?>?}"""   #Se establece las características que debe cumplir una parte de la frase para considerarse un chunk independiente   
            chunkParser=nltk.RegexpParser(chunkGram)    #Le pasamos los patrones de chunkGram para realizar un análisis de la frase basado en su gramática
            chunked=chunkParser.parse(tagged)   #Se le aplica la división por chunks a la frase
            chunked.draw()  #Se dibuja el resultado
            print(chunked)

      
            

            print("")
            entradaOpc= input("¿Desea repetir?: (Si/No) ")
            entradaOpc= entradaOpc.lower() 
            os.system('cls')

    elif (entrada == 3):
        #Frase de ejemplo: The Apple brand from the US was overcome last Wednesday by Samsung with its new Galaxy Note 9
        while entradaOpc != "no":
            frase= input("Introduzca una frase en inglés: ")
            #Para calcular el tiempo de ejecución descomentar la linea siguiente 
            #start_time = time()
            
            tokens=nltk.word_tokenize(frase)
            tagged=nltk.pos_tag(tokens)

            entities=nltk.ne_chunk(tagged)      #Se buscan las entidades con nombre en la frase
            entities.draw()
            print (entities)
           
            
            print("")
            entradaOpc=input("¿Desea repetir?: (Si/No) ")
            entradaOpc= entradaOpc.lower()
            os.system('cls')
    elif(entrada ==4):
        print()
    else:
        print("Introduzca un valor numérico comprendido entre el 1 y el 4 para seleccionar una opción")
