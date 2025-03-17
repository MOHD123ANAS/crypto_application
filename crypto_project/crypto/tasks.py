import requests
from celery import shared_task
from crypto.models import CryptoPrice, Organization

@shared_task
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        btc_price = data.get("bitcoin", {}).get("usd", None)
        eth_price = data.get("ethereum", {}).get("usd", None)

        if btc_price and eth_price:
            org = Organization.objects.first()

            CryptoPrice.objects.create(symbol="BTC", price=btc_price, org=org)
            CryptoPrice.objects.create(symbol="ETH", price=eth_price, org=org)

            print(f"✅ Prices updated! BTC: {btc_price}, ETH: {eth_price}")


            clean_old_prices()

        else:
            print("⚠️ API returned invalid data:", data)

    except requests.exceptions.Timeout:
        print("❌ Request timed out while fetching prices from CoinGecko.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch prices: {e}")

def clean_old_prices():

    total_prices = CryptoPrice.objects.count()
    if total_prices > 100:

        excess_count = total_prices - 100
        old_prices = CryptoPrice.objects.order_by('timestamp')[:excess_count]
        old_prices.delete()
        print(f"🗑️ Deleted {excess_count} old crypto prices to maintain a max of 100 records.")
