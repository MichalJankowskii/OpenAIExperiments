import streamlit as st
import openai

class OpenAIService:
    def init_connection(self):
       openai.organization = st.secrets["organisation"]
       openai.api_key =  st.secrets["apiKey"]

    def modelsList(self):
        return openai.Model.list()
    
    def createCompletion(self, model, prompt, temperature):
        return openai.Completion.create(model=model, prompt=prompt, temperature=temperature, max_tokens=1000)
    
    def createChatCompletion(self, role, content):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": role, "content": content}])
    
    def createModeration(self, text):
        return openai.Moderation.create(input=text)
    
    def createImage(self, description):
        return openai.Image.create(prompt=description, n=4, size="1024x1024")