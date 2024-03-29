import openai
import os

class OpenAI : 
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY') 
    def open_ai_gpt_call(self, user_content, prompt=None, setTemperature=None):
        # Initialize messages
        messages = []

        # If prompt exists, add it as system message
        if prompt:
            messages.append({"role":"system", "content": prompt})

        # Check if user_content is a list and if it contains proper structured messages
        if isinstance(user_content, list):
            messages.extend(user_content)
        else:
            messages.append({"role": "user", "content": user_content})

        # If setTemperature is provided, include it in the completion
        if setTemperature:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=setTemperature
            )
        else:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

        reply_content = completion.choices[0].message.content
        return reply_content  # Returning the reply_content from the function
    def open_ai_gpt4_call(self, user_content, prompt=None, setTemperature=None):
        # Initialize messages
        messages = []

        # If prompt exists, add it as system message
        if prompt:
            messages.append({"role":"system", "content": prompt})

        # Check if user_content is a list and if it contains proper structured messages
        if isinstance(user_content, list):
            messages.extend(user_content)
        else:
            messages.append({"role": "user", "content": user_content})

        # If setTemperature is provided, include it in the completion
        if setTemperature:
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=setTemperature
            )
        else:
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

        reply_content = completion.choices[0].message.content
        return reply_content  # Returning the reply_content from the function