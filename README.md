# Passive-Sentences-Detector

 This small project is meant to build rule-based and machine learning-based models to detect passive sentences.  It takes data from The Third Bush-Kerry Presidential Debat corpus, annotates it and classifies the sentences based on n-gram pos tags as features. The pipeline involves data preprocessing, cleaning, preparation, labeling, applying feature selection, data imbalance handling (SMOTE). Three classifiers were used, Xgboost, Catboost, and logistic regression. Additional code is also added to make the machine classifier available as a simple web API using Flask (a POST request with the text content as a payload).  

The accuracy metrics and performance for the logistic regression classifier were as follows: accuracy 0.92, precision 1.00, recall 0.90, f1 0.95 (based on 20% testing data of the used corpus)


There are three main python files for this project as well as three text files. Here is a brief description of each of them.

1- Passive-Sentences-Detector (Building the models).ipynp:
   This is the main file in which the corpus is read and the sentences are split then pos are found using NLTK libraries. 
   The patterns from the POS tags are used to detect whether a sentence is passive or not. Then the two types of sentences are stored into a dataframe where the corresponding labels are added to them.
   Different models were built where the features used are n-gram POS tags. To reduce feature dimensionality and to speed up the classification, feature selection is used. The top 200 features are utilized for the prediction. Additionally, as the two classes were not balanced in the used dataset, data imbalance handling (SMOTE) was used.
   
   
2- passive_app.py:
  This is a simple web API that was developed using Flask. The main function is new_prediction which predict whether a sentence is passive or not 
  
  
3-  request.py:
    In this file, a POST request with the text content is sent as a payload. It calls the passive_app API to make the prediction.

