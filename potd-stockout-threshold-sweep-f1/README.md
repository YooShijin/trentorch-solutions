# STOCKOUT THRESHOLD SWEEP

Beginner | classification | metrics-and-evaluation

**Difficulty:** Easy
**Tags:** Classification, Metrics & Evaluation

---

### Story

Walmart's stockout classifier ships with a default 0.5 decision threshold, but the business cost of
a missed stockout versus a false alarm isn't symmetric, so the team wants the threshold that
actually maximizes F1 on their validation set, not the framework default.

---

### The Math

For each distinct score value `t` present in the data, using `t` as the decision threshold (predict
positive if `score >= t`), compute `F1(t)`; return the `t` maximizing `F1` (ties broken by the
**larger** threshold).

### Input Format

```
n
score_1 y_1
...
score_n y_n
```

### Output Format

`best_threshold best_f1`, 6 decimals.

### Constraints

- `1 <= n <= 10^5`
- Time limit: 1.0 second.

---

### Example

**Input**

```
8
0.9 1
0.8 1
0.75 0
0.6 1
0.55 0
0.4 0
0.3 1
0.2 0
```

**Output**

```
0.600000 0.750000
```
