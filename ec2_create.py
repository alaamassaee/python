import boto3

ec2_client = boto3.client("ec2", region_name="us-east-1")
instances = ec2_client.run_instances(
    ImageId="ami-041feb57c611358bd",
    MinCount=1,
    MaxCount=1,
    InstanceType="t3.micro"
)
