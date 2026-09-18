"""Shared pytest fixtures for FinRisk tests.

All fixtures are generated offline and deterministically. Fixtures whose
analytical answer is known state that answer in their docstring, so tests
assert against a pre-computed value rather than against the output of the
function under test.
"""

import numpy as np
import pandas as pd
import pytest

SEED = 42


@pytest.fixture
def random_walk_prices() -> pd.DataFrame:
    """Three-asset geometric random walk over 252 business days.

    Seeded with ``SEED``, so repeated runs produce identical values.
    Starts at 100.0 for every asset.
    """
    rng = np.random.default_rng(SEED)
    index = pd.bdate_range("2024-01-01", periods=252)
    returns = rng.normal(0.0005, 0.01, size=(252, 3))
    prices = 100.0 * np.exp(np.cumsum(returns, axis=0))
    return pd.DataFrame(prices, index=index, columns=["AAA", "BBB", "CCC"])


@pytest.fixture
def known_drawdown_series() -> pd.Series:
    """Hand-built price path with an exactly known drawdown.

    Path: 100, 120, 75, 90, 130 on 2024-01-01 .. 2024-01-05 (business days).

    Expected values:
        peak:          120.0 on 2024-01-02
        trough:         75.0 on 2024-01-03
        max drawdown:  75 / 120 - 1 == -0.375  (-37.5%)
        recovery date: 2024-01-05, the first close back at or above the peak
    """
    index = pd.bdate_range("2024-01-01", periods=5)
    return pd.Series([100.0, 120.0, 75.0, 90.0, 130.0], index=index, name="DD")


@pytest.fixture
def constant_return_series() -> pd.Series:
    """Flat 0.1% daily growth over 252 business days, starting at 100.0.

    Expected values:
        volatility: exactly 0.0 (allow ~1e-12 for floating point noise)
        CAGR:       1.001 ** 252 - 1 == 0.28633... at 252 periods per year
        max drawdown: 0.0, the path never declines
    """
    index = pd.bdate_range("2024-01-01", periods=253)
    return pd.Series(100.0 * 1.001 ** np.arange(253), index=index, name="FLAT")


@pytest.fixture
def known_correlation_frame() -> pd.DataFrame:
    """Two return series drawn with a target Pearson correlation of 0.8.

    Built from independent normals via a Cholesky factor of [[1, 0.8], [0.8, 1]].
    The empirical correlation of a finite sample only approaches the target:
    at n=2000 and ``SEED`` it is within ~0.02, so assert with a tolerance.
    """
    rng = np.random.default_rng(SEED)
    target = np.array([[1.0, 0.8], [0.8, 1.0]])
    index = pd.bdate_range("2024-01-01", periods=2000)
    returns = rng.normal(0.0, 0.01, size=(2000, 2)) @ np.linalg.cholesky(target).T
    return pd.DataFrame(returns, index=index, columns=["XXX", "YYY"])


@pytest.fixture
def misaligned_calendar_frame() -> pd.DataFrame:
    """Two assets whose trading calendars differ, joined on the union of dates.

    XXX trades 2024-01-01 .. 2024-01-05 but is closed on 2024-01-03.
    YYY trades 2024-01-02 .. 2024-01-08 and observes no holiday.
    Missing observations are NaN, so alignment logic has to handle both a
    mid-series gap and non-overlapping start and end dates.
    """
    xxx = pd.Series(
        [100.0, 101.0, 102.0, 103.0],
        index=pd.DatetimeIndex(
            ["2024-01-01", "2024-01-02", "2024-01-04", "2024-01-05"]
        ),
    )
    yyy = pd.Series(
        [200.0, 201.0, 202.0, 203.0, 204.0],
        index=pd.bdate_range("2024-01-02", periods=5),
    )
    return pd.DataFrame({"XXX": xxx, "YYY": yyy})
