=============
FINER-ORD
=============

.. contents:: Table of Contents
   :local:

Description
============
**FiNER-ORD** (Financial Named Entity Recognition Open Research Dataset) is the first high‐quality, open research corpus for named entity recognition in the financial domain, created to address the unique semantic and lexical variations of financial texts.

Task Description
-------------------
The FiNER-ORD dataset comprises English financial documents (e.g., news articles, company reports) manually annotated for key entity types. The goal is to benchmark and advance NER systems specifically tuned to financial language.

Key characteristics:
- Contains several thousand sentences drawn from diverse financial sources  
- Annotated with domain‐specific entity types such as Organization, Person, Location, Financial Instrument, Monetary Value, Date, and more  
- Released under the CC BY‐NC 4.0 license with full annotation guidelines  
- Benchmarked with multiple pre‐trained language models (PLMs) and large language models (LLMs)  

Example dataset (`<https://huggingface.co/datasets/gtfintechlab/finer-ord>`_):

.. figure:: ../images/FINER-ORD_image.png
   :width: 100%
   :align: center
   :alt: Example annotations from FiNER-ORD

Evaluation Metrics
--------------------
1. Entity‐level Precision  
2. Entity‐level Recall  
3. Entity‐level F1‐score  

References
------------
.. code-block:: bash

    @author{shah2024finerord,
      title={FiNER-ORD: Financial Named Entity Recognition Open Research Dataset},
      author={Shah, Agam and Gullapalli, Abhinav and Vithani, Ruchit and Galarnyk, Michael and Chava, Sudheer},
      howpublished={\url{https://github.com/gtfintechlab/FiNER-ORD}},
      year={2024}
    } 