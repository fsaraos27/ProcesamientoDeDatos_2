import pandas as pd

""" RUT Nombre Genero Fecha_Nacimiento Previsión Monto_Deuda """

print("")
data = pd.read_csv("/Users/franciscosaraosgarcia/Desktop/Ejercicios_Ucatolica/Caso_Practico1/datos_pacientes.csv", encoding = "utf-8", sep = ";")
df_pacientes = pd.DataFrame(data)
# Muestra de informacion como Data Frame
print(df_pacientes)

print(df_pacientes.loc[(df_pacientes["RUT"].str[-1:] == "9") & (df_pacientes["Genero"] == "MASCULINO") & (df_pacientes["Monto_Deuda"] > 1000000)  ])

#for index, row in df_pacientes.iterrows():
    	#print(row["RUT"])

df_pacientes.columns = ["dia", "mes", "año", "dia", "mes", "año"]
print(df_pacientes)

# Trae la columa Monto Deuda
print(df_pacientes["Monto_Deuda"])

# Trae la fila 651 del data Frame
print(df_pacientes.loc[651])

# Trae las filas del 100 al 200
print(df_pacientes.loc[100:200])

# Trae Rut entre el 100 y 200
print(df_pacientes.loc[100:200]["RUT"])

print(df_pacientes.loc[100:200]["Nombre"])

# Clientes solo FONASA
print(df_pacientes.loc[df_pacientes["Previsión"] == "FONASA" ])

# Monto mayor a $1.000.000
print(df_pacientes.loc[df_pacientes["Monto_Deuda"] > 1000000 ])

# Agrega la columna Nacionalidad al data Frame
df_pacientes["Nacionalidad"] = "CHILE"
print(df_pacientes)

# Se agrega un 3% de reajuste a Monto Deuda
print(df_pacientes["Monto_Deuda"])
df_pacientes["Monto_Deuda"] = df_pacientes["Monto_Deuda"] * 1.03
print(df_pacientes["Monto_Deuda"])

# Eliminar columna Nacionalidad
del df_pacientes["Nacionalidad"]
print(df_pacientes)
print("Columna Nacionalidad eliminada ")

# Mostrar descripcion del Data Frame
print(df_pacientes.describe())

# Muestra cuantas filas y columnas tiene el DataFrame
print(df_pacientes.shape)

# Cambiar nombre a la columna
df_pacientes = df_pacientes.rename(columns = {"Fecha_Nacimiento" : "FECHA_NAC"})
print(df_pacientes.dtypes)
print(df_pacientes)
df_pacientes = df_pacientes.rename(columns = {"FECHA_NAC" : "Fecha_Nacimiento"})
print(df_pacientes)

# Cambiar de tipo de dato una columna
print(df_pacientes.dtypes)
df_pacientes["Monto_Deuda"] = df_pacientes["Monto_Deuda"].astype("object")
print(df_pacientes.dtypes)
df_pacientes["Monto_Deuda"] = df_pacientes["Monto_Deuda"].astype("float64")
print(df_pacientes.dtypes)

# permite conocer la cantidad de datos que tiene el DataFrame
print("Esta base de datos tiene: ", df_pacientes.size, "registros ")

# Cambia el index (indice) de la primera columna
df_pacientes = df_pacientes.set_index("RUT")
print(df_pacientes)

# trae los primeros 5 datos del Dataframe (head)
print(df_pacientes.head())

# trae los ultimos 5 datos del Dataframe (tail)
print(df_pacientes.tail())

# traer clientes sin index utilizando iloc
print(df_pacientes.iloc[0:1000])
print(df_pacientes.iloc[400])

# Agregar datos a columnas
print(df_pacientes.iloc[0])
df_pacientes = df_pacientes.fillna("SIN INFO")
print(df_pacientes.iloc[0])

# print("AGREGAR FILAS AL DATA FRAME ")

# f_pacientes = df.append(df2)

print("Guardar cambios: ")
df_pacientes.to_csv("/Users/franciscosaraosgarcia/Desktop/ejercicios/Caso_Practico1/datos_pacientes_reajuste.csv", sep = ";", index = False)
