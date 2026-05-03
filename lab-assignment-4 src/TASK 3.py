# ============================================================
#  Lab Assignment - 4 | Task 3: SSTF Disk Scheduling
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# SSTF (Shortest Seek Time First):
# At each step, the head moves to the CLOSEST unserviced request.
# This reduces total seek time compared to FCFS.
# Downside: requests far from the head may be "starved" (never serviced).

def sstf(requests, head):
    seek_time = 0
    current = head
    remaining = requests.copy()   # Work on a copy so original is unchanged
    sequence = [head]

    print("\n---- SSTF Disk Scheduling Simulation ----")
    print(f"{'Step':<6} {'From':<8} {'To':<8} {'Distance'}")
    print("-" * 40)

    step = 1
    while remaining:
        # Find the nearest request to current head position
        nearest = min(remaining, key=lambda x: abs(x - current))
        distance = abs(current - nearest)
        seek_time += distance

        print(f"{step:<6} {current:<8} {nearest:<8} {distance}")

        current = nearest          # Move head to nearest request
        sequence.append(current)
        remaining.remove(nearest)  # Mark this request as serviced
        step += 1

    print("-" * 40)
    print(f"\nHead Movement  : {' → '.join(map(str, sequence))}")
    print(f"Total Seek Time: {seek_time} cylinders")
    return seek_time


# ---- Main ----
req_input = input("Enter request sequence (space-separated): ")
requests = list(map(int, req_input.split()))
head = int(input("Enter initial head position: "))

sstf(requests, head)