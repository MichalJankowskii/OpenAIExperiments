import streamlit as st
import openai

class OpenAIService:
    def init_connection(self):
        self.init_openAIConnetion()

    def init_openAIConnetion(self):
        st.warning("Working wih OpenAI service")
        openai.organization = st.secrets["organisation"]
        openai.api_key =  st.secrets["apiKey"]

    def init_AzureConnection(self):
        st.warning("Working wih Azure service")
        openai.api_type = "azure"
        openai.api_key = st.secrets["azureKey"]
        openai.api_base = st.secrets["azureEndPoint"]
        openai.api_version = "2022-12-01"

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