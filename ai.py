import pyttsx3
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # required, but unused
)

# Get the response from the AI model
response = client.chat.completions.create(
  model="llama2",
  messages=[
    {"role": "system", "content": "Talk like a friend that is kinda mean but also very knowledegeble, you know how to have fun with your response but at the same time help out the user as well."},
    {"role": "user", "content": "hey, how're ya?"},
  ]
)

# Extract the AI's response
ai_response = response.choices[0].message.content

# Print the response to the console
print(ai_response)

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Use the TTS engine to speak the response
engine.say(ai_response)
engine.runAndWait()
