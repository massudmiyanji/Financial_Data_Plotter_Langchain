import yfinance as yf
import pandas as pd
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
import matplotlib.pyplot as plt
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import spacy
import requests


api1_key:'1NHALC6WZDFFDBFJ'
load_dotenv()
#lm=OpenAI()
# Streamlit app title
st.title("Financial Document Processing and Visualization with LangChain")

#prompt_template = 
#"""
#you are a AI finacial assitant. Given user rquest identify company name and retrive company name.
#the user request is:{user_request} 


#"""
#prompt=PromptTemplate(template=prompt_template,input_variables=['user_request']  )
#chain=LLMChain(llm=llm,prompt=prompt)

user_request=st.text_input('ENter your financial query')

nlp = spacy.load("en_core_web_lg")


if user_request:
    doc=nlp(user_request.title())
    company_name=[ent.text for ent in doc.ents if ent.label_ == "ORG"]
# get symbol for company name
    def get_ticker(company_name, api_key):
            base_url = "https://www.alphavantage.co/query"
            params = {
                "function": "SYMBOL_SEARCH",
                "keywords": company_name,
                "apikey": api_key
            }
            response = requests.get(base_url, params=params)
            data = response.json()
            if "bestMatches" in data:
                return data["bestMatches"][0]["1. symbol"]
            else:
                return None
    ticker = get_ticker(company_name, 'SFJH1HCL4VJNS5A0')


        # get fundamental report
    def get_fundamentals(symbol, api_key):
            base_url = "https://www.alphavantage.co/query"
            params = {
                "function": "OVERVIEW",
                "symbol": symbol,
                "apikey": api_key
            }
            response = requests.get(base_url, params=params)
            data = response.json()
            return data


    symbol = ticker
    fundamentals = get_fundamentals(symbol, 'SFJH1HCL4VJNS5A0')


    # Get earning reoorts
    def get_earnings(symbol, api_key):
        base_url = "https://www.alphavantage.co/query"
        params = {
            "function": "EARNINGS",
            "symbol": symbol,
            "apikey": api_key
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        return data

    # Example usage:

    symbol = "AAPL"
    earnings = get_earnings(symbol, 'SFJH1HCL4VJNS5A0')
   
    fundamentals_df=pd.DataFrame(fundamentals,index=['{ompany_name}'])

    st.write(fundamentals_df)

    annualEarnings=pd.DataFrame(earnings['annualEarnings'], index=range(len(earnings['annualEarnings'])))
    #dict_keys(['symbol', 'annualEarnings', 'quarterlyEarnings'])
    st.write(annualEarnings)





