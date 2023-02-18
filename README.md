# Metlo - API Testing and Security
Metlo is a simple Python application that allows you to test the security of a web API. It checks for common vulnerabilities and issues, such as SQL injection, cross-site scripting (XSS), rate limiting, and more.

# How to Use
1. Clone this repository to your local machine.
2. Install the required dependencies using pip install -r requirements.txt.
3. Run the application by executing python metlo.py.
4. Enter the API URL and API key in the input fields.
5. Click the "Run Tests" button to start the API test.
6. The result of the test will be displayed in the text area below.

# Dependencies
* requests
* tkinter

# Example Usage
Here's an example of how to use the Metlo application:

![us1](https://i.postimg.cc/Gpq88jH8/us1.jpg)

This code is a Python script that creates a GUI (Graphical User Interface) using the tkinter library. The GUI is used to test the security of an API (Application Programming Interface) by sending requests to the API and checking the response for various security vulnerabilities.

![us2](https://i.postimg.cc/FRzfjJLP/us2.jpg)

It takes the API URL and API key as inputs from the user input fields, validates the input, makes a GET request to the API with the key in the headers, and then checks the response for various security vulnerabilities such as vulnerable endpoints, response status code and HTTPS status, request encryption status, UTF-8 encoding, response encryption status, SQL injection vulnerabilities, cross-site scripting (XSS) vulnerabilities, rate limiting, content type validation, session management, and denial-of-service (DoS) attacks.The run_api_tests function is the main function that sends requests to the API and checks the response for various security vulnerabilities. 

# Contributing
* Roshan Jadhav - roshan.lj@somaiya.edu
* Bilal Inamdar - bilal.i@somaiya.edu
* Anannya Khedekar - anannya.khedekar@somaiya.edu
