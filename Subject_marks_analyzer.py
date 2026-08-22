# Function to get subject marks from user
def get_subject_marks():
    # Collect subject names
    subjects = input("Enter subjects separated by commas (e.g., Math,English,Science): ").split(',')
    subjects = [subject.strip() for subject in subjects if subject.strip()]  # Strip extra whitespace and ignore empty subjects
    
    if not subjects:
        print("Error: No subjects provided. Please enter at least one subject.")
        return {}

    # Check for duplicate subjects
    if len(subjects) != len(set(subjects)):
        print("Error: Duplicate subjects detected.")
        return {}

    # Collect marks
    marks_str = input("Enter marks for each subject separated by spaces (e.g., 85 90 78): ").split()
    
    if not marks_str:
        print("Error: No marks provided. Please enter marks for each subject.")
        return {}

    # Validate number of subjects matches number of marks
    if len(subjects) != len(marks_str):
        print("Error: The number of subjects and marks do not match.")
        return {}

    # Convert marks to integers and validate range
    marks = []
    for mark in marks_str:
        try:
            mark_int = int(mark)
        except ValueError:
            print(f"Error: Invalid mark '{mark}' entered. Marks should be numeric.")
            return
        
        if mark_int > 100:
            print(f"Error: Mark {mark_int} is out of range. Marks should be between 0 and 100.")
            return
        
        marks.append(mark_int)
    
    # Create a dictionary from subjects and marks
    marks_dict = dict(zip(subjects, marks))
    return marks_dict

# Get subject marks from the user
marks_dict = get_subject_marks()

# Only perform calculations if marks_dict is not empty
if marks_dict:
    # Perform calculations
    total_marks = sum(marks_dict.values())
    average_marks = total_marks / len(marks_dict) if marks_dict else 0

    # Display results
    print("Marks per subject:")
    for subject, mark in marks_dict.items():
        print(f"{subject}: {mark}")

    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")

    # Additional note to the user
    print("Note: Please ensure the number of subjects and marks match and are separated by commas and spaces respectively.")
