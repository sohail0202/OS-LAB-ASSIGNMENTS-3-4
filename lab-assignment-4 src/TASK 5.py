# ============================================================
#  Lab Assignment - 4 | Task 5: C-SCAN Disk Scheduling
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# C-SCAN (Circular SCAN):
# Like SCAN, the head moves in ONE direction only (right).
# But instead of reversing, it JUMPS back to cylinder 0 and continues.
# This gives MORE UNIFORM wait times — no request has to wait for a full sweep.

def cscan(requests, head, disk_size):
    seek_time = 0
    current = head
    sequence = [head]

    # Separate requests: left side and right side of head
    left  = sorted([r for r in requests if r < head])   # sorted low→high
    right = sorted([r for r in requests if r >= head])   # sorted low→high

    print("\n---- C-SCAN Disk Scheduling Simulation ----")
    print(f"{'Step':<6} {'From':<8} {'To':<8} {'Distance'} {'Note'}")
    print("-" * 60)

    step = 1

    # Phase 1: Move RIGHT — service all requests to the right of head
    for req in right:
        distance = abs(current - req)
        seek_time += distance
        print(f"{step:<6} {current:<8} {req:<8} {distance:<10} →")
        current = req
        sequence.append(current)
        step += 1

    # Go to the last cylinder (end of disk)
    distance = abs(current - (disk_size - 1))
    seek_time += distance
    print(f"{step:<6} {current:<8} {disk_size-1:<8} {distance:<10} → (reach end)")
    current = disk_size - 1
    sequence.append(current)
    step += 1

    # Jump back to cylinder 0 (circular jump — no requests serviced during jump)
    jump_distance = disk_size - 1
    seek_time += jump_distance
    print(f"{step:<6} {current:<8} {0:<8} {jump_distance:<10} ↩ (circular jump to 0)")
    current = 0
    sequence.append(current)
    step += 1

    # Phase 2: Continue RIGHT from 0 — service remaining requests on left side
    for req in left:
        distance = abs(current - req)
        seek_time += distance
        print(f"{step:<6} {current:<8} {req:<8} {distance:<10} →")
        current = req
        sequence.append(current)
        step += 1

    print("-" * 60)
    print(f"\nHead Movement  : {' → '.join(map(str, sequence))}")
    print(f"Total Seek Time: {seek_time} cylinders")
    return seek_time


# ---- Main ----
req_input = input("Enter request sequence (space-separated): ")
requests = list(map(int, req_input.split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size (e.g. 200): "))

cscan(requests, head, disk_size)