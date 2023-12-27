import gradio as gr
import pandas as pd
from io import StringIO
from model_starter import model_pipeline
def analyze_file(file):
    # Perform analysis on the uploaded file (you can replace this with your own logic)
    try:
        # Use StringIO to convert the file content to a string-like object
        #file_content = file.read().decode('utf-8')
        df = pd.read_csv(file.name)
        result = model_pipeline(df)

        return result
    except Exception as e:
        result = {
            "error": f"Error processing the file: {str(e)}"
        }
        return "Wrong format or no file!"
    

# Define the Gradio interface
iface = gr.Interface(
    fn=analyze_file,  # Function to be called when the file is uploaded
    inputs=gr.File(),  # Use the File input component for file uploads
    outputs="text"  # Display the result as text
)


# Launch the Gradio app
iface.launch()