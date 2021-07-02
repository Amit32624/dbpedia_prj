import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from pandas.io.json import json_normalize
# SPARQL query
query = '''PREFIX foaf: <http://xmlns.com/foaf/0.1/>    
PREFIX dbo: <http://dbpedia.org/ontology/>    
PREFIX dbr: <http://dbpedia.org/resource/>    
PREFIX dbp: <http://dbpedia.org/property/>    
PREFIX ling: <http://purl.org/linguistics/gold/>
SELECT DISTINCT ?a, ?dob, ?ht, ?hpn, ?g, ?name, ?c    
WHERE{{
   ?a a dbo:Athlete; 
      dbo:birthDate ?dob;
      foaf:name ?name.    
   OPTIONAL{{?a  dbo:country ?c}}    
   FILTER(LANG(?name) = "en").    
}}'''
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
print(df_results)