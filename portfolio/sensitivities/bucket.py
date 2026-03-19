def assign_bucket(trade):
    if trade.maturity < 2:
        return "Short"
    elif trade.maturity < 7:
        return "Medium"
    else:
        return "Long"
