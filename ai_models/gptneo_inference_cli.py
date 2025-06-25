from huggingface_hub import InferenceClient

# Replace with your desired model
model_name = "EleutherAI/gpt-neo-2.7B"
api_token = ""
client = InferenceClient(model=model_name, token=api_token)

# Chat function
def chat_with_ai():
    print("AI is ready! Type 'exit' to quit.")
    while True:
        # Take user input
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Send the input to the Inference API
        print("AI: Thinking...")
        try:
            # Use text_generation with corrected parameter name
            response = client.text_generation(
                text=user_input,        # Correct parameter name
                max_new_tokens=50,      # Limit output length
                temperature=0.7,        # Adjust creativity
                top_p=0.9,              # Adjust randomness
            )
            # Extract and print the generated text
            print(f"AI: {response['generated_text']}")
        except Exception as e:
            print(f"Error: {e}")

# Run the chat function
if __name__ == "__main__":
    chat_with_ai()

