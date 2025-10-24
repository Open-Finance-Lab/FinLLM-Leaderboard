=================================
FiQA-SA (Sentiment Analysis)
=================================

.. contents:: Table of Contents
   :local:

Description
===========
**FiQA-SA** is a sentiment analysis dataset for financial question answering, containing financial news headlines and microblog posts. The dataset evaluates sentiment on a continuous scale from -1 (most negative) to 1 (most positive).

Dataset Composition
------------------------
- **Source**: Financial news headlines and social media posts
- **Sample Size**: 1,173 annotated posts
- **Sentiment Scale**: Continuous values from -1 (negative) to 1 (positive)

Example
-------
**Text 1**: "Goldman Sachs upgraded the stock to buy with a price target of $150, citing strong fundamentals"

**Sentiment Score**: 0.8 (positive)

**Text 2**: "Company faces potential bankruptcy as debt obligations exceed available cash reserves"

**Sentiment Score**: -0.9 (very negative)

**Text 3**: "The Federal Reserve maintained interest rates at current levels"

**Sentiment Score**: 0.0 (neutral)

Task Description
================
Sentiment Analysis for Financial Texts
----------------------------------------
- **Input**: Financial news headlines or microblog posts
- **Output**: Sentiment score on a scale of [-1, 1]
- **Challenge**: Requires understanding nuanced financial sentiment and context from both formal news and informal social media

Key Use Cases
----------------
1. **Market Sentiment Analysis**: Tracking investor sentiment from news and social media
2. **Trading Signals**: Using sentiment as input for algorithmic trading strategies
3. **Risk Monitoring**: Identifying negative sentiment around specific assets

Evaluation Metrics
==================
1. **F1-Score**: Macro-averaged F1 for sentiment classification
2. **Accuracy**: Classification accuracy when sentiment is discretized

References
==========
Macedo Maia, Siegfried Handschuh, André Freitas, Brian Davis, Ross McDermott, Manel Zarrouk, and Alexandra Balahur. "WWW'18 Open Challenge: Financial Opinion Mining and Question Answering." In Companion Proceedings of the The Web Conference 2018 (WWW '18), 2018.

For dataset access, visit the `official challenge page <https://sites.google.com/view/fiqa/home>`_ or `HuggingFace <https://huggingface.co/datasets/ChanceFocus/flare-fiqasa>`_.
