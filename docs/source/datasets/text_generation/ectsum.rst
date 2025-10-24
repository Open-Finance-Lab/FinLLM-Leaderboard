=====================================
ECTSUM
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **ECTSUM** dataset is designed to advance **bullet point summarization** of earnings call transcripts. Its primary goals are:

- To enable **extractive summarization** of lengthy earnings calls
- To extract **key financial insights** from executive discussions
- To benchmark **long-document summarization** in finance

Description
===========
**ECTSUM** is a dataset for extractive bullet point summarization of earnings call transcripts, containing transcripts paired with ground-truth extractive summaries in telegram-style bullet points.

Dataset Composition
------------------------
- **Source**: Earnings call transcripts from publicly traded companies
- **Time Period**: Various quarters from earnings call data
- **Sample Size**: 495 earnings call transcripts
- **Content Structure**: Management presentation and analyst Q&A sections

Example
-------
**Input Transcript Excerpt**:

"Good morning, and welcome to our Q2 2021 earnings call. We are pleased to report revenue of $15.2 billion, representing 23% growth year-over-year. This strong performance was driven by our cloud computing division, which saw 47% growth, and our digital advertising segment, which grew 31%. Gross margin improved to 45%, up from 42% in the prior year, reflecting operational efficiencies and scale benefits. Operating income reached $3.1 billion, a 35% increase. We also generated $4.2 billion in free cash flow during the quarter. Looking forward, we are raising our full-year revenue guidance to $62-64 billion, up from our previous range of $58-61 billion..."

**Extractive Summary** (Telegram-style bullet points):

• Q2 2021 revenue: $15.2B, up 23% YoY
• Cloud computing division growth: 47%
• Digital advertising segment growth: 31%
• Gross margin improved to 45% from 42%
• Operating income: $3.1B, up 35%
• Free cash flow: $4.2B
• FY guidance raised to $62-64B from $58-61B

Task Description
=====================
Extractive Bullet Point Summarization
----------------------------------------------
- **Input**: Full earnings call transcript (7,000-15,000 words)
- **Output**: Extractive bullet point summary (telegram-style)
- **Challenge**: Identifying salient sentences from long, unstructured financial discussions and presenting them as concise bullet points

Key Use Cases
----------------
1. **Investor Research**: Quickly extracting critical financial metrics from earnings calls
2. **Financial Analysis**: Identifying key guidance and performance indicators
3. **News Generation**: Creating structured summaries for financial reporting

Evaluation Metrics
==================
1. **ROUGE Scores**: ROUGE-1, ROUGE-2, ROUGE-L for n-gram overlap
2. **BERTScore**: Semantic similarity between generated and reference summaries

References
==========
Rajdeep Mukherjee, Abhinav Bohra, Akash Banerjee, Soumya Sharma, Manjunath Hegde, Afreen Shaikh, Shivani Shrivastava, Koustuv Dasgupta, Niloy Ganguly, Saptarshi Ghosh, and Pawan Goyal. "ECTSum: A New Benchmark Dataset For Bullet Point Summarization of Long Earnings Call Transcripts." In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 10893–10906, 2022.

For dataset access, visit `HuggingFace <https://huggingface.co/datasets/TheFinAI/flare-ectsum>`_.
