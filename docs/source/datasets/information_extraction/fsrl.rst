===============================
FSRL (Financial Semantic Role Labeling)
===============================

.. raw:: html
   :file: images/fsrl_diagram.html

**Figure 1.**

.. contents:: Table of Contents
   :local:

Goal
====
The **FSRL** dataset is designed for **Semantic Role Labeling (SRL)** or **Textual Analogy Parsing (TAP)** in the financial domain. Its primary goals are:

- To parse financial sentences into semantic arguments like **TIME**, **VALUE**, **QUANT**, **AGENT**, and **THEME**.
- To identify "who did what to whom, when, and how much" in financial contexts.
- To structure complex financial narratives into actionable data points.

Description
===========
**FSRL** is a dataset from ChanceFocus, applying semantic role labeling frameworks to financial news and reports.

Dataset Composition
-------------------
- **Task**: Sequence Labeling (Token Classification).
- **Labels**: A rich set of semantic roles tailored for finance:
    - **TIME**, **REF_TIME**: Temporal expressions.
    - **VALUE**, **QUANT**: Monetary amounts and quantities.
    - **AGENT**, **THEME**: Actors and subjects of actions.
    - **MANNER**, **CAUSE**, **CONDITION**: Modifiers explaining how/why.
- **Source**: Financial news articles.
- **Modality**: Text
- **Language**: English

Annotation Process
------------------
Annotators tag every token in a sentence with its semantic role, providing a comprehensive understanding of the sentence structure and meanining.

Example
-------
Below is a representative example of the FSRL task:

.. list-table:: FSRL Examples
   :widths: 15 60 25
   :header-rows: 1

   * - ID
     - Text
     - Roles
   * - 0
     - Earnings totaled $36.6 million in the nine months.
     - | **THEME**: Earnings
       | **VALUE**: $36.6 million
       | **TIME**: in the nine months
   * - 1
     - Shares fell 46% from a year earlier.
     - | **THEME**: Shares
       | **VALUE**: 46%
       | **TIME**: a year earlier

Task Description
================
Semantic Parsing
----------------
- **Input**: A financial sentence.
- **Output**: A sequence of BIO tags assigning semantic roles to tokens (e.g., ``B-TIME``, ``I-VALUE``).
- **Challenge**: Capturing the intricate relationships between numbers, dates, and entities in dense financial text.

Evaluation Metrics
==================
1. **Span-based F1-Score**: Measures the correctness of identified semantic arguments.
2. **Role Accuracy**: Ensuring the correct label is assigned to the correct span.

Why Use FSRL?
=============
- **Deep Understanding**: Moves beyond entity recognition to understanding the *relationships* and *roles* of entities.
- **Question Answering**: Enables systems to answer complex questions like "How much did earnings increase in Q3?".
- **Information Extraction**: Facilitates the extraction of structured event data from news feeds.

References
==========
For dataset access and more details, visit the `HuggingFace dataset page <https://huggingface.co/datasets/ChanceFocus/flare-fsrl>`_.
