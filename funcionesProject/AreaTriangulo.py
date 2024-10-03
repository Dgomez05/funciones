# Ejemplo para calcular el area del tiangulo

#Variables de entrada
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#Invocar la funcion
resultado = calcularAreaTriangulo(base,altura)
print(f"El area del tiangulo cuya base {base} y altura {altura} es: {resultado}")

#Funcion con argumentos predeterminados
def my_function(country = "Colombia"):
    print("Im from " + country)

#Invocar la funcion
my_function()
my_function("Sweden")

#Argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante: " + args[2])

#Invocamos la funcion
mostrarEstudiantes("Emil","Tobias","Linus","Bill","Andres")

#Funcion para argumentos de palabras clave

def mostrarCarros(carro1, carro2, carro3):
    print("El carro es: " + carro2)

#Invocar
mostrarCarros(carro1= "BMW", carro3= "Ferrari", carro2= "Ford")

#Funcion para argumento arbitrario **kwargs
def mostrarCliente(**kwargs):
    print("Su apellido es: " + kwargs["apellido"])

#Invocamos
mostrarCliente(nombre = "Tobias", apellido= "Refsnes")

#Declaracion de paso
def miFuncion():
    pass

#Funciones integradas
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#Funcion pow - elevar un numero = 7^4
num1 = pow(7, 4)

print(num1)


