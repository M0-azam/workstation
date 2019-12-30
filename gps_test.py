import serial
import pynmea2 
from datetime import datetime, timedelta

def parseLatLong( lat ):
    try :
        degrees = int(float(lat))/100
        seconds = float(lat)-degrees*100
        seconds_to_degrees = seconds / 60
        return ( degrees + seconds_to_degrees )
    except Exception as e:
        #print(e)
        return "No Data"

def parseGPS(mystr):
    if mystr.find('GGA') > 0 :
#        print(mystr)
        msg = pynmea2.parse(mystr)
        #print(msg)
        time_stamp = datetime.strptime(str(msg.timestamp),"%H:%M:%S") + timedelta(hours=5,minutes=30)
        cur_time = time_stamp.time()
        #print ("TimeStamp : "+str(cur_time) )
        latitude = parseLatLong( msg.lat )
        #print ("Latitude : "+ latitude+" "+str(msg.lat_dir))
        longitude = parseLatLong( msg.lon )
        #print ("Longitude : "+longitude+" "+str(msg.lon_dir))
        #print ("Altitude : "+str(msg.altitude)+" "+str(msg.altitude_units))
        response = dict()
        response['Timestamp']=str(cur_time)
        response['Latitude']=latitude
        response['Latitude_dir']=msg.lat_dir
        response['Longitude']=longitude
        response['Longitude_dir']=msg.lon_dir
        response['Altitude']=msg.altitude
        response['Altitude_units']= msg.altitude_units
        return response
    elif mystr.find('RMC') > 0 :
        #print(mystr)
        msg = pynmea2.parse(mystr)
        response = dict()
        response['Timestamp']=str(msg.datetime+timedelta(hours=5,minutes=30))
        response['Latitude']=str(parseLatLong(msg.lat))
        response['Latitude_dir']=str(msg.lat_dir)
        response['Longitude']=str(parseLatLong(msg.lon))
        response['Longitude_dir']=str(msg.lon_dir)
        return response

serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

while True:
    try :
        mystr = serialPort.readline()
#        print(type(mystr))
#        print(mystr)
        mystr = mystr.decode("utf-8")
#        print(type(mystr))
#        print(mystr)
        gps_data = parseGPS(mystr)
        if gps_data:
            print(gps_data)
    except Exception as e :
        print(e)
