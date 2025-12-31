import argparse
from src.graph import app

def main():
    parser = argparse.ArgumentParser(description="Agentic Transaction Categorizer")
    parser.add_argument("--merchant", type=str, help="Merchant name to categorize")
    args = parser.parse_args()

    inputs = {"question": args.merchant}
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Node '{key}':")
    
    print("\nFinal Result:", value["generation"])

if __name__ == "__main__":
    main()
