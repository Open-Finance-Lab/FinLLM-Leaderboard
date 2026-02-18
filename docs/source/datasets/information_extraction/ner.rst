===============================
Flare-NER (Financial NER)
===============================

.. raw:: html
   :file: images/flare_ner_diagram.html

**Figure 1.**

.. contents:: Table of Contents
   :local:

Goal
====
The **Flare-NER** dataset is designed for **Named Entity Recognition (NER)** in the financial domain. Its primary goals are:

- To identify key financial entities such as **Persons (PER)**, **Organizations (ORG)**, and **Locations (LOC)** in unstructured financial texts.
- To facilitate the extraction of structured information from **financial agreements** and **SEC filings**.
- To provide a benchmark for evaluating NER models on specialized financial language.

Description
===========
**Flare-NER** is a dataset curated by ChanceFocus, consisting of sentences extracted from financial filings.

Dataset Composition
-------------------
- **Source**: Sentences extracted from **U.S. SEC filings**, specifically financial agreements.
- **Entities**: Annotated with three standard entity types relevant to finance:
    - **PER** (Person)
    - **ORG** (Organization)
    - **LOC** (Location)
- **Modality**: Text
- **Size**: Approximately 600+ rows (based on HuggingFace preview).
- **Format**: Parsing-ready format for sequence labeling tasks.

Annotation Process
------------------
The dataset focuses on categorizing named entities within the complex sentence structures often found in legal and financial documents.

Example
-------
Below is a representative example of the NER task:

.. list-table:: Flare-NER Examples
   :widths: 15 70 15
   :header-rows: 1

   * - ID
     - Text
     - Entities
   * - 0
     - The Borrower shall pay the Bank of New York Mellon, as administrative agent.
     - ORG: Bank of New York Mellon
   * - 1
     - Mr. John Smith, designated as the authorized signatory for ABC Corp, signed the agreement in London.
     - PER: John Smith, ORG: ABC Corp, LOC: London

Task Description
================
Named Entity Recognition
------------------------
- **Input**: A sentence from a financial document (e.g., "Goldman Sachs reported earnings in New York.")
- **Output**: A sequence of tags indicating the start and type of entities (e.g., [B-ORG, I-ORG, O, O, O, B-LOC, I-LOC]).
- **Challenge**: Financial texts often contain complex entity names (e.g., "The Bank of Tokyo-Mitsubishi UFJ, Ltd.") and nested structures.

Evaluation Metrics
==================
1. **F1-Score**: The harmonic mean of precision and recall, strictly matching entity boundaries and types.
2. **Precision**: The percentage of predicted entities that are correct.
3. **Recall**: The percentage of actual entities that were correctly predicted.

Why Use Flare-NER?
==================
- **Domain-Specific**: Tailored for financial agreements and SEC filings, distinct from general news datasets (e.g., CoNLL-2003).
- **Structured Information Extraction**: Essential for downstream tasks like relation extraction and knowledge graph construction in finance.
- **Open Access**: Available on HuggingFace for research and development.

References
==========
For dataset access and more details, visit the `HuggingFace dataset page <https://huggingface.co/datasets/ChanceFocus/flare-ner>`_.
