import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import random

def main():
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
  nrm_rnd_normed = nrm_rnd_abs / nrm_rnd_abs.max(axis=0) # Normalize the normal dist

  # Arrangement Plots
  ## Increasing Order
  plt.title('Increasing Order')
  plt.xlabel('Position in List (Array)', fontsize=10)
  plt.ylabel('Value', fontsize=10)
  plt.bar(uni_prf, uni_prf, bottom=None, align='center', color='blue') 
  plt.savefig("./../img/arng_fwd.png", bbox_inches='tight')
  plt.clf()

  ## Decreasing Order
  plt.title('Decreasing Order')
  plt.xlabel('Position in List (Array)', fontsize=10)
  plt.ylabel('Value', fontsize=10)
  plt.bar(uni_prf, uni_rev, bottom=None, align='center') 
  plt.savefig("./../img/arng_rev.png", bbox_inches='tight')
  plt.clf()

  ## Shuffled Order
  plt.title('Shuffled Order')
  plt.xlabel('Position in List (Array)', fontsize=10)
  plt.ylabel('Value', fontsize=10)
  plt.bar(uni_prf, uni_shf, bottom=None, align='center') 
  plt.savefig("./../img/arng_shf.png", bbox_inches='tight')
  plt.clf()

  ## Random (Uniform)
  plt.title('Random (Uniform)')
  plt.xlabel('Position in List (Array)', fontsize=10)
  plt.ylabel('Value', fontsize=10)
  plt.bar(uni_prf, uni_rnd, bottom=None, align='center') 
  plt.savefig("./../img/arng_uni_rnd.png", bbox_inches='tight')
  plt.clf()

  ## Random (Normal)
  plt.title('Random (Normal)')
  plt.xlabel('Position in List (Array)', fontsize=10)
  plt.ylabel('Value', fontsize=10)
  plt.bar(uni_prf, nrm_rnd_normed, bottom=None, align='center') 
  plt.savefig("./../img/arng_nrm_rnd.png", bbox_inches='tight')

if __name__ == "__main__":
  main()
