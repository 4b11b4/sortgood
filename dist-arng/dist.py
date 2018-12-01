import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import random

def main():
  sns.set(color_codes=True) # Used for seaborn library. Try deleting it.

  # Example Datasets
  N = 100
  uni_prf = [x for x in range(N)]
  uni_rev = [x for x in range(N)]
  uni_rev.reverse() # In-place
  uni_shf = [x for x in range(N)]
  random.shuffle(uni_shf) # In-place
  uni_rnd = np.random.uniform(0,1,N)
  nrm_rnd = np.random.normal(size=N) # This generates neg values
  nrm_rnd_abs = np.absolute(nrm_rnd) # Performs abs() and returns new array 
  nrm_rnd_normed = nrm_rnd / nrm_rnd.max(axis=0) # Normalize the normal dist

  # Distribution Plots
  ## Uniform (Perfect)
  seaplot = sns.distplot(uni_prf, hist=True, kde=True, bins=10, color='blue')
  seaplot.set_title('A Perfectly Uniform Distribution')
  plt.xlabel('Input Values', fontsize=10)
  plt.ylabel('Percentage', fontsize=10)
  seaplot.get_figure().savefig("./../img/dist_uni_prf.png", 
                               bbox_inches='tight')
  plt.clf()
  
  ## Uniform (Random)
  seaplot = sns.distplot(uni_rnd, hist=True, kde=True, bins=10, color='blue')
  seaplot.set_title('A Random Uniform Distribution')
  plt.xlabel('Input Values', fontsize=10)
  plt.ylabel('Percentage', fontsize=10)
  seaplot.get_figure().savefig("./../img/dist_uni_rnd.png", 
                               bbox_inches='tight')
  plt.clf()
  
  ## Normal (Random)
  seaplot = sns.distplot(nrm_rnd, hist=True, kde=True, bins=10, color='blue')
  seaplot.set_title('A Random Normal Distribution')
  plt.xlabel('Input Values', fontsize=10)
  plt.ylabel('Percentage', fontsize=10)
  seaplot.get_figure().savefig("./../img/dist_nrm_rnd.png", 
                               bbox_inches='tight')
  

if __name__ == "__main__":
  main()
