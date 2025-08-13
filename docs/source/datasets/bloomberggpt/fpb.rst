===============================
FPB (Financial PhraseBank)
===============================

.. contents:: Table of Contents
   :local:

Goal
====
The **Financial PhraseBank (FPB)** is a benchmark dataset designed to advance sentiment analysis in **financial and economic texts**. Its primary goals are:

- To provide a **high-quality, domain-specific** resource for training and evaluating sentiment analysis models in finance
- To capture **investor-centric sentiment** (i.e., how news phrases may influence stock prices)
- To address the challenge of **context-dependent semantic orientations** (e.g., "profit increase" vs. "loss increase")

Description
===========
**FPB** is a curated collection of English sentences from financial news and corporate disclosures, annotated for sentiment polarity.

Dataset Composition
------------------------
- **Source**: News articles covering companies listed on the **OMX Helsinki Stock Exchange** (Finland)
- **Time Period**: Articles collected over a multi-year span (Unspecified)
- **Sample Size**: Approximately 5,000 sentences, filtered to ensure relevance
- **Companies**: Broad coverage across industries including banking, manufacturing, and technology

Annotation Process
----------------------
- **Annotators**: 16 finance professionals (researchers and Aalto University Business School graduates)
- **Labels**: Each sentence labeled as **Positive**, **Negative**, or **Neutral** from an investor's perspective
- **Agreement**:
  - 74.9% overall agreement
  - 98.7% agreement on distinguishing Positive vs. Negative
  - Labels determined by majority voting (5-8 annotations per sentence)

Example
-------
Below is a sample from the dataset (available on `HuggingFace <https://huggingface.co/datasets/ChanceFocus/en-fpb>`_):

.. list-table:: Financial PhraseBank Examples
   :widths: 10 60 15 15
   :header-rows: 1

   * - ID
     - Text
     - Label
     - Choices
   * - fpb0
     - The five-storey, eco-efficient building will have a gross floor area of about 15,000 sq m. It will also include apartments.
     - neutral
     - positive, neutral, negative
   * - fpb1
     - According to Seppänen, the new technology UMTS900 solution network building costs are by one-third lower than that of the building of 3.5G networks, operating at 2,100 MHz frequency.
     - positive
     - positive, neutral, negative

Task Description
=====================
Sentiment Classification
---------------------------
- **Input**: Financial news sentence (e.g., "Profit surged by 20% due to strong demand")
- **Output**: Sentiment label (Positive/Negative/Neutral)
- **Challenge**: Financial language often requires domain knowledge (e.g., "dividend cut" is negative, while "cost reduction" may be positive)

Key Use Cases
----------------
1. **Robo-advisors**: Automating sentiment analysis for trading signals
2. **Academic Research**: Benchmarking NLP models in finance
3. **Risk Management**: Monitoring news sentiment for portfolio adjustments

Evaluation Metrics
=====================
1. **Accuracy**: Primary metric for balanced class performance
2. **Macro-averaged F1-score**: Accounts for class imbalance (Neutral sentences dominate)

Why Use FPB?
==============
- **Domain-Specific**: Tailored for finance, unlike generic sentiment datasets (e.g., IMDB, Yelp)
- **Rigorous Annotation**: Expert-labeled with high agreement, reducing noise
- **Publicly Available**: Freely accessible for non-commercial research

References
==========
Pekka Malo, Ankur Sinha, Pekka Korhonen, Jyrki Wallenius, and Pyry Takala. "Good debt or bad debt: Detecting semantic orientations in economic texts." Journal of the Association for Information Science and Technology 65, no. 4 (2014): 782-796.

For dataset access, check the `official repository <https://www.researchgate.net/publication/251231364_FinancialPhraseBank-v10>`_ or HuggingFace link above. 