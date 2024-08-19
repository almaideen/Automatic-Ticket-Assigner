# Finding Relevant Support Team for Complaint Text Using Machine Learning

This repository contains a project aimed at automating the process of routing customer complaints to the appropriate support team based on the content of the complaint. By using machine learning techniques, the project classifies complaint texts and assigns them to the most relevant team, improving response times and customer satisfaction.

**Project Overview**

Customer complaints are an essential feedback mechanism, but manually sorting and directing these complaints to the right support teams can be time-consuming and error-prone. This project leverages natural language processing (NLP) and machine learning to automatically analyze complaint texts and identify the most suitable team to handle the issue.

The primary goal is to enhance operational efficiency by reducing the time it takes to route complaints and ensuring that they are handled by the experts best equipped to resolve them.

**Dataset**

Data for this project is collected from CFPB (Consumer Fianancial Protection Bureau). The CFPB is a U.S. government agency that was established in 2011 to protect consumers in the financial sector. The CFPB manages a consumer complaint database, where individuals can submit complaints about financial products and services. The bureau works to resolve these complaints by contacting the relevant financial institutions and ensuring that consumer issues are addressed. Pulled those data from the website using official API to create dataset for this business problem.

**Features**

Text Preprocessing: Cleaning and preparing the complaint text for analysis.

Feature Engineering: Used tonekization and lemmatization techniques for feature engineering.

Feature Extraction: Using techniques like TF-IDF and word embeddings to represent the complaint text numerically.

Model Training: Implementing and training models to classify complaints.

Classification: Assigning each complaint to a specific support team based on the content.

Model Evaluation: Measuring the accuracy and efficiency of the classification model.

**Models Used**

The project explores various machine learning models for text classification:

Naive Bayes

Random Forest

XGBoost

SimpleRNN

LSTM

GRU

**Results**

The Random Forest classification model achieved an accuracy of 0.94, ensuring that the majority of complaints are accurately routed to the correct support team. This results in faster resolution times and improved customer satisfaction.

**Deployment**

Streamlit is the webframework used to build app for the business problem and deployed on Streamlit Cloud. You can access the app using the [link](https://automatic-ticket-assigner.streamlit.app/).

Model Evaluation: Measuring the accuracy and efficiency of the classification model.
