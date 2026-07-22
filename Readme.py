# %% [markdown]
# # 📊 Quantitative Asset Analysis: Gold, S&P 500 & IBEX 35
# This study analyzes the historical performance, daily volatility, asset correlation, and risk-adjusted efficiency (Sharpe Ratio) across three major market benchmarks.

# %%
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define ticker mapping (Yahoo Finance symbols to standard names)
tickers = {'^IBEX': 'IBEX_35', '^GSPC': 'SP_500', 'GC=F': 'GOLD'}

# Download daily closing prices
data = yf.download(list(tickers.keys()), start='2025-01-01', end='2026-07-19')['Close']
data = data.rename(columns=tickers)

# Fill missing values caused by international trading holidays (Forward Fill)
clean_data = data.ffill().dropna()

# Calculate daily percentage returns
returns = clean_data.pct_change().dropna()
returns.head()

# %% [markdown]
# ## 1. Daily Volatility & Risk Analysis
# 
# Gold (`GC=F`) futures represent a contract of 100 troy ounces with minimum 99.5% purity. Despite its traditional reputation as a "safe-haven" asset, the descriptive statistics below highlight its high daily volatility relative to equity indices.

# %%
# Summary statistics for daily percentage returns
print("--- Daily Percentage Return Statistics ---")
print((returns * 100).describe())

# Calculate daily cumulative capital growth (Base = 1.0)
cumulative_growth = (1 + returns).cumprod()

# Plot Cumulative Capital Evolution
plt.figure(figsize=(12, 6))

for col in cumulative_growth.columns:
    plt.plot(cumulative_growth.index, cumulative_growth[col], label=col, linewidth=1.8)

plt.title('Cumulative Growth of 1€ Invested', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=11)
plt.ylabel('Capital Multiplier (Base = 1.0)', fontsize=11)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 2. Asset Correlation & Portfolio Diversification
# 
# In quantitative portfolio management, evaluating cross-asset correlation is essential for true diversification.

# %%
# Compute correlation matrix on daily returns
correlation_matrix = returns.corr()
print("--- Daily Returns Correlation Matrix ---")
print(correlation_matrix.round(2))

# %% [markdown]
# A low correlation of r = 0.12 was found between Gold and the S&P 500 daily returns, confirming that Gold successfully acts as an effective short-term portfolio diversifier.

# %% [markdown]
# ## 3. Risk-Adjusted Performance: Annualized Sharpe Ratio
# 
# Formulated by William F. Sharpe (1966), the Sharpe Ratio measures excess return per unit of total risk (volatility):
# 
# $$\text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}$$
# 
# Where $R_p$ is the asset return, $R_f$ is the risk-free rate, and $\sigma_p$ is the standard deviation. We assume an annual risk-free rate $R_f = 3\%$, annualized using $\sqrt{252}$ trading days.

# %%
# Risk-Free Rate Setup (3% Annualized)
r_f_annual = 0.03
r_f_daily = r_f_annual / 252

# Excess daily return over risk-free rate
excess_returns = returns.mean() - r_f_daily

# Annualized Sharpe Ratio calculation
sharpe_ratio = (excess_returns / returns.std()) * (252 ** 0.5)

print("--- ANNUALIZED SHARPE RATIOS ---")
print(sharpe_ratio.round(2))

# Visualization
plt.figure(figsize=(8, 8))
colors = ['#2ca02c' if x == 'IBEX_35' else '#FFD700' if x == 'GOLD' else '#1f77b4' for x in sharpe_ratio.index]

ax = sharpe_ratio.plot(kind='bar', color=colors, edgecolor='black', alpha=0.85)

# Add horizontal benchmark line at Sharpe = 1.0
plt.axhline(1.0, color='red', linestyle='--', linewidth=1.5, label='Minimum Acceptable Threshold (1.0)')

plt.title('Annualized Sharpe Ratio (Risk-Adjusted Efficiency)', fontsize=13, fontweight='bold')
plt.ylabel('Sharpe Ratio', fontsize=11)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

# Annotate value labels on top of bars
for i, v in enumerate(sharpe_ratio):
    ax.text(i, v + 0.04, str(round(v, 2)), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
