import streamlit as st
from src.analyzer_agent import load_data, get_summary, analyze_correlation, ask_agent
from src.data_collector import fetch_crypto_data

st.set_page_config(page_title="Crypto Market Agent", page_icon="💰")
st.title("💰 Cryptocurrency Market Analysis Agent")

# Button to refresh data
if st.button("Fetch Latest Data"):
    df = fetch_crypto_data()
else:
    df = load_data()

st.subheader("📊 Latest Market Data")
st.dataframe(df)

st.subheader("📈 Market Summary")
st.text(get_summary(df))
st.text(analyze_correlation(df))

query = st.text_input("💭 Ask your question (e.g., Which coin grew fastest in 24h?)")
if st.button("Ask"):
    answer = ask_agent(query, df)
    st.success(answer)
