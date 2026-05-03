import chromadb

client = chromadb.PersistentClient(path = "./market_memory")
collection = client.get_collection(name = "financial_fillings")
#Retrieve the data
results = collection.get()
print(results.keys())

print(f"\n--- Database Snapshot ---")
print(f"Total chunks stored:{len(results['ids'])}\n")

for i in range(len(results['ids'])):
    print(f"ID: {results['ids'][i]}")
    print(f"Text: {results['documents'][i]}")
    print("-" * 40)






