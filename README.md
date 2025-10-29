# Azure OpenAI Image Generation Starter Kit

This repository provides two simple, beginner-friendly examples for calling a backend API that uses **Azure OpenAI's DALL-E model** for image generation.

The goal is to give students a minimal, working example in both a web environment (HTML/JavaScript) and a scripting environment (Python).

**🚨 IMPORTANT: You MUST replace the placeholder API endpoint with your own backend service URL before use.**

**🚨 The backend endpoint : https://ai-image-generation-backend-ixhr.onrender.com**

**🚨 For the live website checkout here  : dreamcanvas.stackhaus.dev**

## 🚀 Getting Started

This kit includes two main examples:

1.  **Web Example (`web/index.html`):** A simple HTML page with JavaScript that runs directly in a browser.
2.  **Python Example (`python/generate_image.py`):** A Python script that runs from the command line.

---

## 1. Web Example (HTML & JavaScript)

This is the easiest way for students to get started. It requires no setup other than a web browser.

### Prerequisites

*   A modern web browser (Chrome, Firefox, Edge, Safari).
*   **Recommended:** Visual Studio Code (VS Code) with the **Live Server** extension.

### How to Run

1.  **Open the project:** Open the `azure-openai-starter-kit` folder in VS Code.
2.  **Install Live Server (if needed):** In VS Code, search for and install the "Live Server" extension by Ritwick Dey.
3.  **Launch the page:** Right-click on the `web/index.html` file and select **"Open with Live Server"**.
4.  **Interact:** The page will open in your browser. Enter a prompt (e.g., "A robot painting a sunset on Mars") and click the "Generate Image" button.
5.  **View Results:** The generated image will appear below the button.

### Key Code Highlights (`web/index.html`)

The core logic is in the `<script>` tag:

| Code Snippet | Description |
| :--- | :--- |
| `const API_ENDPOINT = "..."` | **The only line you need to change.** This is the URL of your backend service. |
| `const response = await fetch(API_ENDPOINT, { ... });` | This is the **HTTP POST request** that sends the user's prompt to your backend. |
| `body: JSON.stringify({ prompt: prompt })` | This packages the user's text into a **JSON** format that the backend expects. |
| `const data = await response.json();` | This reads the **JSON response** from the backend. |
| `resultImage.src = "data:image/jpeg;base64," + data.photo;` | This takes the **Base64-encoded image string** (`data.photo`) and displays it directly in the browser's `<img>` tag. |

---

## 2. Python Example (Scripting)

This example shows how to perform the same task using a popular scripting language.

### Prerequisites

*   Python 3 installed on your computer.
*   The `requests` library for making HTTP calls.

### Setup

1.  **Navigate to the directory:**
    ```bash
    cd azure-openai-starter-kit/python
    ```
2.  **Install the required library:**
    ```bash
    pip install requests
    ```

### How to Run

1.  **Edit the prompt:** Open `generate_image.py` and change the value of the `my_prompt` variable to your desired description.
2.  **Execute the script:**
    ```bash
    python generate_image.py
    ```
3.  **View Results:** A new file named `generated_image.jpeg` will be saved in the `python` folder.

### Key Code Highlights (`python/generate_image.py`)

| Code Snippet | Description |
| :--- | :--- |
| `API_ENDPOINT = "..."` | **The only line you need to change.** This is the URL of your backend service. |
| `response = requests.post(...)` | This makes the **HTTP POST request** to your backend. |
| `response.raise_for_status()` | A good practice to automatically check if the request was successful (status code 200-299). |
| `base64.b64decode(base64_image)` | This decodes the **Base64-encoded image string** back into raw image data (bytes). |
| `with open(filename, "wb") as f: f.write(image_bytes)` | This saves the raw image data to a file on your computer. |

---

## 🛠️ Customization

1.  **Your Endpoint:** The most critical step is updating the `API_ENDPOINT` variable in both `web/index.html` and `python/generate_image.py`.
2.  **Response Format:** This starter kit assumes your backend returns a JSON object like this:
    ```json
    {
      "photo": "BASE64_ENCODED_IMAGE_STRING_HERE"
    }
    ```
    If your backend uses a different key (e.g., `"image_data"`), you will need to change `data.photo` to `data.image_data` in both files.

---
*Created by Manus AI for educational purposes.*
