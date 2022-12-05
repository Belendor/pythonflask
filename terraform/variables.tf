variable "region" {
  description = "The region Terraform deploys your instances"
  type        = string
  default     = "eu-central-1"
}

variable "vpc_cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "ec2_type_docker" {
  description = "Instance type"
  type        = string
  default     = "t2.micro"
}

variable "ec2_ami" {
  description = "AMI ID"
  type        = string
  default     = "ami-0914982bb64a36219"
}

variable "ec2_count_docker" {
  description = "Number of instances"
  type        = number
  default     = 1
}

variable "rules" {
  type = list(object({
    from_port   = number
    to_port     = number
    proto       = string
    cidr_blocks = list(string)
  }))

  default = [
    {
      from_port   = 1
      to_port     = 40000
      proto       = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]
}
