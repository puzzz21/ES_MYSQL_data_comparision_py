from elasticsearch import Elasticsearch, RequestsHttpConnection

es=Elasticsearch([{'host':'localhost','port':9200}])

e1={
        'id': 1,
        'title': 'The chronicles of Narnia',
        'writer': 'C.S Lewis',
        'published_date': 1950-1-1,
        'description': 'Children book',
        'created_at': 2020-1-19
}

e2={
        'id': 3,
        'title': 'The problem of pain',
        'writer': 'C.S Lewis',
        'published_date': 1996-1-1,
        'description': 'self help',
        'created_at': 2020-1-19,
    }

res=es.index(index='fictional',doc_type='cs_lewis',body=e1)
print(res)
res=es.index(index='fictional',doc_type='cs_lewis',id=2,body=e2)
print(res)
res= es.search(index='books',
               body={
                   'query':
                       {
                           'match_all':
                               {

                               }
                       }
               }
               )
print('Got %d hits:', res['hits']['hits'])