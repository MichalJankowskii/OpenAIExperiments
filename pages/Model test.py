import streamlit as st
import pandas as pd
import numpy as np
import modules.OpenAIService as OpenAIService


st.title('Test models')

openAIService = OpenAIService.OpenAIService()
openAIService.init_connection()

with st.form("my_form"):
   textarea_val = st.text_area("Enter text below:", value="Wrocław 10 places to visit")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.header("ada")
       st.write(openAIService.createCompletion("ada", textarea_val, 0.6).choices[0].text)
       st.header("text-davinci-002")
       st.write(openAIService.createCompletion("text-davinci-002", textarea_val, 0.6).choices[0].text)
       st.header("text-davinci-003")
       st.write(openAIService.createCompletion("text-davinci-003", textarea_val, 0.6).choices[0].text)
       st.header("text-curie-001")
       st.write(openAIService.createCompletion("text-curie-001", textarea_val, 0.6).choices[0].text)
       st.header("text-babbage-001")
       st.write(openAIService.createCompletion("text-babbage-001", textarea_val, 0.6).choices[0].text)
       st.header("Chat")
       st.write(openAIService.createChatCompletion("user", textarea_val).choices[0].message.content)