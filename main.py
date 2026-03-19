from im_engine.portfolio.trade import Trade
from im_engine.portfolio.portfolio import Portfolio
from im_engine.aggregation.im_calculator import compute_initial_margin

# Create trades
t1 = Trade("T1", "Rates", 1_000_000, 1)
t2 = Trade("T2", "Rates", 2_000_000, 5)
t3 = Trade("T3", "FX", 1_500_000, 3)

portfolio = Portfolio([t1, t2, t3])

im = compute_initial_margin(portfolio)

print(f"Initial Margin: {im:,.2f}")