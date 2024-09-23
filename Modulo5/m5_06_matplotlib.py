import matplotlib.pyplot as plt
import numpy as np


# Crea dei dati di esempio
x = np.linspace(0, 10, 100)
y = np.sin(x)

#print(x)
#print(y)

# Crea il grafico a linee
plt.plot(x, y)

# Aggiungi un titolo e delle etichette agli assi
plt.title("Grafico della funzione seno")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Mostra il grafico
plt.show()

# Dati di esempio
objects = ('A', 'B', 'C', 'D')
y_pos = np.arange(len(objects))
performance = [35, 25, 30, 15]

# Crea il grafico a barre
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Performance')
plt.title('Risultati')

plt.show()

# Dati di esempio
np.random.seed(19680801)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

# Crea il grafico a dispersione
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# Dati di esempio
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # solo per la seconda fetta

# Crea il grafico a torta
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Assicura che la torta sia disegnata come un cerchio

plt.savefig("C:/temp/grafico.pdf")

plt.show()

