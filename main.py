import os
import json
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


def extract_customer_support_info(message: str) -> dict:

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. "
            "Please add your Gemini API key to the .env file."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a customer support message classifier.

Analyze the customer message below and extract exactly these fields:

1. intent:
   A short description of the customer's main request.
   Examples: "Refund Request", "Order Status", "Cancellation Request",
   "Damaged Item", "Product Inquiry".

2. urgency:
   Must be exactly one of:
   "High", "Medium", or "Low".

3. order_number:
   Extract the order number as a string if one exists.
   If there is no order number, return null.

Return ONLY a valid JSON object with exactly these keys:
intent
urgency
order_number

Customer message:
{message}
"""


    chat = client.chats.create(model="gemini-3.1-flash-lite"
                               ,config=types.GenerateContentConfig(temperature=0,response_mime_type="application/json")
                               )

    try:
        response = chat.send_message(prompt)
    except Exception as exc:
        error_message = str(exc)
    # print(response.text)


    if not response.text:
        raise ValueError("gemini returned an empty response.")
    try:
        result = json.loads(response.text)
    except json.JSONDecodeError as jser:
        raise ValueError(
            f"Gemini returned invalid JSON:\n{response.text}"
        ) from jser

    
    required_fields = {"intent", "urgency", "order_number"}

    if not required_fields.issubset(result.keys()):
        missing = required_fields - result.keys()
        raise ValueError(f"Missing required fields: {missing}")

    
    allowed_urgency = {"High", "Medium", "Low"}

    if result["urgency"] not in allowed_urgency:
        raise ValueError(
            f"Invalid urgency value: {result['urgency']}. "
            f"Expected one of {allowed_urgency}."
        )

    # check order id
    if result["order_number"] is not None and not isinstance(
        result["order_number"], str
    ):
        result["order_number"] = str(result["order_number"])

    return {
        "intent": result["intent"],
        "urgency": result["urgency"],
        "order_number": result["order_number"],
    }


def main():
    default_messages = [
        "My order #45678 arrived damaged and I want a refund immediately.",
        "Order ORD-12345 has not arrived yet. Can you check its status?",
        "Thank you, my order arrived safely.",
    ]

    print("Customer Support Message Classifier")
    print("Enter a message, or press Enter to run the default test cases.")
    print()

    customer_message = input("Enter your message: ").strip()

    if not customer_message:
        print("\nRunning default test cases...\n")

        for number, message in enumerate(default_messages, start=1):
            print(f"Test Case {number}")
            print(f"Message: {message}")

            try:
                result = extract_customer_support_info(message)
                print("Extracted information:")
                print(json.dumps(result, indent=2))

            except ValueError as error:
                print(f"Error: {error}")

            except RuntimeError as error:
                print(f"API Error: {error}")

            except Exception as error:
                print(f"Unexpected error: {error}")

            print("-" * 50)

        return

    try:
        result = extract_customer_support_info(customer_message)

        print("\nExtracted information:")
        print(json.dumps(result, indent=2))

    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    except Exception as error:
        print(f"Unexpected error: {error}", file=sys.stderr)
        sys.exit(1)



if __name__ == "__main__":
    main()
