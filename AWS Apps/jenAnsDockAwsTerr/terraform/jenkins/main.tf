# Region to use for our infrastructure
provider "aws" {
    region = "us-east-2"
}

variable "name" {
    description = "Name the instance on deploy"
}

# define our AWS EC2 Instance
resource "aws_instance" "devops_01_jenkins" {
    ami           = "ami-01e7ca2ef94a0ae86"
    instance_type = "t2.micro"
    key_name      = "devops_01"

    tags = {
        Name = "${var.name}"
    }
}