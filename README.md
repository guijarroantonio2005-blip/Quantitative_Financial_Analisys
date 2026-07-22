# Quantitative_Financial_Analisys_Proyect
> **Financial Data Science Case Study:** Volatility assessment, cross-classification, and risk-adjusted return (Sharped Ratio)
---
## 📌 Exercise Summary 
In this project I analyzes the behavior of three global benchmark assets (**Gold**, **S&P 500** and **IBEX 35**) to evaluate capital efficiency beyond gross return.
## 💡 Main Discovery
1. **🏆 Efficiency Leader:** The **IBEX 35** achieved the highest **Sharpe Ratio (1.76)**, oferring the best return for each unit of risk assumed.
2. **🎢 Gold's Risk:** It showed the highest **daily volatility (std = 1.5 %)**, behaving as a highly volatile asset during this period.
3. **🛡️ Effective Diversification:** A low correlation of **r = 0.12** was found between Gold and the S&P 500 daily returns. Confirming that Gold **successfully acts as an effective short-term portfolio diversifier**.
## 🛠️ Technologues and Libraries Used**
* **Language:** Python
* **Data Analisys:** 'pandas', 'numpy'
* **Visualization:** 'matplotib','seaborn'
* **Financial Metrics**: Annualized Sharpe Ratio, Daily Volatility($\sigma$), Compound Return Cumprod (.cumprod()').
## 📊 Quantitative Portfolio Metrics
| Assets | Daily Volatility ($\sigma$) | Annualized Sharpe Ratio ($R_f = 3\%$) | Rating |
| :--- | :---: | :---: | ---: |
| **IBEX 35** | **1.07** | **1.76** | **🟢 Excellent** |
|**GOLD** | **1.59%** | **1.05** | **🟡 Acceptable** |
|**S&P 500** | **1.06%** | **0.81** | **🔴 Insufficient** |
---
## Quantitative Methodology
### 1. Annualized Sharpe Ratio
$$\text{Annualized Sharpe} = \frac{\bar{R}_p - \bar{R}_f}{\sigma_p} \times \sqrt{252}$$

Where:
* $\bar{R}_p$: Average daily return of the asset.

* $\bar{R}_f$: Daily risk-free rate (based on 3% per annum).

* $\sigma_p$: Daily standard deviation of returns.

* $\sqrt{252}$: Annualization factor for trading days.