# ============================================================
#  Lab Assignment - 3 | Task 2: FIFO Page Replacement
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# FIFO (First In First Out):
# The page that came into memory FIRST is replaced first.
# Think of it like a queue — oldest page leaves when memory is full.

from collections import deque  # deque helps track insertion order efficiently

def fifo(pages, num_frames):
    frames = []       # Stores pages currently in memory
    queue = deque()   # Tracks the order pages were inserted
    page_faults = 0   # Counter for page faults

    print("\n---- FIFO Page Replacement Simulation ----")
    print(f"{'Page':<6} {'Frames':<30} {'Status'}")
    print("-" * 50)

    for page in pages:
        if page not in frames:
            # Page is NOT in memory → PAGE FAULT
            page_faults += 1

            if len(frames) < num_frames:
                # Memory has space, just add the page
                frames.append(page)
            else:
                # Memory is full → remove the OLDEST page (front of queue)
                oldest = queue.popleft()
                frames[frames.index(oldest)] = page

            queue.append(page)  # Record this page's insertion time
            status = "PAGE FAULT"
        else:
            # Page IS in memory → Hit (no fault)
            status = "Hit"

        print(f"{page:<6} {str(list(frames)):<30} {status}")

    print("-" * 50)
    print(f"Total Page Faults: {page_faults}")
    return page_faults


# ---- Main ----
num_frames = int(input("Enter number of memory frames: "))
page_input = input("Enter page reference string (space-separated): ")
pages = list(map(int, page_input.split()))

fifo(pages, num_frames)