#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install ipywidgets


# In[1]:


import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display


# In[13]:


# Replace with your actual API key
API_KEY = "AIzaSyB--Wa4Nb6cKeI_XmlaGYVh5TSaXXFe07M"


# In[14]:


# Configure the Gemini AI
genai.configure(api_key=API_KEY)


# In[15]:


# Load AI model
model = genai.GenerativeModel("gemini-1.5-pro-latest")
chat_history = []


# In[16]:


# Create input and output widgets
user_input = widgets.Text(placeholder="Type a message...")
send_button = widgets.Button(description="Send")
chat_display = widgets.Output()


# In[17]:


response = model.generate_content("Hello! How are you?")
print(response.text)


# In[18]:


print(model.generate_content("Test message").text)


# In[20]:


def on_send_clicked(b):
    """Handles user input and gets AI response."""
    global chat_history

    user_message = user_input.value.strip()
    if not user_message:
        return  # Don't process empty messages

    with chat_display:
        print(f"User: {user_message}")

    # Add user input in the correct format
    chat_history.append({"role": "user", "parts": [{"text": user_message}]})

    # Get AI response
    try:
        response = model.generate_content(chat_history)  # Gemini expects the correct format
        ai_message = response.text

        # Add AI response in the correct format
        chat_history.append({"role": "model", "parts": [{"text": ai_message}]})

        with chat_display:
            print(f"🤖 AI: {ai_message}\n")

    except Exception as e:
        with chat_display:
            print(f"Error: {e}")

    # Clear input field
    user_input.value = ""

# Attach event listener to button
send_button.on_click(on_send_clicked)

# Display the chatbot UI
display(chat_display, user_input, send_button)


# In[ ]:




