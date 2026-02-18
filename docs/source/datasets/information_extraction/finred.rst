===============================
FinRED (Financial Relation Extraction)
===============================

.. raw:: html
   :file: images/finred_diagram.html

**Figure 1.**

.. contents:: Table of Contents
   :local:

Goal
====
The **FinRED** dataset is designed for **Relation Extraction (RE)** in the financial domain. Its primary goals are:

- To identify and classify semantic relationships between financial entities (e.g., "acquired by", "subsidiary of", "competitor of").
- To facilitate the construction of financial knowledge graphs.
- To enable structured information retrieval from unstructured financial texts.

Description
===========
**FinRED** is a relation extraction dataset from ChanceFocus, consisting of sentence-level relation annotations.

Dataset Composition
-------------------
- **Source**: Financial news and filings.
- **Task**: Extract triples in the format ``(Head Entity, Tail Entity, Relation)``.
- **Size**: 1K - 10K examples (based on HuggingFace metadata).
- **Modality**: Text
- **Format**: Parquet

Annotation Process
------------------
The dataset targets the extraction of specific financial relationships, requiring models to understand the context connecting two entities.

Example
-------
Below is a representative example of the Relation Extraction task:

.. list-table:: FinRED Examples
   :widths: 15 55 30
   :header-rows: 1

   * - ID
     - Text
     - Relations (Head; Tail; Rel)
   * - 0
     - Google acquired YouTube in a billion-dollar deal.
     - Google; YouTube; acquired
   * - 1
     - Apple, based in Cupertino, released the new iPhone.
     - Apple; Cupertino; headquarters_location

Task Description
================
Relation Extraction
-------------------
- **Input**: A sentence containing marked entities.
- **Output**: A list of triplets ``head; tail; rel`` representing the relationships found.
- **Challenge**: Handling multiple relations per sentence and identifying the directionality of relationships.

Evaluation Metrics
==================
1. **F1-Score**: Harmonic mean of precision and recall for extracted triplets.
2. **Precision**: Percentage of extracted relations that are correct.
3. **Recall**: Percentage of ground truth relations that were extracted.

Why Use FinRED?
================
- **Structured Knowledge**: Converts unstructured text into structured databases (Knowledge Graphs).
- **Financial Context**: capturing specific relations relevant to markets (e.g., M&A, leadership changes).
- **Open Resource**: Part of the FLARE benchmark for advancing financial NLP.

References
==========
For dataset access and more details, visit the `HuggingFace dataset page <https://huggingface.co/datasets/ChanceFocus/flare-finred>`_.
