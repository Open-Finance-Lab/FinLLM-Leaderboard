=============
Headlines
=============

.. contents:: Table of Contents
   :local:

Description 
============
**Headlines** is NLP benchmark for determining semantic labels for market signals from news-related headlines. 

Task Description
-------------------
The Headlines dataset consists of English sentences selected from financial news headlines outlets. The goal is to 
test whether a model can detect the signal for price movements.  
Key characteristics: 

- Contains ~79,000 sentences rows of questions 
- Binary classification: "Yes" or "No" 

Example Queries: 
Look for indications that the price of gold is increasing. In the news headline, can you identify a Price or Not pertaining to gold? Your response should be Yes or No.
Text: dec. gold up $2.50 at $1,053.10/oz on globex

Look for indications that the price of gold is increasing. In the news headline, can you identify a Direction Up pertaining to gold? Your response should be Yes or No.
Text: dec. gold up $2.50 at $1,053.10/oz on globex

Example dataset(`<https://huggingface.co/datasets/ChanceFocus/flare-headlines>`_):

.. figure:: ../images/headlines_example.png
   :width: 100%
   :align: center


Evaluation Metrics
--------------------
1. Accuracy
2. F1-score (macro-averaged)

References
------------

.. code-block:: bash

  @article{xie2023pixiu,
    title={Pixiu: A large language model, instruction data and evaluation benchmark for finance},
    author={Xie, Qianqian and Han, Weiguang and Zhang, Xiao and Lai, Yanzhao and Peng, Min and Lopez-Lira, Alejandro and Huang, Jimin},
    journal={arXiv preprint arXiv:2306.05443},
    year={2023}
  } 