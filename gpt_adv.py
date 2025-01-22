from transformers import pipeline

# User selects the model
print("Choose the model to use:")
print("1. BLOOM")
print("2. GPT-Neo-2.7B")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    model_name = "bigscience/bloom"
elif choice == "2":
    model_name = "EleutherAI/gpt-neo-2.7B"
else:
    print("Invalid choice. Exiting.")
    exit()

# Initialize the pipeline
print("Loading model...")
pipe = pipeline("text-generation", model=model_name, use_auth_token=True)  # Ensure your API token is configured

# Chat loop
print("\nAI is ready! Type 'exit' to quit.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    print("AI: Thinking...")
    response = pipe(user_input, max_length=150, temperature=0.7, top_p=0.9)
    print(f"AI: {response[0]['generated_text']}")
