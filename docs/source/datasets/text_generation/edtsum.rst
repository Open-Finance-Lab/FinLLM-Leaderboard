=====================================
EDTSUM
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **EDTSUM** dataset is designed to advance **abstractive summarization** of financial news articles. Its primary goals are:

- To enable **headline generation** from financial news
- To support **event detection** for news-based trading
- To benchmark **news summarization** in finance

Description
===========
**EDTSUM** is a dataset for abstractive summarization of financial news articles, containing news articles paired with their headlines as ground-truth summaries.

Dataset Composition
------------------------
- **Source**: Financial news articles
- **Time Period**: Various timeframes covering financial events
- **Sample Size**: 2,000 news articles with headlines
- **Content Focus**: Corporate events and financial news

Example
-------
**News Article**:

"Apple Inc. reported quarterly earnings that exceeded Wall Street expectations, with revenue reaching $89.5 billion in the fiscal third quarter. The company's iPhone sales showed resilience despite supply chain challenges, contributing to a 15% year-over-year growth. CEO Tim Cook highlighted the strong performance of the services division, which grew 27% from the previous year. The tech giant also announced a $90 billion share buyback program, signaling confidence in future growth."

**Generated Headline**:

"Apple Beats Earnings Expectations with $89.5B Revenue, Announces $90B Buyback"

Task Description
=====================
Abstractive News Summarization
-----------------------------------
- **Input**: Full financial news article
- **Output**: Generated headline/summary capturing the essence of the article
- **Challenge**: Generating concise, informative summaries that capture key financial events while maintaining factual accuracy

Key Use Cases
----------------
1. **Event-Driven Trading**: Identifying trading signals from news events
2. **Financial Monitoring**: Tracking corporate events and announcements
3. **News Aggregation**: Creating concise financial news summaries

Evaluation Metrics
==================
1. **ROUGE Scores**: ROUGE-1, ROUGE-2, ROUGE-L for lexical overlap
2. **BERTScore**: Semantic similarity measurement

References
==========
Zhihan Zhou, Liqian Ma, and Han Liu. "Trade the Event: Corporate Events Detection for News-Based Event-Driven Trading." In Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021, pages 2114–2124, 2021.

For dataset access, visit `HuggingFace <https://huggingface.co/datasets/TheFinAI/flare-edtsum>`_.
