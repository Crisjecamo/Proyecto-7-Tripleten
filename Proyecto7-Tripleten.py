#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduccion" data-toc-modified-id="Introduccion-1">Introduccion</a></span></li><li><span><a href="#DataFrame-1" data-toc-modified-id="DataFrame-1-2">DataFrame 1</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Observacion-describe():" data-toc-modified-id="Observacion-describe():-2.0.1">Observacion describe():</a></span></li><li><span><a href="#Observacion-duplicated():" data-toc-modified-id="Observacion-duplicated():-2.0.2">Observacion duplicated():</a></span></li><li><span><a href="#Observacion-de-los-datos:" data-toc-modified-id="Observacion-de-los-datos:-2.0.3">Observacion de los datos:</a></span></li></ul></li></ul></li><li><span><a href="#DataFrame-2" data-toc-modified-id="DataFrame-2-3">DataFrame 2</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Observacion-describe():" data-toc-modified-id="Observacion-describe():-3.0.1">Observacion describe():</a></span></li><li><span><a href="#Observacion-duplicated():" data-toc-modified-id="Observacion-duplicated():-3.0.2">Observacion duplicated():</a></span></li><li><span><a href="#Observacion-de-los-datos:" data-toc-modified-id="Observacion-de-los-datos:-3.0.3">Observacion de los datos:</a></span></li></ul></li></ul></li><li><span><a href="#DataFrame-3" data-toc-modified-id="DataFrame-3-4">DataFrame 3</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Observacion-describe():" data-toc-modified-id="Observacion-describe():-4.0.1">Observacion describe():</a></span></li><li><span><a href="#Observacion-duplicated():" data-toc-modified-id="Observacion-duplicated():-4.0.2">Observacion duplicated():</a></span></li></ul></li><li><span><a href="#Observacion-de-los-datos:" data-toc-modified-id="Observacion-de-los-datos:-4.1">Observacion de los datos:</a></span></li></ul></li><li><span><a href="#Analisis-de-los-Datos" data-toc-modified-id="Analisis-de-los-Datos-5">Analisis de los Datos</a></span><ul class="toc-item"><li><span><a href="#identificar-los-10-principales-compañias-con-mayores-viajes" data-toc-modified-id="identificar-los-10-principales-compañias-con-mayores-viajes-5.1">identificar los 10 principales compañias con mayores viajes</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.1.1">Observacion:</a></span></li></ul></li><li><span><a href="#identificar-los-10-principales-barrios-con-mayores-viajes-finalizados" data-toc-modified-id="identificar-los-10-principales-barrios-con-mayores-viajes-finalizados-5.2">identificar los 10 principales barrios con mayores viajes finalizados</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.2.1">Observacion:</a></span></li></ul></li><li><span><a href="#Impacto-del-clima-en-la-duracion-de-los-viajes" data-toc-modified-id="Impacto-del-clima-en-la-duracion-de-los-viajes-5.3">Impacto del clima en la duracion de los viajes</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.3.1">Observacion:</a></span></li></ul></li><li><span><a href="#Horas-con-mayor-cantidad-de-viajes" data-toc-modified-id="Horas-con-mayor-cantidad-de-viajes-5.4">Horas con mayor cantidad de viajes</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.4.1">Observacion:</a></span></li></ul></li><li><span><a href="#Cantidad-de-Viajes-por-horas-y-dias" data-toc-modified-id="Cantidad-de-Viajes-por-horas-y-dias-5.5">Cantidad de Viajes por horas y dias</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.5.1">Observacion:</a></span></li></ul></li><li><span><a href="#Promedio-duracion-de-viajes-por-horas-y-dias" data-toc-modified-id="Promedio-duracion-de-viajes-por-horas-y-dias-5.6">Promedio duracion de viajes por horas y dias</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.6.1">Observacion:</a></span></li></ul></li><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.7">Observacion:</a></span></li><li><span><a href="#Duracion-promedio-de-viajes-por-horas-segun-las-condiciones-climaticas" data-toc-modified-id="Duracion-promedio-de-viajes-por-horas-segun-las-condiciones-climaticas-5.8">Duracion promedio de viajes por horas segun las condiciones climaticas</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-5.8.1">Observacion:</a></span></li></ul></li></ul></li><li><span><a href="#Prueba-de-hipótesis" data-toc-modified-id="Prueba-de-hipótesis-6">Prueba de hipótesis</a></span><ul class="toc-item"><li><span><a href="#Observacion:" data-toc-modified-id="Observacion:-6.1">Observacion:</a></span></li></ul></li><li><span><a href="#Conclusion-General" data-toc-modified-id="Conclusion-General-7">Conclusion General</a></span><ul class="toc-item"><li><span><a href="#Top-10-compañias-populares." data-toc-modified-id="Top-10-compañias-populares.-7.1">Top 10 compañias populares.</a></span></li><li><span><a href="#Top-10-Barrios-mas-concurridos." data-toc-modified-id="Top-10-Barrios-mas-concurridos.-7.2">Top 10 Barrios mas concurridos.</a></span></li><li><span><a href="#Promedio-total-de-duracion-del-viaje-dependiendo-de-la-condicion-climatica." data-toc-modified-id="Promedio-total-de-duracion-del-viaje-dependiendo-de-la-condicion-climatica.-7.3">Promedio total de duracion del viaje dependiendo de la condicion climatica.</a></span></li><li><span><a href="#Previsualizacion-de-los-datos-en-un-grafico." data-toc-modified-id="Previsualizacion-de-los-datos-en-un-grafico.-7.4">Previsualizacion de los datos en un grafico.</a></span></li><li><span><a href="#Cantidad-de-Viajes-por-Hora-y-Dias." data-toc-modified-id="Cantidad-de-Viajes-por-Hora-y-Dias.-7.5">Cantidad de Viajes por Hora y Dias.</a></span></li><li><span><a href="#Promedio-duracion-de-viajes-por-dia-y-hora." data-toc-modified-id="Promedio-duracion-de-viajes-por-dia-y-hora.-7.6">Promedio duracion de viajes por dia y hora.</a></span></li><li><span><a href="#Duracion-pomedio-de-viajes-por-horas-segun-las-condiciones-climaticas" data-toc-modified-id="Duracion-pomedio-de-viajes-por-horas-segun-las-condiciones-climaticas-7.7">Duracion pomedio de viajes por horas segun las condiciones climaticas</a></span></li><li><span><a href="#Hipotesis" data-toc-modified-id="Hipotesis-7.8">Hipotesis</a></span></li></ul></li><li><span><a href="#Recomendaciones-Basadas-en-el-Análisis:" data-toc-modified-id="Recomendaciones-Basadas-en-el-Análisis:-8">Recomendaciones Basadas en el Análisis:</a></span><ul class="toc-item"><li><span><a href="#Optimización-de-Recursos-para-Empresas-de-Taxis:" data-toc-modified-id="Optimización-de-Recursos-para-Empresas-de-Taxis:-8.1">Optimización de Recursos para Empresas de Taxis:</a></span></li><li><span><a href="#Estrategias-de-Marketing:" data-toc-modified-id="Estrategias-de-Marketing:-8.2">Estrategias de Marketing:</a></span></li><li><span><a href="#Ajuste-de-Tarifas-Basado-en-la-Demanda:" data-toc-modified-id="Ajuste-de-Tarifas-Basado-en-la-Demanda:-8.3">Ajuste de Tarifas Basado en la Demanda:</a></span></li><li><span><a href="#Mejoras-en-la-Experiencia-del-Usuario:" data-toc-modified-id="Mejoras-en-la-Experiencia-del-Usuario:-8.4">Mejoras en la Experiencia del Usuario:</a></span></li><li><span><a href="#Consideraciones-Climáticas:" data-toc-modified-id="Consideraciones-Climáticas:-8.5">Consideraciones Climáticas:</a></span></li><li><span><a href="#Expansión-de-Flotas-en-Barrios-de-Crecimiento:" data-toc-modified-id="Expansión-de-Flotas-en-Barrios-de-Crecimiento:-8.6">Expansión de Flotas en Barrios de Crecimiento:</a></span></li></ul></li></ul></div>

