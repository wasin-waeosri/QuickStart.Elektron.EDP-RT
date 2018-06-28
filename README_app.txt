THOMSON REUTERS
PYTHON ELEKTRON REAL-TIME EXAMPLE

==========
1. Summary
==========

This example demonstrates authenticating via the Elektron Real-Time Service and
Elektron Data Platform Gateway, and logging in with the retrieved token to 
retrieve market content.

The example first sends an HTTP request to the EDP Gateway, using the specified
username and password. The Gateway provides an authentication token
in response.

The example then opens a WebSocket to the Elektron Real-Time Service at the specified host, logs in
using the authentication token, then retrieves market content.

The example periodically retrieves new authentication tokens, using a refresh
token included in the response from the Gateway instead of the username and
password. Once the new token is retrieved, it sends a login request with this
token over its WebSocket to the Elektron Real-Time Service.

======================
2. Prerequisite
======================

The market_price_edpgw_authentication.py application requires the latest Python 3.6.5 compiler, Python's requests and websocket-client libralies in order to connect and consume data from Elektron Data Platform and Elektron in Cloud. 
1. __Install Python__
    - Go to: <https://www.python.org/downloads/>
    - Select the __Download tile__ for the Python 3.6.5 (and above) version
    - Run the downloaded `python-<version>` file and follow installation instructions
2. __Install libraries__
    - Run (in order):
      - `pip install requests`
      - `pip install websocket-client`
      - (Only for Python versions less than 3.3) `pip install ipaddress`

======================
3. Running the example
======================

The machine image has the necessary Python modules installed.  To run the
example, call the script with the locations of the Elektron Real-Time Service, and the
necessary authentication information

The required command line is as follows:
python market_price_edpgw_authentication.py --user <username> --password <password> --hostname <Elektron Real-Time Service host> 

All Commandline Option Descriptions:

  --auth_hostname   <OPTIONAL> Hostname of the EDP Gateway.
  --auth_port       <OPTIONAL> Port of the EDP Gateway. Defaults to 443
  --hostname        <REQUIRED> Hostname of the Elektron Real-Time Service.
  --port            <OPTIONAL> Port of the Elektron Real-Time Service. Defaults to 443
  --user            <REQUIRED> Username to use when authenticating via Username/Password to the Gateway.
  --password        <REQUIRED> Password to use when authenticating via Username/Password to the Gateway.
  --scope           <OPTIONAL> An authorization scope to include when authenticating. Defaults to 'trapi' 
  --ric             <OPTIONAL> Name of the item to request from the Elektron Real-Time Service. If not specified, EUR= is requested.
  --app_id          <OPTIONAL> Application ID to use when logging in. If not specified, "256" is used.
  --position	    <OPTIONAL> Position to use when logging in. If not specified, the current host is used.
