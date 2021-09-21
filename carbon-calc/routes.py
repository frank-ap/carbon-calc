import os
import googlemaps
import requests
import json
from dotenv import load_dotenv
from flask import flash, Flask, render_template, flash, redirect, url_for, request
from data_dict import stadiums, postcodes, car_ef
from forms import CarbonCalculator

load_dotenv()
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
api_key = os.getenv('API_KEY')

def getList(dict, values=None):
    if values == None:
        list = []
        for key in dict.keys():
            list.append(key)
    else:
        list =[]
        for value in dict.values():
            list.append(value["postcode"])
    return list

def form_data_calc(team, pc, vehicle, games):
    if team is not None and pc is not None:
        dest = stadiums[f"{team}"]["Coordinates"]
        for key in postcodes:
            if postcodes[key]["postcode"] == pc:
                origins = f"{postcodes[key]['latitude']},{postcodes[key]['longitude']}"
                url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={dest}&key={api_key}"
                payload={}
                headers = {}
                response = requests.request("GET", url, headers=headers, data=payload)
                response_json = response.json()
                km = response_json['rows'][0]['elements'][0]['distance']['value']
                ef = car_ef['fuel']['petrol']['p_ef'][3]
                km_games = (int(km) * int(games) / 1000)

                if vehicle in ["Walk", "Cycle"]:
                    km_games = 0
                    total = km_games * ef
                    flash(f"The CO2 emitted per season is {total} kgCO2. Wooohooo!")
                else:
                    total = km_games * ef
                    flash(f"The CO2 emitted per season is {total} kgCO2")
    else:
        print("No data")

teams_lst = getList(stadiums)
pc_lst = getList(postcodes, values=True)
travel_mode = ["Car", "Walk", "Cycle"]

@app.route("/", methods=["GET","POST"])
def dropdown():
    form = CarbonCalculator()
    teams = sorted(teams_lst)
    postcode_list = sorted(pc_lst)
    vehicle = sorted(travel_mode)

    form_data_calc(form.teams.data, form.postcodes.data, form.vehicle.data, form.games.data)

    return render_template("layout.html", teams=teams, postcodes=postcode_list, vehicle=vehicle, form=form)