# ## Introduccion
# 
# En este proyecto, llevaremos a cabo un análisis exploratorio de datos utilizando Python para investigar patrones y tendencias en el servicio de taxis en Chicago. Contamos con dos conjuntos de datos clave que nos permitirán profundizar en el comportamiento de las empresas de taxis y los patrones de finalización de viajes en diferentes barrios de la ciudad durante noviembre de 2017.
# 
# El primer conjunto de datos, denominado project_sql_result_01.csv, contiene información sobre el número de viajes realizados por diferentes compañías de taxis durante los días 15 y 16 de noviembre de 2017. Este dataset nos permitirá analizar la actividad de las empresas de taxis en un corto período y comparar su desempeño.
# 
# El segundo archivo, project_sql_result_04.csv, proporciona datos sobre los barrios de Chicago donde finalizaron los viajes y el promedio de viajes que terminaron en cada uno de ellos durante todo el mes de noviembre de 2017. Este conjunto de datos es crucial para identificar los barrios más populares como destinos finales y para entender la distribución geográfica del servicio de taxis en la ciudad.
# 
# Los objetivos principales de esta fase del proyecto incluyen:
# 
# * Importar y explorar los datos: Asegurarnos de que los datos se importen correctamente y que los tipos de datos sean los adecuados para el análisis.
# 
# * Identificar los principales barrios y empresas de taxis: Analizar los datos para determinar los 10 barrios con más finalizaciones de viajes y comparar el número de viajes entre las distintas compañías de taxis.
# 
# * Visualizar los resultados: Crear gráficos que representen visualmente las principales empresas de taxis y los barrios con más finalizaciones de viajes, lo que nos permitirá identificar patrones y tendencias clave.
# 
# * Sacar conclusiones: Basándonos en los gráficos y el análisis realizado, extraer conclusiones que nos ayuden a entender mejor el comportamiento del servicio de taxis en Chicago durante el período de estudio.
# 
# Además, en la segunda parte del proyecto, abordaremos una prueba de hipótesis utilizando un tercer conjunto de datos (project_sql_result_07.csv). Este dataset incluye información sobre la duración de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare bajo diferentes condiciones climáticas. En esta etapa, se probará la hipótesis de si la duración promedio de estos viajes varía en los sábados lluviosos.
# 
# El análisis y la interpretación de estos datos nos proporcionarán una comprensión más profunda del funcionamiento del servicio de taxis en Chicago y nos permitirán hacer inferencias sobre el impacto de las condiciones climáticas en la duración de los viajes hacia el aeropuerto.

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats as st


# In[2]:


# Cargamos los dataset a trabajar

df1= pd.read_csv('/datasets/project_sql_result_01.csv') 
df2= pd.read_csv('/datasets/project_sql_result_04.csv')
df3= pd.read_csv('/datasets/project_sql_result_07.csv')


# ## DataFrame 1

# In[3]:


#Extraemos y visualizamos los datos en general.

df1.info()


# In[4]:


#realizamos una previsualizacion de los datos numericos.

