"""Tests for Week 1 Homework: Evidence Desk Patterns.

Run from the repository root:
    pytest -q
"""

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from src.challenges import (  # noqa: E402
    count_evidence,
    first_repeated_id,
    largest_time_gap,
    lookup_alias,
    process_reports,
    valid_tags,
)


# -----------------------------------------------------------------------------
# Required Problem 1: count_evidence
# -----------------------------------------------------------------------------

def test_count_evidence_counts_multiple_labels() -> None:
    evidence = ["phone", "receipt", "phone", "cash", "receipt", "phone"]

    assert count_evidence(evidence) == {
        "phone": 3,
        "receipt": 2,
        "cash": 1,
    }


def test_count_evidence_empty_list() -> None:
    assert count_evidence([]) == {}


def test_count_evidence_single_item() -> None:
    assert count_evidence(["keycard"]) == {"keycard": 1}


def test_count_evidence_is_case_sensitive() -> None:
    assert count_evidence(["phone", "Phone", "phone"]) == {
        "phone": 2,
        "Phone": 1,
    }


# -----------------------------------------------------------------------------
# Required Problem 2: first_repeated_id
# -----------------------------------------------------------------------------

def test_first_repeated_id_returns_first_id_that_repeats() -> None:
    ids = ["A17", "B22", "C91", "B22", "A17"]

    assert first_repeated_id(ids) == "B22"


def test_first_repeated_id_returns_none_when_no_repeat() -> None:
    assert first_repeated_id(["A17", "B22", "C91"]) is None


def test_first_repeated_id_handles_empty_list() -> None:
    assert first_repeated_id([]) is None


def test_first_repeated_id_repeat_can_be_first_item() -> None:
    assert first_repeated_id(["X01", "X01", "A17"]) == "X01"


# -----------------------------------------------------------------------------
# Required Problem 3: valid_tags
# -----------------------------------------------------------------------------

@pytest.mark.parametrize(
    "tags",
    [
        "",
        "{[()]}",
        "((()))",
        "[]{}()",
        "case-{A17}[photo](verified)",
    ],
)
def test_valid_tags_returns_true_for_balanced_tags(tags: str) -> None:
    assert valid_tags(tags) is True


@pytest.mark.parametrize(
    "tags",
    [
        "{[(])}",
        "(()",
        ")(",
        "case-{A17[photo]",
        "([)]",
    ],
)
def test_valid_tags_returns_false_for_unbalanced_tags(tags: str) -> None:
    assert valid_tags(tags) is False


# -----------------------------------------------------------------------------
# Required Problem 4: lookup_alias
# -----------------------------------------------------------------------------

def test_lookup_alias_returns_real_name_for_known_alias() -> None:
    aliases = {
        "Big Red": "Marco Silva",
        "The Accountant": "Nina Park",
        "Ghostline": "Eli Brooks",
    }

    assert lookup_alias(aliases, "The Accountant") == "Nina Park"


def test_lookup_alias_returns_none_for_unknown_alias() -> None:
    aliases = {"Big Red": "Marco Silva"}

    assert lookup_alias(aliases, "Unknown") is None


def test_lookup_alias_handles_empty_dictionary() -> None:
    assert lookup_alias({}, "Ghostline") is None


# -----------------------------------------------------------------------------
# Optional Challenge 1: process_reports
# -----------------------------------------------------------------------------

@pytest.mark.skip(reason="Optional challenge: remove this skip to check it.")
def test_process_reports_returns_reports_in_arrival_order() -> None:
    reports = ["burglary", "traffic stop", "missing wallet", "noise complaint"]

    assert process_reports(reports) == reports


@pytest.mark.skip(reason="Optional challenge: remove this skip to check it.")
def test_process_reports_handles_empty_list() -> None:
    assert process_reports([]) == []


# -----------------------------------------------------------------------------
# Optional Challenge 2: largest_time_gap
# -----------------------------------------------------------------------------

@pytest.mark.skip(reason="Optional challenge: remove this skip to check it.")
def test_largest_time_gap_sorts_and_finds_largest_neighbor_gap() -> None:
    assert largest_time_gap([1300, 915, 1600, 945]) == 355


@pytest.mark.skip(reason="Optional challenge: remove this skip to check it.")
def test_largest_time_gap_handles_short_lists() -> None:
    assert largest_time_gap([]) == 0
    assert largest_time_gap([1200]) == 0


@pytest.mark.skip(reason="Optional challenge: remove this skip to check it.")
def test_largest_time_gap_does_not_mutate_input() -> None:
    times = [1300, 915, 1600, 945]

    largest_time_gap(times)

    assert times == [1300, 915, 1600, 945]


# -----------------------------------------------------------------------------
# Student-added tests
# -----------------------------------------------------------------------------

def test_count_evidence_all_same_label() -> None:
    assert count_evidence(["knife", "knife", "knife"]) == {"knife": 3}


def test_count_evidence_all_unique_labels() -> None:
    assert count_evidence(["phone", "receipt", "cash"]) == {"phone": 1, "receipt": 1, "cash": 1}


def test_first_repeated_id_two_identical_items() -> None:
    assert first_repeated_id(["Z99", "Z99"]) == "Z99"


def test_first_repeated_id_returns_earlier_repeat_not_later() -> None:
    assert first_repeated_id(["A17", "B22", "C91", "B22", "A17"]) == "B22"


def test_valid_tags_lone_closing_bracket_is_false() -> None:
    assert valid_tags("}") is False


def test_valid_tags_unclosed_opening_bracket_is_false() -> None:
    assert valid_tags("(((") is False


def test_valid_tags_no_brackets_is_true() -> None:
    assert valid_tags("case-A17-photo") is True


def test_valid_tags_single_pair_is_true() -> None:
    assert valid_tags("()") is True


def test_lookup_alias_is_case_sensitive() -> None:
    aliases = {"big red": "Marco Silva"}
    assert lookup_alias(aliases, "Big Red") is None


def test_lookup_alias_returns_value_even_if_empty_string() -> None:
    assert lookup_alias({"Shadow": ""}, "Shadow") == ""