import pytest
from testrepo.algorithms.duplicate_search import (
    dup_search_brute,
    dup_search_hash,
    dup_search_window,
)

IMPLEMENTATIONS = [dup_search_brute, dup_search_hash, dup_search_window]


@pytest.mark.parametrize("fn", IMPLEMENTATIONS)
class TestDuplicateSearch:
    def test_found_within_window(self, fn):
        assert fn([1, 2, 3, 1], 3) is True

    def test_not_found_outside_window(self, fn):
        assert fn([1, 0, 1, 1], 1) is True

    def test_duplicate_too_far_apart(self, fn):
        assert fn([1, 2, 3, 1, 2, 3], 2) is False

    def test_empty_list(self, fn):
        assert fn([], 0) is False

    def test_single_element(self, fn):
        assert fn([5], 1) is False

    def test_floats(self, fn):
        assert fn([-2.2, 4.0, 5.0, -2.2], 3) is True

    def test_k_zero(self, fn):
        assert fn([1, 1], 0) is False
