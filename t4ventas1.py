#Importacion de librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Creacion de arreglos con numpy
#Arreglo de ventas por semana
ventas_semana = np.array([150,200,170,220,300,250,190])
print("Ventas por semana: ", ventas_semana)

# Operaciones con arreglos
print("Promedio de ventas:",
np.mean(ventas_semana))
print("Ventas máxima:",
np.max(ventas_semana))
print("Ventas mínima:",
np.min(ventas_semana))

# Lectura de archivos CSV con pandas
datos_ventas = pd.read_csv(r"C:\Users\razie\OneDrive\Desktop\Escuela\programación logica y funcional\tec\octavo\plyf\Archivos csv\ventas.csv",
encoding='utf-8')

print("\nDatos de ventas:\n"
, datos_ventas)

# Visualización de datos con matplotlib
# Gráfica de pastel de Unidades Vendidas por Producto
plt.figure(figsize=(8, 8))
plt.pie(datos_ventas['Unidades Vendidas'], 
        labels=datos_ventas['Producto'].astype(str),
        autopct='%1.1f%%',
        colors=plt.cm.Paired.colors,
        startangle=90)
plt.title('Distribución de Unidades Vendidas por Producto')
plt.show()