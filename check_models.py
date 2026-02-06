import ollama
try:
    print("Attempting to list models...")
    models = ollama.list()
    print("Available models:")
    if 'models' in models:
        for m in models['models']:
            print(f"- {m['name']}")
    else:
        print(models)
except Exception as e:
    print(f"Error listing models: {e}")
