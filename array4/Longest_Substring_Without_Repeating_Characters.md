## What I Learned

### Brute-Force (O(n³))
- I tried every substring `(i…j)` and used a `set` to check uniques.
- Worked, but way too slow on longer strings.

### Sliding-Window “Better” (O(n²))
- Kept two pointers `left/right` and grew the window.
- On a duplicate, I moved `left` forward until it vanished.
- No more triple loops, but still did `s[l:r]` and membership checks → can still hit O(n²).

### Optimal with Hash-Map (O(n))
- Used a dictonary `dic` to remember each char’s latest index.
- As I moved `r`, if I hit a duplicate inside the window, I jumped `l` to `dic[ch] + 1`.
- Now every character and pointer moves forward just once → true O(n).
