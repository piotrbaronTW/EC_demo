# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:03:25 2021

@author: JAN38588
"""

# Setup packages
#import os
#from pathlib import Path
#import pickle
from pandas.io.json import json_normalize
from flask import Flask, abort, request
import datetime


# Create app
app=Flask(__name__)


@app.route('/ModelTest', methods=["POST"])    
def ModelTest():
    if not request.json:
        abort(400)
    
    # Start timer
    currentTime = datetime.datetime.now()
    print("Request Received")

    ## Data Prep
    # Convert request from json into pandas df
    data = json_normalize(request.json)
    data["pred"] = (data["AgeMainDriver"] > data["MinimumLicenceLength"])  
    data = data.loc[:, ["pred"]]
    
    # Convert to json - "records" ensures output is like this: [{"pred":y1},{"pred":y2}, ...]
    response = data.to_json(orient='records')
    print(response)
    # End timer
    print("Request Calculated")
    print("Elapsed time: {}".format(datetime.datetime.now() - currentTime))
    
    return(response, 201)
    
## ModelTestEnd


if __name__=="__main__":    
    app.run(debug=False, port=int(5432))
