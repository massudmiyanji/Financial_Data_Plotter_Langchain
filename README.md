# Financial Document Processing and Visualization with LangChain

This is a Streamlit application that allows users to input financial queries and retrieve relevant financial data and visualizations. The app uses various technologies like `yfinance`, `LangChain`, `Spacy`, and `Alpha Vantage` API to process and visualize financial documents.

## Features

- **Financial Query Processing:** Input your financial query, and the app will process it using Spacy's NLP model to extract company names.
- **Company Symbol Retrieval:** The app fetches the stock ticker symbol for the identified company using the Alpha Vantage API.
- **Fundamental Data & Earnings Reports:** Retrieves and displays fundamental data and annual earnings reports for the company.
- **Data Visualization:** Automatically generates plots based on the query, such as earnings over time or an overview of fundamental data.

## Requirements

- Python 3.7+
- The following Python libraries:
  - yfinance
  - pandas
  - streamlit
  - langchain
  - spacy
  - matplotlib
  - requests
  - dotenv
  - for Alphavantage API key, you can get a free API Key from their websit. but bear in mind that their Free API tools in limited to 25 request per day.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/financial-doc-processing.git
   cd financial-doc-processing
