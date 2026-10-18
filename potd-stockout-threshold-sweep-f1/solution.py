def best_f1_threshold(scores: list[float], y: list[int]) -> tuple[float, float]:
    """
    The score threshold that maximizes F1 (predict positive if score >= t).

    scores: n predicted scores. y: n true labels, each 0 or 1.

    For each distinct value in scores, using it as threshold t, compute
    F1(t) over the whole dataset. Return (best_threshold, best_f1).

    Ties for the best F1 are broken by the LARGER threshold. A threshold
    where precision or recall is undefined (a zero denominator) can never
    win. Sort once and sweep with running TP/FP counts, O(n log n), not
    a from-scratch recompute per threshold.
    """
    pairs = sorted(zip(scores, y), key=lambda p: p[0], reverse=True)
    total_pos = sum(y)
    best_thr = None
    best_f1 = -1.0
    tp = 0
    fp = 0
    i = 0
    n = len(pairs)
    while i < n:
        thr = pairs[i][0]
        while i < n and pairs[i][0] == thr:
            if pairs[i][1] == 1:
                tp += 1
            else:
                fp += 1
            i += 1
        if tp + fp == 0 or total_pos == 0:
            continue
        precision = tp / (tp + fp)
        recall = tp / total_pos
        if precision + recall == 0:
            continue
        f1 = 2 * precision * recall / (precision + recall)
        if f1 > best_f1:
            best_f1 = f1
            best_thr = thr
    return (best_thr, best_f1)
