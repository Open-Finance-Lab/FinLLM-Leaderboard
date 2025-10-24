=================================
NER (Named Entity Recognition)
=================================

.. contents:: Table of Contents
   :local:

Description
===========
**NER** is a Named Entity Recognition dataset for the financial domain, containing sentences from financial agreements filed with the U.S. SEC. The dataset identifies critical financial entities such as persons, organizations, and locations.

Dataset Composition
------------------------
- **Source**: Financial agreements and SEC filings
- **Sample Size**: 1,366 annotated sentences
- **Entity Types**: PERSON (PER), ORGANISATION (ORG), LOCATION (LOC)

Example
-------
**Text**: "This LOAN AND SECURITY AGREEMENT dated January 27, 1999, between SILICON VALLEY BANK ('Bank'), a California-chartered bank with its principal place of business at 3003 Tasman Drive, Santa Clara, California 95054 with a loan production office located at 40 William St."

**Named Entities**:

- SILICON VALLEY BANK, ORG
- Bank, ORG
- California, LOC
- 3003 Tasman Drive, LOC
- Santa Clara, LOC
- California, LOC
- 40 William St, LOC

Task Description
================
Named Entity Recognition in Financial Documents
-------------------------------------------------
- **Input**: Sentences from financial agreements and SEC filings
- **Output**: Named entities with their types (PERSON, ORGANISATION, LOCATION)
- **Challenge**: Requires understanding of financial document structure and entity disambiguation in legal/financial contexts

Key Use Cases
----------------
1. **Document Analysis**: Extracting key parties from financial agreements
2. **Compliance Monitoring**: Identifying entities mentioned in regulatory filings
3. **Knowledge Graph Construction**: Building structured representations of financial relationships

Evaluation Metrics
==================
1. **Entity F1**: Entity-level F1 score measuring precision and recall of entity detection and classification

References
==========
Julio Cesar Salinas Alvarado, Karin Verspoor, and Timothy Baldwin. "Domain Adaption of Named Entity Recognition to Support Credit Risk Assessment." In Proceedings of the Australasian Language Technology Association Workshop 2015, pages 84–90, 2015.

For dataset access, visit `HuggingFace <https://huggingface.co/datasets/ChanceFocus/flare-ner>`_.
