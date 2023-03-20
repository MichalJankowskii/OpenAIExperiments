import streamlit as st
import pandas as pd
import numpy as np
import modules.OpenAIService as OpenAIService


st.title('Test models')

openAIService = OpenAIService.OpenAIService()
openAIService.init_connection()

with st.form("my_form"):
   textarea_val = st.text_area("Enter text below:", value="How to clone a cat")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.header("text-davinci-003")
       #st.write(openAIService.createCompletion("text-davinci-003", textarea_val, 0.6).choices[0].text)

       for i in range(0, 10):
         st.header("Temp " + str(i/10.0))
         for j in range (0, 3):
           st.write(str(j) + " - " + openAIService.createCompletion("text-davinci-003", textarea_val, i / 10.0).choices[0].text)
       