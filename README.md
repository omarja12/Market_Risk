# Estimating Value-at-Risk (VaR) for a Multi-Asset, Multi-Currency Portfolio

A comprehensive quantitative analysis of portfolio risk estimation using parametric and historical VaR methodologies, applied to a Russian investor's diversified US-German stock portfolio with foreign exchange exposure.

## Project Overview

This project implements a rigorous Value-at-Risk (VaR) framework to quantify and analyze market risk exposure in a complex, multi-asset scenario involving:

- **60% US equity exposure** (NASDAQ 100 index-linked) with beta = 1.6
- **40% German equity exposure** (DAX index-linked) with beta = 1.3
- **Dual currency components** (USD/RUB and EUR/RUB forex risks)
- **5-year historical dataset** (September 2017 - September 2022)

The analysis accounts for major market events including the COVID-19 pandemic (Feb 2020) and the Russia-Ukraine conflict (Feb 2022), providing realistic risk estimates under extreme market conditions.

## Theory & Concepts (For Everyone)

### What is Value-at-Risk (VaR)?

**Simple Definition**: VaR answers the question: *"What's the worst-case loss I could face in 1 day at a 1% confidence level?"*

**Business Context**: Imagine you manage $1 million in investments. VaR tells you: "There's a 99% chance your portfolio won't lose more than $X tomorrow." This helps:
- **Risk managers** set appropriate limits for traders
- **Executives** understand potential losses for reporting and capital allocation
- **Regulators** ensure banks maintain sufficient buffers
- **Investors** make informed decisions about risk exposure

### Why Multiple Methodologies Matter

#### **Parametric VaR (Normal Distribution Method)**
- **Concept**: Assumes returns follow a "bell curve" (normal distribution)
- **Advantage**: Fast, mathematically elegant, requires less data
- **Limitation**: Real markets have "fat tails" (more extreme events than normal distribution predicts)
- **Use Case**: Good for routine risk estimation and regulatory reporting

#### **Historical VaR (Empirical Method)**
- **Concept**: Uses actual historical returns; no assumptions about distribution shape
- **Advantage**: Captures real market behavior including extreme events
- **Limitation**: Can't predict unprecedented events; relies on past being representative of future
- **Use Case**: Validation and stress-testing; robust alternative to parametric models

### Key Technical Concepts Explained

**Beta (β)**: Measures how sensitive a stock/portfolio is to market movements
- β = 1.0: Moves exactly with the market
- β = 1.6: Moves 60% more than the market (higher volatility)
- β = 0.5: Moves 50% less than the market (lower volatility)
- *This project*: US stocks (β=1.6) and German stocks (β=1.3) capture different market sensitivities

**EWMA (Exponentially Weighted Moving Average)**: A smart way to track changing volatility
- Traditional approach: All historical data weighted equally
- EWMA approach: Recent data matters more; older data fades out
- Parameter λ = 0.94: Balances recent trends (94% weight) with historical stability (6% weight)
- *Result*: Captures how volatility increases during crises, decreases during calm periods

**Covariance Matrix**: Shows how different risks move together
- Positive covariance: When one risk increases, the other tends to increase (not diversified)
- Negative covariance: When one risk increases, the other decreases (good diversification)
- Zero covariance: Risks are independent
- *This project*: Tracks how equity risk and forex risk correlate over time, especially during crises

**Additive Returns Model**: Why this project's approach is sophisticated
- Naive approach: Just multiply equity price by exchange rate
- Sophisticated approach: `Return(RUB) = Return(Equity) + Return(FX)`
- *Why it matters*: Correctly separates equity risk from currency risk, allowing independent management

### Real-World Market Events in This Analysis

This project encompasses two major market crises:

**COVID-19 Pandemic (March 2020)**
- Sudden market shock with extreme volatility
- NASDAQ100 and DAX both dropped significantly
- VaR estimates spiked as correlations increased
- Lesson: Diversification breaks down in crises

**Russia-Ukraine Conflict (February 2022)**
- Geopolitical shock with currency impact
- USD/RUB and EUR/RUB depreciated 30%+ within weeks
- For Russian investor: Portfolio value in rubles actually *increased* (currency effect dominated)
- Lesson: FX risk can overwhelm equity risk in certain scenarios

## Key Features

### 1. **Multi-Factor Risk Decomposition**
- Separates equity risk and foreign exchange risk components
- Models asset returns as additive log-returns: `r_RUB = r_equity + r_forex`
- Applies beta-adjusted returns to capture systematic market risk
- Tracks correlation dynamics between risk factors

