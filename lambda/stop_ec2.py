import boto3

def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    instance_id = "i-0abcd12345xyz"
    ec2.stop_instances(InstanceIds=[instance_id])
    return {"message": "Instance stopped"}
