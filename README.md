# Fake News Classification 📰

## Overview
This project tackles the growing challenge of misinformation by classifying fake news using advanced natural language processing (NLP) techniques. Leveraging transformer-based models, the task involves semantic analysis of news article titles to classify their relationship into the following categories:  
- **Agreed**: Both articles discuss the same fake news.  
- **Disagreed**: One article refutes the other.  
- **Unrelated**: The articles are not related.

This project demonstrates how machine learning and semantic analysis can be applied to address misinformation spread on social media platforms.

---

## Features
- **Data Processing**: Efficiently processes datasets in `.csv` format for training and testing.
- **Semantic Analysis**: Implements transformer-based models for embedding generation and similarity score computation.
- **Classification Pipeline**:
  - Calculates semantic similarity using `Sentence-Transformers`.
  - Identifies keyword patterns to enhance classification accuracy.
  - Combines multiple approaches for robust fake news classification.
- **Visualization**: Generates graphs to visualize classification metrics, degree distribution, and clustering coefficients.

---

## Tools and Libraries
- **Programming Language**: Python
- **Libraries**:
  - `transformers`
  - `sentence-transformers`
  - `numpy`
  - `matplotlib`

---

## Dataset

The datasets for this project are hosted on Kaggle. You can download the training and testing datasets from the following links:

- **Training Data**: [Download the training dataset from Kaggle](https://www.kaggle.com/datasets/haroonarif1/train-dataset)
- **Testing Data**: [Download the testing dataset from Kaggle](https://www.kaggle.com/datasets/haroonarif1/test-data)

The datasets consist of fake news article titles and their relationships:
- **train.csv**: Used for model training, containing news pairs and labels.
- **test.csv**: Used for model testing and evaluation.

Each data record contains the following fields:

- **id**: The ID of the news pair.
- **tid1**: The ID of the first news title.
- **tid2**: The ID of the second news title.
- **title1_en**: The first news title in English.
- **title2_en**: The second news title in English.
- **label**: The relationship between the news articles (Agreed, Disagreed, Unrelated).

---

## Challenges Addressed
- ** Semantic Analysis: Computed similarity scores between articles using pre-trained transformer models. **
- ** Keyword Analysis: Analyzed the frequency and importance of specific keywords for better classification. **
- ** Optimization: Improved runtime by minimizing computational overhead during classification. **

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/HaroonArif1/Fake-News-Classification.git
2. Navigate to the project directory:
   ```bash
    cd Fake-News-Classification
4. Install the necessary libraries manually, run:
   ```bash
    pip install transformers sentence-transformers numpy matplotlib

---

## Usage
1. Prepare your dataset in the .csv format with news pairs and labels.
2. Run the classification script:
   ```bash
    python classify_fake_news.py
4. Visualize the results by running:
   ```bash
    python visualize_results.py

---

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. Issues and feedback are welcome.
