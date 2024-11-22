from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


class SecurityStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Security Group
        self.security_group = ec2.SecurityGroup(
            self,
            "jsstrn-sg",
            vpc=vpc,
            description="Allow SSH and HTTP inbound traffic",
            allow_all_outbound=True,
        )

        # Add inbound rules for SSH
        self.security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH access from anywhere",
        )

        # Add inbound rules for HTTP
        self.security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP access from anywhere",
        )

        # Add inbound rules for port 8080
        self.security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(8080),
            description="Allow port 8080 access from anywhere",
        )
