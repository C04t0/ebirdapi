import sqlite3
import pandas

connection = sqlite3.connect('birds.db')
cursor = connection.cursor()
ebird_taxonomy_df = pandas.read_csv('data/ebird-taxonomy.csv')
print(ebird_taxonomy_df)

ebird_taxonomy_df.to_sql('data/ebird-taxonomy.csv', connection, if_exists='replace', index=False)

cursor.execute('select * from ebird_taxonomy LIMIT 5')
rows = cursor.fetchall()

print(rows)

connection.close()