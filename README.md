# Market Risk Analysis - Value-at-Risk Framework

A comprehensive quantitative analysis implementing Value-at-Risk (VaR) methodology for a multi-currency, multi-asset portfolio. The project analyzes 5 years of market data using EWMA volatility estimation and dual VaR approaches (parametric and historical).

## Overview

**Portfolio Composition:**
- 60% US equity exposure (NASDAQ 100, β = 1.6)
- 40% German equity exposure (DAX, β = 1.3)
- Dual currency risk (USD/RUB and EUR/RUB)

**Time Period:** September 3, 2017 - September 3, 2022 (5 years)

**Analysis Date:** September 3, 2022

**Methodologies:** Parametric VaR, Historical VaR, EWMA volatility estimation

## Data

**File:** `2122_RM_Data.xlsx`

Daily observations including:
- NASDAQ 100 index values
- DAX index values  
- USD/RUB exchange rates
- EUR/RUB exchange rates

The dataset spans two major market events:
- COVID-19 pandemic (March 2020)
- Russia-Ukraine conflict (February 2022)

## Methodology

### Risk Decomposition

Portfolio returns are decomposed into equity and forex components:

```
Return(RUB) = Return(Equity) + Return(Forex)
```

This additive model allows separate analysis of market risk and currency risk.

### Volatility Estimation

EWMA (Exponentially Weighted Moving Average) with smoothing parameter λ = 0.94:

```
σ²ₜ = (1 - λ)r²ₜ₋₁ + λσ²ₜ₋₁
```

The recursive formula emphasizes recent observations (6% weight) while maintaining historical context (94% weight).

### VaR Calculation

**Parametric VaR:**
- Assumes normally distributed returns
- Calculates quantile using standard normal distribution
- Formula: VaR = μ - σ × Z₁₋ₐ

**Historical VaR:**
- Uses empirical distribution of historical returns
- Identifies α-th percentile from sorted returns
- No distributional assumptions

Both methods calculated at 1% significance level (99% confidence).

## Key Findings

### Volatility Analysis

- EWMA volatility increased 3-5x during crisis periods
- Volatility clustering evident around market shocks
- Mean reversion observed during recovery periods

### Correlation Dynamics

- Pre-crisis correlations: 0.3-0.5 (equity and forex relatively independent)
- Crisis correlations: 0.7-0.9 (diversification benefit reduced)
- Correlation breakdown most pronounced during geopolitical events

### VaR Estimates

- 1-day 1% Parametric VaR: 2.1% - 3.8% depending on period
- Historical VaR captured tail events more accurately than parametric approach
- 10-day VaR approximately √10 times 1-day VaR (assuming i.i.d. returns)

### Event Analysis

**March 2020 (COVID-19):**
- NASDAQ declined 25%, DAX declined 35%
- Extreme volatility spike
- Diversification collapsed

**February 2022 (Russia-Ukraine):**
- Equity markets declined ~15%
- Currency depreciated 45-50%
- Net portfolio effect: value increased in RUB due to currency effects

## Project Structure

```
Project_Market_Risk_v6.ipynb    # Complete Jupyter notebook with analysis
2122_RM_Data.xlsx               # Historical market data
Market_Risk_Report.pdf          # Detailed findings and charts
README.md                       # This file
```

## Technical Implementation

**Language:** Python 3.x

**Libraries:**
- Pandas: Data manipulation and time-series analysis
- NumPy: Numerical computing
- Matplotlib: Visualization
- Seaborn: Statistical graphics
- SciPy: Statistical functions

**Key Calculations:**
- Log returns computation
- EWMA volatility recursion
- Covariance matrix estimation
- Correlation analysis
- Quantile calculation

## Results

The analysis produces:
- Time-series plots of market indices and exchange rates
- Volatility evolution charts
- Correlation heatmaps
- VaR estimates for different time horizons
- Comparative analysis of parametric vs. historical VaR

All results are contained in the Jupyter notebook and PDF report.

## Files

- `Project_Market_Risk_v6.ipynb` - Complete analysis with code and output
- `2122_RM_Data.xlsx` - Historical NASDAQ, DAX, and forex data
- `Market_Risk_Report.pdf` - Professional report with findings
- `README.md` - This documentation

## Usage

Open `Project_Market_Risk_v6.ipynb` in Jupyter and run cells sequentially. The notebook includes:
1. Data loading and cleaning
2. Return calculations
3. Volatility estimation
4. VaR calculation
5. Comparative analysis
6. Visualizations

No external dependencies beyond standard Python data science libraries.

## Validation

The analysis validates assumptions and methodologies through:
- Comparison of parametric and historical VaR
- Testing across multiple time periods
- Stress testing with major market events
- Normality testing of returns distributions
- Correlation stability analysis

## Technical Notes

**Returns Calculation:** Log returns used throughout (continuous compounding)

**Missing Data:** Trading days only (weekends and holidays excluded)

**Initial Observations:** First observation excluded (no prior day for return calculation)

**Usable Sample:** ~1,254 daily returns across 5-year period

## References

Methodology follows industry standards including:
- Basel III risk framework
- RiskMetrics EWMA approach
- Standard VaR estimation techniques

---

**Analysis Date:** September 3, 2022  
**Data Period:** September 3, 2017 - September 3, 2022  
**Confidence Level:** 99% (1% significance)
