import json
import os

import requests


def main(context):
    context.log("Function started processing request")
    try:
        # Extract the access token from the request parameters
        access_token = context.req.query.get("access-token")
        if not access_token:
            context.log("Missing access token parameter")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Access token parameter is required"}),
            }

        # Get the API key from environment variables
        api_key = os.environ.get("PLANT_ID_API_KEY")
        if not api_key:
            context.log("API key not configured")
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "API key not configured"}),
            }

        # Construct the GET request to fetch the identification
        status_url = f"https://crop.kindwise.com/api/v1/identification/{access_token}"
        headers = {"Api-Key": api_key, "Content-Type": "application/json"}

        context.log(f"Fetching identification for token: {access_token}")
        response = requests.get(status_url, headers=headers)
        context.log(f"Received response with status code: {response.status_code}")

        # Return the response from the Plant.id API
        return {"statusCode": response.status_code, "body": response.text}

    except Exception as e:
        context.log(f"Error occurred: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
        context.log(f"Error occurred: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
