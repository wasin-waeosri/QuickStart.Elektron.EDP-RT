#!/usr/bin/env python
""" 
Simple example of authenticating to EDP-GW and using the token to login and
retrieve MarketPrice content.  A username, password, and client ID are used to
retrieve this token. The Client ID must be requested from Thomson Reuters.
"""

"""
Modify By Wasin W. with following
1.	The API endpoint is fixed: api.edp.thomsreuters.com and we shouldn’t be asking users for it (--auth_hostname) [Wasin: Done]
2.	The version number (beta1) is hardcoded in sample, and should be made configurable, probably as a variable at the very top. [Wasin: Done]
3.	There is a username/password, but no prompt for Client_ID. It is also a required parameter for getting an OAuth token. [Wasin: Done]
4.	Previous comment about not hardcoding the streaming endpoint, and get it from the REST call instead. [Wasin: Done]
5.	As a part of best practice, we should persist the Refresh Token. See the EDP sample for how it is done. [Wasin: Not do this yet]
"""

import sys
import time
import getopt
import requests
import socket
import json
import websocket
import threading

# Global Default Variables
app_id = '256'
auth_hostname = 'api.edp.thomsonreuters.com'
auth_port = '443'
auth_path = 'auth/oauth2/beta1/token'
hostname = '127.0.0.1'
password = ''
position = ''
sts_token = ''
refresh_token = ''
user = ''
port = '443'
client_secret = ''
scope = 'trapi'
ric = 'TRI.N'

# Add by Wasin W
client_id = ''
EDP_version = '/beta1'
auth_category_URL = '/auth/oauth2'
auth_endpoint_URL = '/token'
TOKEN_ENDPOINT = auth_hostname + auth_category_URL + EDP_version + auth_endpoint_URL
location = 'us-east-1a'
transport = 'websocket'
dataformat='tr_json2'
TOKEN_FILE = "token.txt"

streaming_category_URL = '/streaming/pricing'
hostname_service_endpoint = auth_hostname + streaming_category_URL + EDP_version

# Global Variables
web_socket_app = None
web_socket_open = False
logged_in = False


def process_message(ws, message_json):
    """ Parse at high level and output JSON of message """
    message_type = message_json['Type']

    if message_type == "Refresh":
        if 'Domain' in message_json:
            message_domain = message_json['Domain']
            if message_domain == "Login":
                process_login_response(ws, message_json)
    elif message_type == "Ping":
        pong_json = {'Type': 'Pong'}
        ws.send(json.dumps(pong_json))
        print("SENT:")
        print(json.dumps(pong_json, sort_keys=True, indent=2, separators=(',', ':')))


def process_login_response(ws, message_json):
    """ Send item request """
    global logged_in

    if message_json['State']['Stream'] != "Open" or message_json['State']['Data'] != "Ok":
        print("Login failed.")
        sys.exit(1)

    logged_in = True
    send_market_price_request(ws, ric)


def send_market_price_request(ws, ric_name):
    """ Create and send simple Market Price request """
    mp_req_json = {
        'ID': 2,
        'Key': {
            'Name': ric_name,
        },
    }
    ws.send(json.dumps(mp_req_json))
    print("SENT:")
    print(json.dumps(mp_req_json, sort_keys=True, indent=2, separators=(',', ':')))


def send_login_request(ws, auth_token, is_refresh_token):
    """ 
        Send login request with authentication token.
        Used both for the initial login and subsequent reissues to update the authentication token
    """
    login_json = {
        'ID': 1,
        'Domain': 'Login',
        'Key': {
            'NameType': 'AuthnToken',
            'Elements': {
                'ApplicationId': '',
                'Position': '',
                'AuthenticationToken': ''
            }
        }
    }

    login_json['Key']['Elements']['ApplicationId'] = app_id
    login_json['Key']['Elements']['Position'] = position
    login_json['Key']['Elements']['AuthenticationToken'] = auth_token
    
    # If the token is a refresh token, this is not our first login attempt.
    if is_refresh_token:
        login_json['Refresh'] = False
        
    ws.send(json.dumps(login_json))
    print("SENT:")
    print(json.dumps(login_json, sort_keys=True, indent=2, separators=(',', ':')))


