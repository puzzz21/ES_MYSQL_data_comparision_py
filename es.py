from elasticsearch import Elasticsearch, RequestsHttpConnection

es=Elasticsearch([{'host':'localhost','port':9200}])

res= es.search(index='books',
               body={
                   'query':
                       {
                           'bool':
                            {
                               'must':
                                [
                                    {
                                        'match':
                                        {
                                            'writer': 'Louisa May Alcott'
                                        }
                                    },
                                    {
                                        'match':
                                        {
                                              'description': 'children books'
                                        }
                                    }
                               ]
                           }
                       }
               }
               )
print('Got %d hits:', res['hits']['hits'])