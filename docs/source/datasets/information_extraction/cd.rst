===============================
Causal-CD (Causal Extraction)
===============================

.. raw:: html
   :file: images/causal_cd_diagram.html

**Figure 1.**

.. contents:: Table of Contents
   :local:

Goal
====
The **Causal-CD** dataset is designed for **Causal Extraction** (or Causal Detection) in the financial domain. Its primary goals are:

- To extract specific text spans representing **Cause** and **Effect** within a sentence.
- To perform sequence labeling (BIO tagging) for causal argument extraction.
- To understand the precise triggers and consequences of financial events.

Description
===========
**Causal-CD** is a dataset from ChanceFocus, focusing on the fine-grained extraction of causal elements.

Dataset Composition
-------------------
- **Task**: Sequence Labeling (Token Classification).
- **Labels**:
    - **CAUSE**: The reason or driver of an event.
    - **EFFECT**: The outcome or consequence.
- **Format**: Sentences with BIO tags (e.g., ``B-CAUSE``, ``I-CAUSE``, ``B-EFFECT``, ``I-EFFECT``).
- **Size**: Approximately 200+ examples (Test split).
- **Modality**: Text

Annotation Process
------------------
Annotators identify contiguous text spans that delineate the cause and the effect, leaving connecting words (like "because of", "due to") as "O" (Outside) or part of the structure depending on guidelines.

Example
-------
Below is a representative example of the Causal Extraction task:

.. list-table:: Causal-CD Examples
   :widths: 15 55 30
   :header-rows: 1

   * - ID
     - Text
     - Spans
   * - 0
     - Stock prices fell due to the unexpected inflation report.
     - | **Effect**: Stock prices fell
       | **Cause**: the unexpected inflation report
   * - 1
     - The company ceased trading, resulting in 2000 job losses.
     - | **Cause**: The company ceased trading
       | **Effect**: 2000 job losses

Task Description
================
Causal Sequence Labeling
------------------------
- **Input**: A financial sentence.
- **Output**: A sequence of tags assigning ``CAUSE`` or ``EFFECT`` labels to tokens.
- **Challenge**: Correctly delimiting long, complex causal phrases and handling multiple causal pairs in one sentence.

Evaluation Metrics
==================
1. **Span-based F1-Score**: Measures the overlap of predicted spans with ground truth spans.
2. **Exact Match**: Requires the entire span to be predicted correctly.

Why Use Causal-CD?
==================
- **Granular Understanding**: Goes beyond binary classification (Causal vs Noise) to pinpoint *what* caused *what*.
- **Event Extraction**: Essential for building event chains and logic graphs for market analysis.
- **Precision**: enabling detailed attribution of market movements to specific news factors.

References
==========
For dataset access and more details, visit the `HuggingFace dataset page <https://huggingface.co/datasets/ChanceFocus/flare-cd>`_.
