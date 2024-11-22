import boto3 as boto

# This is a clean up script for CDK bootstrap files.

def delete_bucket(bucket):
    # Delete all objects in bucket
    bucket.objects.all().delete()
    
    # Delete all versions in bucket
    bucket.object_versions.all().delete()
    
    # Delete bucket
    bucket.delete()

    # Wait for bucket to finish deleting
    print("⏳ Waiting for bucket to be deleted...")
    bucket.wait_until_not_exists()
    
    print("✅ Bucket deleted.")

def delete_stack(stack_name):
    cf = boto.client("cloudformation")

    # Delete the stack
    print("🚮 Deleting stack.")
    cf.delete_stack(
        StackName=stack_name
    )

    # Wait for stack to be deleted
    print("⏳ Waiting for stack to be deleted...")
    cf.get_waiter("stack_delete_complete").wait(
        StackName=stack_name
    )

    print("✅ Stack deleted.")

# Get list of all bucket names
s3 = boto.resource("s3")

for bucket in s3.buckets.all():
    if "cdk" in bucket.name:
        # Found the CDK S3 bucket
        print("🚀 Found the CDK S3 bucket.")
        print(f"s3://${bucket.name}")
        
        # Delete the CDK S3 bucket
        print("🚮 Deleting the CDK S3 bucket.")
        delete_bucket(bucket)
        break

# Get all active CloudFormation stacks
cf = boto.client("cloudformation")
stacks = cf.list_stacks(StackStatusFilter=["CREATE_COMPLETE"])

for stack in stacks["StackSummaries"]:
    stack_name = stack["StackName"]
    print(stack_name)
    
    if "CDKToolkit" in stack_name:
        # Found the CDK CloudFormation stack
        print("🚀 Found the CDK CloudFormation stack.")
        print(stack_name)
        
        # Delete the CDK CloudFormation stack
        print("🚮 Deleting the CDK CloudFormation stack.")
        delete_stack(stack_name)
        break
