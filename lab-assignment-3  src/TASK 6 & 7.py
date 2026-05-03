# ============================================================
#  Lab Assignment - 3 | Task 6 & 7: Comparison and Analysis
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# This file runs ALL four page replacement algorithms on the same input
# and compares their total page faults side by side.

from collections import deque


# ── FIFO ──────────────────────────────────────────────────
def fifo(pages, num_frames):
    frames, queue, faults = [], deque(), 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                oldest = queue.popleft()
                frames[frames.index(oldest)] = page
            queue.append(page)
    return faults


# ── LRU ───────────────────────────────────────────────────
def lru(pages, num_frames):
    frames, faults = [], 0
    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                lru_page = min(frames, key=lambda f: max(j for j in range(i) if pages[j] == f))
                frames[frames.index(lru_page)] = page
    return faults


# ── Optimal ───────────────────────────────────────────────
def optimal(pages, num_frames):
    frames, faults = [], 0
    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                farthest, replace = -1, None
                for f in frames:
                    future = [j for j in range(i + 1, len(pages)) if pages[j] == f]
                    next_use = future[0] if future else float('inf')
                    if next_use > farthest:
                        farthest, replace = next_use, f
                frames[frames.index(replace)] = page
    return faults


# ── MRU ───────────────────────────────────────────────────
def mru(pages, num_frames):
    frames, recent, faults = [], [], 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                mru_page = recent[-1]
                frames[frames.index(mru_page)] = page
                recent.remove(mru_page)
            recent.append(page)
        else:
            recent.remove(page)
            recent.append(page)
    return faults


# ── Comparison & Analysis ─────────────────────────────────
def compare_all(pages, num_frames):
    results = {
        "FIFO":    fifo(pages, num_frames),
        "LRU":     lru(pages, num_frames),
        "Optimal": optimal(pages, num_frames),
        "MRU":     mru(pages, num_frames),
    }

    print("\n" + "=" * 45)
    print("   Performance Comparison — Page Replacement")
    print("=" * 45)
    print(f"  {'Algorithm':<12} {'Page Faults':>12}")
    print("-" * 45)
    for algo, faults in results.items():
        print(f"  {algo:<12} {faults:>12}")
    print("-" * 45)

    best  = min(results, key=results.get)
    worst = max(results, key=results.get)
    print(f"\n  Best  : {best}  ({results[best]} faults)")
    print(f"  Worst : {worst} ({results[worst]} faults)")

    print("\n---- Result Analysis (Task 7) ----")
    print("  - Optimal gives the MINIMUM page faults (theoretical benchmark).")
    print("  - LRU closely matches Optimal in real systems.")
    print("  - FIFO is simple but suffers from Belady's Anomaly.")
    print("  - MRU is useful for cyclic/sequential workloads only.")
    print("  - For general use, LRU is the most practical algorithm.")


# ── Main ──────────────────────────────────────────────────
num_frames = int(input("Enter number of memory frames: "))
page_input = input("Enter page reference string (space-separated): ")
pages = list(map(int, page_input.split()))

print(f"\n  Frames    : {num_frames}")
print(f"  Reference : {pages}")

compare_all(pages, num_frames)