# Imports
import matplotlib.pyplot as plt
import random as rd

# Chart configuration
plt.xlabel("Qtd de jogadas / Throws")
plt.ylabel("Porcentagem / Percentage")
plt.title("""Probabilidade de ser "Cara" / Probability of being "Heads" """)
plt.ylim(0, 100)
plt.axhline(y = 50, color = 'black', linestyle = '-')

plot = 0

# Main loop (Create 5 different plots)
while plot < 5:
    listx = []
    listy = []
    qtd = 0
    porcent = 0
    
    # Loop to simulate 5000 throws
    for i in range (1, 5001):
        if rd.choice([0, 1]) == 0:
            qtd += 1
        porcent = (qtd/i) * 100
        listx.append(i)
        listy.append(porcent)
        
    # Add to plot and reset values
    plt.plot(listx, listy)    
    plot += 1

# Show Final plot
plt.show()