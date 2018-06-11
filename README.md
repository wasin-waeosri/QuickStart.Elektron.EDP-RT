# Elektron Data Platform for Real-Time (EDP-RT)
## Overview
Elektron Data Platform is blah blah blah blah blah.

## Introduction
The goal of this Quick Started tutorial is to guide developers to launch the [Amazon AWS EC2](https://aws.amazon.com/ec2/) Instance based on Thomson Reuters's Amazon Machine Images ([AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)) to connect and consume data from EDP-RT.

## Description In this quick start guide, we will cover the following areas:
- Prerequisite
- How to launch your EC2 instance based on Thomson Reuters's AMI 
- How to connect to your EC2 instance
- How to run EDP-RT demo application inside your EC2 instance

## Prerequsit 

The following accounts and softwares are required in order to run this quick start guide:
1. Amazon AWS account
2. Web Browser
3. Internet connection
4. SSH client software
5. Amazon AWS key pair

If you are new to Amazon AWS, you can subscribe [AWS Free Tier](https://aws.amazon.com/free/) which provides you a free hand-on access to AWS platform and services. We highly recommend you follow the Amazon AWS [Setting Up with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html) and [Getting Started with Amazon EC2 Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) tutorials before proceed futher in this quick start guide to create your key-pair, VPC and Security Group which are required for EC2 instance.

## How to launch your EC2 instance based on Thomson Reuters's AMI 
1. Login to [AWS Management Console](https://console.aws.amazon.com/console/home) with your IAM user 

![Figure-1](.\images\edp_rt_1.png "Login to AWS console as IAM user")

2. In the Region section, choose US East (N. Virginia)

![Figure-2](.\images\edp_rt_2.png "Choose US East N. Virginia region")

3. Go to [EC2 Dashboard](https://console.aws.amazon.com/ec2/v2/home) page, then choose IMAGES -> AMIs section.

![Figure-3](.\images\edp_rt_3.png "EC2 Dashboard")

4. In the AMIs page, select "Public images" and then search Thomson Reuters' AMI with "Thomson Reuters" filter.

![Figure-4](.\images\edp_rt_4.png "Searching Thomson Reuters AMI")

5. Select Thomson Reuters AMI, then select "Launch".

![Figure-5](.\images\edp_rt_5.png "Launch instance 1")

6. Select your Instance type based on your preference, then click "Review and Launch" button. You may choose "Configure Instance Details" to configure Instance network, storage, etc based on your requirement. Click "Launch" button to launch your EC2 instance.

![Figure-6](.\images\edp_rt_7.png "Launch instance 2")

7. Select your key pair which will be used to connect to your instance. You can also create a new key-pair for this intance here.

![Figure-7](.\images\edp_rt_8.png "Select key pair")



