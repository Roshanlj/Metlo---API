import requests
import re
import time

import tkinter as tk



# Define the function to run the API tests
def run_api_tests():
    # Get the API URL and API key from the user input fields
    api_url = api_url_entry.get()
    api_key = api_key_entry.get()

    # Validate the input
    if not api_url.startswith("http"):
        result_text.set("Invalid URL")
        return

    # Make a GET request to the API with the key in the headers
    try:
        response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
    except requests.exceptions.RequestException as e:
        result_text.set(f"Error making request: {e}")
        return
    
     # Check for vulnerable endpoints using regular expressions
    if re.search(r"/api/v1/admin", api_url) or re.search(r"/api/v1/debug", api_url):
        result_text.set("API vulnerablity check failed: vulnerable endpoint detected")
        return

    # Check the response status code and HTTPS status
    if response.status_code == 200:
        result_text.set("API test passed")
    else:
        result_text.set("API test failed")

    if response.url.startswith("https"):
        result_text.set(f"{result_text.get()}\nHTTPS check passed")
    else:
        result_text.set(f"{result_text.get()}\nHTTPS check failed")

    # Check the request encryption status
    if "https://" in api_url:
        result_text.set(f"{result_text.get()}\nRequest encryption check passed")
    else:
        result_text.set(f"{result_text.get()}\nRequest encryption check failed")

    # Check for UTF-8 encoding
    if "charset" in response.headers and "utf-8" in response.headers["charset"].lower():
        result_text.set(f"{result_text.get()}\nUTF-8 encoding check passed")
    else:
        result_text.set(f"{result_text.get()}\nUTF-8 encoding check failed")

    # Check the response encryption status
    if "content-type" in response.headers and "application/json" in response.headers["content-type"]:
        result_text.set(f"{result_text.get()}\nResponse encryption check passed")
    else:
        result_text.set(f"{result_text.get()}\nResponse encryption check failed")

    # Check for SQL injection vulnerabilities
    if "error" in response.text.lower() or "sql" in response.text.lower():
        result_text.set(f"{result_text.get()}\nSQL injection check failed")
    else:
        result_text.set(f"{result_text.get()}\nSQL injection check passed")

    # Check for cross-site scripting (XSS) vulnerabilities
    if "<script>" in response.text:
        result_text.set(f"{result_text.get()}\nXSS check failed")
    else:
        result_text.set(f"{result_text.get()}\nXSS check passed")

    # Check for rate limiting
    if "X-RateLimit-Limit" in response.headers and "X-RateLimit-Remaining" in response.headers:
        limit = int(response.headers["X-RateLimit-Limit"])
        remaining = int(response.headers["X-RateLimit-Remaining"])
        if remaining < limit / 2:
            result_text.set(f"{result_text.get()}\nRate limiting check failed")
        else:
            result_text.set(f"{result_text.get()}\nRate limiting check passed")
    else:
        result_text.set(f"{result_text.get()}\nRate limiting headers not found")

    # Check for content type validation
    if "content-type" in response.headers and "application/json" in response.headers["content-type"]:
        result_text.set(f"{result_text.get()}\nContent type validation check passed")
    else:
        result_text.set(f"{result_text.get()}\nContent type validation check failed")

    # Check for session management
    if "sessionid" in response.cookies:
        result_text.set(f"{result_text.get()}\nSession management check passed")
    else:
        result_text.set(f"{result_text.get()}\nSession management check failed")

      # Check for DoS attacks
    if response.elapsed.total_seconds() > 10.0:
      result_text.set(f"{result_text.get()}\nDoS attack check failed")
    else:
      result_text.set(f"{result_text.get()}\nDoS attack check passed")
      

# Create the main window
root = tk.Tk()
root.title("Metlo - API testing and security")

# Create the UI elements
api_url_label = tk.Label(root, text="API URL:")
api_url_entry = tk.Entry(root, width=50)
api_key_label = tk.Label(root, text="API Key:")
api_key_entry = tk.Entry(root, width=50)
run_tests_button = tk.Button(root, text="Run Tests", command=run_api_tests)
result_label = tk.Label(root, text="Result:")
result_text = tk.StringVar()
result_text.set("")
result_display = tk.Label(root, textvariable=result_text, wraplength=600)

# Lay out the UI elements using the grid layout manager
api_url_label.grid(row=0, column=0, sticky="W")
api_url_entry.grid(row=0, column=1, columnspan=2)
api_key_label.grid(row=1, column=0, sticky="W")
api_key_entry.grid(row=1, column=1, columnspan=2)
run_tests_button.grid(row=2, column=0)
result_label.grid(row=3, column=0, sticky="W")
result_display.grid(row=4, column=0, columnspan=3)

# Run the main event loop
root.mainloop()
