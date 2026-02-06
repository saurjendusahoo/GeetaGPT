from rag_engine import AGEngine

if __name__ == "__main__":
    print("Initializing Agent Engine...")
    engine = AGEngine()
    print("Loading and indexing data...")
    engine.load_and_index()
    print("Done.")
