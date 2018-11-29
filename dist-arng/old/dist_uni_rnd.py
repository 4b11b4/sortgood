import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True)

import random
N = 1000

# Shuffled List
'''
s = [x for x in range(N)]
random.shuffle(s)
print(s)
'''

# Random List
random.seed()
s = [random.randint(0,N) for i in range(N)]
#s = np.random.uniform(0,1,N)

# Various Types of Plots
#sns_plot = sns.distplot(s, kde=False, rug=True)
#sns_plot = sns.distplot(s, hist=True)
sns_plot = sns.distplot(s, hist=True, kde=True, bins=100, color='blue')
#sns_plot = sns.distplot(s, hist=True, kde=False, bins=int(180/5), color='blue', hist_kws={'edgecolor':'black'})
#sns_plot = sns.distplot(s, hist=True, kde=False, bins=100, color='blue', hist_kws={'edgecolor':'black'})
#sns_plot = sns.distplot(s, bins=100, kde=True)

sns_plot.set_title('A Random Uniform Distribution')
plt.xlabel('Input Data', fontsize=10)
plt.ylabel('Probability Density', fontsize=10)
fig = sns_plot.get_figure()
fig.savefig("./uni_rnd.png")
