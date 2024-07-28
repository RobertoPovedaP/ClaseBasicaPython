#Ejercicio 1. Imprimir Hola, Mundo
import pdb

print("Hola. Mundo")

#Práctica con listas python
lista_rapp=[1,2,3,4,5,6,7,8]
print(lista_rapp)


lista_rapp.append("Rapp")
print(lista_rapp)

lista_rapp.insert(2,"leo")
print(lista_rapp)

elemento=lista_rapp.pop()
print(elemento)
print(lista_rapp)

lista_rapp.append("Rapp")
print(lista_rapp)

lista_rapp.pop(0)
print(lista_rapp)

lista_rapp.remove(3)
print(lista_rapp)

lista_rapp.reverse()
lista_2=lista_rapp
print(lista_2)
print(lista_rapp)

for i in range(len(lista_rapp)):
    if i==2:
        breakpoint() #punto de interrupción temporal 
        print(f"Valor actual: {i}")
    if i==3:
        breakpoint()
        print(f"Valor actual: {i}")
    #print(f"Índice: {i}: Elemento: {lista_rapp[i]}")



#Practica con diccionario python
dicc_pruebas={}

dicc_rapp_2={
    "nombre": "Roberto",
    "apellido": "Poveda",
    "edad": 36
}

dicc_rapp_2.update({"profesion":"Ingeniero en ciencias computacionales", "signo":"Leo", "fecha_nac":"3/8/1989", "pasatiempo":"ajedrez"})
print(dicc_rapp_2)

valor_eliminado=dicc_rapp_2.pop("signo")
print(valor_eliminado)
print(dicc_rapp_2)

del dicc_rapp_2["pasatiempo"]
print(dicc_rapp_2)

claves=dicc_rapp_2.keys()
print(claves)

valores=dicc_rapp_2.values()
print(valores)

items=dicc_rapp_2.items()
print(items)

for clavecita in dicc_rapp_2:
    print(clavecita)

for valores in dicc_rapp_2.values():
    print(valores)

for clave, valor in dicc_rapp_2.items():
    print(clave," -> ", valor)


