import streamlit as st
import pandas as pd
import numpy as np
import modules.OpenAIService as OpenAIService


st.title('Model list')

openAIService = OpenAIService.OpenAIService()
openAIService.init_connection()

with st.form("my_form"):
   # Every form must have a submit button.
   submitted = st.form_submit_button("List models")
   if submitted:
       st.write(openAIService.modelsList())