import streamlit as st
import pandas as pd
import numpy as np
import random
import math
#%%
st.title('Pachamalayalam dictionary')
#%%
class Widgets:
    def __init__(self):
        self.df = pd.read_csv('ml_en_dict.csv',encoding='utf_8')
        
        self.remarks = st.text_input("Search").lower()

        self.class_label = st.selectbox("Translate from?", ["Malayalam to English", "English to Malayalam"], key=1)

    def ml_en_pred(self, word):
        sub_df = self.df[self.df['MALAYALAM-1'] == word]
        try:
            e1 = str(sub_df['ENGLISH-1'].iloc[0])
            e2 = str(sub_df['ENGLISH-2'].iloc[0])
            e_desc = str(sub_df['ENG DESCRIPTION'].iloc[0])
        except:
            e1 = 'Not found'
            e2 = ''
            e_desc = ''
        return e1, e2, e_desc
        
    def en_ml_pred(self, word):
        sub_df = self.df[self.df['ENGLISH-1'] == word]
        try:
            m1 = str(sub_df['MALAYALAM-1'].iloc[0])
            m2 = str(sub_df['MALAYALAM-2'].iloc[0])
            m_desc = str(sub_df['ML DESCRIPTION'].iloc[0])
        except:
            m1 = 'Not found'
            m2 = ''
            m_desc = ''
        return m1, m2, m_desc        
#%%
W = Widgets()
#%%
if st.button("Search"):
     if W.class_label == "Malayalam to English":
        e1, e2, e_desc = W.ml_en_pred(W.remarks)
        st.write(e1)
     else:
        m1, m2, m_desc = W.en_ml_pred(W.remarks)
        st.write(m1)
    
    
    