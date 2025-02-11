#!/bin/bash

echo "Hello, Terraform!" > /var/www/html/index.html

yum update -y
yum install -y httpd

systemctl start httpd
systemctl enable httpd
