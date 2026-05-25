import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader


def build_memory():
    client = chromadb.PersistentClient(path="./market_memory")
    collection = client.get_or_create_collection(name = "financial_fillings")

    
    print("Fetching real Apple SEC 10-K data from the web...")
    sec_url = "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm"
    
    loader = WebBaseLoader(

        web_path=[sec_url],
        header_template={
            "User-Agent": "LiveMarketSentinel_Project  (ashutoshawasthi23@gmail.com)"
        }

    )

    docs = loader.load()
    real_10k_text = docs[0].page_content


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )


    chunks = text_splitter.split_text(real_10k_text)
    print(type(chunks))


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