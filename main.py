# Create list of students in global scope to be used in later functions
students = [{"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
  {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
  {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]

# Define function to print the name and index number of each student
def list_names(student_list):
  # Iterate through each student, printing name and position in the provided list
  for student in student_list:
    print(str((student_list.index(student)+1)) + ". " + student.get("name"))

def prompt_for_action():
  # Allows user to choose which action they wish to take; returns this value for use in other functions
  while True:
    selected_action = input("Please select which action you'd like to do: add, view, or quit ")
    selected_action = selected_action.upper()
    # Checks if user input is a valid response. If so, returns the response. If not, prompts the user to try again.
    if selected_action.upper() not in ['ADD', 'VIEW', 'QUIT']:
      print("I'm sorry, that option does not exist. Please try again. Enter 'add', 'view' or 'quit'")
    elif selected_action.upper() == "QUIT":
      break
    else:
      return selected_action


def view_student():
  while True:
    student_to_view = int(input(f"Which student would you like to learn more about? Enter a number 1-{len(students)}:"))
    if student_to_view not in range(len(students)+1):
      print("I'm sorry, there is currently no student with that number. Please try again.")
    else:
      current_student = students[student_to_view-1]
      student_details(current_student)
      break
def student_details(student):
  while True:
    print(f"Student {students.index(student)+1} is {student.get('name')}. What would you like to know?")
    category_selection = input("Enter 'hometown' or 'favorite food' ")

    if category_selection.upper() not in ['HOMETOWN', 'FAVORITE FOOD']:
      print("I'm sorry, that is not a valid category, please try again.")
    elif category_selection.upper() == 'HOMETOWN':
      print(f"{student.get('name')} is from {student.get('hometown')}")
      break
    else:
      print(f"{student.get('name')}'s favorite food is {student.get('favorite_food')}")
      break


def get_new_student():
  new_student = {"name": "", "hometown": "", "favorite_food": ""}
  new_student["name"] = input("Please input a name for the new student: ")
  new_student["hometown"] = input("Next please input their hometown: ")
  new_student["favorite_food"] = input("Last please input their favorite food: ")
  students.append(new_student)

def main_program():
  while True:
    n = prompt_for_action()

    if n == None:
      print("Good bye!")
      break

    elif n == "VIEW":
      list_names(students)
      view_student()
    else:
      get_new_student()



if __name__ == "__main__":
  main_program()