df1.describe()


# #### Observacion describe():
# 
# * Alta variabilidad: La alta desviación estándar indica una gran variabilidad en la cantidad de viajes. Algunos días o periodos pueden tener muy pocos viajes, mientras que otros pueden tener muchos.
# 
# 
# 
# * Posibles outliers: El valor máximo de 19558 es mucho más alto que el resto de los valores, lo que sugiere que podría ser un outlier. Estos valores atípicos pueden distorsionar los resultados estadísticos y deben ser investigados.
# 
# 
# 
# * Distribución sesgada: La gran diferencia entre la mediana (50%) y la media sugiere que la distribución de los datos probablemente está sesgada hacia la derecha, es decir, hay una cola larga hacia valores altos. Esto se confirma por la diferencia entre el cuartil 3 y el máximo.
# 
# 
# 
# * Necesidad de análisis más profundo: Este resumen estadístico básico proporciona una primera visión de los datos, pero es necesario realizar un análisis más profundo para comprender completamente la distribución de los viajes y las posibles causas de la alta variabilidad.

# In[5]:


# Verificamos si existen datos duplicados. 

print('Duplicados en todo el Dataframe: ', df1.duplicated().sum())
print()
print('Duplicados en la columna company_name: ', df1['company_name'].duplicated().sum())
print()
print('Duplicados en la columna trips_amount: ', df1['trips_amount'].duplicated().sum())


# #### Observacion duplicated():
# 
# Pudimos verificar que tenemos supuestos datos duplicados en la columna trips_amount, los cuales en realidad no se consideraran como datos duplicados ya que sabemos que esta columna contiene la cantidad de viajes de cada compañia los cuales estas cifras se pueden repetir en varias compañias en este caso son 8 compañias las que tienen datos iguales.

# In[6]:


#Ordenamos los datos en orden descendente y verificamos que ya los datos estan ordenamos de dicha forma.
df1.sort_values(by='trips_amount', ascending=False).head(10)


# In[7]:


sort1= df1['company_name'].unique()
sorted(sort1)


# In[8]:


pattern = r"^\d+ - \d+ .*"
filtered_df = df1[df1['company_name'].str.match(pattern)]
filtered_df


# #### Observacion de los datos:
# 
# En el análisis de los nombres de las empresas, hemos detectado valores atípicos. Exploramos la posibilidad de que estos nombres estuvieran asociados a códigos iniciales, pero no hemos logrado identificar un patrón específico. Estos códigos podrían corresponder a identificadores numéricos únicos asignados a cada empresa (similares a un ID) o, incluso, a números telefónicos. Dada la variedad de posibilidades, no es posible determinar con certeza el significado exacto de dichos códigos.
# 
# En este caso no los eliminares o modificaremos ya que no tiene sentido quitarles dichos codigos y no los eliminaremos para no afectar el resultado final que se podria obtener de estos datos.

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buenas observacion. </div>
# 
# 

# ## DataFrame 2

# In[9]:


#Extraemos y visualizamos los datos en general.

df2.info()


# In[10]:


#realizamos una previsualizacion de los datos numericos.

df2.describe()


# #### Observacion describe():
# 
# * Alta variabilidad: La alta desviación estándar indica una gran variabilidad en la cantidad de viajes. Algunos días o periodos pueden tener muy pocos viajes a los barrios, mientras que otros pueden tener muchos.
# 
# 
# 
# * Posibles outliers: El valor máximo de 10728 es mucho más alto que el resto de los valores, lo que sugiere que podría ser un outlier. Estos valores atípicos pueden distorsionar los resultados estadísticos y deben ser investigados.
# 
# 
# 
# * Distribución sesgada: La gran diferencia entre la mediana (50%) y la media sugiere que la distribución de los datos probablemente está sesgada hacia la derecha, es decir, hay una cola larga hacia valores altos. Esto se confirma por la diferencia entre el cuartil 3 y el máximo.
# 
# 
# 
# * Necesidad de análisis más profundo: Este resumen estadístico básico proporciona una primera visión de los datos, pero es necesario realizar un análisis más profundo para comprender completamente la distribución de los viajes hacia diferentes barrios y las posibles causas de la alta variabilidad.

# In[11]:


# Verificamos si existen datos duplicados. 

print('Duplicados en todo el Dataframe: ', df2.duplicated().sum())
print()
print('Duplicados en la columna dropoff_location_name: ', df2['dropoff_location_name'].duplicated().sum())
print()
print('Duplicados en la columna average_trips: ', df2['average_trips'].duplicated().sum())


# #### Observacion duplicated():
# 
# Pudimos verificar que tenemos supuestos datos duplicados en la columna average_trips, los cuales en realidad no se consideraran como datos duplicados ya que sabemos que esta columna contiene la cantidad de viajes a cada barrio los cuales estas cifras se pueden repetir en varias barrios en este caso son 23 barrios los que tienen datos iguales.

# In[12]:


#convertimos la columna 'average_trips' a int y redondeamos sus valores hacia el mas cercano.
df2['average_trips'] = np.ceil(df2['average_trips']).astype(int)
print(df2.head())
print()
print()
print(df2.info())


# In[13]:


sort2= df2['dropoff_location_name'].unique()
sorted(sort2)


# #### Observacion de los datos:
# 
# En este DataFrame no se identificaron datos atipicos. Sin embargo, se detectó que la columna correspondiente a la cantidad de viajes finalizados tenía un tipo de dato float. Dado que la cantidad de viajes es un valor discreto (entero) y no puede tomar valores fraccionarios, se procedió a redondear los valores al entero más cercano y posteriormente se cambió el tipo de dato a int.

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien . </div>
# 
# 

