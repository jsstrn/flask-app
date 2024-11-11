from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class NetworkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Configure public subnet
        public_subnet_configuration = ec2.SubnetConfiguration(
            name="jsstrn-public-subnet",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24
        )

        # Create VPC with subnet configuration
        self.vpc = ec2.Vpc(
            self, 
            "jsstrn-vpc",
            ip_addresses=ec2.IpAddresses.cidr("192.168.0.0/16"),
            max_azs=1,
            subnet_configuration=[
                public_subnet_configuration
            ]
        )
