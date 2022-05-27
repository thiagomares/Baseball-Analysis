import sqlite3 as sqlite
from types import NoneType
from matplotlib import markers
import matplotlib.pyplot as plt
from numpy import NaN

conector = sqlite.connect('lahmansbaseballdb.sqlite')
cursor = conector.cursor()

jogadores = []
numeros = []
id = []

for i in cursor.execute('SELECT ERA, playerID from pitching WHERE teamID = ? AND yearID = ?', ('SLN', 2015, )):
    if i != NoneType:
        numeros.append(i[0])
        id.append(i[1])
    
for i in id:
    for valor in cursor.execute('SELECT nameFirst, nameLast from people WHERE playerID = ?', (i, )):
        if valor != NoneType:
            jogadores.append(f'{valor[0]} {valor[1]}')
    
print(id)
plt.bar(jogadores, numeros)
plt.xticks(rotation = 45)
plt.show()
