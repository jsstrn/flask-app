from aws_cdk import App
from resources.network import NetworkStack
from resources.security import SecurityStack
from resources.instance import InstanceStack

app = App()

# Create network stack
network_stack = NetworkStack(app, "jsstrn-network-stack")

# Create security stack with VPC
security_stack = SecurityStack(app, "jsstrn-security-stack", network_stack.vpc)

# Create instance stack with VPC and Security Group
instance_stack = InstanceStack(
    app, 
    "jsstrn-instance-stack", 
    network_stack.vpc,
    security_stack.security_group
)

app.synth()
