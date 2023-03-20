import streamlit as st
import pandas as pd
import numpy as np
import modules.OpenAIService as OpenAIService


st.title('Moderation test')

openAIService = OpenAIService.OpenAIService()
openAIService.init_connection()

with st.form("my_form"):
   textarea_val = st.text_area("Enter text below:", value="Wrocław 10 places to visit")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.header("Moderation")
       st.write(openAIService.createModeration(textarea_val))
    