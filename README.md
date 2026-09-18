# finrisk

A lightweight portfolio risk analytics dashboard for exploring historical
returns, volatility, drawdowns, correlations and Value at Risk.

> **Status:** in development. Not usable yet — see the
> [open issues](../../issues) for what's planned.

## Installation

```bash
git clone https://github.com/<user>/finrisk.git
cd finrisk
uv sync
```

## Usage

```bash 
uv run streamlit run app.py

```

## Development

```bash
uv run ruff check .      # lint
uv run pytest            # tests
uv run pre-commit install
```

## Methodology

_Documented as the metrics land._

## Features

Planned scope — checked items are implemented.

**Data**
- [ ] Historical price data for 3–5 tickers via yfinance, with caching
- [ ] Configurable date range and return frequency (daily / weekly / monthly)
- [ ] Trading-calendar alignment across markets

**Risk & performance metrics**
- [ ] Cumulative return, CAGR, annualised volatility
- [ ] Sharpe and Sortino ratios with configurable risk-free rate
- [ ] Maximum drawdown incl. peak, trough and recovery duration
- [ ] Correlation matrix across holdings
- [ ] Value at Risk — historical, parametric and simulated
- [ ] Expected Shortfall (CVaR)
- [ ] Portfolio aggregation from user-defined weights

**Dashboard**
- [ ] Indexed price performance chart
- [ ] Underwater drawdown plot
- [ ] Correlation heatmap
- [ ] Risk/return scatter with portfolio marker
- [ ] Metrics summary table per asset and for the portfolio

**Simulation**
- [ ] Monte Carlo price paths over a 30-day horizon, preserving the
      correlation structure between assets
- [ ] Fan chart with percentile bands

## Disclaimer

This project is for educational purposes. Nothing here is investment advice.

## License

MIT — see [LICENSE](LICENSE).
