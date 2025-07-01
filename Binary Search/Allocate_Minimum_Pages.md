# 📘 Book Allocation Problem

## 🧩 Problem Statement

Given an array `arr[]` of integers where each element represents the number of pages in a book, and an integer `k` representing the number of students, the task is to allocate books to students such that:

- Every student receives **at least one book**.
- Each student is assigned a **contiguous block of books**.
- **No book is assigned to more than one student**.
- The goal is to **minimize the maximum number of pages assigned to any student**.

If it is not possible to allocate books under these constraints, return `-1`.

### Example:

**Input:**

```python
arr = [12, 34, 67, 90]
k = 2
```
**Output**

```python
113

```
### Explanation

Possible allocations and their respective maximum pages:

- `[12]` and `[34, 67, 90]` → Max pages = **191**
- `[12, 34]` and `[67, 90]` → Max pages = **157**
- `[12, 34, 67]` and `[90]` → Max pages = **113** ✅

Out of all valid allocations, **113** is the minimum possible maximum.  
Hence, the optimal solution is **113**.

---

### My Approach

When I initially saw the problem, I wasn't sure how to approach it. The idea of minimizing the **maximum pages** a student gets suggested that it might involve some kind of **optimization strategy**.

After analyzing further, I realized this is a classic **Binary Search on Answer** problem.

---

### Key Insight

The minimum possible value for the maximum number of pages a student can get lies between:

- `max(arr)` → because at least one student must take the largest book.
- `sum(arr)` → because one student might take all the books.

This insight allowed me to **use binary search in this range** to find the smallest feasible maximum pages.

---

### Binary Search + Greedy Validation

To solve the problem efficiently, I combined:

- **Binary Search** to narrow down the answer range.
- A **Greedy function** to validate whether a given value can be a valid maximum page allocation.

### Steps:

1. Perform binary search in the range `[max(arr), sum(arr)]`.
2. For each `mid` value, use a helper function to **check if allocation is possible**.
3. If allocation is valid with current `mid`, try a smaller value to minimize further.
4. If allocation is not possible, increase the `mid` value.

---

## ✅ The `isPossible()` Function

This function checks if it’s feasible to divide the books among `k` students such that **no student gets more than `max_pages_allowed`** and the allocation is **contiguous**.

### Logic:

- Traverse each book in the array.
- Maintain a running sum of pages for the current student.
- If adding a book exceeds `max_pages_allowed`, assign books to the next student.
- Count how many students are needed in this process.
- If the count exceeds `k`, return `False`. Otherwise, return `True`.

This function helps determine the **feasibility** of any mid-value during binary search.


