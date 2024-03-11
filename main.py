import openai

# Set up your OpenAI API credentials
openai.api_key = os.environ['OPENAI_API_KEY']

# Define the prompt for the conversation
prompt = "You: Hello, how can I assist you today?\nAI:"

# Generate a response from ChatGPT
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    temperature=0.7,
    n=1,
    stop=None,
    log_level="info"
)

# Extract the generated reply from the response
reply = response.choices[0].text.strip()

# Print the AI's reply
print("AI:", reply)