# ============================================================
#  Lab Assignment - 3 | Task 1: Input and Page Reference String
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# Task 1: Take input from the user and display the page reference string

# Step 1: Input number of frames (physical memory slots available)
num_frames = int(input("Enter number of memory frames: "))

# Step 2: Input the page reference string (sequence of pages accessed)
page_input = input("Enter page reference string (space-separated numbers): ")
pages = list(map(int, page_input.split()))

# Step 3: Display the inputs clearly
print("\n---- Page Reference Setup ----")
print(f"Number of Frames : {num_frames}")
print(f"Total Pages      : {len(pages)}")
print(f"Page Reference   : {pages}")
print("------------------------------")
print("\nInput received successfully! Ready for simulation.")