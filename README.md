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

# 🧮 Workflow

### Data Preprocessing
- Generated automatic labels using HuggingFace sentiment pipeline  
- Created the dataset as a DataFrame  

### Data Splitting
- Split the data into training and testing sets  
- Loaded data into DataLoaders for batching  

### Class Balancing
- Handled class imbalance by assigning higher weight to the minority class  

### Tokenization
- Tokenized the text using BERT tokenizer  

### Model Building
- Used a pretrained BERT model for classification  
- Performed partial fine-tuning of the model  

### Model Evaluation
- Evaluated using classification report  
- Analyzed performance with confusion matrix
  
# 📊 Visualization
here is visualization of confusion_matrix

