=====================================
BigData22
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **BigData22** dataset is designed to advance **stock movement prediction** with self-supervised learning from sparse noisy tweets. Its primary goals are:

- To predict **stock price movements** from noisy social media data
- To handle **sparse and unreliable** social media signals
- To benchmark **robust forecasting** methods for financial markets

Description
===========
**BigData22** is a stock movement prediction dataset focusing on learning from sparse and noisy tweets combined with historical stock prices.

Dataset Composition
------------------------
- **Source**: Twitter posts and historical stock prices
- **Time Period**: Recent trading periods with social media activity
- **Sample Size**: 7,164 instances
- **Data Modalities**: Text (tweets) and time series (stock prices)

Example
-------
**Stock**: Tesla Inc. (TSLA)

**Historical Prices** (3-day window):
- Day -3: Open $850.00, Close $845.00 (-0.59%)
- Day -2: Open $847.00, Close $862.00 (+1.77%)
- Day -1: Open $863.00, Close $858.00 (-0.58%)

**Sparse Tweets** (noisy data):
- "$TSLA to the moon 🚀🚀" (3 likes, low credibility)
- "Elon musk factory tour tomorrow" (15 likes)
- "$TSLA delivery numbers looking strong this quarter - analyst" (250 likes, higher credibility)

**Prediction Target**: Rise or Fall (movement > ±0.55%)

**Ground Truth**: Rise (+2.1% next day based on actual delivery numbers)

Task Description
=====================
Stock Movement Prediction from Noisy Data
--------------------------------------------
- **Input**: Sparse, noisy tweets and historical stock prices
- **Output**: Binary classification (Rise or Fall)
- **Challenge**: Filtering noise from sparse social media data while extracting meaningful signals for prediction

Key Use Cases
----------------
1. **Retail Trading Signals**: Understanding retail investor sentiment from social media
2. **Noise Filtering**: Developing robust models that handle unreliable data sources
3. **Social Media Analytics**: Measuring impact of social chatter on stock prices

Evaluation Metrics
==================
1. **Accuracy (ACC)**: Percentage of correct predictions
2. **Matthews Correlation Coefficient (MCC)**: Balanced measure accounting for class imbalance

References
==========
Yejun Soun, Jaemin Yoo, Minyong Cho, Jihyeong Jeon, and U Kang. "Accurate Stock Movement Prediction with Self-supervised Learning from Sparse Noisy Tweets." In 2022 IEEE International Conference on Big Data (Big Data), pages 1691–1700, 2022.

For dataset access, visit `HuggingFace <https://huggingface.co/datasets/TheFinAI/flare-sm-bigdata>`_.
