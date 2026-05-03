# ============================================================
#  Lab Assignment - 4 | Task 1: Input and Disk Request Representation
#  Course: Fundamentals of Operating System Lab (ENCA252)
# ============================================================

# Task 1: Understand how disk requests are structured and taken as input.
# The disk head starts at a position and must service a list of cylinder requests.

# Step 1: Input number of disk requests
n = int(input("Enter number of disk requests: "))

# Step 2: Input the request sequence (cylinder numbers to be accessed)
req_input = input("Enter request sequence (space-separated cylinder numbers): ")
requests = list(map(int, req_input.split()))

# Step 3: Input initial head position (where the disk head starts)
head = int(input("Enter initial head position: "))

# Optional: Disk size (total number of cylinders, e.g., 200 for a 0–199 disk)
disk_size = int(input("Enter disk size (total cylinders, e.g. 200): "))

# Display everything clearly
print("\n---- Disk Scheduling Setup ----")
print(f"Number of Requests : {n}")
print(f"Request Queue      : {requests}")
print(f"Initial Head Pos   : {head}")
print(f"Disk Size          : {disk_size} cylinders (0 to {disk_size - 1})")
print("--------------------------------")
print("Input ready! Head will now move to service all requests.")