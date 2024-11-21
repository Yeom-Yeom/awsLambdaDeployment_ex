import json

def lambda_halnder(event, context):
    print("Event:", event)

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from AWS Lambda!",
            "input": event
        })
    }

    return response