### 2. **Dynamic Volatility Modeling**
- **EWMA (Exponentially Weighted Moving Average)** volatility estimation with λ = 0.94
- Captures volatility clustering and time-varying market conditions
- Produces daily-updated covariance matrices
- Compares pre-crisis (Feb 23, 2022) vs. crisis (Sep 3, 2022) risk regimes

### 3. **Parametric VaR Estimation**
- **Normal parametric VaR** assuming normally distributed returns
- Systematic VaR using correlations between market factors
- Stand-alone VaR analysis for equity and forex components
- 1-day and 10-day VaR horizons at 1% significance level

### 4. **Non-Parametric VaR Estimation**
- **Historical VaR** approach without distributional assumptions
- Robust to tail events and extreme market conditions
- Serves as validation against parametric assumptions

### 5. **Risk Analytics & Visualization**
- Time-series evolution of market indexes and exchange rates
- Distribution analysis of portfolio returns
- Volatility surface and correlation dynamics
- Comparative VaR analysis across methodologies and time periods

## Technical Stack

- **Python 3.x**
- **Data Processing**: Pandas, NumPy
- **Statistical Analysis**: SciPy, Numpy
- **Visualization**: Matplotlib, Seaborn
- **Data Source**: Excel (.xlsx) with historical NASDAQ100, DAX, and forex rates

## Dataset

**File**: `2122_RM_Data.xlsx`

Contains daily observations from September 3, 2017 to September 3, 2022:
- NASDAQ 100 index values
- DAX index values
- USD/RUB exchange rates
- EUR/RUB exchange rates

This 5-year span captures two major market shocks, providing robust stress-testing capabilities.

## Project Structure

```
Project_Market_Risk_v6.ipynb   # Complete analysis notebook with all calculations
2122_RM_Data.xlsx              # Historical market data
Market_Risk_Report.pdf         # Detailed findings and interpretations
```

## Analysis Sections

### Part I: Exploratory Data Analysis (EDA)
1. Market index evolution and volatility patterns
2. Currency conversion and impact on portfolio value
3. Daily returns decomposition (equity vs. forex)
4. Distribution analysis and normality testing

### Part II: Risk Factor Modeling
1. EWMA volatility and correlation estimation
2. Portfolio return adjustment for beta exposure
3. Covariance matrix development for risk-neutral pricing
4. Regime comparison (pre-crisis vs. crisis periods)

### Part III: Value-at-Risk Quantification
1. Parametric (Normal) VaR with systematic risk decomposition
2. Stand-alone VaR for equity and forex components
3. Historical VaR validation
4. Sensitivity and stress testing

## Key Findings

- **Significant currency risk**: USD/RUB and EUR/RUB exhibited 30%+ depreciation during Feb 2022 crisis period
- **Volatility clustering**: Both equity and forex returns show pronounced clustering around geopolitical events
- **Correlation dynamics**: Equity and forex risks become highly correlated during crisis periods
- **VaR estimates**: 1-day 1% Normal VaR ranges from 2.1% to 3.8% depending on time period and risk regime
- **Beta adjustment**: Systematic VaR accurately captures market-specific risk exposure

## Methodological Highlights

### EWMA Volatility Estimation
```
σ²ₜ = (1 - λ)r²ₜ₋₁ + λσ²ₜ₋₁
```
Recursive formula with λ = 0.94 emphasizes recent observations while maintaining historical context.

### Normal Parametric VaR
```
VaR = Portfolio Value × (μ - σ × Z₁₋ₐ)
```
Where Z₁₋ₐ is the quantile of standard normal distribution at significance level α.

### Historical VaR
Empirical quantile approach: sorts historical returns and identifies the α-th percentile.

## Real-World Applications & Business Value

### Who Uses VaR Analysis?

**Financial Institutions**
- **Investment Banks**: Determine trading desk limits ("You can risk $5M per day maximum")
- **Hedge Funds**: Size positions to stay within portfolio risk budgets
- **Insurance Companies**: Model claims liabilities and investment risks simultaneously
- **Pension Funds**: Ensure asset allocation stays within risk tolerance
- **Central Banks**: Monitor systemic financial risks

**Regulatory & Compliance**
- **Basel III Framework**: Banks must calculate VaR for regulatory capital requirements
- **Dodd-Frank Act**: Enhanced risk disclosure for large financial institutions
- **MiFID II**: European requirement for risk transparency to clients
- **Central Clearing**: CCPs use VaR to set margin requirements

**Business Decision-Making**
- **CFO Planning**: "What's our worst-case cash flow impact?"
- **Insurance Pricing**: Build risk premiums into customer quotes
- **Mergers & Acquisitions**: Evaluate risk profiles of potential targets
- **Portfolio Management**: Construct optimal asset allocation with known risk constraints

