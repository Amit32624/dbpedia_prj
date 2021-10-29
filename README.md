# Clustering Wikipedia data using DBpedia: Project Overview
* Data extracted from the Wikipedia article pages based on medical devices through DBpedia by running SPARQL queries.
* Dataset created of around 1500 records.
* Performed Data cleaning with the help of regular expression and NLTK library in python.
* Performed data pr-processing with TF-IDF schema and Word embedding method - using Word2Vec module.
* Implemented clustering alogorithms like K-means,K-medoids and hierarchical clustering.
* Determined optimal number of clustering by Elbow Method and silohuette scrore method and plotted them.
* Visualized clustering and  average silhouette scores.

## Code and resources used
Python versoon: 3.8.5
-  Packages: pandas, numpy, scikit-sklearn, matplotlib, searborn, NLTK, genism

## Steps to run the fies:
- First, the SPQRQL query is run from the file - data_extract.py and the generated dataset is saved as 'medical_devices_data.csv' and 'medical_equipments_data.csv' files.
- Secondly, once the data is extracted, data is cleaned using various data clearning operations - data_cleaning.ipynb file, here the files are saved as 'med_devs_clean_data.csv' and 'med_equips_clean_data.csv
- Once the data cleaning operations are performed, two methods are implemented for data pre-processing and models are implemented.
- clustering_word2Vec.ipynb
- clustering_tf-idf.ipynb
