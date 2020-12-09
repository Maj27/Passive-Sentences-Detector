# Passive-Sentences-Detector

 This small project is meant to build rule-based and machine learning-based models to detect passive sentences.  It takes data from The Third Bush-Kerry Presidential Debat corpus, annotates it and classify the sentences based on n gram pos tags as feature. The pipeline involves data preprcessing, cleaning, preparation, labeling, applying feature selection, data imbalanceing (SMOTE). Three classifiers were used, Xgboost, Catboost and logistic regression. Additional code is also added to make the machine classifier available as a simple web API using Flask (a POST request with the text content as a payload).  
The accuracy metrics for the logistic regression classifier were as follows: accuracy 0.92, precision 1.00, recall 0.90, f1 0.95

