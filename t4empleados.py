import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Productividad semanal
productividad = np.array([75, 80, 90, 85, 70])

# Mostrar promedio y valor máximo
print("Promedio de productividad:", np.mean(productividad))
print("Valor máximo de productividad:", np.max(productividad))

# Asegúrate de que el archivo empleados.csv esté en la misma carpeta
empleados = pd.read_csv("C:\\Users\\razie\OneDrive\Desktop\\Escuela\\programación logica y funcional\\tec\\octavo\\plyf\\Archivos csv\\empleados.csv")

# Mostrar empleados del departamento "Ventas"
ventas = empleados[empleados["Departamento"] == "Ventas"]
print("\nEmpleados del departamento de Ventas:")
print(ventas[["Nombre"]])

# Agregar columna 'Bono' que es 10% del salario
empleados["Bono"] = empleados["Salario"] * 0.10

# Mostrar DataFrame con la nueva columna
print("\nDataFrame con columna 'Bono':")
print(empleados.head())

# Gráfica de barras de salario ---
plt.figure(figsize=(12, 6))
plt.bar(empleados["Nombre"], empleados["Salario"], color='skyblue')
plt.xticks(rotation=90)
plt.title("Salario de empleados")
plt.xlabel("Empleado")
plt.ylabel("Salario")
plt.tight_layout()
plt.show()
