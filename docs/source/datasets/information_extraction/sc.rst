===============================
Causal-SC (Causal Sentence Classification)
===============================

.. raw:: html
   :file: images/causal_sc_diagram.html

**Figure 1.**

.. contents:: Table of Contents
   :local:

Goal
====
The **Causal-SC** dataset is designed for **Sentence Classification (SC)** focusing on causality in the financial domain. Its primary goals are:

- To detect causal relationships in financial news and texts (e.g., "Stock rose **due to** strong earnings").
- To distinguish between causal statements and non-causal (noise) text.
- To support the development of models that can understand cause-and-effect in financial markets.

Description
===========
**Causal-SC** is a dataset from ChanceFocus, containing sentences annotated for the presence of causal logic.

Dataset Composition
-------------------
- **Source**: Financial news and SEC filings.
- **Classes**:
    - **Causal**: Sentences containing a cause-effect relationship.
    - **Noise**: Sentences without causal content.
- **Size**: 1K - 10K examples.
- **Modality**: Text
- **Language**: English

Annotation Process
------------------
The dataset focuses on identifying explicit causal links, which are crucial for explaining market movements and financial events.

Example
-------
Below is a representative example of the Causal Classification task:

.. list-table:: Causal-SC Examples
   :widths: 15 70 15
   :header-rows: 1

   * - ID
     - Text
     - Label
   * - 0
     - The company's profits surged because of higher demand in Asia.
     - Causal
   * - 1
     - The board meeting is scheduled for next Monday.
     - Noise

Task Description
================
Sentence Classification
-----------------------
- **Input**: A financial sentence.
- **Output**: Binary classification label (Causal or Noise).
- **Challenge**: Distinguishing subtle causal inferences from mere correlation or temporal sequence.

Evaluation Metrics
==================
1. **Accuracy**: The percentage of correctly classified sentences.
2. **F1-Score**: Particularly important if the classes are imbalanced.

Why Use Causal-SC?
==================
- **Explainability**: Helps in building systems that can explain *why* financial events happen.
- **Event Logic**: Crucial for event-driven trading strategies that rely on cause-effect analysis.
- **Specialized Domain**: Targets financial causality, which differs from general domain causality.

References
==========
For dataset access and more details, visit the `HuggingFace dataset page <https://huggingface.co/datasets/ChanceFocus/flare-causal20-sc>`_.
