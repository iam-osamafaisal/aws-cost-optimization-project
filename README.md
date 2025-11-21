# AWS EC2 Cost Optimization Using Automated Start–Stop Scheduling

This project automates EC2 cost optimization using AWS Lambda, CloudWatch Scheduler, IAM Roles, and local CLI scripts.

<img width="1536" height="1024" alt="Architecture" src="https://github.com/user-attachments/assets/1110ef21-ec09-431b-83a1-102b1bb609cb" />


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
<img width="1898" height="971" alt="Screenshot 2025-11-20 235358" src="https://github.com/user-attachments/assets/b88bf371-f139-4d4d-9590-15c79a8f9f5c" />

🧑‍💻 Author
Osama Faisal
Cloud & DevOps Engineer Intern
LinkedIn Profile
