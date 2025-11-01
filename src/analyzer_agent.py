import pandas as pd
from transformers import pipeline

# Use a small open-source model for free
generator = pipeline("text-generation", model="google/flan-t5-small", device=-1)

def load_data():
    df = pd.read_csv("data/crypto_data.csv")
    return df

def get_summary(df):
    top_gainer = df.loc[df["price_change_percentage_24h"].idxmax()]
    top_loser = df.loc[df["price_change_percentage_24h"].idxmin()]
    return f"Top Gainer: {top_gainer['id']} (+{top_gainer['price_change_percentage_24h']:.2f}%)\nTop Loser: {top_loser['id']} ({top_loser['price_change_percentage_24h']:.2f}%)"

def analyze_correlation(df):
    btc = df[df["id"] == "bitcoin"]["current_price"].values[0]
    eth = df[df["id"] == "ethereum"]["current_price"].values[0]
    return f"BTC-ETH Price Ratio: {btc/eth:.2f}"

def ask_agent(question, df):
    # Prepare data preview
    data_preview = df.head(5).to_string()
    prompt = f"Here is crypto market data:\n{data_preview}\nAnswer this question: {question}"

    # Use Hugging Face model to generate answer
    result = generator(prompt, max_length=200, do_sample=True)
    return result[0]["generated_text"]
