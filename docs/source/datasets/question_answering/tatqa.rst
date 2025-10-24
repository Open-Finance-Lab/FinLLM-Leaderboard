=====================================
TAT-QA (Tabular And Textual QA)
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **TAT-QA** dataset is designed to advance **hybrid question answering** over financial documents. Its primary goals are:

- To enable **numerical reasoning** over combined tabular and textual data
- To support **complex multi-step reasoning** in financial document analysis
- To benchmark **hybrid QA systems** for finance

Description
===========
**TAT-QA** is a large-scale question answering dataset built from real-world financial reports, requiring models to jointly reason over tables and associated text to answer complex questions.

Dataset Composition
------------------------
- **Source**: Financial reports from U.S. companies (10-K, 10-Q filings)
- **Time Period**: Recent financial filings (2018-2020)
- **Sample Size**: 16,552 questions across 2,757 table-text pairs
- **Document Types**: Quarterly and annual financial reports with hybrid content

Example
-------
**Context**: A financial table showing quarterly revenue alongside text describing business performance

**Question**: "What was the total net income for the first half of 2020?"

**Answer**: "$78.8 million" (requires arithmetic: combining Q1 and Q2 net income)

Task Description
=====================
Hybrid Question Answering with Numerical Reasoning
-----------------------------------------------------
- **Input**: A question, an associated financial table, and related text passage
- **Output**: Answer span or computed numerical value
- **Challenge**: Requires understanding table structure, comprehending text, identifying relevant cells/spans, and performing multi-step numerical operations

Key Use Cases
----------------
1. **Financial Analysis**: Automated extraction of insights from earnings reports
2. **Investor Decision Support**: Quick answers to investor queries about company performance
3. **Compliance and Audit**: Verification of financial statement consistency

Evaluation Metrics
=====================
1. **Exact Match (EM)**: Percentage of predictions exactly matching gold answers
2. **F1-Score**: Token-level F1 score for partial credit on numerical answers

References
==========
Fengbin Zhu, Wenqiang Lei, Youcheng Huang, Chao Wang, Shuo Zhang, Jiancheng Lv, Fuli Feng, and Tat-Seng Chua. "TAT-QA: A Question Answering Benchmark on a Hybrid of Tabular and Textual Content in Finance." In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL), 2021.

For dataset access, visit the `official repository <https://github.com/NExTplusplus/TAT-QA>`_ or `HuggingFace <https://huggingface.co/datasets/tatqa>`_.
