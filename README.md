# Gemini Customer Support Message Extractor

A Python application that uses the **Google Gemini API** to extract structured information from a customer support message.

## Features

The application extracts:

* **Intent** — identifies the customer's main request.
* **Urgency** — classifies the request as `High`, `Medium`, or `Low`.
* **Order Number** — extracts the order number or returns `null` if none is found.

## Example Input

```text
My order #12344 arrived damaged, and I need a refund immediately!
```

## Example Output

```json
{
  "intent": "Refund Request",
  "urgency": "High",
  "order_number": "12344"
}
```

## Tech Stack

* Python
* Google Gemini API
* `google-genai`
* `python-dotenv`

## Project Structure

```text
zoyaising-assignment/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/zoyaising-assignment.git
cd zoyaising-assignment
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Do not commit the `.env` file to GitHub.

### 4. Run the application

```bash
python main.py
```

## Error Handling

The application includes basic error handling for:

* Missing Gemini API key
* Empty API responses
* Invalid JSON responses
* Invalid urgency values
* API/request errors

## How It Works

```text
Customer Support Message
          ↓
      Gemini API
          ↓
   Structured JSON
          ↓
 ┌─────────────────┐
 │ intent          │
 │ urgency         │
 │ order_number    │
 └─────────────────┘
          ↓
    Console Output
```

## Assignment

This project was created as part of a customer support LLM extraction assignment requiring a Python dictionary/JSON response containing `intent`, `urgency`, and `order_number`.
