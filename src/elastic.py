import json
from elasticsearch import Elasticsearch, helpers

class ELK():
    def __init__(self, config):

        # Define connection parameters
        self.host: str = config["ELASTICSEARCH_HOST"]
        self.username: str = config["ELASTICSEARCH_USERNAME"]

        ## TODO: implement getter and setter for password
        self.password: str = config["ELASTICSEARCH_PASSWORD"]
        self.index: str = config["INDEX"]


    def establish_es_connection(self):
        # Create an Elasticsearch client instance
        self.es = Elasticsearch(
            hosts=[self.host],
            basic_auth=(self.username, self.password)
        )

    # Check if Elasticsearch is up and running
    def validate_es_connection(self,):
        try:
            # Perform a simple health check
            response = self.es.cluster.health()
            print("Elasticsearch cluster health:", response['status'])
        except Exception as e:
            print("Error connecting to Elasticsearch:", e)

    def create_index(self):
        # Check if an index exists
        if self.es.indices.exists(index=self.index): 
            print(f"Index {self.index} exists")
        else:
            self.es.indices.create(index=self.index)
            print(f"Index {self.index} created")

    def delete_index(self):
        # Delete an index
        if self.es.indices.exists(index=self.index): 
            self.es.indices.delete(index=self.index)
            print(f"Index {self.index} deleted")
        else:
            print(f"Index {self.index} doesn't exist")

    ## TODO: consider using bulk indexing and error handling: https://medium.com/@nataliadianas/unleashing-elasticsearch-with-python-harnessing-the-power-of-search-indexing-and-insights-f467aad42e55
    def index_document(self, document: dict):
        self.es.index(index=self.index, document=document)
        
    def refresh_index(self):
        self.es.indices.refresh(index=self.index)

    def get_index(self, id: int):
        self.es.get(index=self.index, id=id, request_timeout=60)

    def search_index(self, query: str):

        query = {
            "query": {
                "match": {
                    "processed_response": query
                }
            }
        }
        # Execute the search query
        response = self.es.search(index=self.index, body=query) # Extract the results

        return response["hits"]["hits"]