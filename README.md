# Creole-LanguageDetectionNB
Multinomial Naive Bayes Language Classifier: A Fast and Efficient Text Classification Model
LangDetectNB
This is a simple but powerful language classification model built using Multinomial Naive Bayes. It takes in a text input and predicts the language with 99% accuracy based on a dataset of multilingual text samples. The model is trained using a Bag of Words (BoW) approach with CountVectorizer to convert text into numerical form.

How It Works
**CreoleGen4.py** - GENERATES THE CREOLE DATASET in THE FORM OF A CSV. I HAD TO GENERATE MY OWN CREOLE DATASET AS YOU CAN'T FIND ANY ONLINE. THIS CREATES A DATASET OF CREOLE LANGUAGES AND THEIR MAPPING

**CREOLEIDENTIFIER.ipnb**
Cleans & Preprocesses Text – Removes symbols, converts to lowercase, and tokenizes.

Vectorizes Using BoW – Transforms text into a numerical format for better learning.

Trains a Naive Bayes Model – A fast, probabilistic approach ideal for text classification.

Evaluates Performance – Uses accuracy score, a confusion matrix, and a heatmap to analyze results.

Why This Model?
✅ 99% Accuracy – Performs exceptionally well on the dataset.
✅ Fast & Lightweight – Minimal computation required, perfect for quick predictions.
✅ Confidence-Based Predictions – If the model isn't sure, it asks for a longer input instead of guessing.

Usage
Train the model using an 80-20 train-test split.

Run the predict("your text here") function to classify an input.

If the text is too short, the model will ask for a longer sentence to improve accuracy.

Next Steps
Might experiment with TF-IDF vectorization and deep learning models later, but for now, this Naive Bayes approach does the job quickly and efficiently.
