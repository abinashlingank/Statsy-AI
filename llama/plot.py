
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the data.csv file
data = pd.read_csv("data.csv")

# Define the directory where the plots will be saved
output_dir = "output"

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define a function to create a plot and save it to a file
def create_plot(data, title, x_axis, y_axis, file_name):
    # Create a figure and axis object
    fig, ax = plt.subplots()
    
    # Plot the data
    ax.plot(data[x_axis], data[y_axis])
    
    # Add a title and labels
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    
    # Save the plot to a file
    plt.savefig(os.path.join(output_dir, file_name))
    
    # Close the figure
    plt.close()

# Define the list of possible plots
plots = [
    ("Employee_Name", "EmpID", "MarriedID"),
    ("Employee_Name", "EmpID", "MaritalStatusID"),
    ("MaritalStatusID", "GenderID", "EmpStatusID"),
    ("EmpID", "DeptID", "PerfScoreID"),
    ("Employee_Name", "EmpID", "FromDiversityJobFairID"),
    ("Employee_Name", "EmpID", "Salary"),
    ("Employee_Name", "EmpID", "Termd"),
    ("Employee_Name", "PositionID", "Position"),
    ("Employee_Name", "Department", "ManagerName"),
    ("Employee_Name", "Department", "ManagerID"),
    ("Employee_Name", "Department", "RecruitmentSource"),
    ("Employee_Name", "Department", "PerformanceScore"),
    ("Employee_Name", "Department", "EngagementSurvey"),
    ("Employee_Name", "Department", "EmpSatisfaction"),
    ("Employee_Name", "Department", "SpecialProjectsCount"),
    ("Employee_Name", "Department", "DaysLateLast30"),
    ("Employee_Name", "Department", "Absences")
]

# Loop through the list of plots and create each one
for plot in plots:
    create_plot(data, plot[0], plot[1], plot[2], plot[0] + "_" + plot[1] + "_" + plot[2] + ".png")
