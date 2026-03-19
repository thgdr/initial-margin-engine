class Trade:
    def __init__(self, trade_id, asset_class, notional, maturity):
        self.trade_id = trade_id
        self.asset_class = asset_class  # 'Rates' or 'FX'
        self.notional = notional
        self.maturity = maturity
