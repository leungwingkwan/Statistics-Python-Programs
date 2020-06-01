from scipy.stats import t, chi2
import numpy as np

sample_gold = [6.683, 6.681, 6.676, 6.678, 6.679, 6.672]
sample_platinum = [6.662, 6.661, 6.667, 6.667, 6.664]

#1

# gold_miu
gold_mean = np.mean(sample_gold)
print('gold_mean =', gold_mean)
gold_n = len(sample_gold)
print('gold_n =', gold_n)
#gold_var = np.var(sample_gold) * (gold_n) / (gold_n - 1)
#print('gold_var =',gold_var)
gold_std = np.std(sample_gold) * (gold_n ** 0.5) / ((gold_n - 1) ** 0.5)
print('gold_std =', gold_std)
# CL = Confidence Level
gold_cl = 0.9
gold_t = t.isf(((1-gold_cl)/2), gold_n - 1)
print('gold_t =', gold_t)
#gold_miu_range = (gold_var ** 0.5) * gold_t / (gold_n ** 0.5)
gold_miu_range = (gold_std) * gold_t / (gold_n ** 0.5)
gold_miu_upper = gold_mean + gold_miu_range
gold_miu_lower = gold_mean - gold_miu_range
print('gold_miu range: ', gold_miu_lower, ',', gold_miu_upper)

# platinum_miu
platinum_mean = np.mean(sample_platinum)
print('platinum_mean =', platinum_mean)
platinum_n = len(sample_platinum)
print('platinum_n =', platinum_n)
platinum_std = np.std(sample_platinum) * (platinum_n ** 0.5) / ((platinum_n - 1) ** 0.5)
print('platinum_std =',platinum_std)
# CL = Confidence Level
platinum_cl = 0.9
platinum_t = t.isf(((1-platinum_cl)/2), platinum_n - 1)
print('platinum_t =', platinum_t)
platinum_miu_range = (platinum_std) * platinum_t / (platinum_n ** 0.5)
platinum_miu_upper = platinum_mean + platinum_miu_range
platinum_miu_lower = platinum_mean - platinum_miu_range
print('platinum_miu range: ', platinum_miu_lower, ',', platinum_miu_upper)

#2
gold_var = np.var(sample_gold) * (gold_n) / (gold_n - 1)
gold_alpha = (1 - gold_cl)
gold_chi2_lower = chi2.isf(gold_alpha / 2, gold_n - 1)
print('gold_chi2_lower = ', gold_chi2_lower)
gold_chi2_upper = chi2.isf(1 - gold_alpha / 2, gold_n - 1)
print('gold_chi2_upper = ', gold_chi2_upper)
gold_var_lower = (gold_n - 1) * gold_var / gold_chi2_lower
print('gold_var_lower=', gold_var_lower)
gold_var_upper = (gold_n - 1) * gold_var / gold_chi2_upper
print('gold_var_upper=', gold_var_upper)