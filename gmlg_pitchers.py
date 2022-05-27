import openpyxl
import matplotlib.pyplot as plt

arquivo_miles = openpyxl.load_workbook('./gamelogs/gamelogs_miles.xlsx')
gamelogs_miles = arquivo_miles['Worksheet']

jogos = []
era = []

for i in range(2, gamelogs_miles.max_row):
    jogos.append(gamelogs_miles[f'C{i}'].value)
    era.append(gamelogs_miles[f'T{i}'].value)

plt.plot(jogos, era, marker = 'o', color = 'red')
plt.xlabel('Start')
plt.ylabel('ERA')
plt.title('Evolução do Mikolas durante a temporada')
plt.show()