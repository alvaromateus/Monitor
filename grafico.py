import matplotlib.pyplot as plt
import csv
data_hora = []
memoria = []
cpu = []

arquivo = open('log.csv')
linhas = csv.DictReader(arquivo)

for linha in linhas:
    data_hora.append(linha['data_hora'].replace(' ','\n'))
    memoria.append(float(linha['memoria']))
    cpu.append(float(linha['cpu']))

#matplotlib.pyplot.plot(data_hora, memoria)
#fig1, f1_axes = plt.subplots(ncols = 2,nrows = 1,figsize=(15,10))
plt.suptitle("Monitor de Memória e CPU")
#plt.set_title("Memória")
plt.plot(cpu, label="CPU")

plt.plot(memoria, label="Memória")
#plt.set_xlabel("Tempo")
#plt.set_ylabel("Percentual de consumo")

#plt.set_xlabel("Linha do tempo")
#plt.set_ylabel("Percentual de consumo")
#plt.legend()
#plt.set_title("CPU")
#f1_axes[0,1].plot(data_hora)
#f1_axes[1,1].plot(data_hora)
plt.legend()

plt.grid(True)

plt.show()
