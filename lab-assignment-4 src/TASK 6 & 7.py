# ============================================================
#  Lab Assignment - 4 | Task 6 & 7: Comparison and Analysis
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# This file runs ALL four disk scheduling algorithms on the same input
# and compares total seek time to identify the best algorithm.


# ── FCFS ──────────────────────────────────────────────────
def fcfs(requests, head):
    seek_time, current = 0, head
    for req in requests:
        seek_time += abs(current - req)
        current = req
    return seek_time


# ── SSTF ──────────────────────────────────────────────────
def sstf(requests, head):
    seek_time, current = 0, head
    remaining = requests.copy()
    while remaining:
        nearest = min(remaining, key=lambda x: abs(x - current))
        seek_time += abs(current - nearest)
        current = nearest
        remaining.remove(nearest)
    return seek_time


# ── SCAN ──────────────────────────────────────────────────
def scan(requests, head, disk_size):
    seek_time, current = 0, head
    left  = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])
    for r in right:
        seek_time += abs(current - r); current = r
    seek_time += abs(current - (disk_size - 1)); current = disk_size - 1
    for r in left:
        seek_time += abs(current - r); current = r
    return seek_time


# ── C-SCAN ────────────────────────────────────────────────
def cscan(requests, head, disk_size):
    seek_time, current = 0, head
    left  = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    for r in right:
        seek_time += abs(current - r); current = r
    seek_time += abs(current - (disk_size - 1)); current = disk_size - 1
    seek_time += disk_size - 1; current = 0
    for r in left:
        seek_time += abs(current - r); current = r
    return seek_time


# ── Comparison & Analysis ─────────────────────────────────
def compare_all(requests, head, disk_size):
    results = {
        "FCFS":   fcfs(requests, head),
        "SSTF":   sstf(requests, head),
        "SCAN":   scan(requests, head, disk_size),
        "C-SCAN": cscan(requests, head, disk_size),
    }

    print("\n" + "=" * 45)
    print("   Performance Comparison — Disk Scheduling")
    print("=" * 45)
    print(f"  {'Algorithm':<10} {'Seek Time (cylinders)':>22}")
    print("-" * 45)
    for algo, time in results.items():
        print(f"  {algo:<10} {time:>22}")
    print("-" * 45)

    best  = min(results, key=results.get)
    worst = max(results, key=results.get)
    print(f"\n  Best  : {best}  ({results[best]} cylinders)")
    print(f"  Worst : {worst} ({results[worst]} cylinders)")

    print("\n---- Result Analysis (Task 7) ----")
    print("  - FCFS: Simple but highly inefficient for scattered requests.")
    print("  - SSTF: Reduces seek time but risks starvation of far requests.")
    print("  - SCAN: Balanced & fair; like elevator, no request waits too long.")
    print("  - C-SCAN: Most uniform wait time; better than SCAN for heavy loads.")
    print(f"\n  Recommendation: '{best}' performed best for this input.")
    print("  In practice, SCAN or C-SCAN are preferred for real disk systems.")


# ── Main ──────────────────────────────────────────────────
req_input = input("Enter request sequence (space-separated): ")
requests = list(map(int, req_input.split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size (e.g. 200): "))

print(f"\n  Requests  : {requests}")
print(f"  Head      : {head}")
print(f"  Disk Size : {disk_size}")

compare_all(requests, head, disk_size)