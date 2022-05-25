#############################################################################
# SQLAlchemy and Flask Bootcamp challenge
# This script returns JSONified query results from API endpoints
# it serves queries with Flask to enable a Climate Web App
#############################################################################

from flask import Flask, jsonify, render_template, request

import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import datetime as dt
import numpy as np

#############################################################################
# Database Setup
#############################################################################

# Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect database into new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)

# Close session
session.close()

#############################################################################
# Flask Setup
#############################################################################

# Create flask setup
app = Flask(__name__)

#############################################################################
# Flask Routes
#############################################################################

# Create flask routes

# Define what to do do when user hits index route
@app.route("/")
def Home():
    """List all the available API routes"""
    return(
        f"Welcome to Hawaii Climate Page<br/> "
        f"Available Routes:<br/>"
        f"<br/>"  
        f"The list of precipitation data with dates:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"The list of stations and names:<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"The list of temperature observations from a year from the last data point:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"Min, Max. and Avg. temperatures for given start date: (please use 'yyyy-mm-dd' format):<br/>"
        f"/api/v1.0/min_max_avg/&lt;start date&gt;<br/>"
        f"<br/>"
        f"Min. Max. and Avg. temperatures for given start and end date: (please use 'yyyy-mm-dd'/'yyyy-mm-dd' format for start and end values):<br/>"
        f"/api/v1.0/min_max_avg/&lt;start date&gt;/&lt;end date&gt;<br/>"
        f"<br/>"
        f"i.e. <a href='/api/v1.0/min_max_avg/2012-01-01/2016-12-31' target='_blank'>/api/v1.0/min_max_avg/2012-01-01/2016-12-31</a>"
    )

#############################################################################

# Create precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create the session link
    session = Session(engine)

    """Return the dictionary for date and precipitation info"""

    # Query precipitationa and date values
    Results_Date_prcp = session.query(Measurement.date, Measurement.prcp).all()

    # Close session
    session.close()

    # Create a dictionary as date - the key and prcp as the value
    Precipitation = []
    for Result in Results_Date_prcp:
        R = {}
        R[Result[0]] = Result[1]
        Precipitation.append(R)

    # Jsonify precipitation of the dictionary
    return jsonify(Precipitation)

##############################################################################

# Create stations route
@app.route("/api/v1.0/stations")
def Stations():
    # Create the session link
    session = Session(engine)

    """Return a JSON list of the stations."""

    # Query the data to get the station list
    Results_Station = session.query(Station.station, Station.name).all()

    # Close session
    session.close()

    # Convert the list of tubles into a list of dictionaries for each station and name
    StationList = []
    for Result in Results_Station:
        R = {}
        R["station"] = Result[0]
        R["name"] = Result[1]
        StationList.append(R)

    # Jsonify the list
    return jsonify(StationList)


############################################################################

# Create temperature route
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)

    """Return a JASON list of termperature observations (tobs) for the previous year"""

    # Query termperatures from a year from the last data point
    lateststr = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latestdate = dt.datetime.strptime(lateststr, '%Y-%m-%d')
    querydate = dt.date(latestdate.year -1, latestdate.month, latestdate.day)
    sel = [Measurement.date,Measurement.tobs]
    queryresult = session.query(*sel).filter(Measurement.date >= querydate).all()

    # Close the session
    session.close()

    # Convert the list of tubles to show the date and temperature values
    tobsall = []
    for date, tobs in queryresult:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temperature"] = tobs
        tobsall.append(tobs_dict)

    # Jsonify the list
    return jsonify(tobsall)

############################################################################

# Create start only route
@app.route("/api/v1.0/min_max_avg/<start>")
def start(start):
    # Create session link
    session = Session(engine)

    """Return a JSON list of the minimum, average and maximum temperature for a given start date."""

    # Query data for the date value
    Result_Start = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    # Close the session
    session.close()

    # Create a list to hold the results
    TemperatureList = []
    for min, avg, max in Result_Start:
        R = {}
        R["min_temp"] = min
        R["avg_temp"] = avg
        R["max_temp"] = max
        TemperatureList.append(R)

    # Jsonify the list
    return jsonify(TemperatureList)

##########################################################################

# Create start and end route
@app.route("/api/v1.0/min_max_avg/<start>/<end>")
def start_end(start, end):
    # Create session link
    session = Session(engine)

    """Return a JSON list of the minimum, average and maximum temperature for a given start and end date."""

    # Query data for the date value
    Result_Start_End = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Close the session
    session.close()

    # Create a list to hold the results
    Temperature_List = []
    for min, avg, max in Result_Start_End:
        R = {}
        R["min_temp"] = min
        R["avg_temp"] = avg
        R["max_temp"] = max
        Temperature_List.append(R)

    # Jsonify the list
    return jsonify(Temperature_List)


##############################################################################

# Run the app
if __name__ == "__main__":
    app.run(debug=True)