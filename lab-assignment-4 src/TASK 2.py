# ============================================================
#  Lab Assignment - 4 | Task 2: FCFS Disk Scheduling
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# FCFS (First Come First Serve):
# Disk requests are serviced in the EXACT ORDER they arrive.
# Simple to implement but can result in large total seek time
# if requests are scattered far apart.

def fcfs(requests, head):
    seek_time = 0    # Total distance the head travels
    current = head   # Current head position
    sequence = [head]  # Track every position head visits (for display)

    print("\n---- FCFS Disk Scheduling Simulation ----")
    print(f"{'Step':<6} {'From':<8} {'To':<8} {'Distance'}")
    print("-" * 40)

    for step, req in enumerate(requests, start=1):
        distance = abs(current - req)   # Distance to move to this request
        seek_time += distance
        print(f"{step:<6} {current:<8} {req:<8} {distance}")
        current = req                   # Move head to this request
        sequence.append(current)

    print("-" * 40)
    print(f"\nHead Movement  : {' → '.join(map(str, sequence))}")
    print(f"Total Seek Time: {seek_time} cylinders")
    return seek_time


# ---- Main ----
req_input = input("Enter request sequence (space-separated): ")
requests = list(map(int, req_input.split()))
head = int(input("Enter initial head position: "))

fcfs(requests, head)