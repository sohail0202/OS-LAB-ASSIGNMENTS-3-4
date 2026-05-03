# ============================================================
#  Lab Assignment - 3 | Task 4: Optimal Page Replacement
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# Optimal Page Replacement:
# Replace the page that will NOT be used for the LONGEST time in the future.
# This is a theoretical algorithm — it gives the minimum possible page faults.
# It's used as a BENCHMARK to compare other algorithms against.

def optimal(pages, num_frames):
    frames = []      # Stores pages currently in memory
    page_faults = 0  # Counter for page faults

    print("\n---- Optimal Page Replacement Simulation ----")
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
                # Memory is full → find which frame page is used FARTHEST in future
                farthest_use = -1
                page_to_replace = None

                for f in frames:
                    # Look ahead: when is this frame page used next?
                    future_uses = [j for j in range(i + 1, len(pages)) if pages[j] == f]

                    if not future_uses:
                        # This page is NEVER used again → replace it immediately
                        page_to_replace = f
                        break
                    else:
                        next_use = future_uses[0]
                        if next_use > farthest_use:
                            farthest_use = next_use
                            page_to_replace = f

                # Replace the chosen page
                frames[frames.index(page_to_replace)] = page

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

optimal(pages, num_frames)