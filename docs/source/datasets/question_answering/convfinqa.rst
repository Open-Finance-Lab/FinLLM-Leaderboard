=====================================
ConvFinQA
=====================================

.. contents:: Table of Contents
   :local:

Goal
====
The **ConvFinQA** dataset is designed to advance **conversational question answering** over financial documents. Its primary goals are:

- To enable **multi-turn dialogue** systems for financial document analysis
- To capture **context-dependent reasoning** across conversation history
- To benchmark **numerical reasoning** in conversational AI for finance

Description
===========
**ConvFinQA** is a conversational question answering dataset built from earnings reports, where each conversation involves multiple questions that build upon previous context and answers.

Dataset Composition
------------------------
- **Source**: Earnings reports and financial statements from S&P 500 companies
- **Time Period**: Recent financial reports (2019-2020)
- **Sample Size**: 3,892 conversations with 14,115 questions
- **Document Coverage**: Tables and text from quarterly and annual financial reports

Example
-------
**Context**: A table showing company revenue across quarters with associated textual explanation

**Conversation**:

- **Q1**: "What was the revenue in Q2 2020?"
- **A1**: "$135.7 million"

- **Q2**: "How does that compare to the previous quarter?"
- **A2**: "It increased by $15.2 million" (requires referencing Q1 2020 from table and computing difference)

- **Q3**: "What was the percentage growth?"
- **A3**: "12.6%" (requires computing (135.7-120.5)/120.5 * 100)

Task Description
=====================
Conversational Financial Question Answering
----------------------------------------------
- **Input**: A conversation history, current question, financial table, and associated text
- **Output**: Answer (extracted answeror computed value) based on full conversation context
- **Challenge**: Requires tracking conversation state, understanding temporal references, and performing numerical reasoning across turns

Key Use Cases
----------------
1. **Interactive Financial Analysis**: Conversational AI assistants for earnings call analysis
2. **Investor Relations**: Automated systems answering investor queries about financial performance
3. **Financial Advisory**: Dialogue systems helping clients understand investment reports

Evaluation Metrics
=====================
1. **Exact Match (EM)**: Percentage of exact correct answers
2. **F1-Score**: Harmonic mean of precision and recall

References
==========
Zhiyu Chen, Wenhu Chen, Charese Smiley, Sameena Shah, Iana Borova, Dylan Langdon, Reema Moussa, Matt Beane, Ting-Hao Huang, Bryan Routledge, and William Yang Wang. "ConvFinQA: Exploring the Chain of Numerical Reasoning in Conversational Finance Question Answering." In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2022.

For dataset access, visit the `official repository <https://github.com/czyssrs/ConvFinQA>`_ or `HuggingFace <https://huggingface.co/datasets/dreamerdeo/convfinqa>`_.
