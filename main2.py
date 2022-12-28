import pandas as pd
import numpy as np
import pymysql
import matplotlib.pyplot as plt

listaEspacios=["Casa", "Trasporte"]
etapas=range(2)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='MyNewPass',
    db='covid19_automatas'
)
cursor=connection.cursor()

dataPersonas= pd.read_sql("select*,  CONCAT('Edad: ',  edad) As identificador from covid19_automatas.persona where etapa=0;"
              , connection)
#dataEspacios= pd.read_sql(f"SELECT *, Trim(CONCAT(nombre, id_espacio)) As identificador FROM covid19_automatas.espacios where nombre='{listaEspacios[i]}' and etapa={i} and personas_contenidas>0;"
#              , connection)

dataPersonas["identificador"].value_counts().plot.bar()
plt.savefig(f"personasEdad.png")
plt.close()