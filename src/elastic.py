from elasticsearch import Elasticsearch

# Define connection parameters
ELASTICSEARCH_HOST = 'http://localhost:9200'
ELASTICSEARCH_USERNAME = 'elastic'
ELASTICSEARCH_PASSWORD = 'elastic'

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

