"""FinRisk — portfolio risk analytics.

Pure-Python analytics package for historical returns, volatility,
drawdowns, correlations and Value at Risk. Contains no rendering code:
the Streamlit layer in ``app.py`` is a thin shell on top of these
functions.

Submodules:
    data: Market data loading and caching.
    returns: Return calculations and calendar alignment.
    metrics: Performance metrics (volatility, Sharpe, Sortino, drawdown).
    risk: Risk measures such as VaR and CVaR.
    portfolio: Portfolio weights and equity-curve calculation.
    simulate: Monte Carlo simulation utilities.
    charts: Plotly chart builders that return figures without rendering them.
"""
