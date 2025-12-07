import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    args = sys.argv[1:]
    # Check for number of arguments
    if not args:
        print("Error. No prompt provided.\nUsage: uv main.py \"your prompt\" [--verbose]")
        sys.exit(1)
    
    # Flags
    verbose = "--verbose" in args # True or False

    # Search for prompt in args
    non_flag_args = [arg for arg in args if not arg.startswith("-")]

    # Prompt
    user_prompt = non_flag_args[0]
    
    # Load variables from .env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Check if key is avaiable
    if not api_key:
        raise RuntimeError("Can't load Gemini API key from .env")
    
    # Create Gemini client
    client = genai.Client(api_key=api_key)

    # Creat a message
    message = types.Content(
        role="user",
        parts=[types.Part(text=user_prompt)]
    )

    # Call the model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=message,
    )

    print("*** Model response ***")
    print(response.text)
    print()

    # Tokens used
    if verbose:
        print(f"User prompt: {user_prompt}")
        usage = response.usage_metadata
        if usage:
            print(f"Prompt tokens: {usage.prompt_token_count}")
            print(f"Response tokens: {usage.candidates_token_count}")
        else:
            print("No data about tokens usage")

if __name__ == "__main__":
    main()
