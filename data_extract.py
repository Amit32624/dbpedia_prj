# Importing libraries
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from pandas.io.json import json_normalize


# SPARQL query
query = '''PREFIX foaf: <http://xmlns.com/foaf/0.1/>    
PREFIX dbo: <http://dbpedia.org/ontology/>    
PREFIX dbr: <http://dbpedia.org/resource/>    
PREFIX dbp: <http://dbpedia.org/property/>    
PREFIX ling: <http://purl.org/linguistics/gold/>
SELECT DISTINCT ?instance ?label ?comment ?abstract GROUP_CONCAT(DISTINCT ?s,"|") as ?wikicategories GROUP_CONCAT(DISTINCT ?dbo,"|") as ?DBpediaOntology  { 
FILTER (?cat =  <http://dbpedia.org/resource/Category:Medical_devices> ) .  # Comment for the second dataset
#FILTER (?cat =  <http://dbpedia.org/resource/Category:Medical_equipment> ) . # Uncomment for the second dataset.

# getting the instances and the en label
?instance dct:subject ?s .
?instance rdfs:label ?label . FILTER(LANG(?label) = "en").
?instance rdfs:comment ?comment  . FILTER(LANG(?comment) = "en").
?instance dbo:abstract ?abstract . FILTER(LANG(?abstract) = "en").

# DBpedia ontology
?instance rdf:type ?dbo . #FILTER (?dbo LIKE <http://dbpedia.org/ontology/%>). 


# going down the hierarchy
{?s skos:broader ?cat }
UNION
{?s skos:broader/skos:broader ?cat  }
UNION 
{?s skos:broader/skos:broader/skos:broader ?cat  }

}
GROUP BY ?instance ?label ?abstract ?comment
LIMIT 10000'''

# initialise the SPARQL endpoint
sparql = SPARQLWrapper('http://dbpedia.org/sparql')
# set query
sparql.setQuery(query)
# set the response format
sparql.setReturnFormat(JSON)
# execute the query
results = sparql.query().convert()
# normalize the json object to a pandas dataframe
df_results = json_normalize(results['results']['bindings'])
df_results.to_csv('medical_devices_data.csv', index = False) ##Comment when second dataset is created.
# df_results.to_csv('medical_equips_data.csv', index = False) #Uncomment when second dataset is created.
