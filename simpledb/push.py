import boto.sdb
import json
import time

#list of domain names. Could be elimiminated if we reformat our descriptions
descriptions = ["GNSS", "COG_SOG", "Vessel_Heading", "Position", "Wind_Data"]

#connects to our AWS simpledb and creates the domains if they don't exist already
def connectAWS():
	#connect to aws
 	conn = boto.sdb.connect_to_region(
  		'us-east-1',
  		aws_access_key_id='AKIAJ77OGRWLX4JH2PFA',
  		aws_secret_access_key='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'
 	)

 	#get the array of domain names
 	domains = conn.get_all_domains()
	
	#iterate the array of domain names and compare to our array of domain names if it doesn't exist then make it
	for s in descriptions:
 		if s in domains:
 			continue
 		else:
 			conn.create_domain(s)
 	print domains

 	#return the connection to aws
 	return conn

#parses the json string you pass it no error checking cause lazy and I trust alex's jsoning skills
def parseJSON(str):
	return json.loads(str)

#pushes an object to the cloud. We name it the current time and put its attributes. This could be made more efficient
#by sorting first and then batch putting, but again i'm lazy
def pushObject(dom, name, attributes):
		dom.put_attributes(name, attributes)
		print "added object"

#This method parses the data descriptions, it can be totally elimintated if we make our descriptions properly formated domain names
def getIndex(description):
    if(description == "GNSS Position Data"):
    	return 0
    elif(description == "COG & SOG, Rapid Update"):
        return 1
    elif(description == "Vessel Heading"):
        return 2
    elif(description == "Position, Rapid Update"):
        return 3
    elif(description == "Wind Data"):
        return 4
    #we are not currently storing system time, although in the future I could pull that in for time stamping. However, it would be easier
    #if the time stamp came in with the data
    else:
    	return 5

#reads from can_out in data/1 and then writes out the data to the cloud. I have no parser or queries yet, but i'm viewing the cloud through a gui
#called simpledb explorer and exporting it to data/csv_data just so you can see what it looks like 
def main():
    conn = connectAWS()
    
    #open the test file and through line by line sorting and puting as nessisary
    f = open("../data/1/can_out", "r")
    for line in f:
        parsedjson = parseJSON(line)
        description = parsedjson["description"]
        index = getIndex(description)
        if(index != 5):
			dom = conn.get_domain(descriptions[index])
			fields = parsedjson["fields"]
			pushObject(dom, str(time.time()), fields)



if __name__ == "__main__":
 	main()
