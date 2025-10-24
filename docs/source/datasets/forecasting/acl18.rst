=====================================
ACL18
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **ACL18** dataset is designed to advance **stock movement prediction** using social media and historical prices. Its primary goals are:

- To predict **stock price movements** from tweets and historical data
- To benchmark **multimodal financial forecasting** combining text and time series
- To evaluate **sentiment-driven trading signals**

Description
===========
**ACL18** is a stock movement prediction dataset containing tweets and historical stock prices. Models must predict whether a stock's price will rise or fall based on social media sentiment and price trends.

Dataset Composition
------------------------
- **Source**: Twitter posts and historical stock prices
- **Time Period**: Historical trading data with corresponding tweets
- **Sample Size**: 27,053 instances
- **Data Modalities**: Text (tweets) and time series (stock prices)

Example
-------
**Stock**: Apple Inc. (AAPL)

**Historical Prices** (5-day window):
- Day -5: $120.50 → $119.80 (-0.58%)
- Day -4: $119.80 → $121.30 (+1.25%)
- Day -3: $121.30 → $120.90 (-0.33%)
- Day -2: $120.90 → $122.10 (+0.99%)
- Day -1: $122.10 → $121.75 (-0.29%)

**Tweets**:
- "$AAPL new iPhone pre-orders exceed expectations! Strong demand across all models"
- "Apple suppliers ramping up production, bullish signal for Q4"
- "Analysts raising price targets on $AAPL after product launch"

**Prediction Target**: Rise or Fall (next day movement > ±0.5%)

**Ground Truth**: Rise (+1.2% next day)

Task Description
=====================
Stock Movement Prediction
--------------------------------
- **Input**: Historical stock prices (time series) and related tweets (text)
- **Output**: Binary classification (Rise or Fall)
- **Challenge**: Combining noisy social media signals with price patterns to predict short-term movements

Key Use Cases
----------------
1. **Algorithmic Trading**: Short-term trading signals from social sentiment
2. **Market Sentiment Analysis**: Tracking investor sentiment on social media
3. **Risk Management**: Early warning signals from social media discussions

Evaluation Metrics
==================
1. **Accuracy (ACC)**: Percentage of correct predictions
2. **Matthews Correlation Coefficient (MCC)**: Balanced measure for binary classification

References
==========
Yumo Xu and Shay B. Cohen. "Stock Movement Prediction from Tweets and Historical Prices." In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1970–1979, 2018.

For dataset access, visit `HuggingFace <https://huggingface.co/datasets/TheFinAI/flare-sm-acl>`_.
