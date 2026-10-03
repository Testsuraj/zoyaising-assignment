Customer Support Message Classifier

A small GenAI-based customer support message classifier built with Python and the Google Gemini API.

The application takes a customer support message and uses Gemini to extract:

Intent — the main reason for the customer's message

Urgency — High, Medium, or Low

Order Number — the order number if present, otherwise null

The extracted information is returned as valid JSON and printed to the console.

Example
Input
My order #12344 arrived damaged, and I need a refund immediately!

Output
{
  "intent": "Damaged Item and Refund Request",
  "urgency": "High",
  "order_number": "12344"
}

Requirements

Python 3.9+

Gemini API key

Internet connection

Project Structure
zoiya_assignment/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Installation

Clone the repository:

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd zoiya_assignment


Install the required packages:

pip install -r requirements.txt

API Key Setup

Create a .env file in the project directory:

GEMINI_API_KEY=your_gemini_api_key_here


Do not commit the .env file to GitHub.

The application checks for the API key and displays an error if it is missing.

Running the Application

Run:

python main.py


The application will ask for a customer support message:

Customer Support Message Classifier
Enter your message: My order #12344 arrived damaged and I need a refund immediately.


The extracted information will be displayed as JSON:

{
  "intent": "Damaged Item and Refund Request",
  "urgency": "High",
  "order_number": "12344"
}

Error Handling

The application includes basic error handling for:

Missing Gemini API key

Empty customer messages

Gemini API request failures

Gemini API rate limits (429 RESOURCE_EXHAUSTED)

Empty API responses

Invalid JSON returned by the model

Missing required JSON fields

Invalid urgency values

For example, if the Gemini API rate limit is reached, the application displays a short message instead of exposing the complete API error response.

Technologies Used

Python

Google Gemini API

google-genai

python-dotenv

JSON

Notes

The model is instructed to return only the required JSON fields:

intent
urgency
order_number


The returned JSON is parsed and validated by the Python application before being printed.

The Gemini API key is loaded from an environment variable rather than being hard-coded in the source code.