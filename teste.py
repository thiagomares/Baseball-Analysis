import pyodbc as sql
import matplotlib.pyplot as plt


class Verificador:
    def __init__(self):
        self.conector = sql.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                    r'DBQ=./lahman_1871-2021.mdb;')
        self.cursor = self.conector.cursor()

    def buscaPitcher(self, ultimo_nome, primeiro_nome):
        era = []
        ano = []
        for i in self.cursor.execute('SELECT playerID FROM people WHERE nameLast = ? AND nameFirst = ?', (ultimo_nome, primeiro_nome)):
            playerID = i

        for i in self.cursor.execute('SELECT ERA, yearID FROM pitching WHERE playerID = ?', (playerID)):
            era.append(i[0])
            ano.append(i[1])

        return era, ano

    def buscaRebatedor(self, ultimo_nome, primeiro_nome):
        average = []
        ano = []

        for i in self.cursor.execute('SELECT playerID FROM people WHERE nameLast = ? AND nameFirst = ?', (ultimo_nome, primeiro_nome)):
            playerID = i

        for i in self.cursor.execute('SELECT AB, H, yearID FROM batting WHERE playerID = ?', (playerID)):
            average.append((i[1]/i[0]))
            ano.append(i[2])

        return average, ano


opcao = int(input('Digite a função que deseja utilizar: \n 1 - Position Player History \n 2 - Comparação de jogadores de linha \n 3 - Pitching History \n 4 - Pitcher Comparison \n'))

verificador = Verificador()

if opcao == 1:
    nome = input('Digite o nome do Jogador \n')
    name = nome.split()
    plt.bar(verificador.buscaRebatedor(name[1], name[0])[
            1], verificador.buscaRebatedor(name[1], name[0])[0], label=nome)
    plt.legend()
    plt.title(f'Evolução do {nome} durante os anos')
    plt.xlabel('Temporada')
    plt.ylabel('Média')
    plt.show()
elif opcao == 2:
    nome_a = input('Digite o nome do Jogador A \n')
    nome_b = input('Digite o nome do Jogador B \n')
    name_a = nome_a.split()
    name_b = nome_b.split()
    plt.plot(verificador.buscaRebatedor(name_a[1], name_a[0])[
             1], verificador.buscaRebatedor(name_a[1], name_a[0])[0], label=nome_a)
    plt.plot(verificador.buscaRebatedor(name_b[1], name_b[0])[
             1], verificador.buscaRebatedor(name_b[1], name_b[0])[0], label=nome_b)
    plt.legend()
    plt.title(f'Comparação entre {nome_a} e {nome_b} durante os anos')
    plt.xlabel('Temporada')
    plt.ylabel('Média')
    plt.show()
elif opcao == 3:
    nome = input('Digite o nome do Jogador \n')
    name = nome.split()
    plt.bar(verificador.buscaPitcher(name[1], name[0])[
            1], verificador.buscaPitcher(name[1], name[0])[0], label=nome)
    plt.legend()
    plt.title(f'Evolução do {nome} durante os anos')
    plt.xlabel('Temporada')
    plt.ylabel('Média')
    plt.show()
elif opcao == 4:
    nome_a = input('Digite o nome do Jogador A \n')
    nome_b = input('Digite o nome do Jogador B \n')
    name_a = nome_a.split()
    name_b = nome_b.split()
    plt.plot(verificador.buscaPitcher(name_a[1], name_a[0])[
             1], verificador.buscaPitcher(name_a[1], name_a[0])[0], label=nome_a)
    plt.plot(verificador.buscaPitcher(name_b[1], name_b[0])[
             1], verificador.buscaPitcher(name_b[1], name_b[0])[0], label=nome_b)
    plt.legend()
    plt.title(f'Comparação entre {nome_a} e {nome_b} durante os anos')
    plt.xlabel('Temporada')
    plt.ylabel('ERA')
    plt.show()