# ## DataFrame 3

# In[14]:


#Extraemos y visualizamos los datos en general.

df3.info()


# In[15]:


#realizamos una previsualizacion de los datos numericos.

df3.describe()


# #### Observacion describe(): 
# 
# Variabilidad:
# 
# * La desviación estándar (std) es considerablemente alta (769.46 segundos), lo que indica una gran dispersión en los datos. Es decir, los tiempos de duración varían mucho de un evento a otro.
# 
# 
# 
# * El rango entre el valor mínimo y máximo es amplio (0 a 7440 segundos), lo que refuerza la idea de una alta variabilidad.
# 
# 
# 
# Valores Atípicos (Outliers):
# 
# 
# 
# * El valor mínimo de 0 segundos es sospechoso. ¿Es posible que un evento tenga una duración de 0 segundos? Esto podría indicar un error en los datos, un evento no registrado correctamente o una categoría especial de eventos (por ejemplo, eventos cancelados).
# 
# 
# 
# * El valor máximo de 7440 segundos (casi 2 horas) también podría ser considerado un outlier, especialmente si la mayoría de los eventos tienen una duración mucho menor.
# 
# 
# 
# Distribución:
# 
# 
# 
# * La diferencia entre la media y la mediana (50% percentil) sugiere que la distribución de los datos podría estar sesgada hacia la derecha. Esto significa que hay una cola larga de valores altos que están afectando el valor promedio.
# 
# 
# 
# Cuartiles:
# 
# 
# 
# * Los cuartiles nos dan una idea de cómo se distribuyen los datos. El rango intercuartílico (IQR) es bastante amplio, lo que nuevamente indica una gran variabilidad.

# In[16]:


# Verificamos si existen datos duplicados. 

print('Duplicados en todo el Dataframe: ', df3.duplicated().sum())
print()
print('Duplicados en la columna start_ts: ', df3['start_ts'].duplicated().sum())
print()
print('Duplicados en la columna weather_conditions: ', df3['weather_conditions'].duplicated().sum())
print()
print('Duplicados en la columna duration_seconds: ', df3['duration_seconds'].duplicated().sum())


# #### Observacion duplicated(): 
# 
# Pudimos verificar que tenemos supuestos datos duplicados en todo el dataset, los cuales en realidad no se consideraran como datos duplicados ya que sabemos que estas columna contiene las fechas la duracion de los viajes, las condiciones climaticas ylas fechas los cuales estas cifras se pueden repetir en nuestros datos en este caso porque son los registros que se crean cada vez que se realice un viaje en cada dia por diferentes conductores.

# In[17]:


#Convertimos la columna 'start_ts' al formato correcto.
df3['start_ts'] = pd.to_datetime(df3['start_ts'], format='%Y-%m-%d %H:%M:%S')


# In[18]:


df3


# In[19]:


#Observamos que tenemos datos con duracion 0 solo son 6 registros por lo que los eliminaremos.
df3= df3[df3['duration_seconds'] != 0]


# In[20]:


df3.info()


# In[21]:


#Convertimos la columna 'duration_seconds' a formato int ya que se verifico que dicha columna no contenia decimales. 
df3['duration_seconds']= df3['duration_seconds'].astype(int)


# In[22]:


df3.info()


# In[23]:


#Reiniciamos el indice ya que eliminamos algunas filas y debemos restaurarlo.
df3= df3.reset_index(drop=True)
df3


# ### Observacion de los datos:
# 
# Con el objetivo de asegurar la calidad de los datos, se realizó una limpieza inicial. La columna 'start_ts' fue convertida a formato datetime para permitir cálculos temporales. Se filtraron los registros con duración nula, asumiendo que estos podrían ser errores de registro o viajes cancelados instantáneamente. Finalmente, se verificó que la columna 'duration_seconds' no contenía valores fraccionarios y se transformó a tipo int para una representación más eficiente.

# ## Analisis de los Datos

# ### identificar los 10 principales compañias con mayores viajes

# In[24]:


# Verificamos la media de los datos de la columna 'trips_amount'
df1['trips_amount'].mean()


# In[25]:


#Filtramos solo para obtener los datos de las 10 compañias con mayores viajes.
company_10= df1.sort_values(by='trips_amount', ascending=False).head(10)
company_10


# In[26]:


#Creamos nuestro primer grafico de barras para observarlos datos de los viajes por compañias
company_10.plot(kind= 'bar',
       x='company_name',
       rot= 90,
       figsize= [14,6],
       grid= False,
       legend=False
       )

plt.title('Principales Compañías con Mayor Cantidad de Viajes', fontsize= 15)
plt.xlabel('Compañias', fontsize= 12)
plt.ylabel('Cantidad de Viajes', fontsize= 12)

plt.show()


# #### Observacion: 
# 
# Según el gráfico, Flash Cab se destaca como la empresa de transporte con mayor volumen de viajes en Chicago, superando considerablemente a sus competidores. Este resultado sugiere que Flash Cab es la opción preferida por los usuarios en la ciudad, las otras compañias se mantienen en un rango entre 5000 y 12000. De igual forma no podriamos asegurar esto con exactitud ya que esto es una pequeña muestra de 2 dias de noviembre del 2017.

# ### identificar los 10 principales barrios con mayores viajes finalizados

# In[27]:


#Filtramos los 10 primeros barrios con mayores viajes terminados en ellos.
location_10= df2.sort_values(by='average_trips', ascending=False).head(10)
location_10


# In[28]:


#Creamos nuestro grafico para visualizar los datos
plt.figure(figsize=(15, 10))

