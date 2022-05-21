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

#############################################################################
# Flask Setup
#############################################################################

# Create flask setup
app = Flask(__name__)

#############################################################################
# Flask Routes
#############################################################################

# Create flask routes
@app.route("/")
def Home():
    return render_template("index.html")

def cal_temps(StartDate, EndDate):
    """t_min, t_avg, t_max for a list of dates
    
    Args:
        StartDate (string): A date string in the format %Y-%m-%d
        EndDate (string): A date string in the format %Y-%m-%d
        
    Returns:
        t_min, t_avg, and t_max
    """

    session = Session(engine)

    return (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
        .filter(Measurement.date >= StartDate)
        .filter(Measurement.date <= EndDate)
        .all()
    )





    if __name__ == "__main__":
    app.run(debug=True)