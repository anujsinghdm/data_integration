from SPARQLWrapper import SPARQLWrapper, JSON, GET

query = '''
select * {?s ?p ?o} limit 2
'''
endpoint = "http://localhost:7200/repositories/repo_1"

connection = SPARQLWrapper(endpoint)
connection.setCredentials("admin", "admin")
connection.setRequestMethod(GET)
connection.setQuery(query)
connection.setReturnFormat(JSON)
result = connection.query()
for each in result:
    print(each)