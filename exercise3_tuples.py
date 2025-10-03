"""
Exercise 3: Tuples in Medical Records (Healthcare Sector)
Topic: Python Tuples
Scenario: A hospital stores patient vitals as immutable records.
"""

print("=== Exercise 3: Python Tuples in Medical Records ===\n")

1: Create tuple for a patient

print("1. Patient record (tuple):")
patient_1 = ("John Doe", 45, "120/80", 72)
print("   Patient tuple:", patient_1)
print()

2: Access and print age and heart rate

print("2. Accessing patient data:")
age = patient_1[1]
heart_rate = patient_1[3]
print(f"   Age: {age}, Heart Rate: {heart_rate} bpm")
print()

3: Explain why tuples are suitable

print("3. Why tuples are suitable for patient vitals:")
print("   - Immutability: Prevents accidental modification of medical records")
print("   - Data Integrity: Ensures vitals remain unchanged once recorded")
print("   - Security: Protects sensitive patient data from alteration")
print("   - Hashability: Can be used as keys in dictionaries if needed")
print()

4: Convert to list, update, convert back

print("4. Updating heart rate (via list conversion):")
# Convert to list

patient_list = list(patient_1)
print("   Converted to list:", patient_list)
# Update heart rate

patient_list[3] = 75
print("   Updated heart rate in list:", patient_list)
# Convert back to tuple

patient_1_updated = tuple(patient_list)
print("   Converted back to tuple:", patient_1_updated)
print()

5: Create tuple of 5 patients and extract names

print("5. Multiple patients and name extraction:")
patients = (
    ("John Doe", 45, "120/80", 72),
    ("Jane Smith", 34, "110/70", 68),
    ("Bob Johnson", 67, "130/90", 80),
    ("Alice Brown", 29, "118/78", 70),
    ("Charlie Wilson", 52, "125/85", 76)
)

patient_names = [patient[0] for patient in patients]
print("   All patient names:", patient_names)
