import requests
import zipfile
import os
import kaggle

def download_file_from_url(url, local_path):
    """
    Download a file from a direct URL and save it locally.
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()  # This will raise an exception if there is an error

    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"File downloaded successfully and saved to {local_path}")


def extract_zip(zip_path, extract_to):
    """
    Extract a zip file to a specified directory.

    Args:
    zip_path (str): The path to the zip file.
    extract_to (str): The directory to extract the files into.
    """
    # Ensure the target directory exists
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents into the directory
        zip_ref.extractall(extract_to)
        print(f"All files have been extracted to {extract_to}")


# Example command to download a dataset
# Replace 'username/dataset-name' with the actual path of the dataset on Kaggle
dataset_identifier = 'rmisra/news-category-dataset'

# Specify the path where you want to download the dataset
download_path = 'news-category-dataset'

# Download and unzip the dataset
kaggle.api.dataset_download_files(dataset_identifier, path=download_path, unzip=True)


url1 = 'https://www.dropbox.com/scl/fi/pp8gbi3j7lxlunucs93xu/all-the-news.db?rlkey=iy65g92gd7bsaligula1disfn&e=1&dl=1'
url2 = 'https://www.dropbox.com/scl/fi/ri2muuv85ri98odyi9fzn/all-the-news-2-1.zip?rlkey=8qeq5kpg5btk3vq5nbx2aojxx&e=1&dl=1'
url3='https://www.dropbox.com/scl/fi/pm4c66u0exyj0ihaxr95e/nytimes%20front%20page.csv?rlkey=7mus7otnczy9w9q8wr3bo52ga&e=1&dl=1'
# Local path where you want to save the file
local_path1 = 'all-the-news.db'
local_path2='all-the-news-2-1.zip'
local_path3='nytimes_front_page.csv'



download_file_from_url(url1, local_path1)
download_file_from_url(url2, local_path2)
download_file_from_url(url3, local_path3)
# Path to your zip file
zip_path = 'all-the-news-2-1.zip'

# Directory to extract the contents
extract_to = '.'

# Call the function to extract the zip file
extract_zip(zip_path, extract_to)
