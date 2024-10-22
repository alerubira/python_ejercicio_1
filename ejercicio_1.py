# Crear una lista vacía
mi_lista = []

# Pedir al usuario que ingrese 4 elementos
for i in range(4):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    mi_lista.append(elemento)  # Agregar el elemento a la lista

# Mostrar la lista completa
print("La lista completa es:", mi_lista)
