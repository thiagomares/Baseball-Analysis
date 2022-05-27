import sqlite3 as sqlite
from matplotlib import markers
import matplotlib.pyplot as plt

conector = sqlite.connect('lahmansbaseballdb.sqlite')
cursor = conector.cursor()
time_a = []
time_b = []

for i in cursor.execute('SELECT W FROM teams WHERE franchID LIKE ? AND yearID >= ? ', ('STL', 2010, )):
    time_a.append(i)
for i in cursor.execute('SELECT W FROM teams WHERE franchID LIKE ? AND yearID >= ? ', ('CHC', 2010, )):
    time_b.append(i)
    
anos_time_a = []
for i in cursor.execute('SELECT yearID FROM teams WHERE yearID >= ? AND franchID = ?', (2010, 'STL', )):
    anos_time_a.append(i)    
    
anos_time_b = []
for i in cursor.execute('SELECT yearID FROM teams WHERE yearID >= ? AND franchID = ?', (2010, 'CHC', )):
    anos_time_b.append(i)
    
plt.fill_between(anos_time_a, time_a, marker = 'o', label = 'Cardinals')
plt.fill_between(anos_time_b, time_b, marker = 'x', label = 'Cubs')
plt.legend()
plt.xlabel('Ano')
plt.ylabel('Vitórias')
plt.title('Temporadas de Cardinals e Cubs entre 2010 e 2019')

plt.show()