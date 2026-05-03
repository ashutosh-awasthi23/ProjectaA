import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
client = chromadb.PersistentClient(path="./market_memory")
collection = client.get_or_create_collection(name = "financial_fillings")

def build_memory():
    sample_10k_text = """
        Apple Inc. Annual Report.
        Revenue for the year was $383 billion.
        The company is heavily investing in new AI chips to power future generative AI features across its ecosystem.
        Supply chain constraints remain a risk factor for the upcoming fiscal year.
        """

    print("Chunking the financial document...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 10 ,
        chunk_overlap = 5
    )

    chunks = text_splitter.split_text(sample_10k_text)
    print(type(chunks))

    ## Adding the chunks to vector_database

    print(f"Adding {len(chunks)} chunks to long term memory...")
    chunks_ids = [f"chunk_{i}" for i in range(len(chunks))]
    try:
        collection.add(
            documents = chunks,
            ids = chunks_ids
        )

        print("Success! Memory Built and stored locally")

    except Exception as e:
        print(f"Error saving to database")


if __name__ == "__main__":
    build_memory()