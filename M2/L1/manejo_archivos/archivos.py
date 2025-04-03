ejemplo = open("D:/Kodland/Python Pro/M2/L1/texto_leer.txt", "r", encoding="utf-8")
texto = ejemplo.read()
print(texto)
ejemplo.close() 

ejemplo2 = open("D:/Kodland/Python Pro/M2/L1/images.jpeg", "rb")
imagen = ejemplo2.read()
print(imagen)   
ejemplo2.close() 