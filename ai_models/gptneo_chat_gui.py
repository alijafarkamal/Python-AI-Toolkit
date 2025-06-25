from huggingface_hub import InferenceClient
import tkinter as tk
from tkinter import scrolledtext
import threading
# Model and API configuration
model_name = "EleutherAI/gpt-neo-1.3B"
api_token = ""  # Replace with your API token
client = InferenceClient(model=model_name, token=api_token)

def get_ai_response(prompt):
    """Get response from AI."""
    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=300,      # Increase output length
            temperature=0.7,         # Control creativity
            top_p=0.9,               # Control randomness
            repetition_penalty=1.2   # Discourage repetition
        )
        # Directly return the response if it's a string
        if isinstance(response, str):
            return response
        return "Unexpected response format."
    except Exception as e:
        return f"Error: {e}"


def on_submit():
    """Handle user input and display AI response."""
    user_input = user_input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    chat_display.insert(tk.END, f"You: {user_input}\n")
    chat_display.insert(tk.END, "AI: Thinking...\n")
    chat_display.update()

    def fetch_response():
        response = get_ai_response(user_input)
        chat_display.delete("end-2l", tk.END)  # Remove "AI: Thinking..."
        chat_display.insert(tk.END, f"AI: {response}\n\n")

    threading.Thread(target=fetch_response, daemon=True).start()
    user_input_box.delete("1.0", tk.END)

# Create the Tkinter application
root = tk.Tk()
root.title("AI Chat Application")

# Chat display
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=80, state="normal")
chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# User input box
user_input_box = tk.Text(root, height=5, width=60)
user_input_box.grid(row=1, column=0, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=1, column=1, padx=10, pady=10)

# Run the Tkinter application
root.mainloop()

