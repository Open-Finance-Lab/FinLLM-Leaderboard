=====================================
FinTrade
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **FinTrade** dataset is designed to evaluate **strategic decision-making** in stock trading. Its primary goals are:

- To assess **LLM-based trading agents** in realistic market scenarios
- To benchmark **multi-modal financial reasoning** combining prices, news, and sentiment
- To evaluate **risk management** and profitability in trading decisions

Description
===========
**FinTrade** is a stock trading dataset developed for FinBen, containing historical stock prices, financial news, and sentiment data for 10 stocks over one year. It enables evaluation of LLMs as financial trading agents.

Dataset Composition
------------------------
- **Source**: Historical stock prices, financial news, and sentiment analysis
- **Time Period**: One year of trading data
- **Sample Size**: 10 stocks with 3,384 evaluation instances
- **Data Modalities**: Time series (prices), text (news), and sentiment scores

Example
-------
**Trading Scenario for Tesla (TSLA)**:

**Historical Prices**: 
- Day -5: Open $850, Close $845 (-0.6%)
- Day -4: Open $847, Close $855 (+0.9%)
- Day -3: Open $856, Close $848 (-0.9%)
- Day -2: Open $849, Close $862 (+1.5%)
- Day -1: Open $863, Close $858 (-0.6%)

**Recent News**:
"Tesla announces record quarterly deliveries, beating analyst expectations by 12%. CEO Elon Musk highlights expansion of Gigafactory production capacity."

**Sentiment Score**: 0.85 (very positive)

**Current Portfolio**: Holding 10 shares, unrealized gain: +15%

**Decision Required**: Buy more shares / Sell existing position / Hold current position

**Agent Output**: "Buy - Strong positive momentum from delivery beat and production expansion news. Positive sentiment and recent price consolidation suggest upward movement likely."

Task Description
=====================
Stock Trading Decision Making
--------------------------------
- **Input**: Historical stock prices, news articles, sentiment data, and current portfolio state
- **Output**: Trading decision (buy, sell, or hold) with supporting rationale
- **Challenge**: Requires synthesizing information across multiple modalities, understanding market dynamics, and balancing risk versus reward

Key Use Cases
----------------
1. **Algorithmic Trading**: Automated trading decision systems
2. **Portfolio Management**: Strategic investment optimization
3. **Risk Management**: Position management under uncertainty

Evaluation Metrics
=====================
1. **Cumulative Return (CR)**: Total profitability of trading strategy
2. **Sharpe Ratio (SR)**: Risk-adjusted return metric
3. **Maximum Drawdown (MD)**: Largest peak-to-trough decline
4. **Daily Volatility (DV)** and **Annualized Volatility (AV)**: Risk measures

References
==========
Qianqian Xie, Weiguang Han, Zhengyu Chen, Ruoyu Xiang, Xiao Zhang, Yueru He, Mengxi Xiao, Dong Li, Yongfu Dai, Duanyu Feng, et al. "FinBen: An Holistic Financial Benchmark for Large Language Models." arXiv preprint arXiv:2402.12659, 2024.

For dataset access, visit the `FinBen repository <https://github.com/The-FinAI/PIXIU>`_.
