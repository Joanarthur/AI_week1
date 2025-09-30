def get_profitability_advice(crypto_data):
    advice = {}
    for coin, data in crypto_data.items():
        if data['profitability'] > 0.1:  # Example threshold for profitability
            advice[coin] = "Consider investing, as profitability is high."
        elif data['profitability'] > 0:
            advice[coin] = "Caution advised, profitability is positive but low."
        else:
            advice[coin] = "Not recommended for investment due to negative profitability."
    return advice

def get_sustainability_advice(crypto_data):
    advice = {}
    for coin, data in crypto_data.items():
        if data['sustainability'] > 0.7:  # Example threshold for sustainability
            advice[coin] = "Good choice for sustainable investment."
        elif data['sustainability'] > 0.4:
            advice[coin] = "Moderate sustainability; consider other factors."
        else:
            advice[coin] = "Not recommended for sustainable investment."
    return advice