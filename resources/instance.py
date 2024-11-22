from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


class InstanceStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc: ec2.Vpc,
        sg: ec2.SecurityGroup,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # Create key pair for SSH access
        key_pair = ec2.KeyPair(
            self,
            "jsstrn-ssh-key",
            key_pair_name="jsstrn-ssh-key",
            type=ec2.KeyPairType.RSA,
            format=ec2.KeyPairFormat.PEM,
        )

        # Define EC2 instance in public subnet of VPC
        instance = ec2.Instance(
            self,
            "jsstrn-instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            key_pair=key_pair,
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=sg,
        )

        # Add user data
        instance.user_data.add_commands(
            "yum update -y",
            "yum install httpd -y",
            "systemctl start httpd",
            "systemctl enable httpd",
            "echo '<h1>Hello, world!</h1>' > /var/www/html/index.html",
            "yum install python3-pip git -y",
            "pip3 install flask gunicorn",
            "git clone https://github.com/jsstrn/flask-app.git",
            "cd flask-app",
            "gunicorn -b 0.0.0.0:8080 app:app",
        )
