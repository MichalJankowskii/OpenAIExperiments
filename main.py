import streamlit as st
import pandas as pd
import numpy as np
import modules.OpenAIService as OpenAIService


st.title('Open AI Test')

openAIService = OpenAIService.OpenAIService()
openAIService.init_connection()

with st.form("my_form"):
   textarea_val = st.text_area("Enter text below:", value="Enter text here")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write(openAIService.modelsList())
       st.write("slider", textarea_val)

#https://github.com/openai/openai-python

st.write("Outside the form")