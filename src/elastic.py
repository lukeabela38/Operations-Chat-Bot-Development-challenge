from elasticsearch import Elasticsearch
from dotenv import dotenv_values

config = dotenv_values("../.env")  

config["ELASTICSEARCH_HOST"]
# Define connection parameters
ELASTICSEARCH_HOST = config["ELASTICSEARCH_HOST"]
ELASTICSEARCH_USERNAME = config["ELASTICSEARCH_USERNAME"]
ELASTICSEARCH_PASSWORD = config["ELASTICSEARCH_PASSWORD"]

# Create an Elasticsearch client instance
es = Elasticsearch(
    hosts=[ELASTICSEARCH_HOST],
    basic_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD),
)

# Check if Elasticsearch is up and running
def check_connection():
    try:
        # Perform a simple health check
        response = es.cluster.health()
        print("Elasticsearch cluster health:", response['status'])
    except Exception as e:
        print("Error connecting to Elasticsearch:", e)

# Example usage
if __name__ == "__main__":
    check_connection()

