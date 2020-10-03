import boto3
import json
import os
import uuid

def post(event, context):
    try:
        resp = {
            'statusCode':200,
            "message": "Login Successfully"
        }
        return json.dumps(resp)
    except Exception as e:
        response = {
            'statusCode': 500,
            'message': str(e)
        }
        raise Exception(json.dumps(response))
