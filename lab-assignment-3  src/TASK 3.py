# ============================================================
#  Lab Assignment - 3 | Task 3: LRU Page Replacement
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# LRU (Least Recently Used):
# The page that has NOT been used for the LONGEST time is replaced.
# This uses the concept of "temporal locality" — recently used pages
# are likely to be used again soon.

def lru(pages, num_frames):
    frames = []      # Stores pages currently in memory
    page_faults = 0  # Counter for page faults

    print("\n---- LRU Page Replacement Simulation ----")
    print(f"{'Page':<6} {'Frames':<30} {'Status'}")
    print("-" * 50)

    for i, page in enumerate(pages):
        if page not in frames:
            # Page is NOT in memory → PAGE FAULT
            page_faults += 1

            if len(frames) < num_frames:
                # Memory has space, just add the page
                frames.append(page)
            else:
                # Memory is full → find the Least Recently Used page
                # Look backwards through pages[0..i-1] for each frame page
                lru_page = None
                lru_time = float('inf')  # We want the smallest (earliest) last-use index

                for f in frames:
                    # Find the last time this frame page was used before index i
                    last_used = max(j for j in range(i) if pages[j] == f)
                    if last_used < lru_time:
                        lru_time = last_used
                        lru_page = f

                # Replace the LRU page with the new page
                frames[frames.index(lru_page)] = page

            status = "PAGE FAULT"
        else:
            status = "Hit"

        print(f"{page:<6} {str(list(frames)):<30} {status}")

    print("-" * 50)
    print(f"Total Page Faults: {page_faults}")
    return page_faults


# ---- Main ----
num_frames = int(input("Enter number of memory frames: "))
page_input = input("Enter page reference string (space-separated): ")
pages = list(map(int, page_input.split()))

lru(pages, num_frames)