#Solicitamos los datos usuario
nombre = input("Su nombre(s) por favor: ")  #nombre
apellidoP = input("Su apellido paterno por favor: ") #apellido paterno
apellidoM = input("Su apellido materno por favor: ") #apellido materno
#Se pide la edad que siempre es un entero por eso pondremos el int antes del (input)
edad = int(input("Su edad en años por favor: "))
#como la altura es en metros y no centimetros hay que ponerle punto y por eso es un flotante float()
altura = float(input ("Su altura en metros por favor (ejemplo 1.45): "))
#La masa en kilogramos tambien puede tener decimales asi que la dejamos flotante float()
masa = float(input("Su masa en kilogramos por favor (ejemplo 89.200): "))
#al tener los datos anteriores calcularemos IMC con la siguiente ecuacion 
#masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
IMC = masa / altura**2
#Generaremos un print que nos diga si es menor o mayor de edad
if(edad < 18):
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")
#de la pagina oficial del ISSSTE https://www.gob.mx/issste/es/articulos/que-es-el-indice-de-masa-corporal?idiom=es
#descargamos los datos siguientes que nos indicaran nuestro IMC
print("Su IMC es de: " + str(IMC))
#Realizamos las distintas variables publicadas en el articulo para generar un resultado de los datos antes capturados
if IMC >= 0 and IMC <= 18.19 :
    print ("Peso bajo")
elif IMC >= 18.50 and IMC <= 24.99:
    print ("Peso normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print ("Sobre peso")
elif IMC >= 30.00 and IMC <= 34.99:
    print ("Obesidad leve")
elif IMC >= 35.00 and IMC <= 39.99:
    print ("Obesidad media")
elif IMC >= 40.00:
    print ("Obesidad morbida")



