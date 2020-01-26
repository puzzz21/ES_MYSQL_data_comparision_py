from elasticsearch import Elasticsearch, RequestsHttpConnection


def ESData(writer):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    res = es.search(index='books',
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
                                                        'writer': writer
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
    return res['hits']['hits']

if __name__ == '__main__':
    ESData()
