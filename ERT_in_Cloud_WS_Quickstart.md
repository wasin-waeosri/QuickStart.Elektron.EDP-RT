# Elektron WebSocket API Quick Start - Connecting to Elektron Real Time in Cloud
- Last update: August 2019
- Environment: Windows and Linux OS on either on-premise or any Cloud VMs environment
- Compiler: Python
- Prerequisite: [ERT in Cloud Access Credentials](#prerequisite)

## Overview

<!--The goal of this Quick Start tutorial is to guide you through initial steps to consume the Elektron Real time in Cloud (ERT in Cloud) data from [Refinitiv Elektron Data Platform](https://developers.refinitiv.com/elektron-data-platform) using the Elektron Websocket API by way of a small sample application written in [Python](https://www.python.org/) programming language. -->

The goal of this Quick Start tutorial is to guide you through initial steps to run the Elektron Real Time in Cloud (ERT in Cloud) Websocket API example. The example is written in [Python](https://www.python.org/) programming language to connect and consume a streaming data from ERT in Cloud via Elektron WebSocket API connection over internet.

The tutorial is applicable to both Linux and Windows environments.

## Description In this quick start guide, we will cover the following areas:
- [Prerequisite](#prerequisite)
- [How to run ERT in Cloud Python example](#run_instance)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#nextsteps)
- [References](#references)

## <a id="prerequisite"></a>Prerequisite 

The following accounts and softwares are required in order to run this quick start guide:
1. [Python](https://www.python.org/) compiler and runtime
2. Python's [requests](https://pypi.org/project/requests/) library.
3. Python's [websocket-client](https://pypi.org/project/websocket-client/) library (*version 0.49 or greater*).
4. Internet connection
5. ERT in Cloud Username/machine ID, password and client_id access credentials. Please reach out to your Refinitiv representative to acquire ERT in Cloud access credentials.

You need to install examples required libraries via the ```pip install``` command in your environment before running the example:

```
$>pip install requests websocket-client
```

*Note:* 
- The Python example has been qualified with Python versions 2.7.14 and 3.6.7. 
- Please refer to the [pip installation guide page](https://pip.pypa.io/en/stable/installing/) if your environment does not have the [pip tool](https://pypi.org/project/pip/) installed. 
- If your environment already have a websocket-client library installed, you can use ```pip list``` command to verify a library version, then use ```pip install --upgrade websocket-client``` command to upgrade websocket-client library. 

## <a id="run_instance"></a>How to run ERT in Cloud Python example

You can connect to ERT in Cloud from your existing VM, Cloud VM or your local machine. The ERT in Cloud Quick Start example application is available for download at [Refinitiv Developer Community: Elektron WebSocket API download page](https://developers.refinitiv.com/elektron/websocket-api/downloads) or [Refinitiv/websocket-api: GitHub page](https://github.com/Refinitiv/websocket-api/tree/master/Applications/Examples/EDP). The ERT in Cloud Quick Start example package contains the WebSocket API examples for Python, Java and C# languages. 

This Quick Start is focusing on the Python's market_price_edpgw_service_discovery.py application. The market_price_edpgw_service_discovery.py file is an example Python application that sends the HTTP request to the EDP Gateway with the specified username and password for authentication, then it receives an authentication token to sends the HTTP request to EDP Streming Service Discovery to get associcate ERT in Cloud endpoint, then it login and consumes real-time streaming quote data from ERT in Cloud via the [Elektron WebSocket API](https://developers.refinitiv.com/elektron/websocket-api).
<!--You need to install the following required Python libraries via the ```pip install``` command in your environment before running the example:
- [requests](https://pypi.org/project/requests/) library.
- [websocket-client](https://pypi.org/project/websocket-client/) library (*version 0.49 or greater*).

```
$>pip install requests websocket-client
```

*Note:* 
- Please refer to the [pip installation guide page](https://pip.pypa.io/en/stable/installing/) if your environment does not have the [pip tool](https://pypi.org/project/pip/) installed. 
- If your environment already have a websocket-client library installed, you can use ```pip list``` command to verify a library version, then use ```pip install --upgrade websocket-client``` command to upgrade websocket-client library. 
-->
### ERT in Cloud connection parameters

The required connections parameters for the ERT in Cloud application are following
<!--- - *Authorization host of the EDP Gateway*: You can use *api.edp.thomsonreuters.com:443* to request the access token or pass it to ```---auth_hostname``` parameter on the application command line-->
<!--- *Hostname of the Elektron Real-Time Service endpoint*: You can use *wss://amer-1.pricing.streaming.edp.thomsonreuters.com:443* as you API connection point, or pass it to ```--hostname``` parameter on the application command line.-->
- *Username and Password*: To request your access token you must pass in a user name and password credentials (or specify it with ```--user```, ```--password``` parameters on the application command line). You will receive your Machine ID as a user name and a link to activate your machine account and set your password via the Welcome Email that you receive when you subscribe to ERT in Cloud. You must use these credentials to obtain a client_id 
- *client_id*: You must also pass in the client_id credential (or specifiy ig with ```--clientid``` parameter). The Client ID aka AppKey can be generated from an [AppGenerator tool](https://apac1.apps.cp.thomsonreuters.com/apps/AppkeyGenerator) with your username and password credentials. 

If you do not have that email please contact your Refinitiv representative, or if you are not a client please click [Contact Us page](https://my.refinitiv.com) if you would like to try Elektron Real Time data.

Optionally, the application subscribes a delay */TRI.N* RIC code from ERT in Cloud by default. You can pass your interested RIC code to ```--ric``` parameter on the application command line. You can find Refinitiv RIC Code of your interested instrument via [RIC Search page](https://developers.refinitiv.com/elektron/websocket-api/dev-tools?type=ric)

### Running the example

You can run market_price_edpgw_service_discovery.py application with the following command

```
$>python market_price_edpgw_service_discovery.py --user <ERT in Cloud Machine-ID> --password <ERT in Cloud Password> --clientid <ERT in Cloud client_id>
```

The other optional parameters are explained in the [README.md](https://github.com/Refinitiv/websocket-api/blob/master/Applications/Examples/EDP/python/README.md) file. 

Upon execution, you will be presented with authentication and ERT in Cloud Service discovery processes via EDP Gateway REST API, then followed by initial WebSocket connection between the application and ERT in Cloud. 

```
$>python market_price_edpgw_service_discovery.py --user user1 --password password1 --clientid QAZClienTIDZZZ..

('Sending authentication request with password to ', 'https://api.refinitiv.com:443/auth/oauth2/beta1/token', '...')
EDP-GW Authentication succeeded. RECEIVED:
{
  "access_token":"<Access Token>",
  "expires_in":"300",
  "refresh_token":"f69c291b-4d1a-48e8-8210-19fad796b924",
  "scope":"",
  "token_type":"Bearer"
}
Sending EDP-GW service discovery request to https://api.refinitiv.com/streaming/pricing/v1/
EDP-GW Service discovery succeeded. RECEIVED:
{
  "services":[
    {
      "dataFormat":[
        "tr_json2"
      ],
      "endpoint":"amer-3.pricing.streaming.edp.thomsonreuters.com",
      "location":[
        "us-east-1a",
        "us-east-1b"
      ],
      "port":443,
      "provider":"aws",
      "transport":"websocket"
    },
    {
      "dataFormat":[
        "tr_json2"
      ],
      "endpoint":"amer-2.pricing.streaming.edp.thomsonreuters.com",
      "location":[
        "us-east-1b"
      ],
      "port":443,
      "provider":"aws",
      "transport":"websocket"
    },
    {
      "dataFormat":[
        "tr_json2"
      ],
      "endpoint":"amer-1.pricing.streaming.edp.thomsonreuters.com",
      "location":[
        "us-east-1a"
      ],
      "port":443,
      "provider":"aws",
      "transport":"websocket"
    }
  ]
}
Connecting to WebSocket wss://amer-3.pricing.streaming.edp.thomsonreuters.com:443/WebSocket for session1...
WebSocket successfully connected for session1!
SENT on session1:
{
  "Domain":"Login",
  "ID":1,
  "Key":{
    "Elements":{
      "ApplicationId":"256",
      "AuthenticationToken":<Access Token>",
      "Position":"172.31.95.146/ip-172-31-95-146"
    },
    "NameType":"AuthnToken"
  }
}
RECEIVED on session1:
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
        "AuthenticationTTReissue":1530508864,
        "Position":"172.31.95.146/ip-172-31-95-146",
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
      "Name":"AQIC5wM2LY4Sfcz9Qn2Us7g5Ib5L%2BnFvYof2BkNXTAXbNbk%3D%40AAJTSQACMjAAAlNLABM2MjQ0MjU5NzI3ODE2MzM5MTI4AAJTMQACMzI%3D%23"
    },
    "State":{
      "Data":"Ok",
      "Stream":"Open",
      "Text":"Login accepted by host ads-premium-az2-green-2-main-prd.use1-az2."
    },
    "Type":"Refresh"
  }
]
```

Then application will receive an initial image called a RefreshMsg. The RefreshMsg or initial image contains all fields for the requested instrument representing the latest up-to-date market values. Following this image, you will begin to see UpdateMsgs or realtime updates reflecting changes in the market. All messages between the application and ERT in Cloud are in JSON format, you can find more detail regarding the Elektron WebSocket API's JSON message format in [WebSocket API Developer Guide](https://docs-developers.refinitiv.com/1555570705541/14977/) link.

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

**Q: How can I have Elektron Data Platform username, password and client_id?**

**A:** Please contact your Refinitiv representative to help you with EDP/ERT in cloud credential and permission. 

**Q: I have tried to use the App Key Generator page to create my client_id but page keeps asking me Eikon's email username**

**A:** Please contact your Refinitiv representative to help you with EDP/ERT in cloud credential and permission. 

**Q: I have ERT in Cloud account and the required Python libraries, but the example application fails at the Connecting to WebSocket line**
```
Connecting to WebSocket wss://<ERT in Cloud Server URL> for session1...
```
**A:** Please verify your Python and websocket-client versions. The Python examples have been qualified with Python versions 2.7.14, 3.6.7 and  the websocket-client library *version 0.49 or greater*. You can use ```python --version``` and ```pip list``` commands to verify the Python and libraries versions in your environment.

## <a id="nextsteps"></a>Next Steps

Once you have successfully completed the steps above, you can further your learning by following the series of [Elektron WebSocket API tutorials](https://developers.refinitiv.com/elektron/websocket-api/learning) of the [Developer Community](https://developers.refinitiv.com/).
<!--
If you are interested to connect to ERT in Cloud via the RSSL connection with Elektron SDK family,  you can find more detail in the following quick start pagges:
* [EMA Java Quick Start - Connecting to Elektron Real Time in Cloud](https://developers.refinitiv.com/elektron/elektron-sdk-java/quick-start?content=66483&type=quick_start)
* [ETA Java Quick Start - Connecting to Elektron Real Time in Cloud](https://developers.refinitiv.com/elektron/elektron-sdk-java/quick-start?content=66486&type=quick_start)
* [EMA C++ Quick Start - Connecting to Elektron Real Time in Cloud](https://developers.refinitiv.com/elektron/elektron-sdk-cc/quick-start?content=64988&type=quick_start)
* [ETA C++ Quick Start - Connecting to Elektron Real Time in Cloud](https://developers.refinitiv.com/elektron/elektron-sdk-cc/quick-start?content=67018&type=quick_start)
-->
Note: If there are plans to run your WebSocket applications within the Amazon Cloud, you can refer to the [Setting Up an Amazon EC2 instance article](https://developers.refinitiv.com/article/how-setup-refinitivs-amazon-ec2-machine-image-elektron-real-time-cloud) for further details.

## <a id="references"></a>References
For further details, please check out the following resources:
* [Refinitiv Elektron SDK Family page](https://developers.refinitiv.com/elektron) on the [Refinitiv Developer Community](https://developers.thomsonreuters.com/) web site.
* [Refinitiv Elektron WebSocket API page](https://developers.refinitiv.com/websocket-api) 
* [Developer Webinar Recording: Introduction to Electron WebSocket API](https://www.youtube.com/watch?v=CDKWMsIQfaw)
* [Refinitiv Elektron WebSocket API tutorials](https://developers.refinitiv.com/elektron/websocket-api/learning)
* [Refinitiv Elektron Data Platform](https://developers.refinitiv.com/elektron-data-platform)
* [Refinitiv Elektron: RIC Search](https://developers.refinitiv.com/elektron/websocket-api/dev-tools?type=ric)
* [Refinitiv Data Model Discovery page](https://refinitiv.fixspec.com/specserver/specs/reuters): Explore TR data models, content definitions and data update behaviors

For any question related to this quick start guide or Elektron Real Time in Cloud, please use the Developer Community [Q&A Forum](https://community.developers.refinitiv.com/spaces/71/index.html).

<!--* [Refinitiv Elektron WebSocket API: Quick Start Guide](https://developers.thomsonreuters.com/elektron/websocket-api/quick-start)-->
<!--* [Developer Webinar Recording: Introduction to Electron WebSocket API](https://www.youtube.com/watch?v=CDKWMsIQfaw)-->







