# Import os library
import os


# Function to save uploaded file
def save_uploaded_file(uploaded_file):

    # Create save path
    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    # Save file into uploads folder
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Return saved file path
    return save_path
