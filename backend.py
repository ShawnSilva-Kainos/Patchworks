from openai import OpenAI
from azure.storage.blob import BlobServiceClient
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

# Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
# Instantiate the client
# Doesn't have to be OpenAI, depends where the API is hosted (eg Azure, AWS, OpenAI ect)
client = OpenAI(api_key=api_key)

# Define the assistant prompt
# This is the prompt that will be used to instruct the AI model on how to respond to the user's input.
# The prompt is designed to help the AI model understand the context and provide accurate and relevant responses.
assitant_prompt = """
You are a medical expert who specializes in identifying if an image is a type of rash and diagnosing different types of rashes . 
The definition of a rash is : Skin rashes can be red, inflamed, bumpy as well as dry, itchy or painful.
Use this definition for your analysis.
If there is no "Patient Feedback", assume it is NOT a rash but don't provide justfication if you think it is a rash.
You should provide a detailed analysis of the rash and a description of why you believe it is a rash and not another skin condition.
You may list multiple types of rashes for each image, maximum of 3 types per image.
Please use the image provided to make your diagnosis.
Please use the additional information given by the 'Patient Feedback' to help make your diagnosis.
Your response should be clear and concise, using medical terminology where appropriate. 
Return your response in a JSON format with the following keys:
- Rash: A boolean indicating whether you believe it is a rash or not.
- Rash Type: The type of rash you believe it is.
- Description: A detailed description of the rash and its symptoms.
- Justification: Justify your answer
- Confidence: A confidence score from 0 to 100 indicating how sure you are about the diagnosis.
Please only respond with the JSON. Do not respond with any other text.
"""


def api_response(url):
    """
    This function takes a URL as input and returns the response from the OpenAI API.
    Args:
        url (str): The URL of the image to be analyzed.
    Returns:
        str: The response from the OpenAI API in JSON format.
    """
    response = client.responses.create(
        # Can use any model that supports image input
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": assitant_prompt},
                    {
                        "type": "input_image",
                        "image_url": url,
                    },
                ],
            }
        ],
    )

    return response.output[0].content[0].text


def api_response_symptoms(url, symptoms):
    """
    This function takes a URL and symptoms as input and returns the response from the OpenAI API.
    Args:
        url (str): The URL of the image to be analyzed.
        symptoms (str): The symptoms provided by the user.
    Returns:
        str: The response from the OpenAI API in JSON format.
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": assitant_prompt},
                    {
                        "type": "input_image",
                        "image_url": url,
                    },
                    {
                        "type": "input_text",
                        "text": "Patient Feedback: " + symptoms,
                    },
                ],
            }
        ],
    )
    return response.output[0].content[0].text


# If you want to Automate this process by accessing the Azure blob storage account and reading the image from the blob


def get_jpeg_urls_from_folder(
    AZURE_STORAGE_CONTAINER_NAME,
    folder_path,
    AZURE_STORAGE_CONNECTION_STRING,
    AZURE_STORAGE_BLOB_NAME,
):
    #     """
    #     Retrieves URLs of JPEG images stored in a specified folder in Azure Blob Storage.

    #     Args:
    #         container_name (str): The name of the Azure Blob container.
    #         folder_path (str): The path to the virtual folder inside the container (e.g., 'images/folder1/').
    #         connection_string (str): Azure Storage account connection string.

    #     Returns:
    #         List[str]: A list of URLs pointing to JPEG files.
    #     """
    jpeg_urls = []

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(
        AZURE_STORAGE_CONNECTION_STRING
    )

    # Get container client
    container_client = blob_service_client.get_container_client(
        AZURE_STORAGE_CONTAINER_NAME
    )

    # List blobs in the specified folder
    blob_list = container_client.list_blobs(name_starts_with=folder_path)

    for blob in blob_list:
        if blob.name.lower().endswith(".jpg") or blob.name.lower().endswith(".jpeg"):
            blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{AZURE_STORAGE_CONTAINER_NAME}/{AZURE_STORAGE_BLOB_NAME}"
            jpeg_urls.append(blob_url)

    return jpeg_urls
