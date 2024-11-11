from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class InstanceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc, sg: ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define EC2 instance in public subnet of VPC
        instance = ec2.Instance(
            self, 
            "jsstrn-instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            key_pair=ec2.KeyPair.from_key_pair_name(
                self, 
                "jsstrn-ssh-key", 
                "jsstrn-ssh-key"
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=sg,
        )

        # Add user data
        instance.user_data.add_commands(
            "yum update -y",
            "yum install python3-pip git -y",
            "pip3 install flask gunicorn",
            "git clone https://github.com/jaezeu/flask-app.git",
            "cd flask-app",
            "gunicorn -b 0.0.0.0:8080 app:app"
        )
