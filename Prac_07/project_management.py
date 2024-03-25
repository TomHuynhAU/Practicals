# File: project_management.py

import datetime
from project import Project

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            data = line.strip().split('\t')
            projects.append(Project(*data))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}%\n")

def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")
    print_menu()

def filter_projects_by_date(projects, date_string):
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f"  {project}")
    print_menu()  # Add this line to display the menu again after filtering

def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, estimate, completion))
    print_menu()  # Add this line to display the menu again after adding the new project

def update_project(projects):
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    choice = int(input("Project choice: "))
    chosen_project = projects[choice]
    print(chosen_project)  # Print the chosen project details
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        chosen_project.update_completion(int(new_completion))
    if new_priority:
        chosen_project.update_priority(int(new_priority))
    print_menu()  # Add this line to display the menu again after updating

def print_menu():
    print("\n- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def main():
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {filename}")
    print_menu()  # Add this line to display the menu initially

    menu = {
        'l': load_projects,
        's': save_projects,
        'd': display_projects,
        'f': filter_projects_by_date,
        'a': add_new_project,
        'u': update_project
    }

    while True:
        choice = input(">>> ").lower()
        if choice == 'q':
            save_option = input("Would you like to save to projects.txt? ").lower()
            if save_option.startswith('y'):
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        elif choice in menu:
            if choice == 'l':
                filename = input("Enter filename: ")
            elif choice == 's':
                filename = input("Enter filename: ")
                menu[choice](filename, projects)
            elif choice == 'f':
                date_string = input("Show projects that start after date (dd/mm/yyyy): ")
                menu[choice](projects, date_string)
            else:
                menu[choice](projects)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
