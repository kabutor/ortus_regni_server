#!/usr/bin/python

import json
from flask import Flask, jsonify, request, make_response
import ssl
from typing import TypedDict
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#context.load_cert_chain('server.crt', 'server.key')

class EmergencyMessage():
    def __init__(self, message, header):
        self.message = message
        self.header = header

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'name': 'alice',
                       'email': 'alice@outlook.com'})

#Login existing user
@app.route('/api/Accounts/Login', methods = ['POST'])
def login():
    data = request.json
    print(data)
    response = make_response(jsonify( { "code":0,"_ex:":"","payload": {"username":"kabutor"}}))
    #,"authorization":"","registrations":""
    response.headers["Content-Type"] = "application/json"
    response.headers["X-Auth-Token"] = "1111111111111111"
    return response 


# Create Account
@app.route('/api/Accounts/CreateBattleCenterAccount', methods=['POST'])
def create_account():
    data = request.json
    print(request.headers)
    # I get -> {'username': 'kau@me.com', 'password': '1111111', 'email': 'djasdjsad@me.com', 'userId': None, 'authorization': None, 'registrations': None, 'verified': False, 'status': 0, 'emailsub': False, 'steamId': None}
    print (data)
    # Just have to return username (can be different than the one the user sent me)
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"username":"test"}} ) ,200,)
    response.headers["Content-Type"] = "application/json"
    response.headers["X-Auth-Token"] = "1111111111111111"
    return response 

# Get User Status
@app.route('/api/UserStats/GetUserStats', methods=['POST'])
def getstats():
    # Id by X-Auth-Token Header
    # get {'usk': '', 'onw': 0, 'onl': 0, 'offw': 0, 'offl': 0, 'c2p': 0, 'c3p': 0, 'c4p': 0, 'pgr': 0, 'psr': 0, 'pbr': 0}
    # UserPsk  OnlineWins  OnlineLoses   OfflineWins OfflLoses  Current rank 2p 3p 4p     Previous Rank Gold Silver Bronze
    data = request.json
    print(data)
    print("-" * 10)
    print("XAuth: %s" % request.headers['X-Auth-Token'])
    # USK not assigned here, not in the create account "usk":"userstring1234"
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"onw":20,"c2p":12,"c3p":4,"c4p":1,"pgr":10,"psr":2}} ) ,200,)
    response.headers["Content-Type"] = "application/json"
 
    return response

# SetPlayerstatus
@app.route('/api/PlayerStatus/SetPlayerStatus', methods=['POST'])
def setPlayerStatus():
    data = request.json
    print(data)
    print("XAuth: %s" % request.headers['X-Auth-Token'])    
    # Status : 0:offline 1:InMenus 2:Inlobby 3:InMatchmaking (more)
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"":""}} ) ,200,)
    response.headers["Content-Type"] = "application/json"
 
    return response

# Matchmaking seasons
@app.route('/api/Leaderboard/GetPlacementSummaryForSeason', methods=['POST'])
def get_placement_season():
    data = request.json
    print(data)
    print("XAuth: %s" % request.headers['X-Auth-Token'])    
    
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"twopMatches":1, "twopRanking":0, "threepMatches":2, "threepRanking":0, 
                                                                       "fourpMatches":4, "fourpRanking":0, "leaderboardSeason":8 }} ) ,200,)
    response.headers["Content-Type"] = "application/json"
 
    return response



# Matchmaking remaining (there is a max games per season per player to do ranks?)
@app.route('/api/Leaderboard/GetPlacementMatchesRemaining', methods=['POST'])
def get_placement_remaining():
    data = request.json
    print(data)
    print("XAuth: %s" % request.headers['X-Auth-Token'])    
    
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"twopMatches":11, "twopRanking":10, "threepMatches":0, "threepRanking":10, 
                                                                       "fourpMatches":14, "fourpRanking":10, "leaderboardSeason":18 }} ) ,200,)
    response.headers["Content-Type"] = "application/json"
 
    return response

# Request Match
@app.route('/api/Matches/RequestMatch', methods=['POST'])
def request_match():
    data = request.json
    print(data)
    print("XAuth: %s" % request.headers['X-Auth-Token'])    
    
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"":None }} ) ,200,)
    response.headers["Content-Type"] = "application/json"
 
    return response
# Request Match Status
@app.route('/api/Matches/RequestStatus', methods=['GET'])
def request_match_status():
    print("Get Status")
    print("XAuth: %s" % request.headers['X-Auth-Token'])   

    
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"":None }} ) ,200,)
    response.headers["Content-Type"] = "application/json"
 
    return response

# DeleteRequest Match
@app.route('/api/Matches/DeleteRequest', methods=['POST'])
def delete_request_match():
    data = request.json
    print(data)
    print("XAuth: %s" % request.headers['X-Auth-Token'])    
    
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"":None }} ) ,200,)
    response.headers["Content-Type"] = "application/json"
 
    return response






# Get friends
@app.route('/api/Friends/Get', methods=['GET'])
def get_friends():
    #data = request.json
    #print(data)
    print("XAuth: %s" % request.headers['X-Auth-Token'])    
    # approved invited blocked pending
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"approved":None,"invited":None,"blocked":None,"pending":None}} ) ,200,)
    response.headers["Content-Type"] = "application/json"
    return response

# Get Direct Messages (just returns nothing)
@app.route('/api/Messaging/GetDirectMessagesFor', methods=['POST'])
def get_direct_messages():
    data = request.json
    print(data)
    print("XAuth: %s" % request.headers['X-Auth-Token'])    
    response = make_response(jsonify ( {"code":0,"_ex:":"","payload": {"usrs": None, "msgs": None, "smpsk": None}} ) ,200,)
    response.headers["Content-Type"] = "application/json"
    print("Get Direct Messages For")
    return response 


#Login emegency Message (Working)
@app.route('/api/System/EmergencyMessage', methods=['GET'])
def emergency():
    #response = make_response( jsonify( {"code":0,"_ex:":"","payload": {"message":"Kabutor was here!","header":"Mi Cabecera"}} ), 200,)
    #response.headers["Content-Type"] = "application/json"
    return " " 

# Get Min/Max version, ask for update if don't fit (Working)
@app.route('/api/System/GetPlatformSupportedVersions', methods=['GET'])
def plat_versions():
    response = make_response(jsonify( {"code":0,"_ex:":"","payload": {"platformpsk": 1, "minversion":"1.0", "maxversion":"2.0","description":"OR" }} ), 200,)
    response.headers["Content-Type"] = "application/json"
    return response



app.run(host="0.0.0.0", port=80, debug=True)
#app.run(host="0.0.0.0", port=443, debug=True,ssl_context=context)