def on_message(ws, message):
    """ Called when message received, parse message into JSON for processing """
    print("RECEIVED: ")
    message_json = json.loads(message)
    print(json.dumps(message_json, sort_keys=True, indent=2, separators=(',', ':')))

    for singleMsg in message_json:
        process_message(ws, singleMsg)


def on_error(_, error):
    """ Called when websocket error has occurred """
    print(error)


def on_close(_):
    """ Called when websocket is closed """
    global web_socket_open
    web_socket_open = False
    print("WebSocket Closed")


def on_open(ws):
    """ Called when handshake is complete and websocket is open, send login """

    print("WebSocket successfully connected!")
    global web_socket_open
    web_socket_open = True
    send_login_request(ws, sts_token, False)


def get_sts_token(current_refresh_token):
    """ 
        Retrieves an authentication token. 
        :param current_refresh_token: Refresh token retrieved from a previous authentication, used to retrieve a
        subsequent access token. If not provided (i.e. on the initial authentication), the password is used.
    """
    
    # Modify By Wasin W.
    #url = 'https://{}:{}/{}'.format(auth_hostname, auth_port, auth_path)
    url = 'https://{}'.format(TOKEN_ENDPOINT)

    if not current_refresh_token:  # First time through, send password
        data = {'username': user, 'password': password, 'grant_type': 'password', 'takeExclusiveSignOnControl': True,
                'scope': scope}
        #print("Sending authentication request with password to ", url, "...")
        print("Sending authentication request with client_id to ", url, "...")
    else:  # Use the given refresh token
        data = {'username': user, 'refresh_token': current_refresh_token, 'grant_type': 'refresh_token',
                'takeExclusiveSignOnControl': True}
        print("Sending authentication request with refresh token to ", url, "...")

    try:
        r = requests.post(url,
                          headers={'Accept': 'application/json'},
                          data=data,
                          auth=(client_id, client_secret),
                          verify=True)

    except requests.exceptions.RequestException as e:
        print('EDP-GW authentication exception failure:', e)
        return None, None, None

    if r.status_code != 200:
        print('EDP-GW authentication result failure:', r.status_code, r.reason)
        print('Text:', r.text)
        if r.status_code == 401 and current_refresh_token:
            # Refresh token may have expired. Try using our password.
            return get_sts_token(None)
        return None, None, None

    auth_json = r.json()
    print("EDP-GW Authentication succeeded. RECEIVED:")
    print(json.dumps(auth_json, sort_keys=True, indent=2, separators=(',', ':')))

    #save Refresh Token to File:
    saveToken(json.loads(r.text))
    # Modify by Wasin W. to let application reads those auth information from file only
    #return auth_json['access_token'], auth_json['refresh_token'], auth_json['expires_in']
    return auth_json

def get_hostname_url(token):

    """ 
        Retrieves an RealTime Service list. 
    """

    streaming_url = 'https://{}/'.format(hostname_service_endpoint)
    payload = {'transport': transport, 'dataformat': dataformat}

    print("Sending Elektron Data Platform RealTime Service Discovery to ", streaming_url, "...")
    try:
        r = requests.get(streaming_url, 
                            headers={'Accept': 'application/json', 'Authorization': "Bearer " + token},
                            params=payload)

    except requests.exceptions.RequestException as e:
        print('ERT in Cloud RealTime Service Discovery result failure:', e)
        return None, None
    
    if r.status_code != 200:
        print('ERT in Cloud RealTime Service Discovery result failure:', r.status_code, r.reason)
        print('Text:', r.text)
        return None, None

    streaming_list_json = r.json()
    print("ERT in Cloud RealTime Service Discovery succeeded. RECEIVED:")
    print(json.dumps(streaming_list_json, sort_keys=True, indent=2, separators=(',', ':'))) 

    # Filter to get Elektron WebSocket Host with  "location":["us-east-1a"] only
    endpoint = [node for node in streaming_list_json['service'] if node['location'][0] == location and len(node['location']) == 1 ]
    
    return endpoint[0]['endpoint'], endpoint[0]['port']

