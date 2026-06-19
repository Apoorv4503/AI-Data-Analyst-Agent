# Streamlit library
import streamlit as st

# Import Dataset Agent
from agents.dataset_agent import DatasetAgent

# Import File Handler
from utils.file_handler import save_uploaded_file


# Page Title
st.title("AI Data Analyst Agent")


# Page Description
st.write(
    "Upload a CSV or Excel file and let the AI understand your dataset."
)


# File Upload Widget
uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"]
)


# Run only if file uploaded
if uploaded_file:

    # Save uploaded file
    file_path = save_uploaded_file(uploaded_file)

    # Create Dataset Agent
    agent = DatasetAgent(file_path)

    # Load Dataset
    df = agent.load_dataset()

    # Get Dataset Summary
    summary = agent.get_dataset_summary()

    # Show Dataset Summary
    st.subheader("Dataset Summary")

    st.write(f"Rows: {summary['rows']}")
    st.write(f"Columns: {summary['columns']}")

    # Show Column Names
    st.subheader("Column Names")
    st.write(summary["column_names"])

    # Show Data Types
    st.subheader("Data Types")
    st.write(summary["data_types"])

    # Show Missing Values
    st.subheader("Missing Values")
    st.write(summary["missing_values"])

    # Show Numeric Columns
    st.subheader("Numeric Columns")
    st.write(agent.get_numeric_columns())

    # Show Categorical Columns
    st.subheader("Categorical Columns")
    st.write(agent.get_categorical_columns())