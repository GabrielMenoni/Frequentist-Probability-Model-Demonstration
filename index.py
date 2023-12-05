import matplotlib.pyplot as plt
import random as rd

plt.xlabel("Qtd de jogadas / Throws")
plt.ylabel("Porcentagem / Percentage")
plt.title("""Probabilidade de ser "Cara" / Probability of being "Heads" """)
plt.ylim(0, 100)
plt.axhline(y = 50, color = 'black', linestyle = '-')

plot = 0

while plot < 5:
    listx = []
    listy = []
    qtd = 0
    porcent = 0
    
    for i in range (1, 5001):
        if rd.choice([0, 1]) == 0:
            qtd += 1
        porcent = (qtd/i) * 100
        listx.append(i)
        listy.append(porcent)
        
        
    plt.plot(listx, listy)    
    plot += 1

plt.show()