# ============================================================
#  Lab Assignment - 4 | Task 4: SCAN Disk Scheduling
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# SCAN (Elevator Algorithm):
# The disk head moves in ONE direction, servicing all requests along the way.
# When it reaches the END of the disk, it REVERSES direction and services
# requests on the way back.
# This is just like an elevator — it goes up, reaches the top, then comes down.

def scan(requests, head, disk_size):
    seek_time = 0
    current = head
    sequence = [head]

    # Separate requests into left side and right side of current head
    left  = sorted([r for r in requests if r < head], reverse=True)  # sorted high→low
    right = sorted([r for r in requests if r >= head])                # sorted low→high

    print("\n---- SCAN (Elevator) Disk Scheduling Simulation ----")
    print(f"{'Step':<6} {'From':<8} {'To':<8} {'Distance'} {'Direction'}")
    print("-" * 55)

    step = 1

    # Phase 1: Move RIGHT — service all requests to the right of head
    for req in right:
        distance = abs(current - req)
        seek_time += distance
        print(f"{step:<6} {current:<8} {req:<8} {distance:<10} →")
        current = req
        sequence.append(current)
        step += 1

    # Go all the way to the last cylinder (end of disk)
    distance = abs(current - (disk_size - 1))
    seek_time += distance
    print(f"{step:<6} {current:<8} {disk_size - 1:<8} {distance:<10} → (end of disk)")
    current = disk_size - 1
    sequence.append(current)
    step += 1

    # Phase 2: Move LEFT — service all requests to the left of original head
    for req in left:
        distance = abs(current - req)
        seek_time += distance
        print(f"{step:<6} {current:<8} {req:<8} {distance:<10} ←")
        current = req
        sequence.append(current)
        step += 1

    print("-" * 55)
    print(f"\nHead Movement  : {' → '.join(map(str, sequence))}")
    print(f"Total Seek Time: {seek_time} cylinders")
    return seek_time


# ---- Main ----
req_input = input("Enter request sequence (space-separated): ")
requests = list(map(int, req_input.split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size (e.g. 200): "))

scan(requests, head, disk_size)