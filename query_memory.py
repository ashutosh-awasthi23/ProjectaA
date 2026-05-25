import chromadb

def search_memory(query_text):
    print(f"\n--- Searching Corporate Memory for: '{query_text}' ---")
    
    # 1. Connect to our existing database
    client = chromadb.PersistentClient(path="./market_memory")
    
    # Note: We use get_collection here instead of get_or_create because we know it exists
    try:
        collection = client.get_collection(name="financial_fillings")
    except Exception as e:
        print("Error: Could not find the collection. Did you build the memory first?")
        return
    
    # 2. Query the database
    # ChromaDB will automatically convert our text query into an embedding and find the closest matches
    results = collection.query(
        query_texts=[query_text],
        n_results=3 # We want the top 3 most relevant chunks
    )
    
    # 3. Display the results cleanly
    print("\nTop 3 Retrieved Contexts:")
    
    # results['documents'][0] contains the list of text chunks for our single query
    for i, document in enumerate(results['documents'][0], start=1):
        print(f"\n--- Result {i} ---")
        print(document)

if __name__ == "__main__":
    # Let's ask a specific question that should trigger SEC 10-K risk factors or supply chain data
    search_memory("What are the risk factors and constraints regarding the supply chain?")