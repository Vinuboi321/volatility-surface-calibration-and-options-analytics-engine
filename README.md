# Volatility Surface Engine

Black-Scholes assumes every option on a stock shares one volatility. The market disagrees:
options at different strikes and expiries imply different volatilities, and those form a
"smile" or "skew" that changes shape over time. This project pulls real SPY option prices,
extracts the volatility each one implies, fits a smooth surface through them, checks that
surface for arbitrage, and tests whether selling options at implied vol actually makes money
once you hedge.

## Roadmap

| Step | What | Status |
|---|---|---|
| 1 | Implied vol solver (price -> vol) with round-trip tests | |
| 2 | Download and clean SPY option chains | |
| 3 | Plot the smile for each expiry | |
| 4 | Fit an SVI curve to each smile | |
| 5 | Arbitrage checks (calendar and butterfly) | |
| 6 | 3D surface dashboard (Plotly) | |
| 7 | Delta-hedging P&L experiment | |

## Setup (Windows)

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
python scripts/step1_play.py
```

## Layout

```
volsurface/      the library: pricing, implied vol, and later fitting/arbitrage code
tests/           pytest tests; run `pytest` from the project folder
scripts/         runnable scripts for each step
notebooks/       scratch exploration
data/            downloaded option chains (git-ignored)
```