sns.barplot(x="dropoff_location_name", y='average_trips',
             hue="dropoff_location_name",
             data=location_10)
plt.title('Pricipales Barrios con mayor finalizacion de recorridos')
plt.xlabel('Barrios')
plt.ylabel('Promedio de viajes Finalizados')


# #### Observacion:
# 
# Los barrios de Loop y River North se destacan como los destinos más populares, registrando entre 9500 y 10800 viajes finalizados. Streeterville y West Loop le siguen en cuanto a demanda, con aproximadamente 5100 y 6700 viajes respectivamente. Los restantes 6 barrios (O'Hare, Lake view, Grant Park, Museum Campus, Gold Coast, Sheffield & Depaul) presentan un volumen de viajes significativamente menor, fluctuando entre 1260 y 2550.

# In[29]:


#Visualizamos los Datos
df3.head(23)


# In[30]:


#Agrupamos los datos del df3 calculamos el promedio de duracion de tiempo de un viaje dependiendo de la condicion climatica 
df_grouped = df3.groupby('weather_conditions')['duration_seconds'].mean()
df_grouped.head()


# ### Impacto del clima en la duracion de los viajes

# In[31]:


#Generamos nuestro grafico con los datos filtrados en el paso anterior
df_grouped.plot(kind= 'bar',
                x='weather_conditions',
             figsize= [10,5],
              rot= 50,
              color= 'Turquoise' )

plt.title('Impacto del clima en la duración de los viajes', fontsize= 20)
plt.ylabel('Duracion promedio')
plt.xlabel('Condiciones Climaticas')
plt.show()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente seccion de graficos. </div>
# 
# 

# #### Observacion: 
# 
# En nuestro grafico podemos observar que los viajes tienden a tener mayor duracion en mal tiempo.

# In[32]:


# Agrupamos los datos por dia y hora y separamos las fechas de las horas
df3['fecha'] = df3['start_ts'].dt.date #Creamos la columna para las fechas
df3['hora'] = df3['start_ts'].dt.hour #Creamos la columnas para las horas
df_grouped_hours = df3.drop('start_ts', axis=1) #Eliminamos la columna start_ts
df_grouped_hours.head()


# In[47]:


#Filtramos nuestro datos con el metodo tolist para poder realizar nuestro grafico

#Tomamos los valores de 2017-11-4
filtered_per_date4= df_grouped_hours[df_grouped_hours['fecha']== pd.to_datetime('2017-11-04')]
list_per_hour1= filtered_per_date4['hora'].tolist()
list_per_duration1= filtered_per_date4['duration_seconds'].tolist()

#Tomamos los valores de 2017-11-11
filtered_per_date11= df_grouped_hours[df_grouped_hours['fecha']== pd.to_datetime('2017-11-11')]
list_per_hour2= filtered_per_date11['hora'].tolist()
list_per_duration2= filtered_per_date11['duration_seconds'].tolist()

#Tomamos los valores de 2017-11-18
filtered_per_date18= df_grouped_hours[df_grouped_hours['fecha']== pd.to_datetime('2017-11-18')]
list_per_hour3= filtered_per_date18['hora'].tolist()
list_per_duration3= filtered_per_date18['duration_seconds'].tolist()

#Tomamos los valores de 2017-11-25
filtered_per_date25= df_grouped_hours[df_grouped_hours['fecha']== pd.to_datetime('2017-11-25')]
list_per_hour4= filtered_per_date25['hora'].tolist()
list_per_duration4= filtered_per_date25['duration_seconds'].tolist()


# ### Horas con mayor cantidad de viajes

# In[48]:


#Creamos nuestro grafico de barras

fig = go.Figure(data=[
    go.Bar(name='2017-11-04', x=list_per_hour1, y=list_per_duration1, marker_color='indianred'),
    go.Bar(name='2017-11-11', x=list_per_hour2, y=list_per_duration2, marker_color='lightsalmon'),
    go.Bar(name='2017-11-18', x=list_per_hour3, y=list_per_duration3),
    go.Bar(name='2017-11-25', x=list_per_hour4, y=list_per_duration4)
])
# Change the bar mode
fig.update_layout(title_text='Horas con mayor cantidad de viajes', xaxis_title= 'Horas', yaxis_title= 'Total duracion por hora')
fig.update_layout(barmode='group')
fig.show()


# #### Observacion:
# 
# El análisis de los datos revela que los viajes realizados entre las 12:00, las 14:00 horas, así como a las 16:00 horas, presentan una cantidad mayor de viajes solicitados.
# 
# Debemos tener en cuenta que estos estudios se realiza a una muentra de 4 dias del mes de noviembre del año 2017.

# In[49]:


#Filtramos nuestro datos con el metodo tolist para poder realizar nuestro grafico

#Tomamos los valores de 2017-11-4
mean_duration1= filtered_per_date4['hora'].value_counts().reset_index()
mean_duration1= mean_duration1.rename(columns={'index': 'hora', 'hora': 'count'}).sort_values(by='hora')

#Tomamos los valores de 2017-11-11
mean_duration2= filtered_per_date11['hora'].value_counts().reset_index()
mean_duration2= mean_duration2.rename(columns={'index': 'hora', 'hora': 'count'}).sort_values(by='hora')

#Tomamos los valores de 2017-11-18
mean_duration3= filtered_per_date18['hora'].value_counts().reset_index()
mean_duration3 = mean_duration3.rename(columns={'index': 'hora', 'hora': 'count'}).sort_values(by='hora')

