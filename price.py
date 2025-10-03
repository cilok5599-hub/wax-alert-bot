import requests, io
import matplotlib.pyplot as plt
from telegram import Update
from telegram.ext import ContextTypes

async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=wax&vs_currencies=usd"
    chart_url = "https://api.coingecko.com/api/v3/coins/wax/market_chart?vs_currency=usd&days=1"

    data = requests.get(url).json()
    chart_data = requests.get(chart_url).json()

    price = data["wax"]["usd"]

    # Collect data for chart
    prices = [p[1] for p in chart_data["prices"]]
    times = [i for i in range(len(prices))]

    # Create chart
    plt.figure(figsize=(6,3))
    plt.plot(times, prices, label="WAX/USD")
    plt.title("WAX Price - Last 24h")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.legend()

    # Save chart in memory
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    await update.message.reply_text(f"💰 Current WAX Price: ${price:.4f} (source: Coingecko)")
    await update.message.reply_photo(buf)
