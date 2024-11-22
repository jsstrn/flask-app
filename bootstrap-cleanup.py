import boto3 as boto

# CDK does not have a clean up script for bootstrap files.

s3 = boto.resource("s3")

# Get list of all bucket names
for bucket in s3.buckets.all():
    if "cdk" in bucket.name:
        print("🚀 Found the bucket.")
        print(f"s3://${bucket.name}")
        
        print("🚮 Deleting the bucket.")
        
        # delete all objects in bucket
        bucket.objects.all().delete()
        
        # delete all version in bucket
        bucket.object_versions.all().delete()
        
        # delete bucket
        bucket.delete()
        
        # wait for bucket to be deleted
        print("⏳ Waiting for bucket to be deleted...")
        bucket.meta.client.get_waiter(
            'bucket_not_exist'
        ).wait(Bucket=bucket.name)
        
        print("✅ Bucket deleted.")
        break

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

# Get all active CloudFormation stacks
cf = boto.client("cloudformation")
stacks = cf.list_stacks(StackStatusFilter=["CREATE_COMPLETE"])

for stack in stacks["StackSummaries"]:
    stack_name = stack["StackName"]
    print(stack_name)
    if "CDKToolkit" in stack_name:
        print("🚀 Found the CDK CloudFormation stack.")
        print(stack_name)
        # Delete the CloudFormation stack
        print("🚮 Deleting the CDK CloudFormation stack.")
        delete_stack(stack_name)
        break