#Tomamos los valores de 2017-11-25
mean_duration4= filtered_per_date25['hora'].value_counts().reset_index()
mean_duration4= mean_duration4.rename(columns={'index': 'hora', 'hora': 'count'}).sort_values(by='hora')


# ### Cantidad de Viajes por horas y dias

# In[50]:


#Creamos nuestro grafico de barras

fig = go.Figure(data=[
    go.Bar(name='2017-11-04', x=mean_duration1['hora'], y=mean_duration1['count'], marker_color='indianred'),
    go.Bar(name='2017-11-11', x=mean_duration2['hora'], y=mean_duration2['count'], marker_color='lightsalmon'),
    go.Bar(name='2017-11-18', x=mean_duration3['hora'], y=mean_duration3['count']),
    go.Bar(name='2017-11-25', x=mean_duration4['hora'], y=mean_duration4['count'])
])
# Change the bar mode
fig.update_layout(title_text='Cantidad de viajes por horas/dias', xaxis_title= 'Horas', yaxis_title= 'Cantidad de viajes')
fig.update_layout(barmode='group')
fig.show()


# #### Observacion: 
# 
# El análisis de los datos disponibles indica que existe una mayor demanda de viajes durante las horas de la mañana (6:00, 8:00 y 10:00 horas) y las primeras horas de la tarde (12:00, 14:00 y 16:00 horas). No obstante, para confirmar estos patrones y obtener una visión más completa de la demanda, sería necesario analizar un conjunto de datos más amplio que abarque diferentes días de la semana, meses y años.

# In[51]:


#Filtramos nuestro datos con el metodo tolist para poder realizar nuestro grafico

#Tomamos los valores de 2017-11-4
duration1= filtered_per_date4.groupby('hora')['duration_seconds'].mean().reset_index().sort_values(by='hora')

#Tomamos los valores de 2017-11-11
duration2= filtered_per_date11.groupby('hora')['duration_seconds'].mean().reset_index().sort_values(by='hora')

#Tomamos los valores de 2017-11-18
duration3= filtered_per_date18.groupby('hora')['duration_seconds'].mean().reset_index().sort_values(by='hora')

#Tomamos los valores de 2017-11-25
duration4= filtered_per_date25.groupby('hora')['duration_seconds'].mean().reset_index().sort_values(by='hora')


# ### Promedio duracion de viajes por horas y dias

# In[52]:


#Creamos nuestro grafico de barras

fig = go.Figure(data=[
    go.Bar(name='2017-11-04', x=mean_duration1['hora'], y=duration1['duration_seconds'], marker_color='indianred'),
    go.Bar(name='2017-11-11', x=mean_duration2['hora'], y=duration2['duration_seconds'], marker_color='lightsalmon'),
    go.Bar(name='2017-11-18', x=mean_duration3['hora'], y=duration3['duration_seconds']),
    go.Bar(name='2017-11-25', x=mean_duration4['hora'], y=duration4['duration_seconds'])
])
# Change the bar mode
fig.update_layout(title_text='Promedio Duracion de viajes por horas/dias', xaxis_title= 'Horas', yaxis_title= 'Duracion total de viajes')
fig.update_layout(barmode='group')
fig.show()


# #### Observacion:
# 
# El análisis promedio de los datos revela que empiezan a durar mas desde las 10 de la mañana empieza este incremente, a partir de las 3 de la tarde empieza a bajar un poco esta duracion promedio teniendo nuevamente un incremento es a las 6 de la tarde, luego de las 6 empieza a bajar la duracion de los viajes. Esta tendencia podría atribuirse a factores como el aumento del tráfico vehicular y condiciones climáticas adversas durante estas horas pico.
# 
# Asimismo, se observa un viaje excepcionalmente largo a las 2:00 de la madrugada, lo cual sugiere la ocurrencia de un evento extraordinario como condiciones climáticas extremas o un incidente vial que pudo haber obstaculizado el tránsito.

# In[53]:


#Filtramos los datos para obtener solo los datos con buen clima

condition_good= df_grouped_hours[df_grouped_hours['weather_conditions']== 'Good']
print(condition_good.head())
print()
print()
condition_good['duration_seconds'].mean()
condition_good.groupby('fecha')['duration_seconds'].agg(['mean', 'var', 'std',]).reset_index()


# In[54]:


#Filtramos los datos para obtener solo los datos con buen clima

condition_bad= df_grouped_hours[df_grouped_hours['weather_conditions']== 'Bad']
print(condition_bad.head())
print()
print()
condition_bad['duration_seconds'].mean()
condition_bad.groupby('fecha')['duration_seconds'].agg(['mean', 'var', 'std',]).reset_index()


# ### Observacion: 
# 
# En general, la varianza y la desviación estándar de ambas condiciones climaticas son altas, lo que nos indica que la distribución de datos está lejos de la media. podemos observar en los datos analizados que las condiciones climaticas tienden a comportarse en ciertas ocasiones de manera similar dado a los posibles escenarios que se pueden presentar con mal tiempo como con buen tiempo.

# In[55]:


#Agrupamos los datos y calculamos el promedio por hora, fecha y condicion climatica.

df_group= df_grouped_hours.groupby(['fecha', 'hora', 'weather_conditions'])['duration_seconds'].mean().reset_index()
df_group.head()


# ### Duracion promedio de viajes por horas segun las condiciones climaticas

# In[56]:


#Realizamos nuestro grafico para visualizar los comportamientos promedios en los tiempos dependiendo de la condicion climatica

fig = px.scatter(df_group, x="hora", y="duration_seconds", size="duration_seconds", color="weather_conditions",
           hover_name="fecha", log_x=False, size_max=60, title='Duracion pomedio de viajes por horas segun las condiciones climaticas')
