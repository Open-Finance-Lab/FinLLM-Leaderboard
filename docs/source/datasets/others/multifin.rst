=============
Multifin
=============

.. contents:: Table of Contents
   :local:

Description
============
**Multifin** is an NLP benchmark for categorizing English headlines drawn from a large global accounting firm's public‐facing websites into their primary topical domain.  

Task Description
-------------------
The Multifin dataset consists of real‐world article headlines published by a major accounting firm. Each headline must be assigned to exactly one of six high‐level categories. The goal is to evaluate a model's ability to understand domain‐specific language and correctly map each headline to its topic.

Key characteristics:  
- Contains tens of thousands of English headlines.  
- Multi‐class classification with six mutually exclusive labels:
  
  - Finance  
  - Technology  
  - Tax & Accounting  
  - Business & Management  
  - Government & Controls  
  - Industry  

Example Queries  
----------------  
Text: Deal summary Helen Oy / Infratek Finland Oy  
Answer: Finance  

Text: PwC named a Major Player in the IDC MarketScape for Worldwide Intelligent Automation Services 2019  
Answer: Technology  

Text: Proposal for digital services tax  
Answer: Tax & Accounting  

Text: Social Impact Lab  
Answer: Business & Management  

Text: International Financial Reporting Standards (IFRS)  
Answer: Tax & Accounting  

Text: Financial Crime  
Answer: Government & Controls  

Text: Global Entertainment & Media Outlook 2018–2022  
Answer: Industry  

Example dataset (`<https://huggingface.co/datasets/ChanceFocus/flare-multifin-en>`_):

.. figure:: ../images/multifin_image.png
   :width: 100%
   :align: center

Evaluation Metrics
--------------------
1. Accuracy  
2. F1‐score (macro‐averaged)  

References
------------
.. code-block:: bash

  @article{jorgensen2023multifin,
    title={MultiFin: A Dataset for Multilingual Financial NLP},
    author={Jorgensen, Rasmus and Brandt, Oliver and Hartmann, Mareike and Dai, Xiang and Igel, Christian and Elliott, Desmond},
    journal={Findings of the Association for Computational Linguistics: EACL 2023},
    year={2023}
  } 