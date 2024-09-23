import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carichiamo un dataset integrato in Seaborn
tips = sns.load_dataset("tips")

# Creiamo un istogramma per visualizzare la distribuzione delle mance
sns.histplot(data=tips, x="total_bill")
plt.show()

# Scatter plot per visualizzare la relazione tra conto totale e mancia
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()

# Box plot per confrontare la distribuzione delle mance tra fumatori e non fumatori
sns.boxplot(x="smoker", y="tip", data=tips)
plt.show()

# Violin plot per visualizzare la distribuzione delle mance per sesso e giorno della settimana
sns.violinplot(x="day", y="tip", hue="sex", data=tips, split=True)
plt.show()