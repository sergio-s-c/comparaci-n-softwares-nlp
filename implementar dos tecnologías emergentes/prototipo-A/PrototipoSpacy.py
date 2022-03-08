import threading
import os
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.es import Spanish
from spacy import displacy
import webbrowser
import time

def thread_bar(doc):
    displacy.serve(doc, style="dep")
    
   
    
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
            #Frase de ejemplo: El perro corre detrás de la pelota rojo mientras me como un helado de chocolate en el parque Europa
            frase= input("Introduzca una frase: ")

           #Para calcular el tiempo de ejecución descomentar la linea siguiente 
           #start_time = time()

            nlp = spacy.load("es_core_news_sm") #carga del modulo IA
            doc= nlp(frase) #procesado del string
            print("")
            print([token.text for token in doc]) #Tokenización de la frase
            print("")
            for token in doc:                   
                print(token.text, "-->",token.pos_ )  #imprime el token con el texto junto a su tipo de palabra
            #Para calcular el tiempo descomentar las dos linea siguiente   
            #elapsed_time = time() - start_time
            #print("Tiempo transcurrido: %0.10f segundos." % elapsed_time)
            print("")
            entradaOpc= input("¿Desea repetir?: (Si/No) ") 
            entradaOpc= entradaOpc.lower()
            os.system('cls')  

    elif (entrada == 2):
        while entradaOpc != "no":
            #Frase de ejemplo:Peter corre tras la pelota de fútbol y Sarah mira al cielo con sus prismáticos
            frase= input("Introduzca una frase: ")   

            #Para calcular el tiempo de ejecución descomentar la linea siguiente 
            #start_time = time()

            nlp = spacy.load("es_core_news_sm") #carga del modulo IA
            doc= nlp(frase) #procesado del string
            for token in doc:
                print(token.text, " | ",token.pos_, " | ", token.dep_,"-->", token.head.text ) #realización del analisis morfosintáctico

           
            webbrowser.open("http://localhost:5000/")
            x = threading.Thread(target=thread_bar, args=(doc,))
            x.start()
            time.sleep(3)
            #Para calcular el tiempo descomentar las dos linea siguiente   
            #elapsed_time = time() - start_time
            #print("Tiempo transcurrido: %0.10f segundos." % elapsed_time)
            print("")
            entradaOpc= input("¿Desea repetir?: (Si/No) ")
            entradaOpc= entradaOpc.lower() 
            os.system('cls')

    elif (entrada == 3):
        #Frase de ejemplo: La marca Apple procedente de EE.UU, fue superada el pasado miercorles por Samsung con su nuevo Galaxy Note 9
        while entradaOpc != "no":
            frase= input("Introduzca una frase: ")

            #Para calcular el tiempo de ejecución descomentar la linea siguiente 
            #start_time = time()

            nlp = spacy.load("es_core_news_sm") #carga del modulo IA
            doc = nlp(frase) #procesado del string
            for ent in doc.ents:  #realización del etiquetado
                print(ent.text, "-->",ent.label_ ) #spacy.explain explica cada etiqueta, Por ejemplo: spacy.explain("LOC") --> nombre de una localización politica o geográfica
       

            #Para calcular el tiempo descomentar las dos linea siguiente   
            #elapsed_time = time() - start_time
            #print("Tiempo transcurrido: %0.10f segundos." % elapsed_time)
            print("")
            entradaOpc=input("¿Desea repetir?: (Si/No) ")
            entradaOpc= entradaOpc.lower()
            os.system('cls')
    elif(entrada ==4):
        print()
    else:
        print("Introduzca un valor numérico comprendido entre el 1 y el 4 para seleccionar una opción")
