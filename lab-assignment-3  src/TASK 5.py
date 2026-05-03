# ============================================================
#  Lab Assignment - 3 | Task 5: MRU Page Replacement
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# MRU (Most Recently Used):
# The page that was used MOST RECENTLY is replaced first.
# This is the opposite of LRU. It works well in specific patterns
# like cyclic access (e.g., databases scanning large sequential data).

def mru(pages, num_frames):
    frames = []   # Stores pages currently in memory
    recent = []   # Tracks usage order; most recent is at the END
    page_faults = 0

    print("\n---- MRU Page Replacement Simulation ----")
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
                # Memory is full → replace the MOST RECENTLY USED page
                mru_page = recent[-1]                      # Last item = most recent
                frames[frames.index(mru_page)] = page      # Replace it
                recent.remove(mru_page)                    # Remove from recency list

            recent.append(page)   # Add new page as most recent
            status = "PAGE FAULT"
        else:
            # Page IS in memory → Hit
            # Update recency: move this page to the most recent position
            recent.remove(page)
            recent.append(page)
            status = "Hit"

        print(f"{page:<6} {str(list(frames)):<30} {status}")

    print("-" * 50)
    print(f"Total Page Faults: {page_faults}")
    return page_faults


# ---- Main ----
num_frames = int(input("Enter number of memory frames: "))
page_input = input("Enter page reference string (space-separated): ")
pages = list(map(int, page_input.split()))

mru(pages, num_frames)