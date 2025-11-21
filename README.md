# AWS EC2 Cost Optimization Using Automated Start–Stop Scheduling

This project automates EC2 cost optimization using AWS Lambda, CloudWatch Scheduler, IAM Roles, and local CLI scripts.

## Features
- Automatically stop EC2 instances after business hours
- Automatically start EC2 instances during working hours
- Simple frontend to show Available / Not Available status
- Uses AWS serverless services for cost savings
- Reduces EC2 monthly billing significantly

## AWS Services Used
- EC2
- Lambda
- CloudWatch Events
- IAM Roles
- AWS CLI

## Folder Structure
├── lambda/  
├── scripts/  
├── role/  
└── frontend/

## How It Works
CloudWatch triggers Lambda start/stop functions based on cron schedules.
Frontend shows real-time service availability.
Local scripts allow manual control.

🧑‍💻 Author
Osama Faisal
Cloud & DevOps Engineer Intern
LinkedIn Profile
