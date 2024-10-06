import os
import sys
import requests
import pyperclip

def upload_image(image_path):
    url = "图床上传接口xxxxx"
    
    if not os.path.isfile(image_path):
        print("Error: File does not exist.")
        return None
    
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        try:
            response = requests.post(url, files=files)
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    print(f"Response JSON: {result}")
                    
                    image_url = result.get('data') 
                    if image_url:
                        return image_url
                    else:
                        print("Error: No URL found in 'data' field.")
                        return None
                except ValueError:
                    print(f"Response is not JSON: {response.text}")
                    return None
            else:
                print(f"Failed to upload. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")
            return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload_image.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    image_url = upload_image(image_path)
    
    if image_url:
        pyperclip.copy(image_url)
        print("Image URL copied to clipboard!")
        print(image_url)
    else:
        print("Upload failed.")
