import seaborn as sns
import matplotlib.pyplot as plt

data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
sns.histplot(data, color="purple")
plt.title("Test Seaborn!")
plt.show()