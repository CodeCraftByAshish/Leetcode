# Code Craft By Ashish
## Zigzag Conversion

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

---

## Problem Statement
Given a string `s` and an integer `numRows`, arrange the string in a zigzag pattern and then read line by line.

Return the string formed after this zigzag conversion.

---

## Example 1
```
Input:  s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

## Example 2
```
Input:  s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

## Example 3
```
Input:  s = "A", numRows = 1
Output: "A"
```

---

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

---

## Notes
- This is a simulation problem where characters are placed in a zigzag pattern.
- You need to carefully manage row direction (down vs. up) when placing characters.

---

## 📺 My YouTube Channel
**Code Craft By Ashish**  
🔗 [@CodeCraftByAshish](https://www.youtube.com/@CodeCraftByAshish)

