from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path
import requests
from PIL import Image
import urllib.request
import io

def get_pixabay_key():
  # Get Parent dir
  parent_path = Path.cwd().parent.parent
  # Path to env file
  env_path = list(parent_path.glob("**/*.env"))[0]
  # Connect the path with your '.env' file name
  load_dotenv(env_path)
  return os.getenv("PIXABAY_API_KEY")

def display_image(img_url):
    # img_url = 'https://pixabay.com/get/g47b352380e4d608a311324e1cfad4d99f96fce593bb9d480e0e84f19c58ddd44678c05430fef7d3bbbc48ea275aba5eb6274d6ce69568cabe97d4f9687b9ba27_1280.jpg'
    response = requests.get(img_url)
    image_bytes = io.BytesIO(response.content)
    img = Image.open(image_bytes)
    img.show()
    
def save_image(img_url):
    # img_url = 'https://pixabay.com/get/g47b352380e4d608a311324e1cfad4d99f96fce593bb9d480e0e84f19c58ddd44678c05430fef7d3bbbc48ea275aba5eb6274d6ce69568cabe97d4f9687b9ba27_1280.jpg'
    # create file name with matching extension
    Path("saved_images").mkdir(parents=True, exist_ok=True)
    file_name = 'img' + os.path.splitext(img_url)[1]
    current_directory = Path.cwd()
    full_save_path = os.path.join(current_directory, 'saved_images')
    os.chdir(full_save_path)
    # urllib.urlretrieve(img_url, file_name)
    response = requests.get(img_url)
    file = open(file_name, "wb")
    file.write(response.content)
    file.close()

# Generate request to pull images data
base_url = "https://pixabay.com/api/"
PIXABAY_API_KEY = get_pixabay_key()
query_search = "geometry+shapes"
category = "geometric"
image_size = "1000"
amount_of_images_to_return = 200
# selected_order = # can be " "popular", "latest"
params = {
  'q': query_search,
  # 'category': category,
  'image_size': image_size,
  'per_page': amount_of_images_to_return,
  # 'order': selected_order
}
params = '&'.join([k if v is None else f"{k}={v}" for k, v in params.items()])
# url = f"{base_url}?key={PIXABAY_API_KEY}&{params}"
url = f"{base_url}?key={PIXABAY_API_KEY}"
response = requests.get(url, params).json()
img_url = response['hits'][0]['largeImageURL'] # In order to pick random image change the index between 0 - hits
# Save Image
save_image(img_url)
# Display Image
display_image(img_url)

# TODO: Create a dataframe of all urls
# Fields: img_id, img_url, source, relvant_tags
# TODO: Add QRNG support to fetch random image and generate matching target number

