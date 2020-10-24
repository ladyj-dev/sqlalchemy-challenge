# Use Flask to create your routes
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from flask import Flask, jsonify

#Database Setup
engine = create_engine("(Resources/hawaii.sqlite)")

#reflect database
Base = automap_base()
#reflect tables
Base.prepare(engine, reflect=True)
Station = Base.classes.station
Measurement = Base.classes.measurement

#Flask Setup

app = Flask(__name__)

#Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Welcome to the Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
        

    )
climate_app_prcp = [
    {"date": "prcp"}
]

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the climate app precipitation data as json"""
    
    return jsonify(climate_app_prcp)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    """Return a list of all stations"""
    # query dataset
    results = session.query(stations.name).all()

    session.close()

    #convert list of tuples into normal list

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
    def tobs():
        session = Session(engine)

        """Return a list of temperature observations (TOBS) for the previous year"""
        #query all dates and temperatures for the previous year
        results = session.query(Station.station, Station.tobs).all()

        session.close()

        




