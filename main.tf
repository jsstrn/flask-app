provider "aws" {
  region = "ap-southeast-1"
}

# Create a VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "jsstrn-tf-vpc"
  }
}

# Create a public subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "ap-southeast-1a"
  tags = {
    Name = "jsstrn-tf-public-subnet"
  }
}

# Create a security group
resource "aws_security_group" "sg" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "jsstrn-tf-ec2-sg"
  }

  ingress {
    description = "Allow HTTP traffic on port 8080"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # All protocols
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an EC2 instance
resource "aws_instance" "instance" {
  ami             = "ami-07c9c7aaab42cba5a" # Amazon Linux 2 AMI
  instance_type   = "t2.micro"
  subnet_id       = aws_subnet.public.id
  security_groups = [aws_security_group.sg.id]
  user_data       = templatefile("hello.sh", {})
  tags = {
    Name = "jsstrn-tf-instance"
  }
}
