import json

file = open("Attended.json", "r") 
attendedData = json.load(file)
attendedSession = attendedData["sessions"]
data_sessions = attendedSession.split(',')

print ("I have attended " + str(len(data_sessions)) + " sessions!!")