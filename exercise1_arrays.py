"""
Exercise 1: Arrays in Financial Analytics (Banking Sector)
Topic: NumPy Arrays
Scenario: A bank wants to analyze monthly transaction volumes across its branches.
"""

import numpy as np

print("=== Exercise 1: NumPy Arrays in Financial Analytics ===\n")

Task 1: Create 2D array for 4 branches over 6 months

print("1. Transaction volumes for 4 branches over 6 months:")
transaction_volumes = np.array([
    [120, 150, 130, 145, 160, 110],  # Branch 1
    [90, 95, 105, 115, 100, 120],    # Branch 2
    [200, 210, 190, 220, 230, 240],  # Branch 3
    [80, 85, 90, 95, 100, 105]       # Branch 4
])
print(transaction_volumes)
print(f"Array shape: {transaction_volumes.shape}\n")

Task 2: Calculate total transactions per branch

print("2. Total transactions per branch:")
total_per_branch = np.sum(transaction_volumes, axis=1)
for i, total in enumerate(total_per_branch):
    print(f"   Branch {i+1}: {total} transactions")
print()

Task 3: Identify branch with highest total transactions

print("3. Branch with highest transactions:")
highest_branch_index = np.argmax(total_per_branch)
print(f"   Branch {highest_branch_index + 1} has the highest total: {total_per_branch[highest_branch_index]} transactions\n")

4: Compute average monthly transaction volume

print("4. Average monthly transaction volume:")
average_monthly = np.mean(transaction_volumes)
print(f"   Average across all branches and months: {average_monthly:.2f}\n")
