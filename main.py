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

for i in range(2):
    dataPersonas= pd.read_sql("select * from covid19_automatas.persona where id_espacio in "
               f"(SELECT id_espacio FROM covid19_automatas.espacios where nombre='{listaEspacios[i]}' and etapa={i} and personas_contenidas>0) and etapa={i};"
                  , connection)
    dataEspacios= pd.read_sql(f"SELECT *, Trim(CONCAT(nombre, id_espacio)) As identificador FROM covid19_automatas.espacios where nombre='{listaEspacios[i]}' and etapa={i} and personas_contenidas>0;"
                  , connection)

    dataPersonasCasaMenores = dataPersonas[(dataPersonas["edad"] > 0) & (dataPersonas["edad"] < 2)]
    dataPersonasCasaAdultos = dataPersonas[(dataPersonas["edad"] > 1) & (dataPersonas["edad"] < 6)]
    dataPersonasCasaAncianos = dataPersonas[(dataPersonas["edad"] > 5)]

    data = {
        "personas_por_edad": [dataPersonasCasaAncianos["id_persona"].count(),
                              dataPersonasCasaAdultos["id_persona"].count(),
                              dataPersonasCasaMenores["id_persona"].count()],
        "edades": ["Personas Ancianas", "Personas Adultas", "Personas Jovenes"],
        "colores": ["#EE6055", "#60D394", "#AAF683"]
    }
    df = pd.DataFrame(data)

    plt.pie(df["personas_por_edad"], labels=df["edades"], autopct="%0.1f %%", colors=df["colores"])

    plt.savefig(f"data_{i}.png")
    plt.close()
    data2 = {
        "Personas": dataEspacios['personas_contenidas'],
        "Nombre_Casas": dataEspacios['identificador']
    }

    df2 = pd.DataFrame(data2)
    print(df2)
    plt.bar(data2["Nombre_Casas"], data2["Personas"], color='maroon',
            width=0.4)
    plt.savefig(f"data2_{i}.png")
    plt.close()


# dataPersonas= pd.read_sql("select * from covid19_automatas.persona where id_espacio in "
#                "(SELECT id_espacio FROM covid19_automatas.espacios where nombre='Casa' and etapa=0 and personas_contenidas>0) and etapa=0;"
#                   , connection)
#
# dataEspacios= pd.read_sql("SELECT *, Trim(CONCAT(nombre, id_espacio)) As identificador FROM covid19_automatas.espacios where nombre='Casa' and etapa=0 and personas_contenidas>0;"
#                   , connection)



#dataEspacios.plot(x="identificador", y="personas_contenidas", kind="bar")


# #print(dataEspacios['personas_contenidas'])
# # nombresCasas=pd.DataFrame(['Casa 1', 'Casa 2', 'Casa 3'], columns=['nombres'])
# # personasCasas=nombresCasas.join(personasTotalCasas)
#
# #personasCasas.plot(x="nombres", y="personas_contenidas", kind="bar")
# plt.pie(personasCasas["personas_contenidas"], labels=personasCasas["nombres"])
# plt.show()
#
# print(personasCasas)
# #print(pd.merge(dataEspacios['personas_contenidas'],nombresPersonas[1]))
# # ts = left
# # ts.plot(x="key", y="lval",kind="bar");
# # plt.show();
# casa1=dataPersonas[dataPersonas["casa"]==0]
# casa2=dataPersonas[dataPersonas["casa"]==3]
# casa3=dataPersonas[dataPersonas["casa"]==4]






#cursor.execute("SELECT * FROM covid19_automatas.espacios;")
#espacios=pd.dataPersonasFrame(dataPersonas=cursor, columns=nombreEspacios)


#cursor.execute("SELECT * FROM covid19_automatas.persona;")               "(SELECT id_espacio FROM covid19_automatas.espacios where nombre='Casa' and etapa=0 and personas_contenidas>0) and etapa=0;")
#personas = pd.dataPersonasFrame(dataPersonas=cursor.fetchall(), columns=nombresPersonas);


# ts = a.cumsum()
#
# ts.plot();
# plt.show();