# Modify by Wasin W. to save auth information to file
def saveToken(tknObject):
    tf = open(TOKEN_FILE, 'w')
    print('Saving the new token')
	# Append the expiry time to token
    tknObject['expiry_tm'] = time.time() + int(tknObject['expires_in']) - 10
    # Store it in the file
    json.dump(tknObject, tf, indent=4)
    tf.close()

# Modify by Wasin W. to read auth information from file or re-request auth token
def getToken():
    try:
        print("Reading the token from: " + TOKEN_FILE)
        with open(TOKEN_FILE, 'r+') as tf:
            tknObject = json.load(tf)
            if tknObject['expiry_tm'] > time.time():
                return tknObject['access_token'], tknObject['refresh_token'], tknObject['expires_in']
            
        print("Token expired, refreshing a new one...")
        tknObject = get_sts_token(tknObject["refresh_token"])
    except:
        print('Getting a new token...')
        tknObject = get_sts_token(None)
    
    # Persist this token for future queries
    saveToken(tknObject)
    # Return access token
    return tknObject['access_token'], tknObject['refresh_token'], tknObject['expires_in']

if __name__ == "__main__":
    # Get command line parameters
    # Modify By Wasin 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["help", "app_id=", "user=", "password=","client_id=",
                                                      "position=","scope=","ric="])
    except getopt.GetoptError:
        print('Usage: market_price_edpgw_authentication.py [--app_id app_id] '
              '[--user user] [--password password] [--client_id client_id] [--position position]'
              '[--scope scope] [--ric ric] [--help]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in "--help":
            print('Usage: market_price_edpgw_authentication.py  [--app_id app_id] '
                  '[--user user] [--password password] [--client_id client_id] [--position position]'
                  '[--scope scope] [--ric ric] [--help]')
            sys.exit(0)
        # Modify By Wasin W.
        #elif opt in "--hostname":
            #hostname = arg
        #elif opt in "--port":
            #port = arg
        elif opt in "--app_id":
            app_id = arg
        elif opt in "--user":
            user = arg
        elif opt in "--password":
            password = arg   
        # Modify By Wasin 
        elif opt in ("--client_id"):
            client_id = arg
        elif opt in "--position":
            position = arg
        elif opt in "--scope":
            scope = arg
        elif opt in "--ric":
            ric = arg

    if position == '':
        # Populate position if possible
        try:
            position_host = socket.gethostname()
            position = socket.gethostbyname(position_host) + "/" + position_host
        except socket.gaierror:
            position = "127.0.0.1/net"

    # Modify By Wasin W. to get Token from persist file 
    #sts_token, refresh_token, expire_time = get_sts_token(None)
    sts_token, refresh_token, expire_time =getToken()
    if not sts_token:
        sys.exit(1)
    
    # Modify By Wasin W. to get Hostname and Port from REST Service
    hostname, port = get_hostname_url(sts_token)
    if not hostname:
        sys.exit(1)
    # Start websocket handshake
    ws_address = "wss://{}:{}/WebSocket".format(hostname, port)
    print("Connecting to WebSocket " + ws_address + " ...")
    web_socket_app = websocket.WebSocketApp(ws_address, on_message=on_message,
                                            on_error=on_error,
                                            on_close=on_close,
                                            subprotocols=['tr_json2'])
    web_socket_app.on_open = on_open

    # Event loop
    wst = threading.Thread(target=web_socket_app.run_forever, kwargs={'sslopt': {'check_hostname': False}})
    wst.start()

    try:
        while True:
            # Give 30 seconds to obtain the new security token and send reissue
            if int(expire_time) > 30:
                time.sleep(int(expire_time) - 30)
            else:
                # Fail the refresh since value too small
                sys.exit(1)
            sts_token, refresh_token, expire_time = get_sts_token(refresh_token)
            if not sts_token:
                sys.exit(1)

            # Update token.
            if logged_in:
                send_login_request(web_socket_app, sts_token, True)
    except KeyboardInterrupt:
        web_socket_app.close()