from im_engine.portfolio.trade import Trade
from im_engine.portfolio.portfolio import Portfolio
from im_engine.aggregation.im_calculator import compute_initial_margin

def test_im_positive():
    t = Trade("T1", "Rates", 1_000_000, 2)
    portfolio = Portfolio([t])
    
    im = compute_initial_margin(portfolio)
    
    assert im > 0