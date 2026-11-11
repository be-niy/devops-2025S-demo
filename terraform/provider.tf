# This block tells Terraform we need the 'aws' provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0" # Use a recent version
    }
  }
}

# This block configures the provider.
# It will automatically use the credentials you set up with 'aws configure'
provider "aws" {
  region = "us-east-1" # You can change this to your preferred region
}
