# Project Name
Patchwork - Upload your rash
Digital UEC & IUC Hackathon 2025 - Accenture and Kainos

Any questions or concerns, please contact me at [shawn.silva@kainos.com] (via Teams if possible).
## Description
This project is focused on analyzing and experimenting with healthcare data to derive meaningful insights. It includes a Jupyter Notebook that experiments with various skin condition images and some prompt engineering to demonstrate the effectiveness of the system. This work initially is focused on identifying patterns and trends in skin conditions that could be identified as a 'rash'. This however can be expanded to have the capability to identify various different skin conditions. 

The goal is to support decision-making and innovation in healthcare through data-driven approaches.

### Next Steps
- Expand the project to include other skin conditions and analyze their patterns and trends.
- Integrate the project with a healthcare platform to enable real-time analysis and decision-making.
- Conduct further research and analysis to identify potential areas for improvement and innovation.
- Develop a RAG model to ensure identified conditions are in line with NHS guidelines.

## Features
rash_experiment_notebook
    - Experimental Jupyter notebook that identified improving the context, input and prompt improved the output

frontend.py
    - Frontend for the project that takes in a image URL and returns a JSON object with the predicted skin condition
    - The frontend is built using Streamlit, which allows for easy deployment and customization.

rash_dataset folder
    - Folder containing the rash dataset, which includes various skin conditions and their corresponding images.

## Installation
To install the project, use `pip`:
```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

## Running the app
To run the app, use the following command:
```bash
    streamlit run frontend.py
```


