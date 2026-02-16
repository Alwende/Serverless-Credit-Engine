import json
import boto3
import uuid
import os
from datetime import datetime

# Initialize AWS Services
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# CONFIGURATION
TABLE_NAME = 'LoanApplications'
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN') 

def lambda_handler(event, context):
    try:
        # 1. Parse Input
        print("Received Event:", json.dumps(event)) # Debugging log
        body = json.loads(event['body']) if 'body' in event else event
        
        customer_name = body.get('name')
        salary = float(body.get('monthly_salary'))
        loan_amount = float(body.get('loan_amount'))
        email = body.get('email')

        # 2. UNDERWRITING LOGIC
        max_limit = salary * 3
        application_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if loan_amount <= max_limit:
            status = "APPROVED"
            message = f"Congratulations {customer_name}! Loan of ${loan_amount} APPROVED."
        else:
            status = "DECLINED"
            message = f"Dear {customer_name}, loan DECLINED. Limit is ${max_limit}."

        # 3. SAVE TO DYNAMODB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={
            'application_id': application_id,
            'timestamp': timestamp,
            'name': customer_name,
            'amount': str(loan_amount),
            'status': status
        })

        # 4. SEND NOTIFICATION (SNS)
        if SNS_TOPIC_ARN:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject=f"Loan Decision: {status}",
                Message=f"App ID: {application_id}\nApplicant: {customer_name}\nDecision: {message}"
            )

        return {
            'statusCode': 200,
            'body': json.dumps({'application_id': application_id, 'status': status, 'message': message})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}