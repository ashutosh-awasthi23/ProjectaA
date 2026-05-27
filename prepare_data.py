from datasets import load_dataset
import json

def download_and_format_data():
    print("Connect to Huggingface hub")

    try:
        dataset = load_dataset("gbharti/finance-alpaca",split="train")
        print(f"Successfully downloaded {len(dataset)}financial examples.")
    except Exception as e:
        print(f"Error Downloading the data: {e}")
        return
    
    formatted_data = []

    for row in dataset.select(range(5000)):
        formatted_example = {
            "instruction": row.get("instruction","") ,
            "context" : row.get("input", ""),
            "response" : row.get("output","")
        }

        formatted_data.append(formatted_example)

    output_file = "wall_street_training_data.jsonl"

    try:
        with open(output_file,"w",encoding="utf-8") as f:
            for item in formatted_data:
                f.write(json.dumps(item)+"\n")
        print(f"Data saved and formatted successfully locally as {output_file}")

    except Exception as e:
        print(f"Error saving files as :{e}")

if __name__ == "__main__":
    download_and_format_data()





