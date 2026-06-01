"""Week 1 Homework: Evidence Desk Patterns.

Complete each function using the data structure pattern named in the docstring.

Rules:
- Python 3.11+
- Standard library only
- Do not change function names or parameters
- Run tests with: pytest -q
"""

from collections import deque


# -----------------------------------------------------------------------------
# Required Problem 1: Evidence Counter
# -----------------------------------------------------------------------------

def count_evidence(evidence: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each evidence label appears.

    Pattern: frequency counting
    Data structure: dictionary

    Examples:
        >>> count_evidence(["phone", "receipt", "phone"])
        {'phone': 2, 'receipt': 1}
        >>> count_evidence([])
        {}

    Args:
        evidence: A list of evidence labels.

    Returns:
        A dictionary where each key is an evidence label and each value is the
        number of times that label appears.
    """
    counts: dict[str, int] = {}
    for item in evidence:
        counts[item] = counts.get(item, 0) + 1
    return counts


# -----------------------------------------------------------------------------
# Required Problem 2: Repeat Suspect ID
# -----------------------------------------------------------------------------

def first_repeated_id(ids: list[str]) -> str | None:
    """Return the first suspect ID that appears a second time.

    Pattern: seen before
    Data structure: set

    Examples:
        >>> first_repeated_id(["A17", "B22", "C91", "B22"])
        'B22'
        >>> first_repeated_id(["A17", "B22", "C91"])
        None

    Args:
        ids: A list of suspect ID strings.

    Returns:
        The first ID that appears again, or None if there are no repeats.
    """
    seen: set[str] = set()
    for id_ in ids:
        if id_ in seen:
            return id_
        seen.add(id_)
    return None


# -----------------------------------------------------------------------------
# Required Problem 3: Evidence Tag Validator
# -----------------------------------------------------------------------------

def valid_tags(tags: str) -> bool:
    """Return True if all bracket-style evidence tags are balanced.

    Pattern: stack matching
    Data structure: list used as a stack

    Valid tag characters are (), [], and {}.
    Ignore all other characters.

    Examples:
        >>> valid_tags("{[()]}")
        True
        >>> valid_tags("{[(])}")
        False
        >>> valid_tags("case-{A17}[photo]")
        True

    Args:
        tags: A string that may contain bracket characters.

    Returns:
        True if brackets are balanced correctly, otherwise False.
    """
    stack: list[str] = []
    matching: dict[str, str] = {")": "(", "]": "[", "}": "{"}

    for char in tags:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0


# -----------------------------------------------------------------------------
# Required Problem 4: Alias Directory
# -----------------------------------------------------------------------------

def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    """Return the real name connected to an alias.

    Pattern: lookup table
    Data structure: dictionary

    Examples:
        >>> aliases = {"Big Red": "Marco Silva", "Ghostline": "Eli Brooks"}
        >>> lookup_alias(aliases, "Ghostline")
        'Eli Brooks'
        >>> lookup_alias(aliases, "Unknown")
        None

    Args:
        aliases: A dictionary mapping alias names to real names.
        alias: The alias to search for.

    Returns:
        The real name if the alias exists, otherwise None.
    """
    return aliases.get(alias, None)


# -----------------------------------------------------------------------------
# Optional Challenge 1: Dispatch Queue
# -----------------------------------------------------------------------------

def process_reports(reports: list[str]) -> list[str]:
    """Return case reports in first-in, first-out processing order.

    Pattern: queue processing
    Data structure: collections.deque

    Examples:
        >>> process_reports(["burglary", "traffic stop", "noise complaint"])
        ['burglary', 'traffic stop', 'noise complaint']

    Args:
        reports: A list of report labels in arrival order.

    Returns:
        A list of report labels in the order they were processed.
    """
    queue: deque[str] = deque(reports)
    processed: list[str] = []
    while queue:
        processed.append(queue.popleft())
    return processed


# -----------------------------------------------------------------------------
# Optional Challenge 2: Timeline Gap Finder
# -----------------------------------------------------------------------------

def largest_time_gap(times: list[int]) -> int:
    """Return the largest gap between neighboring event times after sorting.

    Pattern: sorting + scan
    Data structure: list

    Examples:
        >>> largest_time_gap([1300, 915, 1600, 945])
        355
        >>> largest_time_gap([1200])
        0

    Args:
        times: A list of integer event times.

    Returns:
        The largest difference between neighboring sorted times. Return 0 if
        there are fewer than two times.
    """
    if len(times) < 2:
        return 0
    sorted_times = sorted(times)
    return max(sorted_times[i + 1] - sorted_times[i] for i in range(len(sorted_times) - 1))