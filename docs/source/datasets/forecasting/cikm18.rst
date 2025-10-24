=====================================
CIKM18
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **CIKM18** dataset is designed to advance **stock movement prediction** using hybrid deep sequential modeling. Its primary goals are:

- To predict **stock price movements** from social text and historical prices
- To benchmark **sequential modeling** approaches for financial forecasting
- To evaluate **deep learning** methods on financial time series

Description
===========
**CIKM18** is a stock movement prediction dataset that combines social text-driven signals with deep sequential modeling of historical prices.

Dataset Composition
------------------------
- **Source**: Social media posts (tweets) and historical stock prices
- **Time Period**: Historical trading data with social media activity
- **Sample Size**: 4,967 instances
- **Data Modalities**: Text (social media) and time series (stock prices)

Example
-------
**Stock**: Amazon.com Inc. (AMZN)

**Historical Prices** (sequential 5-day pattern):
- Day -5: Close $3,200 (volume: 4.2M)
- Day -4: Close $3,185 (volume: 3.8M, -0.47%)
- Day -3: Close $3,210 (volume: 5.1M, +0.79%)
- Day -2: Close $3,195 (volume: 4.5M, -0.47%)
- Day -1: Close $3,220 (volume: 6.2M, +0.78%)

**Social Text**:
- "Amazon Prime Day sales hit record highs, expect strong Q2 earnings"
- "$AMZN cloud services AWS gaining market share from competitors"
- "Retail analysts upgrading Amazon on strong e-commerce growth"

**Sequential Pattern**: Increasing volume with positive price momentum

**Prediction Target**: Rise or Fall (movement > ±0.5%)

**Ground Truth**: Rise (+1.5% following continued momentum)

Task Description
=====================
Stock Movement Prediction with Sequential Modeling
----------------------------------------------------
- **Input**: Social media text and sequential historical price data
- **Output**: Binary classification (Rise or Fall)
- **Challenge**: Capturing sequential dependencies in price movements while integrating social media sentiment signals

Key Use Cases
----------------
1. **Quantitative Trading**: Sequential pattern recognition for trading strategies
2. **Market Prediction**: Combining technical analysis with sentiment analysis
3. **Investment Research**: Understanding price momentum influenced by social sentiment

Evaluation Metrics
==================
1. **Accuracy (ACC)**: Percentage of correct predictions
2. **Matthews Correlation Coefficient (MCC)**: Correlation between predictions and actual outcomes

References
==========
Huizhe Wu, Wei Zhang, Weiwei Shen, and Jun Wang. "Hybrid Deep Sequential Modeling for Social Text-Driven Stock Prediction." In Proceedings of the 27th ACM International Conference on Information and Knowledge Management (CIKM), pages 1627–1630, 2018.

For dataset access, visit `HuggingFace <https://huggingface.co/datasets/TheFinAI/flare-sm-cikm>`_.
