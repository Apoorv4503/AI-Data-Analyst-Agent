# Import DatasetAgent
from agents.dataset_agent import DatasetAgent


# Create agent object
agent = DatasetAgent("data/sample_sales.csv")


# Load dataset
df = agent.load_dataset()


# Get summary
summary = agent.get_dataset_summary()


# Print summary
print(summary)

# Get numeric columns
print("\nNumeric Columns:")
print(agent.get_numeric_columns())

# Get categorical columns
print("\nCategorical Columns:")
print(agent.get_categorical_columns())