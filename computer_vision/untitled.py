import matplotlib.pyplot as plt

x = list(range(0, 11))

y1 = [i for i in x]        # x
y2 = [i**2 for i in x]     # x²
y3 = [i**3 for i in x]     # x³

plt.plot(x, y1, label="x")
plt.plot(x, y2, label="x²")
plt.plot(x, y3, label="x³")
plt.legend()                # affiche la légende
plt.grid(True)
plt.title("x, x², x³")
plt.show() 



