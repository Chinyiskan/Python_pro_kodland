ejemplo = open("D:/Kodland/Python Pro/M2/L1/texto_remover.txt", "w")
text = 'Hola, soy un texto de ejemplo para el archivo de texto.'
ejemplo.write(text)
ejemplo.close()

ejemplo2 = open("D:/Kodland/Python Pro/M2/L1/texto_agregar.txt", "a")
text2 = ' Hola, soy un texto de ejemplo para el archivo de texto.'
ejemplo2.write(text2)
ejemplo2.close()