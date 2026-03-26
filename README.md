# 📌 Overview  
This project is a  BERT-based binary sentiment classifier for news headlines,  
fine-tuned on Indian newspaper IndianExpress data.  
Classifies headlines as Positive (1) or Negative (0) based on writing tone.

# 📂 Project Structure

```bash
├── newspaper.py                            # Web scraping for news headlines
├── news_headings.csv                       # Dataset containg news headlines
├── balanced_news_book.ipynb                # Jupyter notebook for model building
├── balanced_news_model.pth                 # Saved model
├── balanced_news_prediction.ipynb          # Jupyter notebook for prediction of random news text
└── README.md                               # documentation
```

# 📈 Dataset
The dataset `news_headings.csv` contains news headlines collected from The Indian Express, with the following columns:

- **news**: Text of the headline  
- **label**: Binary label indicating sentiment — Positive (1) or Negative (0)

# 🧮 Methodology
1. Data Preprocessing
   * generated automatic labels using HuggingFace sentiment Pipeline
   * created the dataframe
2. Data Splitting
   * splited the data into train and test and loaded data into DataLoader
3. Class balancing
   * handled class imbalance giving more weight to small class
4. Tokenized the data
   * made tokens of the text using BERT Tokenizer
5. Model Buidling
    * used pretrained BERT Model for Classification
    * partially fine tunned the model
6. Model Evaluation
    * Classification_report
    * Confusion_matrix

# Visualization
