# =================================================================================================
# Azure OpenAI Image Generation - Python Starter Script
#
# This script shows how to call a backend API that uses Azure OpenAI's DALL-E model
# to generate an image based on a text prompt.
#
# Prerequisites:
# 1. Python installed (version 3.6 or higher)
# 2. The 'requests' library installed: pip install requests
# 3. A backend API endpoint that accepts a POST request with a 'prompt' and returns
#    a JSON object containing a base64-encoded image string under the key 'photo'.
# =================================================================================================

import requests
import json
import base64
import os

# =================================================================================================
# STEP 1: REPLACE THIS WITH YOUR ACTUAL BACKEND ENDPOINT
# The user provided this example endpoint:
API_ENDPOINT = "https://ai-image-generation-backend-ixhr.onrender.com/api/v1/dalle"
# =================================================================================================

def generate_image(prompt: str):
    """
    Calls the image generation API and saves the resulting image.

    :param prompt: The text description of the image to generate.
    """
    print(f"--- Starting Image Generation ---")
    print(f"Prompt: '{prompt}'")
    print(f"API Endpoint: {API_ENDPOINT}")

    # The data we are sending to the API
    payload = {
        "prompt": prompt
    }

    try:
        # STEP 2: Make the POST request to the API
        response = requests.post(
            API_ENDPOINT,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        # Check if the request was successful (HTTP status code 200)
        response.raise_for_status()

        # STEP 3: Parse the JSON response
        data = response.json()

        # STEP 4: Check for the base64 image data
        if "photo" in data:
            base64_image = data["photo"]
            
            # STEP 5: Decode the base64 string to get the raw image bytes
            image_bytes = base64.b64decode(base64_image)
            
            # Create a safe filename
            filename = "generated_image.jpeg"
            
            # STEP 6: Save the image to a file
            with open(filename, "wb") as f:
                f.write(image_bytes)
            
            print(f"✅ Success! Image saved as '{os.path.abspath(filename)}'")

        else:
            print("❌ Generation failed: API response was successful but did not contain the expected 'photo' data.")
            print("Full API Response:", data)

    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during the API request:")
        # Check if 'response' was assigned before the error occurred
        if 'response' in locals() and response is not None:
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")
        else:
            print(f"Error: {e}")
    except json.JSONDecodeError:
        print("❌ Failed to decode JSON response from the API.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    # --- CHANGE THIS PROMPT TO TEST YOUR GENERATOR ---
    my_prompt = "A majestic lion wearing a crown, drawn in the style of a children's book."
    # ------------------------------------------------
    
    generate_image(my_prompt)

    # To run this script:
    # 1. Make sure you are in the 'python' directory.
    # 2. Run: python generate_image.py
