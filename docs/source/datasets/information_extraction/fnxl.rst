===============================
FNXL (Financial Numeric Extraction)
===============================

.. raw:: html
   :file: images/fnxl_diagram.html

**Figure 1.**

.. contents:: Table of Contents
   :local:

Goal
====
The **FNXL** dataset is designed for **Numeric Entity Recognition** and **Linking** in the financial domain. Its primary goals are:

- To extract numeric values from financial texts and link them to rigorous financial concepts (taxonomy tags).
- To handle extremely fine-grained semantic labels found in financial reporting standards (like XBRL).
- To bridge the gap between unstructured financial text and structured financial data.

Description
===========
**FNXL** is a dataset from ChanceFocus, dealing with the identification and categorization of numeric entities in SEC filings.

Dataset Composition
-------------------
- **Task**: Sequence Labeling (Token Classification) for numeric entities.
- **Labels**: High-cardinality label set corresponding to financial taxonomy concepts (e.g., ``DeferredCompensationArrangementWithIndividualCompensationExpense``).
- **Source**: Financial reports and 10-K filings.
- **Modality**: Text
- **Language**: English

Annotation Process
------------------
The dataset involves tagging numbers with specific, standardized financial tags, often requiring deep domain knowledge and context from the surrounding text.

Example
-------
Below is a representative example of the FNXL task:

.. list-table:: FNXL Examples
   :widths: 15 50 35
   :header-rows: 1

   * - ID
     - Text
     - Tagged Entities
   * - 0
     - Compensation expense was $0.6 million in 2019.
     - | **$0.6**: DeferredCompensationArrangement...
   * - 1
     - The company recorded a tax benefit of $1.2 billion.
     - | **$1.2**: TaxCutsAndJobsActOf2017...

Task Description
================
Numeric Entity Labeling
-----------------------
- **Input**: A financial sentence containing numerical data.
- **Output**: A sequence of tags assigning specific financial concepts to the numbers.
- **Challenge**: The sheer number of unique labels (thousands of potential XBRL tags) and the need to disambiguate similar numbers based on context.

Evaluation Metrics
==================
1. **Micro-F1**: Weighted average of F1 scores across all classes.
2. **Key-F1**: Performance on the most frequent or important financial tags.

Why Use FNXL?
=============
- **Automated Auditing**: Verification of reported numbers against textual descriptions.
- **Financial Analysis**: Extracting structured data series from unstructured notes.
- **Taxonomy Alignment**: Direct mapping to standardized accounting principles.

References
==========
For dataset access and more details, visit the `HuggingFace dataset page <https://huggingface.co/datasets/ChanceFocus/flare-fnxl>`_.
