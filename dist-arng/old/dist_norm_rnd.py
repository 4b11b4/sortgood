import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

N = 1000

# Random Normla Distribution List
s = np.random.normal(size=N)

# Various Types of Plots
sns_plot = sns.distplot(s, hist=True, kde=True, bins=100, color='blue')

sns_plot.set_title('A Random Normal Distribution')
plt.xlabel('Input Data', fontsize=10)
plt.ylabel('Probability Density', fontsize=10)
fig = sns_plot.get_figure()
fig.savefig("../img/norm_rnd.png")
