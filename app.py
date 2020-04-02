from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import pymongo
import json

# Flask setup
app = Flask(__name__)



# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/stations')
def stations():
    return render_template('stations.html')

@app.route('/stations1')
def stations1():
    return render_template('stations1.html')

@app.route('/citibike')
def citibike():
    return render_template('citibike.html')

@app.route('/nyc_stat')
def nyc():
    return render_template('nyc_stat.html')

@app.route('/age')
def nyc_total_trips():
    return render_template('nyc_age.html')

@app.route('/citibike_stat')
def filter():
    return render_template('blank1.html')

#to clear cache
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#To get data from MongoDB
@app.route('/stationlocations')
def stationlocation():
    conn='mongodb://localhost:27017'
    client = MongoClient(conn)
    db=client.bikeshareDB
    stations = db.bike_companies.find()

    
    data=[]
    
    for station in stations:
        
        data.append({'id': station['id'],'name': station['name'], 'country': station['location']['country'], 'city': station['location']['city'],
        'lat': station['location']['latitude'], 'lng': station['location']['longitude'], 'stations':station['stations']})
        
    return {'companies':data}

@app.route('/nyc_data_july')
def july_nycdata():
    
    conn='mongodb://localhost:27017'
    client = MongoClient(conn)
    db=client.bikeshareDB
    trips=[]
    
    trips = db.nyc_bikes.find()
    
    data=[]
    i=0
    for trip in trips:    
        if (i>100000): 
            break
        data.append({'duration':trip['tripduration'], 'gender':trip['gender'], 'birth_year':trip['birth year']})  
        i=i+1
    
    
    return {'trips':data} 

@app.route('/nyc_data_oct')
def oct_nycdata():
    
    conn='mongodb://localhost:27017'
    client = MongoClient(conn)
    db=client.bikeshareDB
    trips=[]
    
    trips = db.nyc_bikes_oct.find()
    
    data=[]
    i=0
    for trip in trips:    
        if (i>100000): 
            break
        data.append({'duration':trip['tripduration'], 'gender':trip['gender'], 'birth_year':trip['birth year']})  
        i=i+1
    
    
    return {'trips':data} 

@app.route('/nyc_data_jan')
def jan_nycdata():
    
    conn='mongodb://localhost:27017'
    client = MongoClient(conn)
    db=client.bikeshareDB
    trips=[]
    
    trips = db.nyc_bikes_jan.find()
    
    data=[]
    i=0
    for trip in trips:    
        if (i>100000): 
            break
        data.append({'duration':trip['tripduration'], 'gender':trip['gender'], 'birth_year':trip['birth year']})  
        i=i+1
    
    
    return {'trips':data} 

@app.route('/nyc_data_apr')
def apr_nycdata():
    
    conn='mongodb://localhost:27017'
    client = MongoClient(conn)
    db=client.bikeshareDB
    trips=[]
    
    trips = db.nyc_bikes_apr.find()
    
    data=[]
    i=0
    for trip in trips:    
        if (i>100000): 
            break
        data.append({'duration':trip['tripduration'], 'gender':trip['gender'], 'birth_year':trip['birth year']})  
        i=i+1
    
    
    return {'trips':data} 

if __name__ == '__main__':
    app.run(debug=True)