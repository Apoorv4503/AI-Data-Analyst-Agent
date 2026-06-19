# Plotly is used for interactive charts
import plotly.express as px


class VisualizationAgent:

    # Constructor
    def __init__(self, dataframe):

        # Store dataframe
        self.df = dataframe

    # Create histogram
    def create_histogram(self, column):

        fig = px.histogram(
            self.df,
            x=column,
            title=f"Distribution of {column}"
        )

        return fig