[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cm6PS4yt)
# Week 1 Homework: Evidence Desk Patterns

## Student Name

KHADKA PRABIN

## Summary

This homework practices four fundamental data structure patterns using a detective investigation theme. Each problem maps to a classic pattern: frequency counting with a dictionary, duplicate detection with a set, bracket matching with a stack (list), and key-value lookup with a dictionary. Two optional challenges add queue processing with `deque` and a sort-and-scan approach for finding time gaps. The goal is not just to make tests pass but to understand *why* each data structure fits each problem.

## How to Run Tests

From the repository root, run:

```bash
pytest -q
```

To run one test file:

```bash
pytest -q tests/test_challenges.py
```

---

# Problem Notes

## 1. Evidence Counter

### Pattern

Frequency counting

### Data Structure

Dictionary (`dict[str, int]`)

### Approach

- Start with an empty dictionary `counts`.
- Loop through every item in `evidence`.
- For each item, use `counts.get(item, 0) + 1` to increment the count — this handles both the "first time seen" and "already seen" cases in one line.
- Return the completed dictionary.

### Complexity

- Time: `O(n)` — one pass through the list of `n` items; each dictionary operation (`get` and assignment) is `O(1)` average.
- Space: `O(k)` — the dictionary holds one entry per unique label. In the worst case (all labels distinct) this is `O(n)`.

### Edge Cases Checked

- [x] Empty list — returns `{}`
- [x] One item — returns `{item: 1}`
- [x] Repeated items — count accumulates correctly
- [x] Different labels — each gets its own entry
- [x] All items the same label — count equals list length
- [x] Case sensitivity — `"phone"` and `"Phone"` are counted separately

---

## 2. Repeat Suspect ID

### Pattern

Seen before (duplicate detection)

### Data Structure

Set (`set[str]`)

### Approach

- Start with an empty set `seen`.
- Loop through `ids` one at a time.
- Before adding each ID, check if it is already in `seen` — set membership is `O(1)` average.
- If it is already there, return it immediately (this is the *first* repeat).
- Otherwise, add it to `seen` and continue.
- After the loop, return `None` — no repeat was found.

### Complexity

- Time: `O(n)` — one pass through `n` IDs; each `in` check and `add` is `O(1)` average.
- Space: `O(n)` — in the worst case (no repeats) the set holds all `n` IDs.

**Tradeoff:** Using a dictionary instead of a set would also work, but a set is the cleaner choice here because we only need to track *presence*, not count.

### Edge Cases Checked

- [x] Empty list — returns `None`
- [x] No repeated IDs — returns `None`
- [x] First two IDs match — returns the first ID immediately
- [x] Multiple repeated IDs — returns the *first* one to repeat, not the most frequent
- [x] Only two items, both the same — returns that ID

---

## 3. Evidence Tag Validator

### Pattern

Stack matching (open/close bracket balancing)

### Data Structure

List used as a stack (`list[str]`)

### Approach

- Start with an empty list `stack` and a dictionary `matching` that maps each closing bracket to its expected opening bracket: `{")": "(", "]": "[", "}": "{"}`.
- Loop through every character in the string.
- If the character is an opening bracket (`(`, `[`, `{`), push it onto the stack.
- If it is a closing bracket, check two conditions: the stack must not be empty, and the top of the stack (`stack[-1]`) must equal the expected opener from `matching`. If either condition fails, return `False` immediately.
- If the character is neither, ignore it.
- After the loop, return `True` only if the stack is empty — an empty stack means every opener was closed.

### Complexity

- Time: `O(n)` — one pass through the `n` characters; each stack push/pop and dictionary lookup is `O(1)`.
- Space: `O(n)` — in the worst case (all opening brackets) the stack holds `n` entries.

**Why a stack works here:** Brackets must close in *reverse* order of opening — the most recently opened bracket must close first. That last-in, first-out property is exactly what a stack provides.

### Edge Cases Checked

- [x] Empty string — returns `True` (no brackets to violate)
- [x] Correctly nested tags — returns `True`
- [x] Mismatched tags `{[(])}` — returns `False`
- [x] Closing bracket before any opening bracket `)` — returns `False`
- [x] Unclosed opening bracket `(((` — returns `False` (stack not empty)
- [x] Non-bracket characters — ignored correctly
- [x] Single matching pair `()` — returns `True`

---

## 4. Alias Directory

### Pattern

Lookup table

### Data Structure

Dictionary (`dict[str, str]`)

### Approach

- Use `aliases.get(alias, None)` — if the key exists, it returns the value; otherwise it returns `None`.
- This is a single-line solution because dictionary lookup is exactly what this pattern is designed for.

### Complexity

- Time: `O(1)` average — dictionary key lookup is constant time on average due to hashing.
- Space: `O(1)` — no extra data structures are created; we just read from the existing dictionary.

**Tradeoff:** Using `if alias in aliases: return aliases[alias]` would also be correct but does two lookups. `get` does it in one.

### Edge Cases Checked

- [x] Known alias — returns the correct real name
- [x] Unknown alias — returns `None`
- [x] Empty dictionary — returns `None`
- [x] Alias that maps to an empty string — returns `""` (not `None`)
- [x] Case sensitivity — `"big red"` and `"Big Red"` are different keys

---

## Optional Challenge 1: Dispatch Queue

### Pattern

Queue processing (FIFO — first in, first out)

### Data Structure

`collections.deque`

### Approach

- Create a `deque` from the input list.
- Repeatedly call `popleft()` (removes from the front, `O(1)`) and append each result to a `processed` list.
- Return `processed`.

### Complexity

- Time: `O(n)` — `n` popleft operations, each `O(1)`.
- Space: `O(n)` — the deque and result list each hold `n` items.

**Why `deque` over a plain list:** `list.pop(0)` is `O(n)` because it shifts every remaining element. `deque.popleft()` is `O(1)`. For queue processing, `deque` is the correct choice.

---

## Optional Challenge 2: Timeline Gap Finder

### Pattern

Sorting + scan

### Data Structure

List

### Approach

- Return `0` immediately if fewer than two times are given.
- Use `sorted(times)` to get a new sorted list without mutating the input.
- Walk neighboring pairs with a loop and track the maximum difference.

### Complexity

- Time: `O(n log n)` — dominated by the sort; the scan is `O(n)`.
- Space: `O(n)` — `sorted()` creates a new list of `n` items.

---

# Assistance & Sources

## AI Used?

- [x] Yes

## If yes, what did AI help with?

- Explaining why `deque.popleft()` is O(1) while `list.pop(0)` is O(n)
- Suggesting additional edge cases (empty string for valid_tags, case sensitivity for lookup_alias)
- README wording and complexity explanations

## Other Sources

- Python `collections.deque` docs: https://docs.python.org/3/library/collections.html#collections.deque
- Course lecture notes on stacks, sets, and dictionaries