fig.show()


# #### Observacion:
# 
# El análisis de los datos de nuestro grafico confirma que las condiciones climáticas adversas y las horas pico tienen un impacto significativo en la duración promedio de los viajes. En general, se observa un aumento considerable en el tiempo de viaje durante condiciones climáticas desfavorables debido a la reducción de la velocidad y el incremento de las congestiones vehiculares. Estos hallazgos corroboran los resultados obtenidos en el análisis anterior, donde se evidenció una duración promedio mayor en viajes realizados bajo condiciones climáticas adversas y con condiciones climaticas buenas pero en horas picos de mucha afluencia vehicular.
# 

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buena seccion de exploracion y busqueda de patrones, con cada observacion agregaste valor. Muy bueno. </div>
# 
# 

# ## Prueba de hipótesis

# "La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos".

# In[57]:


# Dividir los datos en dos grupos
lluvioso = df3[df3['weather_conditions'] == 'Bad']['duration_seconds']
no_lluvioso = df3[df3['weather_conditions'] == 'Good']['duration_seconds']

# Realizar la prueba t
t_statistic, p_value = st.ttest_ind(lluvioso, no_lluvioso)

print('Valor p:', p_value)

# Interpretar el resultado
if p_value < 0.05:
    print("Rechazamos la hipótesis nula. La duración promedio de los viajes es diferente en sábados lluviosos.")
else:
    print("No rechazamos la hipótesis nula. No hay evidencia suficiente para afirmar que la duración promedio de los viajes cambia en sábados lluviosos.")


# In[58]:


# Prueba las hipótesis
# Creamos una funcion de prueba estadística: prueba t de dos muestras

def t_test(sample1, sample2, alpha):
    p_value_levene=st.levene(sample1, sample2).pvalue.astype(int)

    if p_value_levene<alpha:
        option_var=False
    else:
        option_var=True

    p_value=st.ttest_ind(sample1, sample2, nan_policy='omit', equal_var=option_var).pvalue.astype(int)
    if p_value<alpha:
        print('Rechazamos la hipótesis nula: La duración promedio de los viajes es diferente en sábados lluviosos.')
    else:
        print( "No rechazar la hipótesis nula: No hay evidencia suficiente para afirmar que la duración promedio de los viajes cambia en sábados lluviosos.")


# In[59]:


# mirando solo el valor p
st.ttest_ind(lluvioso, no_lluvioso).pvalue


# In[60]:


#aplicamos t_test a la tabla ingresos_pivot para ambos planes
alpha= 0.05
t_test(lluvioso, no_lluvioso, alpha)


# ### Observacion:
# 
# De acuerdo al resultado, podemos confirmar que la duración promedio de los viajes es diferente en sábados lluviosos. El valor de p nos dice que existe una gran probabilidad de que existe una diferencia entre las condiciones climaticas de Bad y Good los dias sabados.
# 
# Esta hipotesis la formule creando uns funcion y filtrando el Dataframe por 'Bad' y por 'Good', colocando como parametro dentro de la funcion equal_var= si levenue era menor que alpha entonces era Flase o si no era True,  el cual es un parámetro opcional que especifica si las varianzas de las poblaciones en este caso condiciones climaticas deben considerarse iguales o no. Se pasa como equal_var = True o equal_var = False (True significa que consideramos las varianzas iguales, False significa que no)

# ## Conclusion General
# 
# ### Top 10 compañias populares.
# 
# ![grafico1-2.png](attachment:grafico1-2.png)
# 
# Según el gráfico, Flash Cab se destaca como la empresa de transporte con mayor volumen de viajes en Chicago, superando considerablemente a sus competidores. Este resultado sugiere que Flash Cab es la opción preferida por los usuarios en la ciudad, las otras compañias se mantienen en un rango entre 5000 y 12000. De igual forma no podriamos asegurar esto con exactitud ya que esto es una pequeña muestra de 2 dias de noviembre del 2017.

# ### Top 10 Barrios mas concurridos.
# 
# ![grafico2.png](attachment:grafico2.png)
# 
# Los barrios de Loop y River North se destacan como los destinos más populares, registrando entre 9500 y 10800 viajes finalizados. Streeterville y West Loop le siguen en cuanto a demanda, con aproximadamente 5100 y 6700 viajes respectivamente. Los restantes 6 barrios (O'Hare, Lake view, Grant Park, Museum Campus, Gold Coast, Sheffield & Depaul) presentan un volumen de viajes significativamente menor, fluctuando entre 1260 y 2550.

# ### Promedio total de duracion del viaje dependiendo de la condicion climatica.
# 
# ![grafico3.png](attachment:grafico3.png)
# 
# En nuestro grafico podemos observar que los viajes tienden a tener mayor duracion en mal tiempo.

# ### Previsualizacion de los datos en un grafico.
# 
# ![Screenshot_7.jpg](attachment:Screenshot_7.jpg)
# 
# 
# El análisis de los datos revela que los viajes realizados entre las 12:00, las 14:00 horas, así como a las 16:00 horas, presentan una cantidad mayor de viajes solicitados.
# 
# Debemos tener en cuenta que estos estudios se realiza a una muentra de 4 dias del mes de noviembre del año 2017.

# ### Cantidad de Viajes por Hora y Dias.
# 
# ![Screenshot_8.jpg](attachment:Screenshot_8.jpg)
# 
# 
# El análisis de los datos disponibles indica que existe una mayor demanda de viajes durante las horas de la mañana (6:00, 8:00 y 10:00 horas) y las primeras horas de la tarde (12:00, 14:00 y 16:00 horas). No obstante, para confirmar estos patrones y obtener una visión más completa de la demanda, sería necesario analizar un conjunto de datos más amplio que abarque diferentes días de la semana, meses y años

