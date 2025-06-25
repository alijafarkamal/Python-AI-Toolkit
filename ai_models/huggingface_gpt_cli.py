# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# # Load the model and tokenizer
# print("Loading model...")
# model_name = "distilgpt2"

# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name, 
#     device_map=None, 
#     torch_dtype=torch.float32
# )

# # Chat function
# def chat_with_ai():
#     print("AI is ready! Type 'exit' to quit.")
#     while True:
#         # Take user input
#         user_input = input("\nYou: ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
        
#         # Tokenize input (remove .to("cuda"))
#         inputs = tokenizer(user_input, return_tensors="pt")

#         # Generate response
#         print("AI: Thinking...")
#         outputs = model.generate(
#             inputs.input_ids, 
#             max_length=150, 
#             temperature=0.7, 
#             top_p=0.9, 
#             pad_token_id=tokenizer.eos_token_id
#         )

#         # Decode and print response
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#         print(f"AI: {response}")

# # Run the chat function
# if __name__ == "__main__":
#     chat_with_ai()

# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# # Load the model and tokenizer
# print("Loading LLaMA-2 model...")
# model_name = "meta-llama/Llama-2-7b-hf"

# token = ""

# tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     use_auth_token=token,
#     device_map="auto",  # Automatically map to available device (GPU/CPU)
#     torch_dtype=torch.float16  # Use float16 for efficiency (requires a GPU)
# )

# # Chat function
# def chat_with_ai():
#     print("AI is ready! Type 'exit' to quit.")
#     while True:
#         # Take user input
#         user_input = input("\nYou: ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
        
#         # Tokenize input
#         inputs = tokenizer(user_input, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

#         # Generate response
#         print("AI: Thinking...")
#         outputs = model.generate(
#             inputs.input_ids,
#             max_length=150,
#             temperature=0.7,
#             top_p=0.9,
#             pad_token_id=tokenizer.eos_token_id
#         )

#         # Decode and print response
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#         print(f"AI: {response}")

# # Run the chat function
# if __name__ == "__main__":
#     chat_with_ai()



from transformers import AutoModelForCausalLM, AutoTokenizer
import torch



api_token = ""



# Load the model and tokenizer using your Hugging Face token
print("Loading model...")
# model_name = "meta-llama/Llama-2-7b-chat-hf"  # Use the LLaMA model name you want
model_name = "EleutherAI/gpt-neo-2.7B"  # Replace with a free model
# model_name = "EleutherAI/gpt-neo-2.7B"  # Replace with a free model
api_token = ""
client = InferenceClient(model=model_name, token=api_token)

# Your Hugging Face API token (replace with your actual token)


# Load tokenizer and model with authentication
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=api_token)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    use_auth_token=api_token,
    device_map=None,  # Set to None for CPU
    torch_dtype=torch.float32
)

# Chat function
def chat_with_ai():
    print("AI is ready! Type 'exit' to quit.")
    while True:
        # Take user input
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Tokenize input
        inputs = tokenizer(user_input, return_tensors="pt")

        # Generate response
        print("AI: Thinking...")
        outputs = model.generate(
            inputs.input_ids, 
            max_length=50,  # Limit output length
            temperature=0.7, 
            top_p=0.9, 
            pad_token_id=tokenizer.eos_token_id
        )

        # outputs = model.generate(
        #     inputs.input_ids,
        #     max_length=150,
        #     temperature=0.7,
        #     top_p=0.9,
        #     pad_token_id=tokenizer.eos_token_id
        # )

        # Decode and print response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"AI: {response}")

# Run the chat function
if __name__ == "__main__":
    chat_with_ai()

# from huggingface_hub import InferenceClient

# # Use a smaller and efficient model
# model_name = "EleutherAI/gpt-neo-1.3B"
# api_token = ""  # Replace with your Hugging Face token
# # Initialize client
# client = InferenceClient(model=model_name, token=api_token)

# def chat_with_ai():
#     print("AI is ready! Type 'exit' to quit.")
#     while True:
#         user_input = input("\nYou: ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break

#         print("AI: Thinking...")
#         try:
#             # Generate response with controlled settings
#             response = client.text_generation(
#                 user_input,
#                 max_new_tokens=150,
#                 temperature=0.7,
#                 top_p=0.9
#             )
#             print(f"AI: {response}")
#         except Exception as e:
#             print(f"Error: {e}")

# if __name__ == "__main__":
#     chat_with_ai()





# from huggingface_hub import InferenceClient

# # Initialize the Inference Client
# # model_name = "tiiuae/falcon-7b"  # Replace with the desired model
# model_name = "bigscience/bloom-3b"
# # model_name = "EleutherAI/gpt-neo-2.7B"  # Replace with a free model

# client = InferenceClient(model=model_name, token=api_token)

# # Chat function
# def chat_with_ai():
#     print("AI is ready! Type 'exit' to quit.")
#     while True:
#         # Take user input
#         user_input = input("\nYou: ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break

#         # Send the input to the Inference API
#         print("AI: Thinking...")
#         try:
#             response = client.text_generation(user_input, max_new_tokens=200)
#             # Extract and print the generated text
#             print(f"AI: {response}")
#         except Exception as e:
#             print(f"Error: {e}")

# # Run the chat function
# if __name__ == "__main__":
#     chat_with_ai()
