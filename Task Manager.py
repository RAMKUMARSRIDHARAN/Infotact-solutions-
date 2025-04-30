import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    data = {
        "Task ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "Task Description": [
            "Fix login issue", "Update landing page UI", "Deploy new release", "Write API documentation", 
            "Set up monitoring alerts", "Optimize SQL queries", "Patch security bug", "Create user onboarding flow",
            "Test checkout functionality", "Update project roadmap", "Refactor authentication module", 
            "Perform load testing", "Implement role-based access", "Backup production DB", "Prepare release notes"
        ],
        "Category": [
            "Backend", "Frontend", "DevOps", "Documentation", "DevOps", "Database", "Security", "Frontend", 
            "QA", "Project Management", "Backend", "QA", "Security", "Database", "Documentation"
        ],
        "Priority": [
            "High", "Medium", "High", "Low", "Medium", "High", "High", "Medium", "High", "Low", "Medium", "Medium",
            "High", "High", "Low"
        ],
        "Deadline": [
            "2025-05-01", "2025-05-02", "2025-05-03", "2025-05-04", "2025-05-05", "2025-05-06", "2025-05-07", 
            "2025-05-08", "2025-05-09", "2025-05-10", "2025-05-01", "2025-05-02", "2025-05-03", "2025-05-04", 
            "2025-05-05"
        ],
        "Status": [
            "In Progress", "Pending", "Pending", "Completed", "In Progress", "Pending", "In Progress", "Pending", 
            "Pending", "Completed", "Pending", "In Progress", "Pending", "Completed", "Pending"
        ]
    }
    return pd.DataFrame(data)

# Main app function
def main():
    st.title("Task Management System")
    
    # Load the dataset
    df = load_data()
    
    # Show the dataset
    st.subheader("Task List")
    st.dataframe(df)

    # Filter options
    category_filter = st.selectbox('Select Category', df['Category'].unique())
    status_filter = st.selectbox('Select Task Status', df['Status'].unique())
    
    # Filter the data based on user inputs
    filtered_df = df[(df['Category'] == category_filter) & (df['Status'] == status_filter)]
    st.subheader(f"Tasks in Category: {category_filter} and Status: {status_filter}")
    st.dataframe(filtered_df)
    
    # Sentiment Analysis on Task Descriptions
    st.subheader("Sentiment Analysis (Prioritize Tasks)")
    task_description = st.text_area("Enter a task description to get its sentiment:")
    if task_description:
        sentiment = "Positive" if "fix" in task_description.lower() or "improve" in task_description.lower() else "Negative"
        st.write(f"The sentiment of the task is: {sentiment}")
    
    # Prioritize tasks based on Sentiment (Simple prioritization logic)
    priority_filter = st.selectbox('Filter tasks by priority', df['Priority'].unique())
    prioritized_df = df[df['Priority'] == priority_filter]
    st.subheader(f"Prioritized Tasks with {priority_filter} Priority")
    st.dataframe(prioritized_df)
    
if __name__ == "__main__":
    main()
