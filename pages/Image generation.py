import streamlit as st
import pandas as pd
import numpy as np
import modules.OpenAIService as OpenAIService


st.title('Image creation')

openAIService = OpenAIService.OpenAIService()
openAIService.init_connection()

with st.form("my_form"):
   textarea_val = st.text_area("Enter text below:", value="two cats playing chess, oil painting as Vincent van Gogh")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.header("Image")
       image = openAIService.createImage(textarea_val)
       for imageUlr in image['data']:
           st.image(imageUlr['url'])
           