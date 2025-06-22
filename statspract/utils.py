# utils.py
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats



def chi2plot(f_obs, f_exp=None, alpha=0.05, contingency=False):
    
    chistat, pvalue, df, expected = [None]*4
    
    
    if contingency:
        chistat, pvalue, df, expected = stats.chi2_contingency(f_obs)
    else:
        chistat, pvalue = stats.chisquare(f_obs, f_exp)
        df = f_obs.index.size - 1
    
    critical_value = stats.chi2.ppf(1 - alpha, df)
    
    end = stats.chi2.ppf(0.999,df)
    x = np.linspace(0, end, 1000)
    y = stats.chi2.pdf(x, df)

    plt.figure(figsize=(8, 5))
    sns.lineplot(x=x, y=y, label=f'Chi-square Distribution (df={df})')
    plt.fill_between(x, 0, y, where=(x >= critical_value), color='blue', alpha=0.3, label=f'Rejection Region (α = {alpha})')
    plt.axvline(critical_value, color='blue', linestyle='--', label=f'Critical Value = {critical_value:.2f}')
    plt.axvline(chistat, color='red', linestyle='--', label=f'Observed χ² = {chistat:.2f}')

    plt.title(f"Chi-square Test Visualization (df = {df})")
    plt.xlabel("Chi-square value")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
    return chistat, pvalue, df