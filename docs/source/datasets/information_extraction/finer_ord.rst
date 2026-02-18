===============================
FiNER-ORD (Financial NER)
===============================

.. raw:: html
   :file: images/finer_ord_diagram.html

**Figure 1.**

.. contents:: Table of Contents
   :local:

Goal
====
The **FiNER-ORD** dataset is a high-quality financial Named Entity Recognition (NER) dataset. Its primary goals are:

- To address the lack of open-source, manually annotated NER datasets in the financial domain.
- To benchmark NER models on financial news articles.
- To identify standard entities (**PER**, **LOC**, **ORG**) in a specialized context.

Description
===========
**FiNER-ORD** consists of financial news stories collected from **Webz.io**, manually annotated for named entities.

Dataset Composition
-------------------
- **Source**: Financial news articles from Webz.io.
- **Selection**: 201 manually annotated articles selected from a larger corpus of 47,851 documents.
- **Entities**:
    - **PER** (Person)
    - **ORG** (Organization)
    - **LOC** (Location)
- **Modality**: Text
- **Language**: English

Annotation Process
------------------
The dataset was manually annotated by experts to ensure high quality, serving as a gold-standard benchmark for financial NER.

Example
-------
Below is a representative example of the NER task in FiNER-ORD:

.. list-table:: FiNER-ORD Examples
   :widths: 15 70 15
   :header-rows: 1

   * - ID
     - Text
     - Entities
   * - 0
     - Elon Musk, CEO of Tesla, announced the new factory in Berlin.
     - PER: Elon Musk, ORG: Tesla, LOC: Berlin
   * - 1
     - Apple Inc. shares rose after the report released in Cupertino.
     - ORG: Apple Inc., LOC: Cupertino

Task Description
================
Named Entity Recognition
------------------------
- **Input**: A sentence or paragraph from a financial news article.
- **Output**: A sequence of tags indicating the start and type of entities.
- **Challenge**: Distinguishing between financial entities in complex news narratives.

Evaluation Metrics
==================
1. **F1-Score**: The primary metric for evaluating NER performance.
2. **Precision**: Accuracy of the predicted entities.
3. **Recall**: Ability to find all relevant entities.

Why Use FiNER-ORD?
==================
- **Real-World Data**: Based on actual financial news, reflecting real-world usage.
- **High-Quality Annotations**: Manually curated to minimize noise.
- **Open Benchmark**: Freely available for research, fostering community progress.

References
==========
For dataset access and more details, visit the `HuggingFace dataset page <https://huggingface.co/datasets/ChanceFocus/flare-finer-ord>`_.
