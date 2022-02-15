from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

def esearch(keywords="", gender=""):
	client = Elasticsearch("http://localhost:9200")
	q = Q("bool", should=[Q("match", keywords=keywords), 
	Q("match", gender=gender)], minimum_should_match=1)
	s = Search(using=client, index="envri").query(q)[:20]
	response = s.execute()
	#print("%d hits found." % response.hits.total)
	search = get_results(response)
	return search


def get_results(response):
	results = []
	for hit in response:
		result_tuple = (hit.identifier)
		results.append(result_tuple)
	return results

#print("results:\n", esearch(keywords = "anatomy"))