# ### Promedio duracion de viajes por dia y hora.
# 
# ![Screenshot_9.jpg](attachment:Screenshot_9.jpg)
# 
# El análisis promedio de los datos revela que empiezan a durar mas desde las 10 de la mañana empieza este incremente, a partir de las 3 de la tarde empieza a bajar un poco esta duracion promedio teniendo nuevamente un incremento es a las 6 de la tarde, luego de las 6 empieza a bajar la duracion de los viajes. Esta tendencia podría atribuirse a factores como el aumento del tráfico vehicular y condiciones climáticas adversas durante estas horas pico.
# 
# Asimismo, se observa un viaje excepcionalmente largo a las 2:00 de la madrugada, lo cual sugiere la ocurrencia de un evento extraordinario como condiciones climáticas extremas o un incidente vial que pudo haber obstaculizado el tránsito.

# ### Duracion pomedio de viajes por horas segun las condiciones climaticas
# 
# En general, la varianza y la desviación estándar de ambas condiciones climaticas son altas, lo que nos indica que la distribución de datos está lejos de la media. podemos observar en los datos analizados que las condiciones climaticas tienden a comportarse en ciertas ocasiones de manera similar dado a los posibles escenarios que se pueden presentar con mal tiempo como con buen tiempo.
# 
# ![Screenshot_6.jpg](attachment:Screenshot_6.jpg)
# 
# El análisis de los datos de nuestro grafico confirma que las condiciones climáticas adversas y las horas pico tienen un impacto significativo en la duración promedio de los viajes. En general, se observa un aumento considerable en el tiempo de viaje durante condiciones climáticas desfavorables debido a la reducción de la velocidad y el incremento de las congestiones vehiculares. Estos hallazgos corroboran los resultados obtenidos en el análisis anterior, donde se evidenció una duración promedio mayor en viajes realizados bajo condiciones climáticas adversas y con condiciones climaticas buenas pero en horas picos de mucha afluencia vehicular.
# 
# ### Hipotesis 
# 
# * "La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos"
# 
# De acuerdo al resultado, podemos confirmar que La duración promedio de los viajes es diferente en sábados lluviosos. El valor de p nos dice que existe una gran probabilidad de que existe una diferencia entre las condiciones climaticas de Bad y Good los dias sabados.

# ## Recomendaciones Basadas en el Análisis:
# 
# ### Optimización de Recursos para Empresas de Taxis:
# 
# * Focalización en Barrios Populares: Las empresas de taxis pueden considerar aumentar la disponibilidad de taxis en los barrios con mayor número de finalizaciones de viajes. Esto puede ayudar a satisfacer la demanda en áreas populares y maximizar los ingresos.
# 
# 
# 
# * Análisis de Competencia: Empresas como "Flash Cab" y "Taxi Affiliation Services" dominan en términos de número de viajes. Otras compañías podrían analizar las estrategias de estas empresas para mejorar su posición en el mercado.
# 
# 
# 
# ### Estrategias de Marketing:
# 
# * Promociones en Barrios con Menor Actividad: Implementar promociones o descuentos en barrios con menor actividad podría estimular la demanda en estas áreas.
# 
# 
# 
# 
# * Asociaciones con Negocios Locales: Colaborar con negocios en los barrios con alta finalización de viajes puede ser una estrategia efectiva para atraer más clientes, como ofrecer descuentos en viajes hacia esos negocios.
# 
# 
# 
# 
# ### Ajuste de Tarifas Basado en la Demanda:
# 
# 
# 
# 
# * Tarifas Dinámicas: Las empresas podrían considerar la implementación de tarifas dinámicas basadas en la demanda durante ciertos días y horas. Esto puede incluir la elevación de tarifas en los momentos de alta demanda o la reducción de precios para atraer más clientes en horas de baja demanda.
# 
# 
# 
# 
# ### Mejoras en la Experiencia del Usuario:
# 
# 
# 
# 
# * Reducción de Tiempos de Espera: Con un enfoque en los barrios de alta demanda, las empresas podrían trabajar en reducir los tiempos de espera, lo cual mejoraría la experiencia del usuario y podría aumentar la lealtad del cliente.
# 
# 
# 
# 
# * Integración Tecnológica: Fomentar el uso de aplicaciones móviles para mejorar la accesibilidad y facilidad de uso del servicio de taxis, permitiendo a los usuarios reservar viajes en tiempo real y conocer la disponibilidad en su área.
# 
# 
# 
# 
# ### Consideraciones Climáticas:
# 
# 
# 
# 
# * Preparación para Condiciones Climáticas: Dado que se investigó la influencia de las condiciones climáticas en la duración de los viajes, las empresas deberían preparar a sus conductores y flota para condiciones climáticas adversas, especialmente en los días lluviosos.
# 
# 
# 
# 
# 
# ### Expansión de Flotas en Barrios de Crecimiento:
# 
# 
# 
# 
# * Si se identifica un crecimiento en la demanda en ciertos barrios, las empresas de taxis podrían considerar expandir su flota o servicios en esas áreas para capturar una mayor cuota de mercado.
# 
# 
# 
# 
# Estas recomendaciones pueden ayudar a las empresas de taxis a optimizar sus operaciones, mejorar la experiencia del cliente y maximizar sus ingresos en el mercado competitivo de Chicago.

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente conclusion general.</div>
# 
# 
# 
# 
