import json

def lambda_halnder(event, context):
    return {
        "statusCode": 200,
        "body": "Hello, AWS Lambda!"
    }