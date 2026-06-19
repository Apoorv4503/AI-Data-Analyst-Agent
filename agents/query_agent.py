# Query Agent
# Responsible for understanding questions
# and returning answers

class QueryAgent:

    # Constructor
    def __init__(self, dataframe):

        # Store dataframe
        self.df = dataframe

    # Main Question Answering Function
    def answer_question(self, question):

        # Convert question to lowercase
        question = question.lower()

        # Number of rows
        if "row" in question:

            return f"Total Rows = {self.df.shape[0]}"

        # Number of columns
        elif "column" in question:

            return f"Total Columns = {self.df.shape[1]}"

        # Column names
        elif "column names" in question or "columns" in question:

            return list(self.df.columns)

        # Missing values
        elif "missing" in question:

            return self.df.isnull().sum().to_dict()

        # Unknown question
        else:

            return "Sorry, I don't understand that question yet."