### Why This Project Matters

✓ **Demonstrates end-to-end quantitative thinking**: From raw data to actionable risk metrics  
✓ **Handles complexity**: Multi-currency, multi-asset, multi-factor portfolio  
✓ **Addresses real constraints**: Forex exposure isn't theoretical—it's critical for global investors  
✓ **Applies multiple methodologies**: No single approach; validates findings across techniques  
✓ **Incorporates market realities**: Stress-tested against COVID and geopolitical crises  

### Skills Demonstrated

| Category | Skill | Application |
|----------|-------|-------------|
| **Programming** | Python, Pandas, NumPy | Data processing & calculations |
| **Statistics** | Volatility modeling, hypothesis testing | EWMA, correlation analysis |
| **Finance** | VaR, beta adjustment, portfolio theory | Risk decomposition & measurement |
| **Communication** | Clear explanations of complex concepts | Professional report with charts |
| **Problem-Solving** | Decomposing multi-factor problems | Separating equity and FX risk |

## Results & Interpretations

Comprehensive PDF report (`Market_Risk_Report.pdf`) includes:
- Statistical tables of volatility, correlations, and VaR estimates
- Discussion of assumptions and limitations
- Real-world interpretation of risk metrics
- Comparison of methodologies and robustness checks

## How to Use

1. **Open the notebook**: `Project_Market_Risk_v6.ipynb` in Jupyter
2. **Review the data**: Check `2122_RM_Data.xlsx` for historical prices
3. **Run the analysis**: Execute all cells sequentially
4. **Generate outputs**: Visualizations and risk tables are produced automatically
5. **Read the report**: `Market_Risk_Report.pdf` for detailed interpretation

## Code Quality

- Well-commented Python code
- Modular structure with clear section headers
- Error handling and data validation
- Reproducible results with fixed random seeds
- Professional visualization standards

## Insights for Risk Practitioners

- **Demonstrates mastery of**: quantitative risk analysis, time-series modeling, statistical inference
- **Solves complex problem**: multi-factor, multi-currency portfolio risk with FX exposure
- **Handles real scenarios**: incorporates major market crises and regime changes
- **Produces actionable output**: VaR estimates for risk committees and trading desks

## What This Project Says About the Developer

### For HR & Hiring Managers

This project demonstrates:

**🎯 Problem-Solving Ability**
- Takes a complex, real-world scenario (Russian investor with USD/EUR exposure)
- Breaks it into manageable components (equity risk + FX risk)
- Solves each component rigorously, then integrates them
- *What this means*: Can tackle undefined business problems and deliver structured solutions

**📊 Data Fluency**
- Works with unstructured time-series data
- Cleans, transforms, and validates data quality
- Applies statistical methods appropriately
- *What this means*: Can own analytics projects from data to delivery

**🏗️ Technical Foundation**
- Implements mathematical concepts (EWMA, covariance, VaR) correctly
- Writes production-quality Python
- Handles edge cases (missing data, market shocks)
- *What this means*: Can maintain code over time and adapt to new requirements

**📈 Business Acumen**
- Understands why VaR matters to real organizations
- Knows regulatory constraints (Basel, risk limits)
- Translates quantitative outputs into business language
- *What this means*: Won't optimize for the wrong metric; understands business impact

**🧪 Analytical Rigor**
- Validates assumptions (normality testing)
- Compares methodologies against each other
- Tests across multiple time periods
- *What this means*: Produces trustworthy analysis, not just numbers

### For Technical Teams

This project shows:
- Mastery of quantitative finance concepts
- Professional Python and data science skills
- Ability to handle real financial data complexities
- Understanding of statistical pitfalls and assumptions
- Communication skills (clear report writing)

---

## Perfect For

✅ **Remote Work Roles**
- Risk analysis consultant
- Quantitative analyst (quant)
- Data scientist (finance/fintech)
- Financial technology engineer
- Risk modeling specialist

✅ **Freelance Opportunities**
- Portfolio risk assessments
- VaR model development
- Risk framework consulting
- Financial analysis reports

✅ **Consulting & Startups**
- Risk advisory projects
- Model validation work
- Financial due diligence
- Risk dashboard development

---

**Last Updated**: April 2022  
**Analysis Date**: September 3, 2022  
**Data Period**: September 3, 2017 - September 3, 2022

---

## Getting Started

1. **Review this README** to understand the problem and approach
2. **Read Market_Risk_Report.pdf** for detailed findings
3. **Run Project_Market_Risk_v6.ipynb** to see all analyses and visualizations
4. **Explore the data** using 2122_RM_Data.xlsx

All code is production-ready and well-commented for review and modification.

