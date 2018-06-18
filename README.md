# Elektron Real Time in Cloud (ERT in Cloud) Quick Start
## Overview

Elektron Data Platform (EDP) gives you seamless and holistic access to all of Thomson Reuters content (whether real-time or non- real-time, analytics or alternative datasets), commingled with your own content, enriching, integrating and distributing the data through a single interface, delivered wherever you need it.

As part of the Elektron Data Platform, Elektron Real Time in Cloud (ERT in Cloud) gives you access to best in class Real Time market data delivered in the cloud.  ERT in Cloud is a new delivery mechanism for EDP, using the AWS (Amazon Web Services) cloud. Once a connection to EDP is established using ERT in Cloud, data can be retrieved using any one of the Elektron APIs.

The goal of this Quick Start tutorial is to guide you through launching an [Amazon AWS EC2](https://aws.amazon.com/ec2/) Instance based on a Thomson Reuters Amazon Machine Image (([AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)), connecting to it and finally consuming EDP data through ERT in Cloud. Data retrieval uses a small Python sample code based on the [Elektron WebSocket API](https://developers.thomsonreuters.com/elektron/websocket-api) (EWA).

## Connecting to the API from Amazon AWS

Elektron Real Time in Cloud (ERT in Cloud) supports Amazon EC2's [Amazon Linux](https://aws.amazon.com/amazon-linux-ami/) instance customers only. Thomson Reuters will not support customers outside of Amazon EC2 service until further notice.

## Description In this quick start guide, we will cover the following areas:
- [Prerequisite](#prerequisite)
- [How to launch your EC2 Amazon Linux instance based on Thomson Reuters's AMI](#launch)
- [How to connect to your EC2 Amazon Linux instance](#connect)
- [How to run Elektron in Cloud demo application inside your newly created EC2 Amazon Linux instance](#run_ami)
- [How to run Elektron in Cloud demo application from your existing EC2 Amazon Linux instance](#run_instance)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## <a id="prerequisite"></a>Prerequisite 

The following accounts and softwares are required in order to run this quick start guide:
1. Amazon AWS account
2. Web Browser
3. Internet connection
4. SSH client software or Putty application
5. Amazon AWS key pair

If you are new to Amazon AWS, you can subscribe to [AWS Free Tier](https://aws.amazon.com/free/) account which gives you a free hands-on access to AWS platform and services. We highly recommend you follow the Amazon AWS [Setting Up with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html) and [Getting Started with Amazon EC2 Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) tutorials before proceeding futher in this quick start guide to create your key-pair, VPC and Security Group which are required for your EC2 instance.

## <a id="launch"></a>How to launch your EC2 Amazon Linux instance based on Thomson Reuters's AMI 
1. Login to [AWS Management Console](https://console.aws.amazon.com/console/home) with your IAM user 

    ![Figure-1](images/draft4/edp_rt_1.png "Login to AWS console as IAM user")

2. In the Region section, choose "US East (N. Virginia)"

    ![Figure-2](images/draft4/edp_rt_2.png "Choose US East N. Virginia region")

3. Go to [EC2 Dashboard](https://console.aws.amazon.com/ec2/v2/home) page, then choose IMAGES -> AMIs section.

    ![Figure-3](images/draft4/edp_rt_3.png "EC2 Dashboard")

4. In the AMIs page, select "Public images" and then search Thomson Reuters' AMI name with **Thomson Reuters Elektron Real-Time Examples - Amazon Linux AMI** name filter.

    ![Figure-4](images/draft4/edp_rt_4.png "Searching Thomson Reuters AMI")

5. Select Thomson Reuters AMI, then select "Launch".

    ![Figure-5](images/draft4/edp_rt_5.png "Launch instance 1")

6. Select your Instance type based on your preference and requirement, then click "Review and Launch" button. You may choose "Configure Instance Details" button to configure Instance network and public IP address (see more detail [here](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-ip-addressing.html#vpc-public-ip)), storage, etc based on your requirement. Click "Launch" button to launch your EC2 Linux instance.

    ![Figure-6](images/draft4/edp_rt_7.png "Launch instance 2")

7. Select your key pair which will be used to connect to your instance with your local machine. You can also create a new key-pair for this intance here. Click "Launch Instances" button to launch your Linux instance.

    ![Figure-7](images/draft4/edp_rt_8.png "Select key pair")

8. Back to EC2 Dashboard, you will see your newly created Amazon Linux instance is running with the instance information such as Instance ID, Public DNS (IPv4), IPv4 Public IP, etc. The main information is Public DNS (IPv4) which is required to connect to this instance.

    ![Figure-8](images/draft4/edp_rt_9.png "Instance is running")

## <a id="connect"></a>How to connect to your EC2 Amazon Linux instance

Once your Amazon Linux instance is running, you can connect to your Amazon Linux instance using Putty or SSH client applications. The following information are required to connect to your instance.
- Your private key file (example: key-pair.pem)
- Your Linux intance Public DNS

You can find more details regarding how to connect to your Amazon Linux instance from the following AWS document links:
- [Connecting to Your Linux Instance from Windows Using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)
- [Connecting to Your Linux Instance Using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

This Quick Start Guide uses [Git Bash](https://git-scm.com/downloads) application as a SSH client to connect to Amazon Linux instance with the following command

```
ssh -i "<your private key file name>" ec2-user@<Your Linux intance Public DNS>
```

Example:
```
ssh -i "Administrator-key-pair-us-east-1.pem" ec2-user@ec2-54-88-108-197.compute-1.amazonaws.com
```
![Figure-9](images/draft4/edp_rt_10.png "Connecting to Linux instance")

## <a id="run_ami"></a>How to run Elektron in Cloud demo application inside your newly created EC2 Amazon Linux instance

Once you have connected to your Amazon Linux instance, you will be available in your home folder **/home/ec2-user** location. Your home folder contains the following file and folder
- *python folder*: contains the market_price_edpgw_authentication.py Elektron in Cloud example application and its README.txt files
- *README.txt*: Thomon Reuters Amazon Linux Machine Image README file

The market_price_edpgw_authentication.py file is an example Python application that sends the HTTP request to the EDP Gateway with the specified username and password for authentication, then it receives an authentication token to login and consume real-time streaming quote data of TRI.N instrument from ERT in Cloud via the [Elektron WebSocket API](https://developers.thomsonreuters.com/elektron/websocket-api).

*Note:* This Thomson Reuters based AMI machined already installed all required libraries. 

## <a id="run_instance"></a>How to run Elektron in Cloud demo application from your existing EC2 Amazon Linux instance

If you already have an existing Amazon Linux instance in your EC2 service, you can download the market_price_edpgw_authentication.py application from [Thomson Reuters Developer Community: Elektron Data Platform](https://developers.thomsonreuters.com/elektron-data-platform/elektron-data-platform-early-access-apis/downloads) download page and upload the file to your Amazon Linux instance. 

![Figure-9](images/draft4/edp_rt_13.png "Downloading the application")

Before running the application, you need to install the following  application required libraries via the ```pip install``` command
- [requests](https://pypi.org/project/requests/) library
- [websocket-client](https://pypi.org/project/websocket-client/) library

```
$>pip install requests websocket-client
```

### Running the example

You can run market_price_edpgw_authentication.py application with the following command

```
$>python market_price_edpgw_authentication.py --auth_hostname <Hostname of the EDP Gateway> --hostname <Hostname of the Elektron Real-Time Service> --user <EDP Username> --password <EDP Password>
```

You can use *api.edp.thomsreuters.com* EDP Gateway for the ```--auth_hostname``` and *amer-1.pricing.streaming.edp.thomsonreuters.com* ERT hostname for the ```--hostname``` parameters. The other optional parameters are explained in the README.txt file. 

Upon execution, you will be presented with authentication process via EDP Gateway REST API, then followed by initial WebSocket connection between the application and ERT in Cloud. 

```
$>python market_price_edpgw_authentication.py --auth_hostname api.edp.thomsreuters.com --hostname amer-1.pricing.streaming.edp.thomsonreuters.com --user user1 --password password1

('Sending authentication request with password to ', 'https://api.edp.thomsonreuters.com:443/auth/oauth2/beta1/token', '...')
EDP-GW Authentication succeeded. RECEIVED:
{
  "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJyZWYiOiIwYjRkNjg0ZC0wYmRjLTQ4ZjctYTIyOS03YWU0ZTg1OTI5YWYiLCJhdWQiOiJHRS1BLTAxMTAzODY3LTMtNTU0IiwiaXNzIjoiaHR0cHM6Ly9maW5hbmNpYWwudGhvbXNvbnJldXRlcnMuY29tL2FwaS9pZGVudGl0eS9zdHNfcHJvZCIsImV4cCI6MTUyODg2NTEwMSwiaWF0IjoxNTI4ODY0ODAxfQ.GLDlw7h_JOTzRfw4yPQHtYtL0KA-Ek562tTV9HpSe2b3RDHyo-bXU6m7ORK3tzOA7zhfZa-GNPuUPtxKorHU_hYx9RP3qbaZJhuaK-uSwSKR6AwdCv55TJg959ebXghpSL0Ve5LR590fPO22AUVqPz5ahN5lpASNZeRzqKjRPbXOC5vWnNhLNhFMZ-Zwbv-WLKC8M8BSAJ72UOqV7YP_USeZKOxkkxVcLgC0V8WRb2JEJLDRRhM3MSMySeWIHj3FWC7rlXW625okcgy0OZiH10SfmnYMZtk9lp0njVBDJRYDh-QytYrnC3synNS8IruGfXfakmZUZIJwPNSGnMUhFQ",
  "expires_in":"300",
  "refresh_token":"288e1d89-248f-41e2-936c-d25631ad37bd",
  "scope":"",
  "token_type":"Bearer"
}
Connecting to WebSocket wss://amer-1.pricing.streaming.edp.thomsonreuters.com:443/WebSocket ...
WebSocket successfully connected!
SENT:
{
  "Domain":"Login",
  "ID":1,
  "Key":{
    "Elements":{
      "ApplicationId":"256",
      "AuthenticationToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJyZWYiOiIwYjRkNjg0ZC0wYmRjLTQ4ZjctYTIyOS03YWU0ZTg1OTI5YWYiLCJhdWQiOiJHRS1BLTAxMTAzODY3LTMtNTU0IiwiaXNzIjoiaHR0cHM6Ly9maW5hbmNpYWwudGhvbXNvbnJldXRlcnMuY29tL2FwaS9pZGVudGl0eS9zdHNfcHJvZCIsImV4cCI6MTUyODg2NTEwMSwiaWF0IjoxNTI4ODY0ODAxfQ.GLDlw7h_JOTzRfw4yPQHtYtL0KA-Ek562tTV9HpSe2b3RDHyo-bXU6m7ORK3tzOA7zhfZa-GNPuUPtxKorHU_hYx9RP3qbaZJhuaK-uSwSKR6AwdCv55TJg959ebXghpSL0Ve5LR590fPO22AUVqPz5ahN5lpASNZeRzqKjRPbXOC5vWnNhLNhFMZ-Zwbv-WLKC8M8BSAJ72UOqV7YP_USeZKOxkkxVcLgC0V8WRb2JEJLDRRhM3MSMySeWIHj3FWC7rlXW625okcgy0OZiH10SfmnYMZtk9lp0njVBDJRYDh-QytYrnC3synNS8IruGfXfakmZUZIJwPNSGnMUhFQ",
      "Position":"10.0.0.40/ip-10-0-0-40"
    },
    "NameType":"AuthnToken"
  }
}
RECEIVED: 
[
  {
    "Domain":"Login",
    "Elements":{
      "MaxMsgSize":61430,
      "PingTimeout":30
    },
    "ID":1,
    "Key":{
      "Elements":{
        "AllowSuspectData":1,
        "ApplicationId":"256",
        "ApplicationName":"ADS",
        "AuthenticationErrorCode":0,
        "AuthenticationErrorText":{
          "Data":null,
          "Type":"AsciiString"
        },
        "AuthenticationTTReissue":1528865101,
        "Position":"10.0.0.40/ip-10-0-0-40",
        "ProvidePermissionExpressions":1,
        "ProvidePermissionProfile":0,
        "SingleOpen":1,
        "SupportBatchRequests":7,
        "SupportEnhancedSymbolList":1,
        "SupportOMMPost":1,
        "SupportOptimizedPauseResume":0,
        "SupportPauseResume":0,
        "SupportStandby":0,
        "SupportViewRequests":1
      },
      "Name":"AQIC5wM2LY4SfcydaoLdG...zUyMQACUzEAAjM0%23"
    },
    "State":{
      "Data":"Ok",
      "Stream":"Open",
      "Text":"Login accepted by host ads-premium-az1-blue-1-main-prd.use1-az1."
    },
    "Type":"Refresh"
  }
]
```

Then application will receive an initial image called a RefreshMsg. The RefreshMsg or initial image contains all fields for the requested instrument representing the latest up-to-date market values. Following this image, you will begin to see UpdateMsgs or realtime updates reflecting changes in the market. All messages between the application and ERT in Cloud are in JSON format, you can find more detail regarding the Elektron WebSocket API's JSON message format in [WebSocket API Developer Guide](https://docs-developers.thomsonreuters.com/1528863829980/14977/) link.

You can (Ctrl+C) to exit the application at any time.

```
SENT:
{
  "ID":2,
  "Key":{
    "Name":"TRI.N"
  }
}
RECEIVED: 
[
  {
    "Fields":{
      "DSPLY_NAME":"THOMSON REUTERS",
      "52WK_HIGH":48.6,
      "52WK_LOW":36.53,
      "52W_HDAT":"2017-10-17",
      "52W_HIND":null,
      "52W_LDAT":"2018-05-11",
      "52W_LIND":null,
      "ACVOL_1":198379,
      "ACVOL_UNS":198379,
      "AC_TRN_CRS":null,
      "AC_VOL_CRS":0,
      "ADJUST_CLS":41.0,
      "ASK":40.78,
      "ASKSIZE":1,
      "ASK_1":40.78,
      ...
      "YRLOW":36.53,
      "YRLOWDAT":"2018-05-11",
      "YRLO_IND":"Yr.Low  "
    },
    "ID":2,
    "Key":{
      "Name":"TRI.N",
      "Service":"ELEKTRON_DD"
    },
    "PermData":"AwEBZWLA",
    "Qos":{
      "Rate":"JitConflated",
      "Timeliness":"Realtime"
    },
    "SeqNumber":29678,
    "State":{
      "Data":"Ok",
      "Stream":"Open",
      "Text":"*All is well"
    },
    "Type":"Refresh"
  }
]

RECEIVED: 
[
  {
    "Fields":{
      "ASK":90.2,
      "ASKSIZE":16000,
      "BEST_ASIZ1":16000,
      "QUOTIM":"05:49:53",
      "QUOTIM_MS":20993225
    },
    "ID":2,
    "Key":{
      "Name":"TRI.N",
      "Service":"ELEKTRON_DD"
    },
    "SeqNumber":26768,
    "Type":"Update",
    "UpdateType":"Quote"
  }
]
```

## <a id="troubleshooting"></a>Troubleshooting

**Q: How can I have Elektron in Cloud username and password**

**A:** Please contact your Thomson Reuters's Technical Account Manager or Technical Relationship Manager to help you to access EDP account and services.

**Q: I do not have a private key pair file**

**A:** Please follow the steps in [AWS Document: Create a Key Pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html#create-a-key-pair) link to create your private key pair file.

**Q: My Amazon Linux instance does not have a Public DNS IP address**

**A:** The instance Public DNS and IP address need to be configured before launching the instance. Please refer to this [AWS Document: Assigning a Public IPv4 Address During Instance Launch](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-ip-addressing.html#vpc-public-ip) link. This public IPv4 address is automatically released in certain cases (stop instance, etc). If you already launched the instance or need a persistance public IP address, you can associate an [AWS Elastic IP Address](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-eips.html) with the instance.

*Note:* AWS Elastic IP Address is not included in the AWS Free Tier services.

**Q: What should I do after finish running an example application**

**A:** You can "Terminate" instance to delete your Amazon Linux instance permanently or "Stop" instance to just shutdown your instance and release all public DNS IP address. Please refer to [AWS Document: Clean Up Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-clean-up-your-instance) link for more detail. 

## <a id="references"></a>References
For further details, please check out the following resources:
* [Thomson Reuters Elektron SDK Family page](https://developers.thomsonreuters.com/elektron) on the [Thomson Reuters Developer Community](https://developers.thomsonreuters.com/) web site.
* [Thomson Reuters Elektron WebSocket API page](https://developers.thomsonreuters.com/websocket-api) 
* [Developer Webinar Recording: Introduction to Electron Websocket API](https://www.youtube.com/watch?v=CDKWMsIQfaw)
* [Thomson Reuters Elektron: RIC Search](https://developers.thomsonreuters.com/elektron/websocket-api/dev-tools?type=ric)
* [Thomson Reuters Data Model Discovery page](https://thomsonreuters.fixspec.com/specserver/specs/reuters): Explore TR data models, content definitions and data update behaviors

For any question related to this quick start guide or Elektron in Cloud, please use the Developer Community [Q&A Forum](https://community.developers.thomsonreuters.com/spaces/71/index.html).

<!--* [Thomson Reuters Elektron WebSocket API: Quick Start Guide](https://developers.thomsonreuters.com/elektron/websocket-api/quick-start)-->
<!--* [Developer Webinar Recording: Introduction to Electron Websocket API](https://www.youtube.com/watch?v=CDKWMsIQfaw)-->







