import pandas as pd;
from pandas.core.frame import DataFrame;

df = pd.read_csv('/content/database.csv', index_col=0);

# convertir la columna de edad a númerico
df['Perpetrator Age'] = pd.to_numeric(df['Perpetrator Age'], errors='coerce');

# print(df.head(10)); # primeros datos
# print(df.tail(10)); # ultimos datos
# df.shape; # muestra número de columnas y filas
df.head()

total_asesinatos_por_estado = df.groupby('State')['Victim Count'].sum();
print(total_asesinatos_por_estado);

mujeres_asesinas = df[df['Perpetrator Sex'] == 'Female']['State'].value_counts();
mujeres_asesinas = DataFrame(mujeres_asesinas)
mujeres_asesinas.columns = ['Crimenes de Mujeres'];
mujeres_asesinas

mujeres_menores_asesinas = df[(df['Perpetrator Sex'] == 'Female') & (df['Perpetrator Age'] < 21)]['State'].value_counts();
mujeres_menores_asesinas = DataFrame(mujeres_menores_asesinas)
mujeres_menores_asesinas.columns = ['Crimenes de Mujeres Menores de Edad'];
mujeres_menores_asesinas

raza_asesina = df['Perpetrator Race'].value_counts();
raza_asesina