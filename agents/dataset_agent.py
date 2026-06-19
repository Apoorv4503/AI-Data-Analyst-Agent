# Import pandas library
# Pandas is used to read and analyze datasets
import pandas as pd


# DatasetAgent is responsible for:
# 1. Loading datasets
# 2. Understanding datasets
# 3. Providing metadata to other agents
class DatasetAgent:

    # Constructor
    # Runs automatically when an object is created
    def __init__(self, file_path):

        # Store the dataset path
        self.file_path = file_path

        # Placeholder for DataFrame
        # Initially no dataset is loaded
        self.df = None

    # Function to load dataset
    def load_dataset(self):

        # Check if file is CSV
        if self.file_path.endswith(".csv"):

            # Read CSV file into DataFrame
            self.df = pd.read_csv(self.file_path)

        # Check if file is Excel
        elif self.file_path.endswith(".xlsx"):

            # Read Excel file into DataFrame
            self.df = pd.read_excel(self.file_path)

        # Return loaded DataFrame
        return self.df
        # Function to generate dataset summary
    def get_dataset_summary(self):

        # Create a dictionary containing dataset information
        summary = {

            # Total number of rows
            "rows": self.df.shape[0],

            # Total number of columns
            "columns": self.df.shape[1],

            # List of column names
            "column_names": list(self.df.columns),

            # Data type of each column
            "data_types": self.df.dtypes.astype(str).to_dict(),

            # Missing values in each column
            "missing_values": self.df.isnull().sum().to_dict()
        }

        # Return dataset summary
        return summary
    
    # Get numeric columns
    def get_numeric_columns(self):

     return list(
        self.df.select_dtypes(
            include=["int64", "float64"]
        ).columns
    )

# Get categorical columns
    def get_categorical_columns(self):

     return list(
        self.df.select_dtypes(
            include=["object", "string"]
        ).columns
    )
    