import pytest
from testrepo.algorithms.stock_profit import (
    max_profit_brute,
    max_profit_linear,
    max_profit_kadane,
)

IMPLEMENTATIONS = [max_profit_brute, max_profit_linear, max_profit_kadane]


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
class TestStockProfit:
    def test_basic_profit(self, fn):
        assert fn([1, 10, 2, 13]) == 12

    def test_buy_low_sell_high(self, fn):
        assert fn([7, 1, 5, 3, 6, 4]) == 5

    def test_no_profit(self, fn):
        assert fn([7, 6, 4, 3, 1]) == 0

    def test_single_price(self, fn):
        assert fn([5]) == 0

    def test_two_prices_profit(self, fn):
        assert fn([1, 2]) == 1

    def test_two_prices_no_profit(self, fn):
        assert fn([2, 1]) == 0

    def test_all_same(self, fn):
        assert fn([3, 3, 3, 3]) == 0

    def test_profit_at_end(self, fn):
        assert fn([2, 4, 1, 7]) == 6
