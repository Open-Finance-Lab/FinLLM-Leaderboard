=====================================
FinQA
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **FinQA** dataset is designed to advance **numerical reasoning** over financial documents. Its primary goals are:

- To enable **multi-step numerical reasoning** over financial reports
- To support **program synthesis** for answering complex financial questions
- To benchmark **quantitative reasoning** in financial AI

Description
===========
**FinQA** is a large-scale dataset for numerical reasoning over financial documents, requiring models to synthesize reasoning programs to answer questions from earnings reports.

Dataset Composition
------------------------
- **Source**: Earnings reports from S&P 500 companies
- **Time Period**: Reports from 2016-2019
- **Sample Size**: 8,281 question-answer pairs
- **Document Coverage**: Mix of tables and text from quarterly and annual reports

Example
-------
**Context**: Financial table showing revenue and expenses

**Question**: "What is the change in operating margin from 2018 to 2019?"

**Answer**: "5 percentage points" (requires multi-step calculation)

Task Description
=====================
Financial Numerical Reasoning
--------------------------------
- **Input**: Question, financial document (tables and text)
- **Output**: Numerical answer with reasoning program
- **Challenge**: Requires extracting relevant facts, understanding financial concepts, and performing multi-step numerical operations

Key Use Cases
----------------
1. **Automated Financial Analysis**: Extracting quantitative insights from earnings reports
2. **Investment Research**: Answering analyst questions about company performance
3. **Financial Education**: Interactive learning systems for financial statement analysis

Evaluation Metrics
=====================
1. **Execution Accuracy**: Percentage of questions where the predicted program generates the correct answer
2. **Program Accuracy**: Percentage of questions where the predicted program exactly matches the gold program

References
==========
Zhiyu Chen, Wenhu Chen, Charese Smiley, Sameena Shah, Iana Borova, Dylan Langdon, Reema Moussa, Matt Beane, Ting-Hao Huang, Bryan Routledge, and William Yang Wang. "FinQA: A Dataset of Numerical Reasoning over Financial Data." In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2021.

For dataset access, visit the `official repository <https://github.com/czyssrs/FinQA>`_ or `HuggingFace <https://huggingface.co/datasets/dreamerdeo/finqa>`_.
