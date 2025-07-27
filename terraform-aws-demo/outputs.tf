output "public_ip" {
  description = "EC2 Public IP Address"
  value       = aws_instance.demo.public_ip
}

output "ami_id" {
  description = "AMI ID used for instance"
  value       = data.aws_ami.amazon_linux.id
}