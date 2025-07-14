## LeetCode 224. Basic Calculator

### Problem Description

The **Basic Calculator** problem requires us to evaluate a given mathematical expression string that can include:
- Non-negative integers
- Operators: `+`, `-`
- Parentheses: `(` and `)`
- Optional spaces

### Constraints:
- The string is guaranteed to be a **valid mathematical expression**.
- You are **not allowed to use `eval()`** or any built-in expression evaluators.
- You must manually **parse and compute** the result.

### Example:

```python
Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## What I Learned

---

- First, I created a function called `into_splits` to manually break the input string into a list of tokens.
  - I faced challenges in properly handling **multi-digit numbers** and ignoring spaces.
  - To solve this, I used a temporary variable `num` to keep building the number character by character until a symbol or parenthesis was found, then added it to `splits`.

- After splitting, I created a main `calculate` function to evaluate the tokens.
  - Here, I learned how to use a **stack** to keep track of previous `res` and `sign` values when I encounter an opening parenthesis `(`.
  - When I find a closing parenthesis `)`, I **pop the last sign and result** from the stack and combine it with the current `res`.

- I used the `sign` variable to manage whether the current number should be added or subtracted.
  - This made it easy to apply the sign just when a number is found, keeping the logic clean.

- Overall, separating the logic into `into_splits` and `calculate` helped me write modular and understandable code.
  - It also made debugging easier since I could test tokenization and evaluation independently.
