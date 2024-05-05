import pandas as pd;
from pandas.core.frame import DataFrame;

df = pd.read_csv('/content/database.csv', index_col=0);

# convertir la columna de edad a númerico
df['Perpetrator Age'] = pd.to_numeric(df['Perpetrator Age'], errors='coerce');

df.head()

# 1. Listar las primeras 5 ciudades con el mayor numero de agencias
auxiliar = df.groupby(['City'])['Agency Code'].unique();
ciudades_agencias = auxiliar.apply(lambda x: len(x));
ciudades_agencias = ciudades_agencias.sort_values(ascending=False);
print(ciudades_agencias.head())

#2. Listar los estados más afectados por crimenes perpetrados por mujeres

female_crimes = df[df['Perpetrator Sex'] == 'Female']

female_crimes_by_state = female_crimes.groupby('State').size().reset_index(name='Female Crimes Count')

female_crimes_by_state_sorted = female_crimes_by_state.sort_values(by='Female Crimes Count', ascending=False)

top_states_female_crimes = female_crimes_by_state_sorted.head()

top_states_female_crimes

# 3. Listar los estados mas afectados por crimenes perpetrados por hombres
male_crimes = df[df['Perpetrator Sex'] == 'Male']

male_crimes_by_state = male_crimes.groupby('State').size().reset_index(name='Male Crimes Count')

male_crimes_by_state_sorted = male_crimes_by_state.sort_values(by='Male Crimes Count', ascending=False)

top_states_male_crimes = male_crimes_by_state_sorted.head()

top_states_male_crimes

# 4. Determinar el numero exacto del numero de crimenes hechos por mujeres de raza Asian/Pacific Islander

female_asian_crimes = df[(df['Perpetrator Sex'] == 'Female') & (df['Perpetrator Race'] == 'Asian/Pacific Islander')]

num_female_asian_crimes = len(female_asian_crimes)

num_female_asian_crimes

#5. Determinar el numero exacto de hispanos que han asesinado mediante la estrangulacion
hispanic_strangulation_crimes = df[(df['Perpetrator Race'] == 'Hispanic') & (df['Weapon'] == 'Strangulation')]

num_hispanic_strangulation_crimes = len(hispanic_strangulation_crimes)

num_hispanic_strangulation_crimes

#6. Determinar el tipo de relacion mas peligrosa, el cual comete mas homicidios con armas de tipo Shotgun=escopeta

shotgun_crimes = df[df['Weapon'] == 'Shotgun']

relationship_shotgun_counts = shotgun_crimes.groupby('Relationship').size().reset_index(name='Homicide Count')

most_dangerous_relationship = relationship_shotgun_counts.loc[relationship_shotgun_counts['Homicide Count'].idxmax()]

print("El tipo de relación más peligroso que comete más homicidios con armas de tipo escopeta es:", most_dangerous_relationship['Relationship'])
print("Número de homicidios con escopeta cometidos por esta relación:", most_dangerous_relationship['Homicide Count'])

#7. cual es el sexo que mas homicidios ha comentido con Veneno=Poison
poison_crimes = df[df['Weapon'] == 'Poison']

sex_poison_counts = poison_crimes.groupby('Perpetrator Sex').size().reset_index(name='Homicide Count')

most_dangerous_sex = sex_poison_counts.loc[sex_poison_counts['Homicide Count'].idxmax()]

print("El sexo que ha cometido más homicidios con veneno es:", most_dangerous_sex['Perpetrator Sex'])
print("Número de homicidios con veneno cometidos por este sexo:", most_dangerous_sex['Homicide Count'])

#8. cuantos homicidios de raza negra atrapo el FBI
black_victim_crimes = df[df['Victim Race'] == 'Black']

fbi_solved_black_victim_crimes = black_victim_crimes[black_victim_crimes['Crime Solved'] == 'Yes']

num_fbi_solved_black_victim_crimes = len(fbi_solved_black_victim_crimes)

num_fbi_solved_black_victim_crimes

#9. cual es el total de homicidios desde el año 1995 hasta el año 2000 perpetrado por hombres de raza negra por sofocacion=suffocatino
black_male_suffocation_crimes = df[(df['Perpetrator Sex'] == 'Male') &
                                     (df['Perpetrator Race'] == 'Black') &
                                     (df['Weapon'] == 'Suffocation')]

black_male_suffocation_crimes_1995_to_2000 = black_male_suffocation_crimes[
    (black_male_suffocation_crimes['Year'] >= 1995) & (black_male_suffocation_crimes['Year'] <= 2000)
]

total_homicides_1995_to_2000 = len(black_male_suffocation_crimes_1995_to_2000)

total_homicides_1995_to_2000

#10. Determinar los homicidios de la policia municipalde la ciudadde nueva york del cual hayan sido por relaciones de tipo ex-wife, y ademas que su arma haya sido la estrangulacion=Strangulation
nyc_police_crimes = df[df['Agency Name'] == 'New York City Police Department']

nyc_police_exwife_strangulation_crimes = nyc_police_crimes[(nyc_police_crimes['Relationship'] == 'Ex-wife') &
                                                           (nyc_police_crimes['Weapon'] == 'Strangulation')]

total_nyc_police_exwife_strangulation_crimes = len(nyc_police_exwife_strangulation_crimes)

print("Número de homicidios investigados por la policía municipal de la ciudad de Nueva York donde la relación era con la ex esposa y la causa fue estrangulación:", total_nyc_police_exwife_strangulation_crimes)