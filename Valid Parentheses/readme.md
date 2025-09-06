# Code Craft By Ashish
## Valid Parentheses

Determine if a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'` is **valid**.

A string is **valid** if:

- Open brackets must be closed by the **same type** of brackets.
- Open brackets must be closed in the **correct order** (i.e., last opened, first closed).
- Every close bracket has a **corresponding open bracket** of the same type.

---

## Examples

**Example 1**
```
Input:  s = "()"
Output: true
```

**Example 2**
```
Input:  s = "()[]{}"
Output: true
```

**Example 3**
```
Input:  s = "(]"
Output: false
```

**Example 4**
```
Input:  s = "([])"
Output: true
```

**Example 5**
```
Input:  s = "([)]"
Output: false
```

---

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists only of the characters `'()[]{}'`.

---

## Intuition
Use a **stack** to track open brackets. When you see a closing bracket, it must match the **most recent** unmatched opening bracket at the top of the stack.

Key ideas:
- Push opening brackets onto the stack.
- For a closing bracket, check if the stack is non-empty **and** the top matches the corresponding opener.
- In the end, the stack must be empty for the string to be valid.

**Time Complexity:** `O(n)` — each character is processed once.

**Space Complexity:** `O(n)` in the worst case — when all characters are opening brackets.

---

---

## Edge Cases to Consider
- **Odd length** strings → immediately invalid (cannot pair perfectly).
- **Starts with a closing bracket** → invalid.
- **Mismatched types** like `"(]"` or cross-ordering like `"([)]"` → invalid.
- **Nested correctness**: `"([]{})"` should be valid.
- **Repeated single type**: `"((((()))))"` valid; `"(((()"` invalid.

---

## Testing
Try these quick checks:

```
"()"          -> true
"()[]{}"      -> true
"(]"          -> false
"([])"        -> true
"([)]"        -> false
"((((()))))"  -> true
"(((()"       -> false
"]"            -> false
```

---

## Why this works
A stack enforces **Last-In, First-Out (LIFO)** order, which mirrors how brackets must be closed. Each opener waits on the stack until its matching closer appears.

---

## Common Pitfalls
- Forgetting to check for an **empty stack** before peeking/popping when a closing bracket appears.
- Returning `true` without verifying the stack is **empty at the end**.
- Using an opener→closer map and pushing the *expected closer* can work, but be careful with early mismatches.

---

## Additional Notes
- This is a canonical stack problem (LeetCode #20: *Valid Parentheses*).
- The greedy stack approach is optimal under the given constraints.


## 📺 My YouTube Channel
Check out my channel for more coding problems and solutions:

**Code Craft By Ashish**  
🔗 [@CodeCraftByAshish](https://www.youtube.com/@CodeCraftByAshish)


