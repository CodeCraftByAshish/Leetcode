# Code Craft By Ashish
## String to Integer (atoi)

Implement the `myAtoi(string s)` function which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi`).

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in `s` is not a valid integral number, or if no such sequence exists because either `s` is empty or it contains only whitespace characters, no conversion is performed and `0` is returned.

If the numerical value is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, clamp the integer so that it remains in the range. Specifically, values smaller than `-2^31` should be clamped to `-2^31`, and values larger than `2^31 - 1` should be clamped to `2^31 - 1`.

---

## Requirements

* Read the input string `s` and return the 32-bit signed integer conversion according to the rules above.
* Do **not** use built-in library functions that directly perform the full conversion; implement the parsing and clamping behavior explicitly.

---

## Examples

**Example 1**

```
Input:  s = "42"
Output: 42
Explanation: The string "42" converts directly to the integer 42.
```

**Example 2**

```
Input:  s = "   -42"
Output: -42
Explanation: After trimming leading whitespace, the first non-whitespace character is '-', which indicates a negative sign. The rest of the digits form the number 42.
```

**Example 3**

```
Input:  s = "4193 with words"
Output: 4193
Explanation: Conversion stops at the first non-digit character ' ' after reading the digits.
```

**Example 4**

```
Input:  s = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a signed digit, so no valid conversion can be performed.
```

**Example 5**

```
Input:  s = "-91283472332"
Output: -2147483648
Explanation: The number is less than INT_MIN = -2^31, so it is clamped.
```

---

## Constraints

* `0 <= s.length <= 200`
* `s` consists of English letters (both uppercase and lowercase), digits (`0-9`), space `' '`, plus `'+'`, minus `'-'`, and other printable ASCII characters.

---

## Parsing Rules Breakdown (step-by-step)

1. **Discard leading whitespace** until the first non-whitespace character is found.
2. **Optional sign**: Check if the next character is `+` or `-`. Record the sign for the final number.
3. **Parse digits**: Read in the next characters until the next non-digit character or the end of the input. Convert these digits into an integer.
4. **Clamp**: If the integer is out of the 32-bit signed integer range, clamp to `[-2^31, 2^31 - 1]`.
5. **Return** the final integer with the appropriate sign.

---

## Important Points / Edge Cases

* **Only whitespace or empty string** → return `0`.
* **Sign with no digits** (e.g., `"+"`, `"-"`) → return `0`.
* **Non-digit at start** after trimming → return `0`.
* **Digits followed by characters** → stop parsing at first non-digit and return the integer parsed so far.
* **Overflow / Underflow** → clamp to `INT_MAX = 2^31 - 1 = 2147483647` or `INT_MIN = -2^31 = -2147483648`.
* **Leading zeros** should be handled correctly (e.g., `"00000123"` → `123`).

---

## Approach (conceptual — no code provided)

* Iterate through the string while maintaining an index pointer.
* Skip initial whitespace by advancing the pointer.
* Check and store the sign (`+` or `-`) if present, then advance the pointer.
* While the current character is a digit:

  * Convert the digit character to its numeric value (e.g., `ch - '0'`).
  * Before adding the digit to the accumulated result, check whether appending this digit would cause overflow. You can do this by comparing the current result with `(INT_MAX - digit) / 10` (for positive numbers) or by symmetric logic for negatives.
  * If overflow would occur, immediately return the clamped boundary value according to the sign.
  * Otherwise, update the accumulated result: `result = result * 10 + digit`.
* Apply the recorded sign to the accumulated result and return it.

---

## Complexity

* **Time Complexity:** `O(n)` where `n` is the length of the string `s` (each character is processed at most once).
* **Space Complexity:** `O(1)` — only a few variables are used for state (index, sign, result).

---

## Test Cases

```
"42"                     -> 42
"   -42"                 -> -42
"4193 with words"        -> 4193
"words and 987"          -> 0
"-91283472332"           -> -2147483648  (clamped)
"21474836460"           -> 2147483647   (clamped)
"+1"                     -> 1
"+"                      -> 0
"-"                      -> 0
"   +0 123"              -> 0
"00000-42a1234"          -> 0
"   000001234"           -> 1234
```

---

## 📺 My YouTube Channel

**Code Craft By Ashish**
🔗 [@CodeCraftByAshish](https://www.youtube.com/@CodeCraftByAshish)  🎬

---

*This file contains the full problem description, detailed parsing rules, edge cases, approach, complexity notes, and test cases for manual verification. No direct code solution is included as requested.*
