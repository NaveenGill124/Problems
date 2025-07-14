## 🧮 LeetCode 224. Basic Calculator

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

### ✅ 1. Manual Expression Parsing


- first I splits the given string with a function
  - with proper spliting I created another main function in that my cahllenges comes like how to split it properly then in mainn function, 

---

### ✅ 2. Stack-Based Evaluation
Parentheses introduce **nested scopes**, so I learned to use a **stack** to:

- Save the current result and sign when entering a parenthesis `(`
- Restore and combine results when exiting a parenthesis `)`

This mimics how we solve expressions on paper and is a common technique used in compilers and interpreters.

---

### ✅ 3. Sign Management
Instead of evaluating every expression immediately, I learned to keep track of the **current sign** (`+` as `+1`, `-` as `-1`) and apply it when the next number comes.  
This simplified the logic and made it easier to handle **deeply nested expressions**.

---

### ✅ 4. Edge Case Awareness
This problem made me more attentive to subtle edge cases like:

- Leading, trailing, or multiple spaces
- Nested parentheses
- Multi-digit numbers
- When to apply the sign vs. when to push/pop from the stack

---

### ✅ 5. Clean Code and Separation of Concerns
I structured my solution with **clear separation of responsibilities**:

- A `tokenize()` function to handle input parsing
- An `evaluate()` function to process the expression logic

This made my code more **modular, readable, and reusable** — a valuable practice in real-world development.

---
