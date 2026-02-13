tea_prices_inr = {
    "Masala chai": 40,
    "Elachi chai": 50,
    "Spicy chai": 200

}
tea_prices_usd = {tea:price/80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)