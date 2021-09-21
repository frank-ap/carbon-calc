user_data = {
    "frequency_per_season":[1,10,20,38],
    "travel_mode":["car","taxi","bus","train","cycle","walk"],
    "fuel": ["petrol","diesel","hybrid","electric"],
    "car_size": ["large","medium","small"]
    }

car_ef = {
     "type":['small','medium','large','average'],
     "unit":['CO2e','km','km','km','km'],
     "fuel": {"diesel": { "d_ef": [0.13721,0.16637,0.20419,0.16844],
                          "d_unit": ["kg CO2e"]},
              "petrol": { "p_ef": [0.14836,0.18659,0.27807,0.1743],
                          "p_unit": ["kg CO2e"]},
              "hybrid": { "h_ef" :[0.10275,0.10698,0.1448,0.11558],
                          "h_unit":["kg CO2e"]}
     }  
    
}

user = {"measuring": {"account_id": [1,2,3],
                      "postcode": ["b13", "n15", "e9"]}
}


stadiums = {"Liverpool": {
   "Stadium": "Anfield",
   "Club": "Liverpool",
   "Location": "Liverpool",
   "Capacity": "54,074",
   "Coordinates": "53.430833,-2.960833"
 },
 "Norwich City":
 {
   "Stadium": "Carrow Road",
   "Club": "Norwich City",
   "Location": "Norwich",
   "Capacity": "27,359",
   "Coordinates": "52.622222,1.309167"
 },

 "Manchester City":
 {
   "Stadium": "City of Manchester Stadium",
   "Club": "Manchester City",
   "Location": "Manchester",
   "Capacity": "55,017",
   "Coordinates": "53.483056,-2.200278"
 },
 "Leeds United":
 {
   "Stadium": "Elland Road",
   "Club": "Leeds United",
   "Location": "Leeds",
   "Capacity": "37,792",
   "Coordinates": "53.777778,-1.572222"
 },
 "Arsenal":
 {
   "Stadium": "Emirates Stadium",
   "Club": "Arsenal",
   "Location": "London",
   "Capacity": "60,704",
   "Coordinates": "51.555,-0.108611"
 },
 "Everton":
 {
   "Stadium": "Goodison Park",
   "Club": "Everton",
   "Location": "Liverpool",
   "Capacity": "39,414",
   "Coordinates": "53.438889,-2.966389"
 },
 "Leicester City":
 {
   "Stadium": "King Power Stadium\nFormerly Walkers Stadium",
   "Club": "Leicester City",
   "Location": "Leicester",
   "Capacity": "32,261",
   "Coordinates": "52.620278,-1.142222"
 },
 "West Ham United":
 {
   "Stadium": "London Stadium\nFormerly Olympic Stadium",
   "Club": "West Ham United",
   "Location": "London",
   "Capacity": "60,000",
   "Coordinates": "51.538611,-0.016389"
 },
 "Wolverhampton Wanderers":
 {
   "Stadium": "Molineux Stadium",
   "Club": "Wolverhampton Wanderers",
   "Location": "Wolverhampton",
   "Capacity": "32,050",
   "Coordinates": "52.590278,-2.130278"
 },
 "Manchester United":
 {
   "Stadium": "Old Trafford",
   "Club": "Manchester United",
   "Location": "Manchester",
   "Capacity": "75,643",
   "Coordinates": "53.463056,-2.291389"
 },
 "Newcastle United":
 {
   "Stadium": "St James' Park",
   "Club": "Newcastle United",
   "Location": "Newcastle upon Tyne",
   "Capacity": "52,305",
   "Coordinates": "54.975556,-1.621667"
 },
 "Southampton":
 {
   "Stadium": "St Mary's Stadium",
   "Club": "Southampton",
   "Location": "Southampton",
   "Capacity": "32,384",
   "Coordinates": "50.905833,-1.391111"
 },
 "Crystal Palace":
 {
   "Stadium": "Selhurst Park",
   "Club": "Crystal Palace",
   "Location": "London",
   "Capacity": "25,486",
   "Coordinates": "51.398333,-0.085556"
 },
 "Chelsea":
 {
   "Stadium": "Stamford Bridge",
   "Club": "Chelsea",
   "Location": "London",
   "Capacity": "40,834",
   "Coordinates": "51.481667,-0.191111"
 },
 "Tottenham Hotspur":
 {
   "Stadium": "Tottenham Hotspur Stadium",
   "Club": "Tottenham Hotspur",
   "Location": "London",
   "Capacity": "62,214[37]",
   "Coordinates": "51.604722,-0.066389"
 },
 "Burnley":
 {
   "Stadium": "Turf Moor",
   "Club": "Burnley",
   "Location": "Burnley",
   "Capacity": "21,944",
   "Coordinates": "53.789167,-2.230278"
 },
 "Watford":
 {
   "Stadium": "Vicarage Road",
   "Club": "Watford",
   "Location": "Watford",
   "Capacity": "22,200",
   "Coordinates": "51.65,-0.401667"
 },
 "Aston Villa":
 {
   "Stadium": "Villa Park",
   "Club": "Aston Villa",
   "Location": "Birmingham",
   "Capacity": "42,749",
   "Coordinates": "52.509167,-1.884722"
 },
 "Brentford F.C.":
 {
   "Stadium": "Brentford Community Stadium",
   "Club": "Brentford F.C.",
   "Location": "London",
   "Capacity": "17,250",
   "Coordinates": "51.490825,-0.2887"
 }}

# Postcode data source https://www.freemaptools.com/download-uk-postcode-lat-lng.htm
postcodes = {
   "1": {
      "postcode": "B34",
      "latitude": 52.4964133,
      "longitude": -1.7817039
   },
   "2": {
      "postcode": "IP10",
      "latitude": 52.0189774,
      "longitude": 1.2699895
   },
   "3": {
      "postcode": "G2",
      "latitude": 55.862907,
      "longitude": -4.2561591
   },
   "4": {
      "postcode": "GL19",
      "latitude": 51.9461577,
      "longitude": -2.2909682
   },
   "5": {
      "postcode": "L36",
      "latitude": 53.4144065,
      "longitude": -2.841731
   },
   "6": {
      "postcode": "NE32",
      "latitude": 54.9677908,
      "longitude": -1.4844933
   },
   "7": {
      "postcode": "L12",
      "latitude": 53.4349803,
      "longitude": -2.8958012
   },
   "8": {
      "postcode": "NR28",
      "latitude": 52.8224263,
      "longitude": 1.397492
   },
   "9": {
      "postcode": "SO21",
      "latitude": 51.0753776,
      "longitude": -1.3162444
   },
   "10": {
      "postcode": "CV3",
      "latitude": 52.3909775,
      "longitude": -1.4781403
   },
   "11": {
      "postcode": "TQ10",
      "latitude": 50.4234657,
      "longitude": -3.8260896
   },
   "12": {
      "postcode": "NE37",
      "latitude": 54.9127512,
      "longitude": -1.5279619
   },
   "13": {
      "postcode": "NW11",
      "latitude": 51.5783915,
      "longitude": -0.1974603
   },
   "14": {
      "postcode": "ST14",
      "latitude": 52.9043124,
      "longitude": -1.8699946
   },
   "15": {
      "postcode": "TN35",
      "latitude": 50.8828713,
      "longitude": 0.6140004
   },
   "16": {
      "postcode": "ME7",
      "latitude": 51.379774,
      "longitude": 0.5557972
   },
   "17": {
      "postcode": "BB3",
      "latitude": 53.6978859,
      "longitude": -2.4662858
   },
   "18": {
      "postcode": "SE14",
      "latitude": 51.4758845,
      "longitude": -0.0424768
   },
   "19": {
      "postcode": "WA12",
      "latitude": 53.4533844,
      "longitude": -2.6332824
   },
   "20": {
      "postcode": "GL1",
      "latitude": 51.8593662,
      "longitude": -2.2437389
   },
   "21": {
      "postcode": "EC3R",
      "latitude": 51.5104555,
      "longitude": -0.0835753
   },
   "22": {
      "postcode": "BS6",
      "latitude": 51.4707656,
      "longitude": -2.6003841
   },
   "23": {
      "postcode": "NG22",
      "latitude": 53.1820817,
      "longitude": -0.9786955
   },
   "24": {
      "postcode": "DE22",
      "latitude": 52.9340758,
      "longitude": -1.4996719
   },
   "25": {
      "postcode": "BD6",
      "latitude": 53.7645222,
      "longitude": -1.7861654
   },
   "26": {
      "postcode": "HR1",
      "latitude": 52.0590736,
      "longitude": -2.6797236
   },
   "27": {
      "postcode": "BN10",
      "latitude": 50.7959843,
      "longitude": 0.0013219
   },
   "28": {
      "postcode": "PL17",
      "latitude": 50.5150098,
      "longitude": -4.3103836
   },
   "29": {
      "postcode": "SA6",
      "latitude": 51.6761659,
      "longitude": -3.9226054
   },
   "30": {
      "postcode": "CA15",
      "latitude": 54.7122276,
      "longitude": -3.4809087
   },
   "31": {
      "postcode": "WV13",
      "latitude": 52.5851575,
      "longitude": -2.0581222
   },
   "32": {
      "postcode": "DN1",
      "latitude": 53.5216788,
      "longitude": -1.1307019
   },
   "33": {
      "postcode": "PH36",
      "latitude": 56.7221628,
      "longitude": -5.8512969
   },
   "34": {
      "postcode": "LL12",
      "latitude": 53.0875778,
      "longitude": -2.9891854
   },
   "35": {
      "postcode": "OX14",
      "latitude": 51.667524,
      "longitude": -1.2770907
   },
   "36": {
      "postcode": "CM17",
      "latitude": 51.7731801,
      "longitude": 0.1464635
   },
   "37": {
      "postcode": "TA11",
      "latitude": 51.0605815,
      "longitude": -2.7024096
   },
   "38": {
      "postcode": "WF6",
      "latitude": 53.7003289,
      "longitude": -1.415639
   },
   "39": {
      "postcode": "G23",
      "latitude": 55.9024808,
      "longitude": -4.2851022
   },
   "40": {
      "postcode": "L13",
      "latitude": 53.4184709,
      "longitude": -2.9204372
   },
   "41": {
      "postcode": "GL16",
      "latitude": 51.795578,
      "longitude": -2.6128048
   },
   "42": {
      "postcode": "OL11",
      "latitude": 53.6059003,
      "longitude": -2.1767392
   },
   "43": {
      "postcode": "SN26",
      "latitude": 51.613983,
      "longitude": -1.7881065
   },
   "44": {
      "postcode": "LL47",
      "latitude": 52.9020279,
      "longitude": -4.0628852
   },
   "45": {
      "postcode": "ST17",
      "latitude": 52.7881373,
      "longitude": -2.0991013
   },
   "46": {
      "postcode": "NE99",
      "latitude": 54.970433,
      "longitude": -1.6139305
   },
   "47": {
      "postcode": "DY11",
      "latitude": 52.3845094,
      "longitude": -2.2621081
   },
   "48": {
      "postcode": "ST18",
      "latitude": 52.8150827,
      "longitude": -2.0806107
   },
   "49": {
      "postcode": "DH99",
      "latitude": 54.7882304,
      "longitude": -1.5493991
   },
   "50": {
      "postcode": "PE35",
      "latitude": 52.8271575,
      "longitude": 0.509056
   },
   "51": {
      "postcode": "FK17",
      "latitude": 56.2399069,
      "longitude": -4.219863
   },
   "52": {
      "postcode": "CW12",
      "latitude": 53.1659013,
      "longitude": -2.2135769
   },
   "53": {
      "postcode": "WV2",
      "latitude": 52.5736442,
      "longitude": -2.118343
   },
   "54": {
      "postcode": "NE16",
      "latitude": 54.9312689,
      "longitude": -1.6926762
   },
   "55": {
      "postcode": "DE4",
      "latitude": 53.1268023,
      "longitude": -1.5654429
   },
   "56": {
      "postcode": "BN25",
      "latitude": 50.7765238,
      "longitude": 0.1083361
   },
   "57": {
      "postcode": "NG33",
      "latitude": 52.8165291,
      "longitude": -0.5808488
   },
   "58": {
      "postcode": "GU1",
      "latitude": 51.2430276,
      "longitude": -0.564939
   },
   "59": {
      "postcode": "ML9",
      "latitude": 55.7245642,
      "longitude": -3.9676426
   },
   "60": {
      "postcode": "BT80",
      "latitude": 54.6462975,
      "longitude": -6.74572
   },
   "61": {
      "postcode": "NE65",
      "latitude": 55.3149288,
      "longitude": -1.7484073
   },
   "62": {
      "postcode": "NE7",
      "latitude": 55.0001093,
      "longitude": -1.5797332
   },
   "63": {
      "postcode": "SG8",
      "latitude": 52.0643705,
      "longitude": -0.0147945
   },
   "64": {
      "postcode": "W6",
      "latitude": 51.4926401,
      "longitude": -0.2287797
   },
   "65": {
      "postcode": "DN55",
      "latitude": 53.5129234,
      "longitude": -1.1257209
   },
   "66": {
      "postcode": "FK10",
      "latitude": 56.1158189,
      "longitude": -3.7831309
   },
   "67": {
      "postcode": "M46",
      "latitude": 53.5258654,
      "longitude": -2.4922988
   },
   "68": {
      "postcode": "AB41",
      "latitude": 57.3739596,
      "longitude": -2.1040725
   },
   "69": {
      "postcode": "KA26",
      "latitude": 55.2170854,
      "longitude": -4.8357773
   },
   "70": {
      "postcode": "SN15",
      "latitude": 51.4723,
      "longitude": -2.0830579
   },
   "71": {
      "postcode": "LE16",
      "latitude": 52.4861071,
      "longitude": -0.8959935
   },
   "72": {
      "postcode": "DH4",
      "latitude": 54.8540433,
      "longitude": -1.4925925
   },
   "73": {
      "postcode": "WD99",
      "latitude": 51.648776,
      "longitude": -0.422087
   },
   "74": {
      "postcode": "PH31",
      "latitude": 56.8922176,
      "longitude": -4.8143283
   },
   "75": {
      "postcode": "LL18",
      "latitude": 53.3102991,
      "longitude": -3.4760171
   },
   "76": {
      "postcode": "TF8",
      "latitude": 52.6293306,
      "longitude": -2.4821233
   },
   "77": {
      "postcode": "PA66",
      "latitude": 56.3287392,
      "longitude": -6.3528986
   },
   "78": {
      "postcode": "WD17",
      "latitude": 51.663945,
      "longitude": -0.4056406
   },
   "79": {
      "postcode": "RG17",
      "latitude": 51.4435994,
      "longitude": -1.5030377
   },
   "80": {
      "postcode": "W1S",
      "latitude": 51.5112227,
      "longitude": -0.1423455
   },
   "81": {
      "postcode": "TA7",
      "latitude": 51.131561,
      "longitude": -2.910703
   },
   "82": {
      "postcode": "SY13",
      "latitude": 52.9521685,
      "longitude": -2.6900901
   },
   "83": {
      "postcode": "G53",
      "latitude": 55.8211417,
      "longitude": -4.3526677
   },
   "84": {
      "postcode": "PR8",
      "latitude": 53.6262751,
      "longitude": -3.0097883
   },
   "85": {
      "postcode": "NP11",
      "latitude": 51.6438627,
      "longitude": -3.1315958
   },
   "86": {
      "postcode": "KA12",
      "latitude": 55.6191336,
      "longitude": -4.6651904
   },
   "87": {
      "postcode": "SK10",
      "latitude": 53.2756794,
      "longitude": -2.1312485
   },
   "88": {
      "postcode": "WA8",
      "latitude": 53.3730238,
      "longitude": -2.7415958
   },
   "89": {
      "postcode": "EC2M",
      "latitude": 51.5185932,
      "longitude": -0.0862326
   },
   "90": {
      "postcode": "W13",
      "latitude": 51.5130201,
      "longitude": -0.3212138
   },
   "91": {
      "postcode": "BT12",
      "latitude": 54.5929184,
      "longitude": -5.9584163
   },
   "92": {
      "postcode": "FY4",
      "latitude": 53.7909588,
      "longitude": -3.0275782
   },
   "93": {
      "postcode": "NN4",
      "latitude": 52.2144778,
      "longitude": -0.8994462
   },
   "94": {
      "postcode": "TN27",
      "latitude": 51.1678981,
      "longitude": 0.6938213
   },
   "95": {
      "postcode": "G32",
      "latitude": 55.8488374,
      "longitude": -4.1655409
   },
   "96": {
      "postcode": "DE72",
      "latitude": 52.8931608,
      "longitude": -1.3588522
   },
   "97": {
      "postcode": "SA36",
      "latitude": 51.9577914,
      "longitude": -4.6087195
   },
   "98": {
      "postcode": "BT82",
      "latitude": 54.8264822,
      "longitude": -7.4303378
   },
   "99": {
      "postcode": "WF2",
      "latitude": 53.6723728,
      "longitude": -1.5124139
   },
   "100": {
      "postcode": "LL15",
      "latitude": 53.1031832,
      "longitude": -3.3161613
   },
   "101": {
      "postcode": "SO45",
      "latitude": 50.8468498,
      "longitude": -1.394766
   },
   "102": {
      "postcode": "CR90",
      "latitude": 51.3780681,
      "longitude": -0.113274
   },
   "103": {
      "postcode": "YO15",
      "latitude": 54.094995,
      "longitude": -0.1766616
   },
   "104": {
      "postcode": "LD8",
      "latitude": 52.2645156,
      "longitude": -3.0484652
   },
   "105": {
      "postcode": "WR1",
      "latitude": 52.1956174,
      "longitude": -2.2220478
   },
   "106": {
      "postcode": "RG14",
      "latitude": 51.3994972,
      "longitude": -1.3231202
   },
   "107": {
      "postcode": "OX5",
      "latitude": 51.8306381,
      "longitude": -1.2818093
   },
   "108": {
      "postcode": "PO39",
      "latitude": 50.6803617,
      "longitude": -1.5401345
   },
   "109": {
      "postcode": "AB11",
      "latitude": 57.1392011,
      "longitude": -2.0928839
   },
   "110": {
      "postcode": "TS27",
      "latitude": 54.7239957,
      "longitude": -1.2907917
   },
   "111": {
      "postcode": "HP27",
      "latitude": 51.7206955,
      "longitude": -0.8325872
   },
   "112": {
      "postcode": "BT9",
      "latitude": 54.5721032,
      "longitude": -5.9500064
   },
   "113": {
      "postcode": "SL0",
      "latitude": 51.5259965,
      "longitude": -0.5171775
   },
   "114": {
      "postcode": "NE22",
      "latitude": 55.1351381,
      "longitude": -1.5871076
   },
   "115": {
      "postcode": "LE12",
      "latitude": 52.7677846,
      "longitude": -1.191655
   },
   "116": {
      "postcode": "TR4",
      "latitude": 50.2858425,
      "longitude": -5.1375346
   },
   "117": {
      "postcode": "TS11",
      "latitude": 54.5876196,
      "longitude": -1.0269506
   },
   "118": {
      "postcode": "IG5",
      "latitude": 51.5911739,
      "longitude": 0.063456
   },
   "119": {
      "postcode": "RH5",
      "latitude": 51.1903735,
      "longitude": -0.343837
   },
   "120": {
      "postcode": "TQ1",
      "latitude": 50.4730506,
      "longitude": -3.523599
   },
   "121": {
      "postcode": "LL67",
      "latitude": 53.4111466,
      "longitude": -4.4576366
   },
   "122": {
      "postcode": "LS26",
      "latitude": 53.7518196,
      "longitude": -1.4495543
   },
   "123": {
      "postcode": "LL32",
      "latitude": 53.2580548,
      "longitude": -3.8411359
   },
   "124": {
      "postcode": "LE21",
      "latitude": 52.627845,
      "longitude": -1.1405305
   },
   "125": {
      "postcode": "SA14",
      "latitude": 51.735052,
      "longitude": -4.1062507
   },
   "126": {
      "postcode": "CR7",
      "latitude": 51.3991799,
      "longitude": -0.1067344
   },
   "127": {
      "postcode": "BA6",
      "latitude": 51.1420762,
      "longitude": -2.7078987
   },
   "128": {
      "postcode": "G74",
      "latitude": 55.7689037,
      "longitude": -4.1752217
   },
   "129": {
      "postcode": "IV5",
      "latitude": 57.4684807,
      "longitude": -4.410852
   },
   "130": {
      "postcode": "PA11",
      "latitude": 55.8570966,
      "longitude": -4.5846807
   },
   "131": {
      "postcode": "RH20",
      "latitude": 50.9374494,
      "longitude": -0.4705572
   },
   "132": {
      "postcode": "L5",
      "latitude": 53.4248813,
      "longitude": -2.9771396
   },
   "133": {
      "postcode": "SE26",
      "latitude": 51.4279399,
      "longitude": -0.0547761
   },
   "134": {
      "postcode": "AB16",
      "latitude": 57.1600441,
      "longitude": -2.1566958
   },
   "135": {
      "postcode": "TS25",
      "latitude": 54.6630533,
      "longitude": -1.2252844
   },
   "136": {
      "postcode": "BS15",
      "latitude": 51.4596293,
      "longitude": -2.5068855
   },
   "137": {
      "postcode": "GU19",
      "latitude": 51.3599273,
      "longitude": -0.6919847
   },
   "138": {
      "postcode": "LL51",
      "latitude": 52.9740004,
      "longitude": -4.2389782
   },
   "139": {
      "postcode": "HR2",
      "latitude": 52.0098796,
      "longitude": -2.7854912
   },
   "140": {
      "postcode": "ST15",
      "latitude": 52.9000776,
      "longitude": -2.1504385
   },
   "141": {
      "postcode": "HP19",
      "latitude": 51.8236624,
      "longitude": -0.8280878
   },
   "142": {
      "postcode": "PL33",
      "latitude": 50.6218997,
      "longitude": -4.7316297
   },
   "143": {
      "postcode": "CH5",
      "latitude": 53.2040122,
      "longitude": -3.04214
   },
   "144": {
      "postcode": "TN22",
      "latitude": 50.9820991,
      "longitude": 0.1003886
   },
   "145": {
      "postcode": "LS19",
      "latitude": 53.859728,
      "longitude": -1.6839678
   },
   "146": {
      "postcode": "YO90",
      "latitude": 53.959708,
      "longitude": -1.0902501
   },
   "147": {
      "postcode": "S1",
      "latitude": 53.3800229,
      "longitude": -1.4710499
   },
   "148": {
      "postcode": "DT5",
      "latitude": 50.5488467,
      "longitude": -2.4424653
   },
   "149": {
      "postcode": "PA71",
      "latitude": 56.4806916,
      "longitude": -5.981512
   },
   "150": {
      "postcode": "BA11",
      "latitude": 51.2332006,
      "longitude": -2.3245542
   },
   "151": {
      "postcode": "NR16",
      "latitude": 52.4735481,
      "longitude": 1.0538628
   },
   "152": {
      "postcode": "SW12",
      "latitude": 51.4463283,
      "longitude": -0.1491401
   },
   "153": {
      "postcode": "PL1",
      "latitude": 50.3705757,
      "longitude": -4.154261
   },
   "154": {
      "postcode": "EH54",
      "latitude": 55.8923064,
      "longitude": -3.5243492
   },
   "155": {
      "postcode": "SR2",
      "latitude": 54.8860669,
      "longitude": -1.3765988
   },
   "156": {
      "postcode": "CV31",
      "latitude": 52.2778388,
      "longitude": -1.5246631
   },
   "157": {
      "postcode": "SW4",
      "latitude": 51.4611107,
      "longitude": -0.1364914
   },
   "158": {
      "postcode": "PE1",
      "latitude": 52.5866097,
      "longitude": -0.2380334
   },
   "159": {
      "postcode": "G71",
      "latitude": 55.8223628,
      "longitude": -4.0748284
   },
   "160": {
      "postcode": "LD2",
      "latitude": 52.1422615,
      "longitude": -3.3937041
   },
   "161": {
      "postcode": "DN19",
      "latitude": 53.6841316,
      "longitude": -0.3604471
   },
   "162": {
      "postcode": "KY16",
      "latitude": 56.3425731,
      "longitude": -2.8225656
   },
   "163": {
      "postcode": "NG23",
      "latitude": 53.1163408,
      "longitude": -0.7998116
   },
   "164": {
      "postcode": "KY1",
      "latitude": 56.1288777,
      "longitude": -3.1375619
   },
   "165": {
      "postcode": "BT67",
      "latitude": 54.4869748,
      "longitude": -6.2660667
   },
   "166": {
      "postcode": "SP9",
      "latitude": 51.233459,
      "longitude": -1.6649674
   },
   "167": {
      "postcode": "TQ4",
      "latitude": 50.4228675,
      "longitude": -3.5722576
   },
   "168": {
      "postcode": "M50",
      "latitude": 53.4749848,
      "longitude": -2.2944426
   },
   "169": {
      "postcode": "PA30",
      "latitude": 56.013332,
      "longitude": -5.4494977
   },
   "170": {
      "postcode": "TS29",
      "latitude": 54.7107686,
      "longitude": -1.4202463
   },
   "171": {
      "postcode": "BS13",
      "latitude": 51.4120999,
      "longitude": -2.6119989
   },
   "172": {
      "postcode": "PL9",
      "latitude": 50.3547404,
      "longitude": -4.087228
   },
   "173": {
      "postcode": "LA15",
      "latitude": 54.1558463,
      "longitude": -3.1796666
   },
   "174": {
      "postcode": "DA13",
      "latitude": 51.3784991,
      "longitude": 0.3518275
   },
   "175": {
      "postcode": "BS41",
      "latitude": 51.4220916,
      "longitude": -2.6534866
   },
   "176": {
      "postcode": "TS3",
      "latitude": 54.5605009,
      "longitude": -1.1968742
   },
   "177": {
      "postcode": "G70",
      "latitude": 55.949877,
      "longitude": -3.9879809
   },
   "178": {
      "postcode": "EH17",
      "latitude": 55.9054568,
      "longitude": -3.1436333
   },
   "179": {
      "postcode": "PA38",
      "latitude": 56.5953129,
      "longitude": -5.3282856
   },
   "180": {
      "postcode": "HA6",
      "latitude": 51.6118666,
      "longitude": -0.4224386
   },
   "181": {
      "postcode": "IV15",
      "latitude": 57.5993429,
      "longitude": -4.4314883
   },
   "182": {
      "postcode": "BT16",
      "latitude": 54.5906801,
      "longitude": -5.7976783
   },
   "183": {
      "postcode": "GU16",
      "latitude": 51.3095532,
      "longitude": -0.7260287
   },
   "184": {
      "postcode": "DD10",
      "latitude": 56.7487217,
      "longitude": -2.4270468
   },
   "185": {
      "postcode": "BH14",
      "latitude": 50.7214367,
      "longitude": -1.9445851
   },
   "186": {
      "postcode": "PH10",
      "latitude": 56.6069517,
      "longitude": -3.3593082
   },
   "187": {
      "postcode": "N14",
      "latitude": 51.6343428,
      "longitude": -0.1308896
   },
   "188": {
      "postcode": "B15",
      "latitude": 52.4661665,
      "longitude": -1.9233802
   },
   "189": {
      "postcode": "SS17",
      "latitude": 51.5216078,
      "longitude": 0.4376424
   },
   "190": {
      "postcode": "KA1",
      "latitude": 55.595248,
      "longitude": -4.4975073
   },
   "191": {
      "postcode": "TW15",
      "latitude": 51.4311588,
      "longitude": -0.4585262
   },
   "192": {
      "postcode": "SP6",
      "latitude": 50.9365589,
      "longitude": -1.8023782
   },
   "193": {
      "postcode": "BH25",
      "latitude": 50.75283,
      "longitude": -1.6579866
   },
   "194": {
      "postcode": "CA12",
      "latitude": 54.6025378,
      "longitude": -3.1344633
   },
   "195": {
      "postcode": "AB51",
      "latitude": 57.2876297,
      "longitude": -2.403827
   },
   "196": {
      "postcode": "TN26",
      "latitude": 51.0964754,
      "longitude": 0.797358
   },
   "197": {
      "postcode": "NE42",
      "latitude": 54.9620117,
      "longitude": -1.8548407
   },
   "198": {
      "postcode": "NE70",
      "latitude": 55.593707,
      "longitude": -1.8171698
   },
   "199": {
      "postcode": "BD9",
      "latitude": 53.8128852,
      "longitude": -1.7924051
   },
   "200": {
      "postcode": "EX39",
      "latitude": 51.015257,
      "longitude": -4.2457737
   },
   "201": {
      "postcode": "WS6",
      "latitude": 52.6585504,
      "longitude": -2.0231546
   },
   "202": {
      "postcode": "G4",
      "latitude": 55.8676044,
      "longitude": -4.2523731
   },
   "203": {
      "postcode": "GU4",
      "latitude": 51.2432497,
      "longitude": -0.5403949
   },
   "204": {
      "postcode": "NE18",
      "latitude": 55.0378909,
      "longitude": -1.8649114
   },
   "205": {
      "postcode": "G9",
      "latitude": 55.86874,
      "longitude": -4.243491
   },
   "206": {
      "postcode": "CV12",
      "latitude": 52.4789841,
      "longitude": -1.4724008
   },
   "207": {
      "postcode": "BT40",
      "latitude": 54.8457073,
      "longitude": -5.8237859
   },
   "208": {
      "postcode": "B3",
      "latitude": 52.4850123,
      "longitude": -1.9024305
   },
   "209": {
      "postcode": "WF11",
      "latitude": 53.7117458,
      "longitude": -1.2561796
   },
   "210": {
      "postcode": "PO13",
      "latitude": 50.8122549,
      "longitude": -1.1810192
   },
   "211": {
      "postcode": "YO12",
      "latitude": 54.273341,
      "longitude": -0.4249517
   },
   "212": {
      "postcode": "NE27",
      "latitude": 55.0329496,
      "longitude": -1.5149818
   },
   "213": {
      "postcode": "SE28",
      "latitude": 51.5023617,
      "longitude": 0.104435
   },
   "214": {
      "postcode": "WS1",
      "latitude": 52.5794509,
      "longitude": -1.9786869
   },
   "215": {
      "postcode": "BN3",
      "latitude": 50.8352718,
      "longitude": -0.1777197
   },
   "216": {
      "postcode": "CH32",
      "latitude": 53.3619659,
      "longitude": -2.9976234
   },
   "217": {
      "postcode": "ME17",
      "latitude": 51.2331334,
      "longitude": 0.6111241
   },
   "218": {
      "postcode": "M30",
      "latitude": 53.4843432,
      "longitude": -2.3551494
   },
   "219": {
      "postcode": "CB11",
      "latitude": 51.9992272,
      "longitude": 0.2120024
   },
   "220": {
      "postcode": "S70",
      "latitude": 53.5411537,
      "longitude": -1.4749041
   },
   "221": {
      "postcode": "CA23",
      "latitude": 54.5152203,
      "longitude": -3.4929534
   },
   "222": {
      "postcode": "TA18",
      "latitude": 50.8829255,
      "longitude": -2.7874829
   },
   "223": {
      "postcode": "TR19",
      "latitude": 50.1001216,
      "longitude": -5.6316273
   },
   "224": {
      "postcode": "GU47",
      "latitude": 51.3494201,
      "longitude": -0.7920355
   },
   "225": {
      "postcode": "CB8",
      "latitude": 52.2302078,
      "longitude": 0.4279081
   },
   "226": {
      "postcode": "LN5",
      "latitude": 53.1742178,
      "longitude": -0.5568934
   },
   "227": {
      "postcode": "TN11",
      "latitude": 51.2070078,
      "longitude": 0.2646847
   },
   "228": {
      "postcode": "NE47",
      "latitude": 54.9286141,
      "longitude": -2.2549406
   },
   "229": {
      "postcode": "WC2N",
      "latitude": 51.509081,
      "longitude": -0.1248873
   },
   "230": {
      "postcode": "WS14",
      "latitude": 52.6640162,
      "longitude": -1.8161526
   },
   "231": {
      "postcode": "RG21",
      "latitude": 51.2648843,
      "longitude": -1.0886279
   },
   "232": {
      "postcode": "IP29",
      "latitude": 52.190897,
      "longitude": 0.6587294
   },
   "233": {
      "postcode": "LS18",
      "latitude": 53.8386122,
      "longitude": -1.6395178
   },
   "234": {
      "postcode": "CF14",
      "latitude": 51.5198959,
      "longitude": -3.2042721
   },
   "235": {
      "postcode": "SY8",
      "latitude": 52.3650723,
      "longitude": -2.6953443
   },
   "236": {
      "postcode": "TD6",
      "latitude": 55.5818814,
      "longitude": -2.6932118
   },
   "237": {
      "postcode": "KW16",
      "latitude": 58.9608956,
      "longitude": -3.2768723
   },
   "238": {
      "postcode": "SA73",
      "latitude": 51.7174251,
      "longitude": -5.0122032
   },
   "239": {
      "postcode": "AB56",
      "latitude": 57.6743925,
      "longitude": -2.9288909
   },
   "240": {
      "postcode": "TW10",
      "latitude": 51.4477641,
      "longitude": -0.3029046
   },
   "241": {
      "postcode": "DG16",
      "latitude": 54.9971615,
      "longitude": -3.0685694
   },
   "242": {
      "postcode": "WC1A",
      "latitude": 51.5201536,
      "longitude": -0.1203458
   },
   "243": {
      "postcode": "SR7",
      "latitude": 54.8304225,
      "longitude": -1.3630969
   },
   "244": {
      "postcode": "EX10",
      "latitude": 50.6931776,
      "longitude": -3.2466004
   },
   "245": {
      "postcode": "PH33",
      "latitude": 56.8218973,
      "longitude": -5.1122203
   },
   "246": {
      "postcode": "S43",
      "latitude": 53.2676283,
      "longitude": -1.3399055
   },
   "247": {
      "postcode": "B91",
      "latitude": 52.4139981,
      "longitude": -1.7833291
   },
   "248": {
      "postcode": "DA14",
      "latitude": 51.4250037,
      "longitude": 0.1117751
   },
   "249": {
      "postcode": "DL3",
      "latitude": 54.5324842,
      "longitude": -1.5715984
   },
   "250": {
      "postcode": "TR2",
      "latitude": 50.2545424,
      "longitude": -4.9504488
   },
   "251": {
      "postcode": "RM15",
      "latitude": 51.5087484,
      "longitude": 0.2762291
   },
   "252": {
      "postcode": "B30",
      "latitude": 52.421961,
      "longitude": -1.9277595
   },
   "253": {
      "postcode": "RG12",
      "latitude": 51.4067523,
      "longitude": -0.7500218
   },
   "254": {
      "postcode": "WN8",
      "latitude": 53.5531891,
      "longitude": -2.7694762
   },
   "255": {
      "postcode": "DN40",
      "latitude": 53.6210283,
      "longitude": -0.2267379
   },
   "256": {
      "postcode": "GL4",
      "latitude": 51.8406968,
      "longitude": -2.2188091
   },
   "257": {
      "postcode": "W1G",
      "latitude": 51.5193162,
      "longitude": -0.1482679
   },
   "258": {
      "postcode": "EH3",
      "latitude": 55.9519117,
      "longitude": -3.2070932
   },
   "259": {
      "postcode": "CV32",
      "latitude": 52.2979862,
      "longitude": -1.531491
   },
   "260": {
      "postcode": "M35",
      "latitude": 53.5072006,
      "longitude": -2.1549109
   },
   "261": {
      "postcode": "LS88",
      "latitude": 53.7653158,
      "longitude": -1.5014304
   },
   "262": {
      "postcode": "SA33",
      "latitude": 51.8495123,
      "longitude": -4.4408804
   },
   "263": {
      "postcode": "BN12",
      "latitude": 50.8139666,
      "longitude": -0.4292747
   },
   "264": {
      "postcode": "CH49",
      "latitude": 53.3810989,
      "longitude": -3.1039353
   },
   "265": {
      "postcode": "BT7",
      "latitude": 54.5819589,
      "longitude": -5.9245497
   },
   "266": {
      "postcode": "SW14",
      "latitude": 51.4653809,
      "longitude": -0.2669998
   },
   "267": {
      "postcode": "HS4",
      "latitude": 57.87087,
      "longitude": -6.6963068
   },
   "268": {
      "postcode": "IV12",
      "latitude": 57.5743529,
      "longitude": -3.8644897
   },
   "269": {
      "postcode": "E11",
      "latitude": 51.5686864,
      "longitude": 0.0135501
   },
   "270": {
      "postcode": "WR6",
      "latitude": 52.2298799,
      "longitude": -2.3821575
   },
   "271": {
      "postcode": "BS9",
      "latitude": 51.487328,
      "longitude": -2.6267518
   },
   "272": {
      "postcode": "BH4",
      "latitude": 50.7212551,
      "longitude": -1.8997372
   },
   "273": {
      "postcode": "NP7",
      "latitude": 51.8294388,
      "longitude": -3.0112466
   },
   "274": {
      "postcode": "DA10",
      "latitude": 51.4417805,
      "longitude": 0.3049871
   },
   "275": {
      "postcode": "OX28",
      "latitude": 51.7869462,
      "longitude": -1.4860576
   },
   "276": {
      "postcode": "NE83",
      "latitude": 54.93464,
      "longitude": -1.6151031
   },
   "277": {
      "postcode": "TD5",
      "latitude": 55.5881056,
      "longitude": -2.4173178
   },
   "278": {
      "postcode": "YO41",
      "latitude": 53.9705289,
      "longitude": -0.9005201
   },
   "279": {
      "postcode": "WN2",
      "latitude": 53.5359217,
      "longitude": -2.5821236
   },
   "280": {
      "postcode": "NN9",
      "latitude": 52.3345261,
      "longitude": -0.5945016
   },
   "281": {
      "postcode": "LN7",
      "latitude": 53.493235,
      "longitude": -0.3455524
   },
   "282": {
      "postcode": "SO25",
      "latitude": 51.0675552,
      "longitude": -1.2973027
   },
   "283": {
      "postcode": "CB6",
      "latitude": 52.4046657,
      "longitude": 0.2216208
   },
   "284": {
      "postcode": "NE4",
      "latitude": 54.9739843,
      "longitude": -1.6445129
   },
   "285": {
      "postcode": "CH31",
      "latitude": 53.3297,
      "longitude": -3.0988332
   },
   "286": {
      "postcode": "BB10",
      "latitude": 53.7995625,
      "longitude": -2.2195134
   },
   "287": {
      "postcode": "N21",
      "latitude": 51.6366698,
      "longitude": -0.0997398
   },
   "288": {
      "postcode": "BT77",
      "latitude": 54.4273568,
      "longitude": -7.1188959
   },
   "289": {
      "postcode": "IV49",
      "latitude": 57.2290084,
      "longitude": -5.9436275
   },
   "290": {
      "postcode": "WC1X",
      "latitude": 51.5266751,
      "longitude": -0.1151125
   },
   "291": {
      "postcode": "PL15",
      "latitude": 50.6330692,
      "longitude": -4.3969382
   },
   "292": {
      "postcode": "DH8",
      "latitude": 54.8569909,
      "longitude": -1.8504107
   },
   "293": {
      "postcode": "PH24",
      "latitude": 57.2561205,
      "longitude": -3.7449612
   },
   "294": {
      "postcode": "IV44",
      "latitude": 57.1087675,
      "longitude": -5.8827494
   },
   "295": {
      "postcode": "NE9",
      "latitude": 54.9313591,
      "longitude": -1.5854323
   },
   "296": {
      "postcode": "GU51",
      "latitude": 51.2843531,
      "longitude": -0.8424509
   },
   "297": {
      "postcode": "RG4",
      "latitude": 51.4827626,
      "longitude": -0.9698039
   },
   "298": {
      "postcode": "WC2E",
      "latitude": 51.5118792,
      "longitude": -0.1233747
   },
   "299": {
      "postcode": "GL20",
      "latitude": 52.0022332,
      "longitude": -2.132268
   },
   "300": {
      "postcode": "TW14",
      "latitude": 51.4533965,
      "longitude": -0.4217772
   },
   "301": {
      "postcode": "TD9",
      "latitude": 55.3973065,
      "longitude": -2.7767413
   },
   "302": {
      "postcode": "CA4",
      "latitude": 54.8471428,
      "longitude": -2.8318231
   },
   "303": {
      "postcode": "GL13",
      "latitude": 51.692474,
      "longitude": -2.4613325
   },
   "304": {
      "postcode": "SA13",
      "latitude": 51.6057851,
      "longitude": -3.7258236
   },
   "305": {
      "postcode": "CM6",
      "latitude": 51.8783006,
      "longitude": 0.3661906
   },
   "306": {
      "postcode": "ME18",
      "latitude": 51.2417887,
      "longitude": 0.4154143
   },
   "307": {
      "postcode": "SL1",
      "latitude": 51.5178471,
      "longitude": -0.6222163
   },
   "308": {
      "postcode": "HP3",
      "latitude": 51.7359452,
      "longitude": -0.4707053
   },
   "309": {
      "postcode": "SA68",
      "latitude": 51.7295615,
      "longitude": -4.7650739
   },
   "310": {
      "postcode": "M45",
      "latitude": 53.5473467,
      "longitude": -2.2903765
   },
   "311": {
      "postcode": "TN9",
      "latitude": 51.1916379,
      "longitude": 0.2749493
   },
   "312": {
      "postcode": "LL41",
      "latitude": 52.9694465,
      "longitude": -3.9393403
   },
   "313": {
      "postcode": "PA72",
      "latitude": 56.5183484,
      "longitude": -5.9661761
   },
   "314": {
      "postcode": "CT1",
      "latitude": 51.2776176,
      "longitude": 1.0859171
   },
   "315": {
      "postcode": "CW3",
      "latitude": 52.9979416,
      "longitude": -2.4084452
   },
   "316": {
      "postcode": "B6",
      "latitude": 52.5051401,
      "longitude": -1.8860786
   },
   "317": {
      "postcode": "SW1X",
      "latitude": 51.4982019,
      "longitude": -0.1566313
   },
   "318": {
      "postcode": "N17",
      "latitude": 51.5980699,
      "longitude": -0.0717424
   },
   "319": {
      "postcode": "EN11",
      "latitude": 51.7655817,
      "longitude": -0.0091349
   },
   "320": {
      "postcode": "SY2",
      "latitude": 52.705579,
      "longitude": -2.729248
   },
   "321": {
      "postcode": "LL52",
      "latitude": 52.9248691,
      "longitude": -4.2409055
   },
   "322": {
      "postcode": "ML7",
      "latitude": 55.8299394,
      "longitude": -3.7954225
   },
   "323": {
      "postcode": "KW7",
      "latitude": 58.1867247,
      "longitude": -3.5017376
   },
   "324": {
      "postcode": "OX18",
      "latitude": 51.7628074,
      "longitude": -1.5916671
   },
   "325": {
      "postcode": "HU15",
      "latitude": 53.7485753,
      "longitude": -0.6207806
   },
   "326": {
      "postcode": "HR8",
      "latitude": 52.0447156,
      "longitude": -2.4453658
   },
   "327": {
      "postcode": "SP8",
      "latitude": 51.0373048,
      "longitude": -2.2910983
   },
   "328": {
      "postcode": "BR1",
      "latitude": 51.4119969,
      "longitude": 0.0208833
   },
   "329": {
      "postcode": "KY99",
      "latitude": 56.0529028,
      "longitude": -3.4360203
   },
   "330": {
      "postcode": "CH60",
      "latitude": 53.32649,
      "longitude": -3.0960749
   },
   "331": {
      "postcode": "BD13",
      "latitude": 53.7867466,
      "longitude": -1.8612838
   },
   "332": {
      "postcode": "GL52",
      "latitude": 51.9190904,
      "longitude": -2.0581561
   },
   "333": {
      "postcode": "WS2",
      "latitude": 52.5892854,
      "longitude": -2.0043778
   },
   "334": {
      "postcode": "NE69",
      "latitude": 55.6047765,
      "longitude": -1.7187958
   },
   "335": {
      "postcode": "L30",
      "latitude": 53.4845057,
      "longitude": -2.9725553
   },
   "336": {
      "postcode": "PH6",
      "latitude": 56.3717976,
      "longitude": -3.9999352
   },
   "337": {
      "postcode": "KT22",
      "latitude": 51.3015607,
      "longitude": -0.3393496
   },
   "338": {
      "postcode": "PH42",
      "latitude": 56.9018804,
      "longitude": -6.1427489
   },
   "339": {
      "postcode": "ZE1",
      "latitude": 60.1514981,
      "longitude": -1.1705115
   },
   "340": {
      "postcode": "SG10",
      "latitude": 51.8467689,
      "longitude": 0.0754693
   },
   "341": {
      "postcode": "DA3",
      "latitude": 51.3841204,
      "longitude": 0.3083751
   },
   "342": {
      "postcode": "LL63",
      "latitude": 53.2184987,
      "longitude": -4.4722288
   },
   "343": {
      "postcode": "PH20",
      "latitude": 57.056667,
      "longitude": -4.147518
   },
   "344": {
      "postcode": "CT19",
      "latitude": 51.0890794,
      "longitude": 1.1679444
   },
   "345": {
      "postcode": "NG13",
      "latitude": 52.9486758,
      "longitude": -0.9073222
   },
   "346": {
      "postcode": "NR99",
      "latitude": 52.6266507,
      "longitude": 1.3092653
   },
   "347": {
      "postcode": "LU7",
      "latitude": 51.9072379,
      "longitude": -0.6629591
   },
   "348": {
      "postcode": "AL7",
      "latitude": 51.7969028,
      "longitude": -0.1872378
   },
   "349": {
      "postcode": "HP22",
      "latitude": 51.8076076,
      "longitude": -0.7693074
   },
   "350": {
      "postcode": "WD6",
      "latitude": 51.6573773,
      "longitude": -0.2756334
   },
   "351": {
      "postcode": "PE14",
      "latitude": 52.6392767,
      "longitude": 0.2075469
   },
   "352": {
      "postcode": "B40",
      "latitude": 52.4569283,
      "longitude": -1.7225262
   },
   "353": {
      "postcode": "N22",
      "latitude": 51.5998948,
      "longitude": -0.1102841
   },
   "354": {
      "postcode": "BD17",
      "latitude": 53.8475875,
      "longitude": -1.768364
   },
   "355": {
      "postcode": "CO3",
      "latitude": 51.88449,
      "longitude": 0.8563017
   },
   "356": {
      "postcode": "IP27",
      "latitude": 52.4302192,
      "longitude": 0.5819065
   },
   "357": {
      "postcode": "NP22",
      "latitude": 51.7712366,
      "longitude": -3.2581432
   },
   "358": {
      "postcode": "SG14",
      "latitude": 51.8081282,
      "longitude": -0.0940096
   },
   "359": {
      "postcode": "BT20",
      "latitude": 54.6585904,
      "longitude": -5.665505
   },
   "360": {
      "postcode": "M23",
      "latitude": 53.399557,
      "longitude": -2.288912
   },
   "361": {
      "postcode": "MK45",
      "latitude": 52.0216132,
      "longitude": -0.4703173
   },
   "362": {
      "postcode": "BD5",
      "latitude": 53.7781758,
      "longitude": -1.7591405
   },
   "363": {
      "postcode": "CH42",
      "latitude": 53.3738774,
      "longitude": -3.0227343
   },
   "364": {
      "postcode": "PA48",
      "latitude": 55.7384868,
      "longitude": -6.3848707
   },
   "365": {
      "postcode": "S64",
      "latitude": 53.4907312,
      "longitude": -1.2988429
   },
   "366": {
      "postcode": "B20",
      "latitude": 52.515504,
      "longitude": -1.9192015
   },
   "367": {
      "postcode": "LN10",
      "latitude": 53.1584629,
      "longitude": -0.2171187
   },
   "368": {
      "postcode": "LL44",
      "latitude": 52.7909039,
      "longitude": -4.0972031
   },
   "369": {
      "postcode": "SA41",
      "latitude": 51.9952157,
      "longitude": -4.7058717
   },
   "370": {
      "postcode": "TW7",
      "latitude": 51.4730054,
      "longitude": -0.3358063
   },
   "371": {
      "postcode": "TN16",
      "latitude": 51.2930684,
      "longitude": 0.0517089
   },
   "372": {
      "postcode": "CH33",
      "latitude": 53.2905598,
      "longitude": -3.0626386
   },
   "373": {
      "postcode": "IV99",
      "latitude": 57.481332,
      "longitude": -4.2239504
   },
   "374": {
      "postcode": "WV98",
      "latitude": 52.4053675,
      "longitude": -2.2199919
   },
   "375": {
      "postcode": "BT37",
      "latitude": 54.6775107,
      "longitude": -5.9080795
   },
   "376": {
      "postcode": "SW11",
      "latitude": 51.4681801,
      "longitude": -0.1637256
   },
   "377": {
      "postcode": "PH18",
      "latitude": 56.7731976,
      "longitude": -3.8901941
   },
   "378": {
      "postcode": "SA5",
      "latitude": 51.6489448,
      "longitude": -3.9712026
   },
   "379": {
      "postcode": "S13",
      "latitude": 53.3646431,
      "longitude": -1.3836802
   },
   "380": {
      "postcode": "NR4",
      "latitude": 52.612059,
      "longitude": 1.256665
   },
   "381": {
      "postcode": "BN27",
      "latitude": 50.8718389,
      "longitude": 0.2634568
   },
   "382": {
      "postcode": "W8",
      "latitude": 51.5011337,
      "longitude": -0.1943202
   },
   "383": {
      "postcode": "HU12",
      "latitude": 53.7238645,
      "longitude": -0.1267684
   },
   "384": {
      "postcode": "KY9",
      "latitude": 56.2091528,
      "longitude": -2.8357263
   },
   "385": {
      "postcode": "CT50",
      "latitude": 51.0795333,
      "longitude": 1.1435601
   },
   "386": {
      "postcode": "PO41",
      "latitude": 50.7009701,
      "longitude": -1.4750973
   },
   "387": {
      "postcode": "PL30",
      "latitude": 50.5017989,
      "longitude": -4.7283944
   },
   "388": {
      "postcode": "SY21",
      "latitude": 52.6581949,
      "longitude": -3.2070323
   },
   "389": {
      "postcode": "GU25",
      "latitude": 51.4011369,
      "longitude": -0.5718272
   },
   "390": {
      "postcode": "SW1E",
      "latitude": 51.4979064,
      "longitude": -0.1397427
   },
   "391": {
      "postcode": "DN38",
      "latitude": 53.5604981,
      "longitude": -0.3911523
   },
   "392": {
      "postcode": "SA8",
      "latitude": 51.7217976,
      "longitude": -3.8477059
   },
   "393": {
      "postcode": "YO61",
      "latitude": 54.1179291,
      "longitude": -1.1960242
   },
   "394": {
      "postcode": "PA5",
      "latitude": 55.8310416,
      "longitude": -4.5097445
   },
   "395": {
      "postcode": "EH55",
      "latitude": 55.8464431,
      "longitude": -3.5752962
   },
   "396": {
      "postcode": "NR17",
      "latitude": 52.5153469,
      "longitude": 0.9944934
   },
   "397": {
      "postcode": "SG6",
      "latitude": 51.9790227,
      "longitude": -0.2227304
   },
   "398": {
      "postcode": "EX15",
      "latitude": 50.8776038,
      "longitude": -3.3405027
   },
   "399": {
      "postcode": "TF9",
      "latitude": 52.8968634,
      "longitude": -2.4700531
   },
   "400": {
      "postcode": "IP33",
      "latitude": 52.2429658,
      "longitude": 0.7086249
   },
   "401": {
      "postcode": "NE13",
      "latitude": 55.0437667,
      "longitude": -1.6474838
   },
   "402": {
      "postcode": "SY5",
      "latitude": 52.6515091,
      "longitude": -2.8328135
   },
   "403": {
      "postcode": "S95",
      "latitude": 53.4184381,
      "longitude": -1.403692
   },
   "404": {
      "postcode": "YO19",
      "latitude": 53.905948,
      "longitude": -1.0207826
   },
   "405": {
      "postcode": "BT22",
      "latitude": 54.5017687,
      "longitude": -5.5145457
   },
   "406": {
      "postcode": "NW8",
      "latitude": 51.5322682,
      "longitude": -0.1745786
   },
   "407": {
      "postcode": "SG2",
      "latitude": 51.8965414,
      "longitude": -0.1640911
   },
   "408": {
      "postcode": "PO6",
      "latitude": 50.846598,
      "longitude": -1.0700466
   },
   "409": {
      "postcode": "PA43",
      "latitude": 55.7556052,
      "longitude": -6.2841924
   },
   "410": {
      "postcode": "LS27",
      "latitude": 53.7486959,
      "longitude": -1.6035106
   },
   "411": {
      "postcode": "KA17",
      "latitude": 55.6106607,
      "longitude": -4.2791346
   },
   "412": {
      "postcode": "LS10",
      "latitude": 53.7622905,
      "longitude": -1.5325445
   },
   "413": {
      "postcode": "LL28",
      "latitude": 53.2878956,
      "longitude": -3.7618075
   },
   "414": {
      "postcode": "SG9",
      "latitude": 51.9507491,
      "longitude": -0.0091601
   },
   "415": {
      "postcode": "SO31",
      "latitude": 50.8700098,
      "longitude": -1.2998114
   },
   "416": {
      "postcode": "LL64",
      "latitude": 53.2287185,
      "longitude": -4.5183068
   },
   "417": {
      "postcode": "OL15",
      "latitude": 53.6448116,
      "longitude": -2.0999458
   },
   "418": {
      "postcode": "SE23",
      "latitude": 51.4414858,
      "longitude": -0.0491513
   },
   "419": {
      "postcode": "WA1",
      "latitude": 53.3942536,
      "longitude": -2.5714198
   },
   "420": {
      "postcode": "IV7",
      "latitude": 57.5832458,
      "longitude": -4.3867307
   },
   "421": {
      "postcode": "BT45",
      "latitude": 54.7600743,
      "longitude": -6.6390822
   },
   "422": {
      "postcode": "ME99",
      "latitude": 51.2783241,
      "longitude": 0.5190996
   },
   "423": {
      "postcode": "OL9",
      "latitude": 53.5391534,
      "longitude": -2.1442485
   },
   "424": {
      "postcode": "PE21",
      "latitude": 52.9744837,
      "longitude": -0.0238791
   },
   "425": {
      "postcode": "SP7",
      "latitude": 51.0050805,
      "longitude": -2.1843108
   },
   "426": {
      "postcode": "CF83",
      "latitude": 51.5867146,
      "longitude": -3.2188145
   },
   "427": {
      "postcode": "PR4",
      "latitude": 53.7546364,
      "longitude": -2.8341777
   },
   "428": {
      "postcode": "YO32",
      "latitude": 54.0124771,
      "longitude": -1.0593934
   },
   "429": {
      "postcode": "M31",
      "latitude": 53.4194153,
      "longitude": -2.4242176
   },
   "430": {
      "postcode": "CT14",
      "latitude": 51.2167502,
      "longitude": 1.3854115
   },
   "431": {
      "postcode": "TF6",
      "latitude": 52.7362755,
      "longitude": -2.5560077
   },
   "432": {
      "postcode": "AL5",
      "latitude": 51.8153821,
      "longitude": -0.3520548
   },
   "433": {
      "postcode": "IG7",
      "latitude": 51.6143123,
      "longitude": 0.0956944
   },
   "434": {
      "postcode": "EX18",
      "latitude": 50.9020189,
      "longitude": -3.8876032
   },
   "435": {
      "postcode": "CH62",
      "latitude": 53.334283,
      "longitude": -2.981572
   },
   "436": {
      "postcode": "HG4",
      "latitude": 54.1569575,
      "longitude": -1.5666498
   },
   "437": {
      "postcode": "S44",
      "latitude": 53.2252186,
      "longitude": -1.3139748
   },
   "438": {
      "postcode": "PO16",
      "latitude": 50.8508807,
      "longitude": -1.1591621
   },
   "439": {
      "postcode": "PO3",
      "latitude": 50.8162998,
      "longitude": -1.059158
   },
   "440": {
      "postcode": "CR5",
      "latitude": 51.311096,
      "longitude": -0.1414477
   },
   "441": {
      "postcode": "N81",
      "latitude": 51.5663135,
      "longitude": -0.0767356
   },
   "442": {
      "postcode": "PO40",
      "latitude": 50.6824755,
      "longitude": -1.5218166
   },
   "443": {
      "postcode": "KT9",
      "latitude": 51.3639202,
      "longitude": -0.3032309
   },
   "444": {
      "postcode": "EX13",
      "latitude": 50.7871097,
      "longitude": -3.0071442
   },
   "445": {
      "postcode": "MK4",
      "latitude": 52.0040459,
      "longitude": -0.7842687
   },
   "446": {
      "postcode": "PO22",
      "latitude": 50.8001082,
      "longitude": -0.6476773
   },
   "447": {
      "postcode": "PL24",
      "latitude": 50.3552292,
      "longitude": -4.7111784
   },
   "448": {
      "postcode": "B18",
      "latitude": 52.4913461,
      "longitude": -1.9255863
   },
   "449": {
      "postcode": "IV19",
      "latitude": 57.8039848,
      "longitude": -4.0627885
   },
   "450": {
      "postcode": "EH34",
      "latitude": 55.9082618,
      "longitude": -2.8808453
   },
   "451": {
      "postcode": "BS8",
      "latitude": 51.4575672,
      "longitude": -2.6221985
   },
   "452": {
      "postcode": "G46",
      "latitude": 55.8033439,
      "longitude": -4.3078361
   },
   "453": {
      "postcode": "SA63",
      "latitude": 51.8742755,
      "longitude": -4.8563094
   },
   "454": {
      "postcode": "PR11",
      "latitude": 53.7945597,
      "longitude": -2.6849868
   },
   "455": {
      "postcode": "CW98",
      "latitude": 53.0886586,
      "longitude": -2.4311449
   },
   "456": {
      "postcode": "NW2",
      "latitude": 51.5581501,
      "longitude": -0.2202562
   },
   "457": {
      "postcode": "TN7",
      "latitude": 51.0960303,
      "longitude": 0.1026001
   },
   "458": {
      "postcode": "G84",
      "latitude": 56.0141483,
      "longitude": -4.7557604
   },
   "459": {
      "postcode": "SM3",
      "latitude": 51.3712541,
      "longitude": -0.2162485
   },
   "460": {
      "postcode": "RH13",
      "latitude": 51.0337894,
      "longitude": -0.3279851
   },
   "461": {
      "postcode": "PL7",
      "latitude": 50.3927332,
      "longitude": -4.0456918
   },
   "462": {
      "postcode": "EH27",
      "latitude": 55.8907993,
      "longitude": -3.416388
   },
   "463": {
      "postcode": "BT13",
      "latitude": 54.6058982,
      "longitude": -5.9596444
   },
   "464": {
      "postcode": "TD7",
      "latitude": 55.5365991,
      "longitude": -2.8730161
   },
   "465": {
      "postcode": "NG2",
      "latitude": 52.9348691,
      "longitude": -1.1344936
   },
   "466": {
      "postcode": "LS6",
      "latitude": 53.8200966,
      "longitude": -1.5707608
   },
   "467": {
      "postcode": "NG8",
      "latitude": 52.9649766,
      "longitude": -1.2134133
   },
   "468": {
      "postcode": "CA8",
      "latitude": 54.9394064,
      "longitude": -2.686449
   },
   "469": {
      "postcode": "RG8",
      "latitude": 51.5062415,
      "longitude": -1.1063426
   },
   "470": {
      "postcode": "SK1",
      "latitude": 53.4075932,
      "longitude": -2.1515586
   },
   "471": {
      "postcode": "KY7",
      "latitude": 56.1977936,
      "longitude": -3.1580986
   },
   "472": {
      "postcode": "GU10",
      "latitude": 51.1965791,
      "longitude": -0.7979139
   },
   "473": {
      "postcode": "CH30",
      "latitude": 53.3789453,
      "longitude": -3.0984344
   },
   "474": {
      "postcode": "CF39",
      "latitude": 51.5999318,
      "longitude": -3.4255613
   },
   "475": {
      "postcode": "WD18",
      "latitude": 51.6491262,
      "longitude": -0.4146492
   },
   "476": {
      "postcode": "BD8",
      "latitude": 53.8017321,
      "longitude": -1.7839736
   },
   "477": {
      "postcode": "S61",
      "latitude": 53.4441131,
      "longitude": -1.3949172
   },
   "478": {
      "postcode": "DG1",
      "latitude": 55.0735752,
      "longitude": -3.5817215
   },
   "479": {
      "postcode": "IV16",
      "latitude": 57.6647729,
      "longitude": -4.3379167
   },
   "480": {
      "postcode": "GL55",
      "latitude": 52.0639021,
      "longitude": -1.7695409
   },
   "481": {
      "postcode": "E1",
      "latitude": 51.5173859,
      "longitude": -0.0595023
   },
   "482": {
      "postcode": "CM12",
      "latitude": 51.6282277,
      "longitude": 0.4145027
   },
   "483": {
      "postcode": "HX6",
      "latitude": 53.6968778,
      "longitude": -1.927434
   },
   "484": {
      "postcode": "M25",
      "latitude": 53.5283859,
      "longitude": -2.2757491
   },
   "485": {
      "postcode": "S73",
      "latitude": 53.5244965,
      "longitude": -1.3950715
   },
   "486": {
      "postcode": "PE2",
      "latitude": 52.5584209,
      "longitude": -0.2605213
   },
   "487": {
      "postcode": "KA11",
      "latitude": 55.6186396,
      "longitude": -4.6276773
   },
   "488": {
      "postcode": "SA48",
      "latitude": 52.1449088,
      "longitude": -4.11325
   },
   "489": {
      "postcode": "HP7",
      "latitude": 51.6644833,
      "longitude": -0.6102425
   },
   "490": {
      "postcode": "KT14",
      "latitude": 51.3384121,
      "longitude": -0.4882369
   },
   "491": {
      "postcode": "NR29",
      "latitude": 52.6942516,
      "longitude": 1.6362126
   },
   "492": {
      "postcode": "TA6",
      "latitude": 51.1256664,
      "longitude": -3.0008114
   },
   "493": {
      "postcode": "CO5",
      "latitude": 51.8152485,
      "longitude": 0.8199292
   },
   "494": {
      "postcode": "SE11",
      "latitude": 51.4898569,
      "longitude": -0.1115597
   },
   "495": {
      "postcode": "CV33",
      "latitude": 52.2554168,
      "longitude": -1.4875182
   },
   "496": {
      "postcode": "HP10",
      "latitude": 51.6083649,
      "longitude": -0.6974711
   },
   "497": {
      "postcode": "DA5",
      "latitude": 51.4406947,
      "longitude": 0.1461798
   },
   "498": {
      "postcode": "BA5",
      "latitude": 51.212571,
      "longitude": -2.6552733
   },
   "499": {
      "postcode": "GU30",
      "latitude": 51.0754992,
      "longitude": -0.8042741
   },
   "500": {
      "postcode": "W1B",
      "latitude": 51.5143738,
      "longitude": -0.1409766
   },
   "501": {
      "postcode": "BB18",
      "latitude": 53.9145757,
      "longitude": -2.1720306
   },
   "502": {
      "postcode": "BL0",
      "latitude": 53.6484286,
      "longitude": -2.3169628
   },
   "503": {
      "postcode": "CT9",
      "latitude": 51.3833635,
      "longitude": 1.389298
   },
   "504": {
      "postcode": "SY7",
      "latitude": 52.4254259,
      "longitude": -2.8867442
   },
   "505": {
      "postcode": "PH3",
      "latitude": 56.3019354,
      "longitude": -3.7043969
   },
   "506": {
      "postcode": "SO41",
      "latitude": 50.7554651,
      "longitude": -1.5665136
   },
   "507": {
      "postcode": "BA20",
      "latitude": 50.937984,
      "longitude": -2.6452044
   },
   "508": {
      "postcode": "B8",
      "latitude": 52.4911095,
      "longitude": -1.8413277
   },
   "509": {
      "postcode": "PL12",
      "latitude": 50.4193974,
      "longitude": -4.2502369
   },
   "510": {
      "postcode": "SO30",
      "latitude": 50.9198664,
      "longitude": -1.3069752
   },
   "511": {
      "postcode": "S74",
      "latitude": 53.5009685,
      "longitude": -1.4411464
   },
   "512": {
      "postcode": "B16",
      "latitude": 52.4771886,
      "longitude": -1.9342144
   },
   "513": {
      "postcode": "DL16",
      "latitude": 54.6989434,
      "longitude": -1.6056739
   },
   "514": {
      "postcode": "TA9",
      "latitude": 51.2255918,
      "longitude": -2.9567138
   },
   "515": {
      "postcode": "GU21",
      "latitude": 51.3210516,
      "longitude": -0.5804072
   },
   "516": {
      "postcode": "MK16",
      "latitude": 52.0896113,
      "longitude": -0.7217314
   },
   "517": {
      "postcode": "SP5",
      "latitude": 51.021579,
      "longitude": -1.770351
   },
   "518": {
      "postcode": "ML8",
      "latitude": 55.7314933,
      "longitude": -3.8429126
   },
   "519": {
      "postcode": "CA14",
      "latitude": 54.6346926,
      "longitude": -3.5380221
   },
   "520": {
      "postcode": "B94",
      "latitude": 52.3495479,
      "longitude": -1.793885
   },
   "521": {
      "postcode": "TR18",
      "latitude": 50.1174074,
      "longitude": -5.5425056
   },
   "522": {
      "postcode": "L74",
      "latitude": 53.3930523,
      "longitude": -2.9882833
   },
   "523": {
      "postcode": "SM4",
      "latitude": 51.393147,
      "longitude": -0.1996608
   },
   "524": {
      "postcode": "CM18",
      "latitude": 51.7552911,
      "longitude": 0.1060047
   },
   "525": {
      "postcode": "W1U",
      "latitude": 51.5187153,
      "longitude": -0.1534804
   },
   "526": {
      "postcode": "WS13",
      "latitude": 52.6925953,
      "longitude": -1.8189572
   },
   "527": {
      "postcode": "TS21",
      "latitude": 54.628183,
      "longitude": -1.4287816
   },
   "528": {
      "postcode": "PE32",
      "latitude": 52.7278429,
      "longitude": 0.6349892
   },
   "529": {
      "postcode": "SS3",
      "latitude": 51.5432969,
      "longitude": 0.7891019
   },
   "530": {
      "postcode": "E8",
      "latitude": 51.5436904,
      "longitude": -0.0661452
   },
   "531": {
      "postcode": "MK3",
      "latitude": 51.9937256,
      "longitude": -0.7517663
   },
   "532": {
      "postcode": "E14",
      "latitude": 51.5061699,
      "longitude": -0.0184998
   },
   "533": {
      "postcode": "M1",
      "latitude": 53.4774963,
      "longitude": -2.2362343
   },
   "534": {
      "postcode": "TW3",
      "latitude": 51.4681228,
      "longitude": -0.3638733
   },
   "535": {
      "postcode": "WR99",
      "latitude": 52.1948626,
      "longitude": -2.203101
   },
   "536": {
      "postcode": "LE6",
      "latitude": 52.6570218,
      "longitude": -1.2331852
   },
   "537": {
      "postcode": "NR26",
      "latitude": 52.9387975,
      "longitude": 1.2088922
   },
   "538": {
      "postcode": "WF1",
      "latitude": 53.6874355,
      "longitude": -1.4935886
   },
   "539": {
      "postcode": "PE37",
      "latitude": 52.6410311,
      "longitude": 0.6995141
   },
   "540": {
      "postcode": "ME9",
      "latitude": 51.3358666,
      "longitude": 0.7219229
   },
   "541": {
      "postcode": "PH15",
      "latitude": 56.6097022,
      "longitude": -3.9407898
   },
   "542": {
      "postcode": "BN14",
      "latitude": 50.8340609,
      "longitude": -0.3817303
   },
   "543": {
      "postcode": "DA7",
      "latitude": 51.4656011,
      "longitude": 0.1459735
   },
   "544": {
      "postcode": "EH26",
      "latitude": 55.8334533,
      "longitude": -3.2242391
   },
   "545": {
      "postcode": "IP28",
      "latitude": 52.3308885,
      "longitude": 0.5278417
   },
   "546": {
      "postcode": "KA23",
      "latitude": 55.6934667,
      "longitude": -4.8575881
   },
   "547": {
      "postcode": "ML2",
      "latitude": 55.7768458,
      "longitude": -3.9138139
   },
   "548": {
      "postcode": "BS99",
      "latitude": 51.4450405,
      "longitude": -2.5956233
   },
   "549": {
      "postcode": "CO7",
      "latitude": 51.8816629,
      "longitude": 1.0052818
   },
   "550": {
      "postcode": "SO14",
      "latitude": 50.9071878,
      "longitude": -1.3973862
   },
   "551": {
      "postcode": "EH45",
      "latitude": 55.6544414,
      "longitude": -3.1908306
   },
   "552": {
      "postcode": "KA2",
      "latitude": 55.5956268,
      "longitude": -4.566525
   },
   "553": {
      "postcode": "LE67",
      "latitude": 52.7156016,
      "longitude": -1.362308
   },
   "554": {
      "postcode": "SY24",
      "latitude": 52.4727828,
      "longitude": -4.0207042
   },
   "555": {
      "postcode": "KW13",
      "latitude": 58.478332,
      "longitude": -3.8949963
   },
   "556": {
      "postcode": "TW17",
      "latitude": 51.39821,
      "longitude": -0.4476473
   },
   "557": {
      "postcode": "NG3",
      "latitude": 52.9695328,
      "longitude": -1.1273629
   },
   "558": {
      "postcode": "EX17",
      "latitude": 50.8116834,
      "longitude": -3.7053311
   },
   "559": {
      "postcode": "BS35",
      "latitude": 51.5977668,
      "longitude": -2.5487713
   },
   "560": {
      "postcode": "BT25",
      "latitude": 54.3959469,
      "longitude": -6.1138325
   },
   "561": {
      "postcode": "HA1",
      "latitude": 51.5799962,
      "longitude": -0.3383049
   },
   "562": {
      "postcode": "NG14",
      "latitude": 53.0177831,
      "longitude": -1.0390068
   },
   "563": {
      "postcode": "BA2",
      "latitude": 51.3592543,
      "longitude": -2.3793066
   },
   "564": {
      "postcode": "DG6",
      "latitude": 54.8371503,
      "longitude": -4.0555469
   },
   "565": {
      "postcode": "KT20",
      "latitude": 51.2864936,
      "longitude": -0.2311279
   },
   "566": {
      "postcode": "CW5",
      "latitude": 53.0619376,
      "longitude": -2.5221792
   },
   "567": {
      "postcode": "CH63",
      "latitude": 53.3442867,
      "longitude": -3.0125451
   },
   "568": {
      "postcode": "DN18",
      "latitude": 53.6811955,
      "longitude": -0.4476705
   },
   "569": {
      "postcode": "HP5",
      "latitude": 51.7128444,
      "longitude": -0.6085614
   },
   "570": {
      "postcode": "RG25",
      "latitude": 51.2271784,
      "longitude": -1.1624243
   },
   "571": {
      "postcode": "PA19",
      "latitude": 55.9529227,
      "longitude": -4.8261532
   },
   "572": {
      "postcode": "ME6",
      "latitude": 51.3228393,
      "longitude": 0.4347653
   },
   "573": {
      "postcode": "LL29",
      "latitude": 53.2891437,
      "longitude": -3.7084555
   },
   "574": {
      "postcode": "BH1",
      "latitude": 50.7249204,
      "longitude": -1.8602459
   },
   "575": {
      "postcode": "IV24",
      "latitude": 57.8912204,
      "longitude": -4.3559987
   },
   "576": {
      "postcode": "GU46",
      "latitude": 51.3385812,
      "longitude": -0.8320474
   },
   "577": {
      "postcode": "LD1",
      "latitude": 52.2607456,
      "longitude": -3.3662735
   },
   "578": {
      "postcode": "WC2R",
      "latitude": 51.5116889,
      "longitude": -0.1183208
   },
   "579": {
      "postcode": "TN20",
      "latitude": 51.0167888,
      "longitude": 0.2503568
   },
   "580": {
      "postcode": "FY3",
      "latitude": 53.8212841,
      "longitude": -3.0204371
   },
   "581": {
      "postcode": "SK5",
      "latitude": 53.4351388,
      "longitude": -2.1525459
   },
   "582": {
      "postcode": "EH37",
      "latitude": 55.8613517,
      "longitude": -2.9598479
   },
   "583": {
      "postcode": "G61",
      "latitude": 55.9191422,
      "longitude": -4.3315668
   },
   "584": {
      "postcode": "DN11",
      "latitude": 53.448826,
      "longitude": -1.0821884
   },
   "585": {
      "postcode": "EX23",
      "latitude": 50.8243103,
      "longitude": -4.5328043
   },
   "586": {
      "postcode": "B12",
      "latitude": 52.4607564,
      "longitude": -1.8836558
   },
   "587": {
      "postcode": "NP8",
      "latitude": 51.8618552,
      "longitude": -3.1546668
   },
   "588": {
      "postcode": "BT30",
      "latitude": 54.3352858,
      "longitude": -5.702726
   },
   "589": {
      "postcode": "WD19",
      "latitude": 51.6308706,
      "longitude": -0.390642
   },
   "590": {
      "postcode": "TA22",
      "latitude": 51.0456933,
      "longitude": -3.5451925
   },
   "591": {
      "postcode": "PH39",
      "latitude": 56.9123133,
      "longitude": -5.841732
   },
   "592": {
      "postcode": "LD6",
      "latitude": 52.3100474,
      "longitude": -3.5092516
   },
   "593": {
      "postcode": "W1D",
      "latitude": 51.5133117,
      "longitude": -0.1327615
   },
   "594": {
      "postcode": "NE17",
      "latitude": 54.9125064,
      "longitude": -1.8171473
   },
   "595": {
      "postcode": "EH48",
      "latitude": 55.8989296,
      "longitude": -3.6648047
   },
   "596": {
      "postcode": "GL2",
      "latitude": 51.8431569,
      "longitude": -2.2702834
   },
   "597": {
      "postcode": "TA16",
      "latitude": 50.9094738,
      "longitude": -2.7935591
   },
   "598": {
      "postcode": "PH43",
      "latitude": 57.0154066,
      "longitude": -6.2814874
   },
   "599": {
      "postcode": "HS5",
      "latitude": 57.7653976,
      "longitude": -7.0112702
   },
   "600": {
      "postcode": "SK6",
      "latitude": 53.4051341,
      "longitude": -2.080279
   },
   "601": {
      "postcode": "HP14",
      "latitude": 51.6524063,
      "longitude": -0.8387317
   },
   "602": {
      "postcode": "SE27",
      "latitude": 51.4305427,
      "longitude": -0.1023126
   },
   "603": {
      "postcode": "EH35",
      "latitude": 55.9108636,
      "longitude": -2.9447636
   },
   "604": {
      "postcode": "GL7",
      "latitude": 51.7113826,
      "longitude": -1.8967753
   },
   "605": {
      "postcode": "NR33",
      "latitude": 52.4540969,
      "longitude": 1.7167978
   },
   "606": {
      "postcode": "TR9",
      "latitude": 50.4134665,
      "longitude": -4.9352015
   },
   "607": {
      "postcode": "KA3",
      "latitude": 55.6454507,
      "longitude": -4.496797
   },
   "608": {
      "postcode": "GL5",
      "latitude": 51.7381408,
      "longitude": -2.2210178
   },
   "609": {
      "postcode": "G82",
      "latitude": 55.9517278,
      "longitude": -4.5740174
   },
   "610": {
      "postcode": "SE4",
      "latitude": 51.4610268,
      "longitude": -0.0352253
   },
   "611": {
      "postcode": "DN5",
      "latitude": 53.538349,
      "longitude": -1.1744232
   },
   "612": {
      "postcode": "EH28",
      "latitude": 55.9298906,
      "longitude": -3.3887501
   },
   "613": {
      "postcode": "SN3",
      "latitude": 51.5616826,
      "longitude": -1.7456549
   },
   "614": {
      "postcode": "RM1",
      "latitude": 51.582909,
      "longitude": 0.1835712
   },
   "615": {
      "postcode": "ST13",
      "latitude": 53.1009844,
      "longitude": -2.0193009
   },
   "616": {
      "postcode": "WR9",
      "latitude": 52.2667884,
      "longitude": -2.1583548
   },
   "617": {
      "postcode": "OX39",
      "latitude": 51.701667,
      "longitude": -0.9158158
   },
   "618": {
      "postcode": "CT15",
      "latitude": 51.1725483,
      "longitude": 1.2818765
   },
   "619": {
      "postcode": "CF30",
      "latitude": 51.5196309,
      "longitude": -3.1195669
   },
   "620": {
      "postcode": "FK8",
      "latitude": 56.131702,
      "longitude": -4.0593036
   },
   "621": {
      "postcode": "LE19",
      "latitude": 52.5844805,
      "longitude": -1.2064606
   },
   "622": {
      "postcode": "SA99",
      "latitude": 51.6699957,
      "longitude": -3.9454456
   },
   "623": {
      "postcode": "LA4",
      "latitude": 54.0702298,
      "longitude": -2.8525004
   },
   "624": {
      "postcode": "NE5",
      "latitude": 54.9961368,
      "longitude": -1.6888196
   },
   "625": {
      "postcode": "TS9",
      "latitude": 54.4659991,
      "longitude": -1.1652944
   },
   "626": {
      "postcode": "PH34",
      "latitude": 56.9203102,
      "longitude": -4.927653
   },
   "627": {
      "postcode": "PH12",
      "latitude": 56.575892,
      "longitude": -3.1549046
   },
   "628": {
      "postcode": "PL31",
      "latitude": 50.4691274,
      "longitude": -4.7226505
   },
   "629": {
      "postcode": "LL60",
      "latitude": 53.2154645,
      "longitude": -4.274545
   },
   "630": {
      "postcode": "WR4",
      "latitude": 52.203734,
      "longitude": -2.1898149
   },
   "631": {
      "postcode": "TR17",
      "latitude": 50.1255013,
      "longitude": -5.4684713
   },
   "632": {
      "postcode": "NG10",
      "latitude": 52.9005705,
      "longitude": -1.2841731
   },
   "633": {
      "postcode": "OX20",
      "latitude": 51.8558919,
      "longitude": -1.3577401
   },
   "634": {
      "postcode": "PO14",
      "latitude": 50.8387029,
      "longitude": -1.2188991
   },
   "635": {
      "postcode": "SO51",
      "latitude": 50.9959687,
      "longitude": -1.5037602
   },
   "636": {
      "postcode": "BH5",
      "latitude": 50.725298,
      "longitude": -1.8322739
   },
   "637": {
      "postcode": "SP11",
      "latitude": 51.2275811,
      "longitude": -1.5120802
   },
   "638": {
      "postcode": "BT3",
      "latitude": 54.6172417,
      "longitude": -5.903704
   },
   "639": {
      "postcode": "TD10",
      "latitude": 55.7114784,
      "longitude": -2.4518628
   },
   "640": {
      "postcode": "EC1Y",
      "latitude": 51.5230455,
      "longitude": -0.0924717
   },
   "641": {
      "postcode": "BB12",
      "latitude": 53.8034114,
      "longitude": -2.2927166
   },
   "642": {
      "postcode": "TS6",
      "latitude": 54.5656389,
      "longitude": -1.1534611
   },
   "643": {
      "postcode": "DD7",
      "latitude": 56.5028985,
      "longitude": -2.7195271
   },
   "644": {
      "postcode": "E2",
      "latitude": 51.5296098,
      "longitude": -0.062627
   },
   "645": {
      "postcode": "SY15",
      "latitude": 52.5532761,
      "longitude": -3.1331948
   },
   "646": {
      "postcode": "DH9",
      "latitude": 54.8684514,
      "longitude": -1.7109643
   },
   "647": {
      "postcode": "WR14",
      "latitude": 52.1144453,
      "longitude": -2.3204072
   },
   "648": {
      "postcode": "PE5",
      "latitude": 52.5748693,
      "longitude": -0.3505212
   },
   "649": {
      "postcode": "DL7",
      "latitude": 54.3378836,
      "longitude": -1.4855331
   },
   "650": {
      "postcode": "CH41",
      "latitude": 53.3942234,
      "longitude": -3.0326994
   },
   "651": {
      "postcode": "G66",
      "latitude": 55.9404977,
      "longitude": -4.153923
   },
   "652": {
      "postcode": "BD98",
      "latitude": 53.816805,
      "longitude": -1.7653258
   },
   "653": {
      "postcode": "ST20",
      "latitude": 52.798281,
      "longitude": -2.2761054
   },
   "654": {
      "postcode": "LU3",
      "latitude": 51.9086465,
      "longitude": -0.4426142
   },
   "655": {
      "postcode": "AL3",
      "latitude": 51.7803976,
      "longitude": -0.3775501
   },
   "656": {
      "postcode": "DG8",
      "latitude": 54.8722279,
      "longitude": -4.5163917
   },
   "657": {
      "postcode": "TN10",
      "latitude": 51.2120053,
      "longitude": 0.2840864
   },
   "658": {
      "postcode": "HU14",
      "latitude": 53.728421,
      "longitude": -0.4993848
   },
   "659": {
      "postcode": "PE10",
      "latitude": 52.7746766,
      "longitude": -0.377177
   },
   "660": {
      "postcode": "NR35",
      "latitude": 52.4618856,
      "longitude": 1.4328948
   },
   "661": {
      "postcode": "OX27",
      "latitude": 51.9363464,
      "longitude": -1.1505518
   },
   "662": {
      "postcode": "CV9",
      "latitude": 52.5861653,
      "longitude": -1.5616215
   },
   "663": {
      "postcode": "UB8",
      "latitude": 51.5352408,
      "longitude": -0.4738505
   },
   "664": {
      "postcode": "SO15",
      "latitude": 50.9170655,
      "longitude": -1.4245244
   },
   "665": {
      "postcode": "BN95",
      "latitude": 50.823154,
      "longitude": -0.330024
   },
   "666": {
      "postcode": "DA4",
      "latitude": 51.3885873,
      "longitude": 0.232219
   },
   "667": {
      "postcode": "SG12",
      "latitude": 51.8143338,
      "longitude": -0.0169035
   },
   "668": {
      "postcode": "AB53",
      "latitude": 57.5250408,
      "longitude": -2.3937282
   },
   "669": {
      "postcode": "TQ3",
      "latitude": 50.443945,
      "longitude": -3.5764405
   },
   "670": {
      "postcode": "IV25",
      "latitude": 57.8890332,
      "longitude": -4.0419737
   },
   "671": {
      "postcode": "PL4",
      "latitude": 50.3755331,
      "longitude": -4.1280288
   },
   "672": {
      "postcode": "KY3",
      "latitude": 56.0637385,
      "longitude": -3.2305775
   },
   "673": {
      "postcode": "DN34",
      "latitude": 53.5573926,
      "longitude": -0.1133186
   },
   "674": {
      "postcode": "RG10",
      "latitude": 51.4823983,
      "longitude": -0.8532308
   },
   "675": {
      "postcode": "PO31",
      "latitude": 50.7554074,
      "longitude": -1.3073561
   },
   "676": {
      "postcode": "KW14",
      "latitude": 58.588615,
      "longitude": -3.5547823
   },
   "677": {
      "postcode": "E3",
      "latitude": 51.527941,
      "longitude": -0.0252696
   },
   "678": {
      "postcode": "LL74",
      "latitude": 53.3191598,
      "longitude": -4.2293713
   },
   "679": {
      "postcode": "SW1Y",
      "latitude": 51.5074759,
      "longitude": -0.1345996
   },
   "680": {
      "postcode": "KW1",
      "latitude": 58.4566982,
      "longitude": -3.1224058
   },
   "681": {
      "postcode": "OX2",
      "latitude": 51.7659091,
      "longitude": -1.2807181
   },
   "682": {
      "postcode": "LU4",
      "latitude": 51.8983235,
      "longitude": -0.4686662
   },
   "683": {
      "postcode": "S71",
      "latitude": 53.5744126,
      "longitude": -1.4561067
   },
   "684": {
      "postcode": "LE95",
      "latitude": 52.6061749,
      "longitude": -1.1905604
   },
   "685": {
      "postcode": "WA6",
      "latitude": 53.2727629,
      "longitude": -2.7247283
   },
   "686": {
      "postcode": "W11",
      "latitude": 51.512272,
      "longitude": -0.2164413
   },
   "687": {
      "postcode": "BL1",
      "latitude": 53.5905339,
      "longitude": -2.4448299
   },
   "688": {
      "postcode": "DL5",
      "latitude": 54.6176722,
      "longitude": -1.578451
   },
   "689": {
      "postcode": "LL76",
      "latitude": 53.3007473,
      "longitude": -4.2397465
   },
   "690": {
      "postcode": "CT6",
      "latitude": 51.3644106,
      "longitude": 1.1295235
   },
   "691": {
      "postcode": "DG10",
      "latitude": 55.3200502,
      "longitude": -3.4381997
   },
   "692": {
      "postcode": "BN45",
      "latitude": 50.8967169,
      "longitude": -0.1902402
   },
   "693": {
      "postcode": "IV51",
      "latitude": 57.4741873,
      "longitude": -6.2434474
   },
   "694": {
      "postcode": "BS22",
      "latitude": 51.3610555,
      "longitude": -2.9293627
   },
   "695": {
      "postcode": "W3",
      "latitude": 51.5106335,
      "longitude": -0.2679031
   },
   "696": {
      "postcode": "EH30",
      "latitude": 55.9856246,
      "longitude": -3.3939638
   },
   "697": {
      "postcode": "BT17",
      "latitude": 54.5534071,
      "longitude": -6.0198284
   },
   "698": {
      "postcode": "NG32",
      "latitude": 52.951308,
      "longitude": -0.6513436
   },
   "699": {
      "postcode": "KA18",
      "latitude": 55.4514123,
      "longitude": -4.2427574
   },
   "700": {
      "postcode": "TQ12",
      "latitude": 50.5294305,
      "longitude": -3.6123156
   },
   "701": {
      "postcode": "CH61",
      "latitude": 53.3491491,
      "longitude": -3.1020354
   },
   "702": {
      "postcode": "AB37",
      "latitude": 57.3275842,
      "longitude": -3.3524834
   },
   "703": {
      "postcode": "B31",
      "latitude": 52.4081108,
      "longitude": -1.9733848
   },
   "704": {
      "postcode": "LA12",
      "latitude": 54.2031951,
      "longitude": -3.0836203
   },
   "705": {
      "postcode": "KT19",
      "latitude": 51.3525254,
      "longitude": -0.2707598
   },
   "706": {
      "postcode": "SS12",
      "latitude": 51.60537,
      "longitude": 0.5205007
   },
   "707": {
      "postcode": "M24",
      "latitude": 53.5514675,
      "longitude": -2.1982858
   },
   "708": {
      "postcode": "DN2",
      "latitude": 53.5337629,
      "longitude": -1.1026264
   },
   "709": {
      "postcode": "SA38",
      "latitude": 52.0402001,
      "longitude": -4.476398
   },
   "710": {
      "postcode": "ME8",
      "latitude": 51.3613848,
      "longitude": 0.5967776
   },
   "711": {
      "postcode": "OL7",
      "latitude": 53.4907107,
      "longitude": -2.1072525
   },
   "712": {
      "postcode": "SW3",
      "latitude": 51.4891244,
      "longitude": -0.1657226
   },
   "713": {
      "postcode": "B63",
      "latitude": 52.4514517,
      "longitude": -2.0699158
   },
   "714": {
      "postcode": "L20",
      "latitude": 53.4530856,
      "longitude": -2.9890292
   },
   "715": {
      "postcode": "PE11",
      "latitude": 52.8055261,
      "longitude": -0.1668409
   },
   "716": {
      "postcode": "HP9",
      "latitude": 51.6103131,
      "longitude": -0.6407522
   },
   "717": {
      "postcode": "PA74",
      "latitude": 56.5329478,
      "longitude": -6.2297513
   },
   "718": {
      "postcode": "MK18",
      "latitude": 51.978349,
      "longitude": -0.9695075
   },
   "719": {
      "postcode": "WF90",
      "latitude": 53.6744344,
      "longitude": -1.4908921
   },
   "720": {
      "postcode": "KT5",
      "latitude": 51.3906807,
      "longitude": -0.2867503
   },
   "721": {
      "postcode": "SW1H",
      "latitude": 51.4987321,
      "longitude": -0.1337132
   },
   "722": {
      "postcode": "OX3",
      "latitude": 51.7622825,
      "longitude": -1.211732
   },
   "723": {
      "postcode": "L18",
      "latitude": 53.3805747,
      "longitude": -2.9083261
   },
   "724": {
      "postcode": "SY9",
      "latitude": 52.4991445,
      "longitude": -2.9906924
   },
   "725": {
      "postcode": "CF91",
      "latitude": 51.4655659,
      "longitude": -3.1939894
   },
   "726": {
      "postcode": "EX20",
      "latitude": 50.7519249,
      "longitude": -4.019293
   },
   "727": {
      "postcode": "ML6",
      "latitude": 55.8677284,
      "longitude": -3.9613387
   },
   "728": {
      "postcode": "LA21",
      "latitude": 54.3628108,
      "longitude": -3.0785695
   },
   "729": {
      "postcode": "BT76",
      "latitude": 54.4200957,
      "longitude": -7.1921901
   },
   "730": {
      "postcode": "PA67",
      "latitude": 56.3142224,
      "longitude": -6.2313622
   },
   "731": {
      "postcode": "SE3",
      "latitude": 51.4694787,
      "longitude": 0.0196345
   },
   "732": {
      "postcode": "PO17",
      "latitude": 50.889723,
      "longitude": -1.17331
   },
   "733": {
      "postcode": "AB34",
      "latitude": 57.0936452,
      "longitude": -2.8113866
   },
   "734": {
      "postcode": "RG42",
      "latitude": 51.4277905,
      "longitude": -0.7570056
   },
   "735": {
      "postcode": "LL30",
      "latitude": 53.3180209,
      "longitude": -3.8162186
   },
   "736": {
      "postcode": "DT3",
      "latitude": 50.6422651,
      "longitude": -2.4683307
   },
   "737": {
      "postcode": "SY12",
      "latitude": 52.9028027,
      "longitude": -2.8954535
   },
   "738": {
      "postcode": "CH3",
      "latitude": 53.1647192,
      "longitude": -2.8197563
   },
   "739": {
      "postcode": "CM13",
      "latitude": 51.6152603,
      "longitude": 0.3385145
   },
   "740": {
      "postcode": "KY13",
      "latitude": 56.2084615,
      "longitude": -3.4334289
   },
   "741": {
      "postcode": "SP2",
      "latitude": 51.0750553,
      "longitude": -1.8258872
   },
   "742": {
      "postcode": "TA21",
      "latitude": 50.9777888,
      "longitude": -3.2445571
   },
   "743": {
      "postcode": "TA8",
      "latitude": 51.2451467,
      "longitude": -2.9950311
   },
   "744": {
      "postcode": "HP12",
      "latitude": 51.6259591,
      "longitude": -0.7795608
   },
   "745": {
      "postcode": "TA17",
      "latitude": 50.9082091,
      "longitude": -2.8361593
   },
   "746": {
      "postcode": "SG7",
      "latitude": 52.0045147,
      "longitude": -0.1754105
   },
   "747": {
      "postcode": "LN9",
      "latitude": 53.2172832,
      "longitude": -0.1120184
   },
   "748": {
      "postcode": "TF7",
      "latitude": 52.63923,
      "longitude": -2.4504763
   },
   "749": {
      "postcode": "KT7",
      "latitude": 51.3881177,
      "longitude": -0.3337295
   },
   "750": {
      "postcode": "LS23",
      "latitude": 53.9003968,
      "longitude": -1.3484233
   },
   "751": {
      "postcode": "LL35",
      "latitude": 52.5467868,
      "longitude": -4.0413751
   },
   "752": {
      "postcode": "RH2",
      "latitude": 51.2351176,
      "longitude": -0.2030862
   },
   "753": {
      "postcode": "BT51",
      "latitude": 55.060214,
      "longitude": -6.6830653
   },
   "754": {
      "postcode": "DG9",
      "latitude": 54.8777681,
      "longitude": -5.0228028
   },
   "755": {
      "postcode": "NE46",
      "latitude": 54.9790665,
      "longitude": -2.1076079
   },
   "756": {
      "postcode": "G60",
      "latitude": 55.9225474,
      "longitude": -4.4557485
   },
   "757": {
      "postcode": "SO18",
      "latitude": 50.9241213,
      "longitude": -1.3620137
   },
   "758": {
      "postcode": "DE13",
      "latitude": 52.8072661,
      "longitude": -1.6937154
   },
   "759": {
      "postcode": "RH3",
      "latitude": 51.2326558,
      "longitude": -0.2778643
   },
   "760": {
      "postcode": "RM11",
      "latitude": 51.5710765,
      "longitude": 0.2185278
   },
   "761": {
      "postcode": "WF14",
      "latitude": 53.6797839,
      "longitude": -1.6960552
   },
   "762": {
      "postcode": "WV1",
      "latitude": 52.5864721,
      "longitude": -2.1158825
   },
   "763": {
      "postcode": "IV3",
      "latitude": 57.4764724,
      "longitude": -4.2479131
   },
   "764": {
      "postcode": "NE26",
      "latitude": 55.0527885,
      "longitude": -1.4577261
   },
   "765": {
      "postcode": "HU9",
      "latitude": 53.7560073,
      "longitude": -0.289433
   },
   "766": {
      "postcode": "L38",
      "latitude": 53.5244465,
      "longitude": -3.0511596
   },
   "767": {
      "postcode": "AB39",
      "latitude": 56.979377,
      "longitude": -2.2170154
   },
   "768": {
      "postcode": "PL34",
      "latitude": 50.6597186,
      "longitude": -4.7443504
   },
   "769": {
      "postcode": "S33",
      "latitude": 53.3438997,
      "longitude": -1.7396963
   },
   "770": {
      "postcode": "PE29",
      "latitude": 52.3323569,
      "longitude": -0.1792855
   },
   "771": {
      "postcode": "CV21",
      "latitude": 52.3768752,
      "longitude": -1.25063
   },
   "772": {
      "postcode": "EH42",
      "latitude": 55.9935934,
      "longitude": -2.5254885
   },
   "773": {
      "postcode": "TR10",
      "latitude": 50.1676099,
      "longitude": -5.1189764
   },
   "774": {
      "postcode": "L31",
      "latitude": 53.5134057,
      "longitude": -2.9378113
   },
   "775": {
      "postcode": "DY6",
      "latitude": 52.4984945,
      "longitude": -2.1644135
   },
   "776": {
      "postcode": "G51",
      "latitude": 55.8577477,
      "longitude": -4.3165267
   },
   "777": {
      "postcode": "EH19",
      "latitude": 55.8724184,
      "longitude": -3.105045
   },
   "778": {
      "postcode": "L6",
      "latitude": 53.4189254,
      "longitude": -2.9515685
   },
   "779": {
      "postcode": "PH17",
      "latitude": 56.6864534,
      "longitude": -4.3747262
   },
   "780": {
      "postcode": "KW5",
      "latitude": 58.2871721,
      "longitude": -3.3827428
   },
   "781": {
      "postcode": "BT36",
      "latitude": 54.6768193,
      "longitude": -5.9562895
   },
   "782": {
      "postcode": "PL18",
      "latitude": 50.5154431,
      "longitude": -4.2217893
   },
   "783": {
      "postcode": "TW2",
      "latitude": 51.446354,
      "longitude": -0.3544949
   },
   "784": {
      "postcode": "SO97",
      "latitude": 50.9484861,
      "longitude": -1.3619614
   },
   "785": {
      "postcode": "IP7",
      "latitude": 52.0687092,
      "longitude": 0.9424582
   },
   "786": {
      "postcode": "TF13",
      "latitude": 52.5787304,
      "longitude": -2.5824227
   },
   "787": {
      "postcode": "KY12",
      "latitude": 56.0770695,
      "longitude": -3.4965561
   },
   "788": {
      "postcode": "RG31",
      "latitude": 51.4566563,
      "longitude": -1.0456059
   },
   "789": {
      "postcode": "BB4",
      "latitude": 53.7037431,
      "longitude": -2.2919089
   },
   "790": {
      "postcode": "EX22",
      "latitude": 50.8277967,
      "longitude": -4.3680718
   },
   "791": {
      "postcode": "S3",
      "latitude": 53.3874982,
      "longitude": -1.4740209
   },
   "792": {
      "postcode": "YO7",
      "latitude": 54.2246863,
      "longitude": -1.3514255
   },
   "793": {
      "postcode": "HU17",
      "latitude": 53.8467937,
      "longitude": -0.4287013
   },
   "794": {
      "postcode": "TF3",
      "latitude": 52.6674608,
      "longitude": -2.4483576
   },
   "795": {
      "postcode": "WC1B",
      "latitude": 51.5194545,
      "longitude": -0.1259647
   },
   "796": {
      "postcode": "LU5",
      "latitude": 51.910954,
      "longitude": -0.5140444
   },
   "797": {
      "postcode": "OL13",
      "latitude": 53.700821,
      "longitude": -2.2044339
   },
   "798": {
      "postcode": "CR44",
      "latitude": 51.3823469,
      "longitude": -0.1328753
   },
   "799": {
      "postcode": "BT66",
      "latitude": 54.4550926,
      "longitude": -6.3329464
   },
   "800": {
      "postcode": "DT1",
      "latitude": 50.7118787,
      "longitude": -2.4448216
   },
   "801": {
      "postcode": "DE21",
      "latitude": 52.9340572,
      "longitude": -1.4320438
   },
   "802": {
      "postcode": "TN32",
      "latitude": 50.9791601,
      "longitude": 0.4904213
   },
   "803": {
      "postcode": "CV35",
      "latitude": 52.2215666,
      "longitude": -1.593202
   },
   "804": {
      "postcode": "WV15",
      "latitude": 52.5159774,
      "longitude": -2.3744083
   },
   "805": {
      "postcode": "HD9",
      "latitude": 53.5804475,
      "longitude": -1.7973107
   },
   "806": {
      "postcode": "RH19",
      "latitude": 51.1256226,
      "longitude": -0.0142356
   },
   "807": {
      "postcode": "PA8",
      "latitude": 55.9007534,
      "longitude": -4.453165
   },
   "808": {
      "postcode": "EH32",
      "latitude": 55.9674629,
      "longitude": -2.9509183
   },
   "809": {
      "postcode": "G77",
      "latitude": 55.7739434,
      "longitude": -4.3319996
   },
   "810": {
      "postcode": "OX1",
      "latitude": 51.7451905,
      "longitude": -1.2614253
   },
   "811": {
      "postcode": "M6",
      "latitude": 53.4926929,
      "longitude": -2.2990621
   },
   "812": {
      "postcode": "L32",
      "latitude": 53.4783273,
      "longitude": -2.889272
   },
   "813": {
      "postcode": "L16",
      "latitude": 53.3987049,
      "longitude": -2.8874699
   },
   "814": {
      "postcode": "LS4",
      "latitude": 53.8105301,
      "longitude": -1.5848257
   },
   "815": {
      "postcode": "IV18",
      "latitude": 57.7024425,
      "longitude": -4.1548212
   },
   "816": {
      "postcode": "IV1",
      "latitude": 57.4840542,
      "longitude": -4.2347448
   },
   "817": {
      "postcode": "G75",
      "latitude": 55.7507329,
      "longitude": -4.1985241
   },
   "818": {
      "postcode": "CA21",
      "latitude": 54.4454251,
      "longitude": -3.5163777
   },
   "819": {
      "postcode": "B42",
      "latitude": 52.5346593,
      "longitude": -1.9124526
   },
   "820": {
      "postcode": "W12",
      "latitude": 51.5083087,
      "longitude": -0.2407824
   },
   "821": {
      "postcode": "B61",
      "latitude": 52.3464135,
      "longitude": -2.068307
   },
   "822": {
      "postcode": "N5",
      "latitude": 51.5538671,
      "longitude": -0.0986076
   },
   "823": {
      "postcode": "CV2",
      "latitude": 52.4244967,
      "longitude": -1.4635562
   },
   "824": {
      "postcode": "RH1",
      "latitude": 51.2373631,
      "longitude": -0.1576051
   },
   "825": {
      "postcode": "LL40",
      "latitude": 52.7567851,
      "longitude": -3.8749667
   },
   "826": {
      "postcode": "B70",
      "latitude": 52.5209224,
      "longitude": -2.0044143
   },
   "827": {
      "postcode": "BT49",
      "latitude": 55.0473469,
      "longitude": -6.9508217
   },
   "828": {
      "postcode": "SR1",
      "latitude": 54.9061193,
      "longitude": -1.3782118
   },
   "829": {
      "postcode": "BL4",
      "latitude": 53.5462411,
      "longitude": -2.4015686
   },
   "830": {
      "postcode": "SL8",
      "latitude": 51.5787364,
      "longitude": -0.7087112
   },
   "831": {
      "postcode": "TW18",
      "latitude": 51.4276663,
      "longitude": -0.5044353
   },
   "832": {
      "postcode": "WA10",
      "latitude": 53.4542967,
      "longitude": -2.7561819
   },
   "833": {
      "postcode": "IV40",
      "latitude": 57.2743006,
      "longitude": -5.6473471
   },
   "834": {
      "postcode": "CH70",
      "latitude": 53.1927439,
      "longitude": -2.9225567
   },
   "835": {
      "postcode": "DE3",
      "latitude": 52.9096926,
      "longitude": -1.5425124
   },
   "836": {
      "postcode": "IV14",
      "latitude": 57.5857945,
      "longitude": -4.5489794
   },
   "837": {
      "postcode": "SN11",
      "latitude": 51.4393874,
      "longitude": -1.9990879
   },
   "838": {
      "postcode": "DN22",
      "latitude": 53.3237589,
      "longitude": -0.9278773
   },
   "839": {
      "postcode": "SE1",
      "latitude": 51.4991997,
      "longitude": -0.0916245
   },
   "840": {
      "postcode": "W4",
      "latitude": 51.4912309,
      "longitude": -0.2640107
   },
   "841": {
      "postcode": "LL62",
      "latitude": 53.2108742,
      "longitude": -4.3859556
   },
   "842": {
      "postcode": "OL16",
      "latitude": 53.6123706,
      "longitude": -2.1313519
   },
   "843": {
      "postcode": "SN4",
      "latitude": 51.530429,
      "longitude": -1.8406454
   },
   "844": {
      "postcode": "CB22",
      "latitude": 52.1284294,
      "longitude": 0.1354878
   },
   "845": {
      "postcode": "TS16",
      "latitude": 54.5222224,
      "longitude": -1.3559066
   },
   "846": {
      "postcode": "RH14",
      "latitude": 51.0330425,
      "longitude": -0.4847114
   },
   "847": {
      "postcode": "GL9",
      "latitude": 51.5555981,
      "longitude": -2.3033165
   },
   "848": {
      "postcode": "L28",
      "latitude": 53.4353243,
      "longitude": -2.8656215
   },
   "849": {
      "postcode": "HP21",
      "latitude": 51.8052172,
      "longitude": -0.8058581
   },
   "850": {
      "postcode": "BT93",
      "latitude": 54.4678402,
      "longitude": -7.8268864
   },
   "851": {
      "postcode": "RG40",
      "latitude": 51.4001248,
      "longitude": -0.8360988
   },
   "852": {
      "postcode": "BD15",
      "latitude": 53.8100727,
      "longitude": -1.8383321
   },
   "853": {
      "postcode": "PA23",
      "latitude": 55.9537952,
      "longitude": -4.9334508
   },
   "854": {
      "postcode": "SG4",
      "latitude": 51.9206087,
      "longitude": -0.2595399
   },
   "855": {
      "postcode": "L33",
      "latitude": 53.4900539,
      "longitude": -2.8768007
   },
   "856": {
      "postcode": "ST11",
      "latitude": 52.9657745,
      "longitude": -2.0645769
   },
   "857": {
      "postcode": "LA19",
      "latitude": 54.2966419,
      "longitude": -3.3802097
   },
   "858": {
      "postcode": "MK77",
      "latitude": 52.041499,
      "longitude": -0.8172717
   },
   "859": {
      "postcode": "CO8",
      "latitude": 51.9733754,
      "longitude": 0.7656644
   },
   "860": {
      "postcode": "DA18",
      "latitude": 51.4942848,
      "longitude": 0.1364966
   },
   "861": {
      "postcode": "PA3",
      "latitude": 55.8515026,
      "longitude": -4.4456692
   },
   "862": {
      "postcode": "DG7",
      "latitude": 54.9685747,
      "longitude": -4.0135194
   },
   "863": {
      "postcode": "GU35",
      "latitude": 51.1167316,
      "longitude": -0.8490969
   },
   "864": {
      "postcode": "RH77",
      "latitude": 51.1387737,
      "longitude": -0.1697793
   },
   "865": {
      "postcode": "SE5",
      "latitude": 51.4738341,
      "longitude": -0.0914963
   },
   "866": {
      "postcode": "M4",
      "latitude": 53.4848676,
      "longitude": -2.2300315
   },
   "867": {
      "postcode": "RM5",
      "latitude": 51.6013387,
      "longitude": 0.1647727
   },
   "868": {
      "postcode": "CH99",
      "latitude": 53.1763583,
      "longitude": -2.8948703
   },
   "869": {
      "postcode": "DL98",
      "latitude": 54.5275154,
      "longitude": -1.5597017
   },
   "870": {
      "postcode": "GU11",
      "latitude": 51.2489707,
      "longitude": -0.7634252
   },
   "871": {
      "postcode": "M9",
      "latitude": 53.5220075,
      "longitude": -2.2139408
   },
   "872": {
      "postcode": "PE15",
      "latitude": 52.5375062,
      "longitude": 0.0858982
   },
   "873": {
      "postcode": "BH22",
      "latitude": 50.8053042,
      "longitude": -1.888586
   },
   "874": {
      "postcode": "PA15",
      "latitude": 55.9425234,
      "longitude": -4.7476824
   },
   "875": {
      "postcode": "FK11",
      "latitude": 56.149895,
      "longitude": -3.8517203
   },
   "876": {
      "postcode": "CV7",
      "latitude": 52.446762,
      "longitude": -1.569683
   },
   "877": {
      "postcode": "SY99",
      "latitude": 52.7128256,
      "longitude": -2.74961
   },
   "878": {
      "postcode": "TN12",
      "latitude": 51.1724422,
      "longitude": 0.4445547
   },
   "879": {
      "postcode": "LA6",
      "latitude": 54.1754174,
      "longitude": -2.6103862
   },
   "880": {
      "postcode": "RM14",
      "latitude": 51.5569004,
      "longitude": 0.264491
   },
   "881": {
      "postcode": "M90",
      "latitude": 53.3635148,
      "longitude": -2.2780731
   },
   "882": {
      "postcode": "LD3",
      "latitude": 51.9607697,
      "longitude": -3.369993
   },
   "883": {
      "postcode": "CV10",
      "latitude": 52.5260857,
      "longitude": -1.502331
   },
   "884": {
      "postcode": "L15",
      "latitude": 53.3975793,
      "longitude": -2.9205924
   },
   "885": {
      "postcode": "WF17",
      "latitude": 53.7188923,
      "longitude": -1.6426028
   },
   "886": {
      "postcode": "KA29",
      "latitude": 55.755735,
      "longitude": -4.854085
   },
   "887": {
      "postcode": "CH43",
      "latitude": 53.3843247,
      "longitude": -3.0596357
   },
   "888": {
      "postcode": "B44",
      "latitude": 52.5456674,
      "longitude": -1.8850992
   },
   "889": {
      "postcode": "BN99",
      "latitude": 50.8231149,
      "longitude": -0.3490648
   },
   "890": {
      "postcode": "N19",
      "latitude": 51.5652742,
      "longitude": -0.1298808
   },
   "891": {
      "postcode": "KW9",
      "latitude": 58.0136902,
      "longitude": -3.8588509
   },
   "892": {
      "postcode": "AB30",
      "latitude": 56.8467032,
      "longitude": -2.4778654
   },
   "893": {
      "postcode": "RG18",
      "latitude": 51.4314131,
      "longitude": -1.2602125
   },
   "894": {
      "postcode": "DD8",
      "latitude": 56.6558721,
      "longitude": -2.9220215
   },
   "895": {
      "postcode": "EH44",
      "latitude": 55.6191253,
      "longitude": -3.0635531
   },
   "896": {
      "postcode": "RM6",
      "latitude": 51.5757994,
      "longitude": 0.1295444
   },
   "897": {
      "postcode": "LN3",
      "latitude": 53.2418341,
      "longitude": -0.4171042
   },
   "898": {
      "postcode": "DN9",
      "latitude": 53.5059237,
      "longitude": -0.8929973
   },
   "899": {
      "postcode": "PA75",
      "latitude": 56.6125781,
      "longitude": -6.1143844
   },
   "900": {
      "postcode": "CF31",
      "latitude": 51.5088642,
      "longitude": -3.5784949
   },
   "901": {
      "postcode": "ME13",
      "latitude": 51.3036496,
      "longitude": 0.8945604
   },
   "902": {
      "postcode": "HP17",
      "latitude": 51.7768478,
      "longitude": -0.8843057
   },
   "903": {
      "postcode": "GU33",
      "latitude": 51.0517463,
      "longitude": -0.8903635
   },
   "904": {
      "postcode": "ME2",
      "latitude": 51.3915327,
      "longitude": 0.4815053
   },
   "905": {
      "postcode": "BT27",
      "latitude": 54.5091942,
      "longitude": -6.0237607
   },
   "906": {
      "postcode": "RH11",
      "latitude": 51.1106463,
      "longitude": -0.2081205
   },
   "907": {
      "postcode": "WA2",
      "latitude": 53.4108251,
      "longitude": -2.5811919
   },
   "908": {
      "postcode": "NE10",
      "latitude": 54.9472035,
      "longitude": -1.5540428
   },
   "909": {
      "postcode": "B90",
      "latitude": 52.3989824,
      "longitude": -1.8260954
   },
   "910": {
      "postcode": "S14",
      "latitude": 53.3460139,
      "longitude": -1.4444011
   },
   "911": {
      "postcode": "YO21",
      "latitude": 54.4770514,
      "longitude": -0.7104006
   },
   "912": {
      "postcode": "SA1",
      "latitude": 51.6266504,
      "longitude": -3.9402316
   },
   "913": {
      "postcode": "LA22",
      "latitude": 54.4229898,
      "longitude": -2.9912561
   },
   "914": {
      "postcode": "SE20",
      "latitude": 51.4123248,
      "longitude": -0.0594187
   },
   "915": {
      "postcode": "IV10",
      "latitude": 57.5845661,
      "longitude": -4.1264965
   },
   "916": {
      "postcode": "NN15",
      "latitude": 52.3822978,
      "longitude": -0.7029196
   },
   "917": {
      "postcode": "B21",
      "latitude": 52.506938,
      "longitude": -1.9415679
   },
   "918": {
      "postcode": "TS17",
      "latitude": 54.5355555,
      "longitude": -1.3046467
   },
   "919": {
      "postcode": "EX4",
      "latitude": 50.7313128,
      "longitude": -3.526701
   },
   "920": {
      "postcode": "EH16",
      "latitude": 55.922607,
      "longitude": -3.1528183
   },
   "921": {
      "postcode": "E6",
      "latitude": 51.5264995,
      "longitude": 0.053874
   },
   "922": {
      "postcode": "NE92",
      "latitude": 54.9417753,
      "longitude": -1.6149882
   },
   "923": {
      "postcode": "B73",
      "latitude": 52.5537182,
      "longitude": -1.841907
   },
   "924": {
      "postcode": "NN7",
      "latitude": 52.2082231,
      "longitude": -0.9287786
   },
   "925": {
      "postcode": "PA60",
      "latitude": 55.8786751,
      "longitude": -5.9157646
   },
   "926": {
      "postcode": "NE88",
      "latitude": 54.9504939,
      "longitude": -1.6102416
   },
   "927": {
      "postcode": "CV34",
      "latitude": 52.2816351,
      "longitude": -1.5783799
   },
   "928": {
      "postcode": "DG2",
      "latitude": 55.0646623,
      "longitude": -3.6588521
   },
   "929": {
      "postcode": "SS99",
      "latitude": 51.5477702,
      "longitude": 0.7142613
   },
   "930": {
      "postcode": "CM21",
      "latitude": 51.8122758,
      "longitude": 0.1452281
   },
   "931": {
      "postcode": "BA8",
      "latitude": 50.9962542,
      "longitude": -2.411865
   },
   "932": {
      "postcode": "BT42",
      "latitude": 54.8548266,
      "longitude": -6.2755735
   },
   "933": {
      "postcode": "G34",
      "latitude": 55.8679239,
      "longitude": -4.1123443
   },
   "934": {
      "postcode": "BN17",
      "latitude": 50.8149225,
      "longitude": -0.5399594
   },
   "935": {
      "postcode": "SO52",
      "latitude": 50.9775491,
      "longitude": -1.4438927
   },
   "936": {
      "postcode": "AB33",
      "latitude": 57.2255966,
      "longitude": -2.740868
   },
   "937": {
      "postcode": "NG18",
      "latitude": 53.1382628,
      "longitude": -1.1840991
   },
   "938": {
      "postcode": "BD7",
      "latitude": 53.783468,
      "longitude": -1.7857283
   },
   "939": {
      "postcode": "WF15",
      "latitude": 53.7082837,
      "longitude": -1.700436
   },
   "940": {
      "postcode": "PO35",
      "latitude": 50.6868571,
      "longitude": -1.0855937
   },
   "941": {
      "postcode": "LS1",
      "latitude": 53.7975973,
      "longitude": -1.5516427
   },
   "942": {
      "postcode": "EX1",
      "latitude": 50.7280574,
      "longitude": -3.5003048
   },
   "943": {
      "postcode": "EN9",
      "latitude": 51.6961713,
      "longitude": 0.0149921
   },
   "944": {
      "postcode": "DN15",
      "latitude": 53.6143425,
      "longitude": -0.6522291
   },
   "945": {
      "postcode": "CO15",
      "latitude": 51.7963698,
      "longitude": 1.1548306
   },
   "946": {
      "postcode": "TN8",
      "latitude": 51.1951342,
      "longitude": 0.0779767
   },
   "947": {
      "postcode": "SA10",
      "latitude": 51.6875078,
      "longitude": -3.8007881
   },
   "948": {
      "postcode": "RG29",
      "latitude": 51.2458368,
      "longitude": -0.9459765
   },
   "949": {
      "postcode": "FK9",
      "latitude": 56.1448526,
      "longitude": -3.9433641
   },
   "950": {
      "postcode": "EH15",
      "latitude": 55.9462301,
      "longitude": -3.1125696
   },
   "951": {
      "postcode": "WV6",
      "latitude": 52.5968273,
      "longitude": -2.1827471
   },
   "952": {
      "postcode": "TF5",
      "latitude": 52.717189,
      "longitude": -2.5392219
   },
   "953": {
      "postcode": "AB23",
      "latitude": 57.2132774,
      "longitude": -2.0892647
   },
   "954": {
      "postcode": "NW1",
      "latitude": 51.5332718,
      "longitude": -0.1438882
   },
   "955": {
      "postcode": "HD6",
      "latitude": 53.7024215,
      "longitude": -1.7843814
   },
   "956": {
      "postcode": "BS7",
      "latitude": 51.4869402,
      "longitude": -2.5814899
   },
   "957": {
      "postcode": "GU27",
      "latitude": 51.0813045,
      "longitude": -0.7216203
   },
   "958": {
      "postcode": "TD8",
      "latitude": 55.4759086,
      "longitude": -2.542383
   },
   "959": {
      "postcode": "M38",
      "latitude": 53.5324424,
      "longitude": -2.4232927
   },
   "960": {
      "postcode": "RH16",
      "latitude": 51.0014151,
      "longitude": -0.0983341
   },
   "961": {
      "postcode": "BA13",
      "latitude": 51.2621061,
      "longitude": -2.1816707
   },
   "962": {
      "postcode": "EX14",
      "latitude": 50.8140317,
      "longitude": -3.1914327
   },
   "963": {
      "postcode": "PR25",
      "latitude": 53.6945907,
      "longitude": -2.6937368
   },
   "964": {
      "postcode": "E10",
      "latitude": 51.5679608,
      "longitude": -0.0143353
   },
   "965": {
      "postcode": "M41",
      "latitude": 53.4509537,
      "longitude": -2.3655029
   },
   "966": {
      "postcode": "SY6",
      "latitude": 52.5371062,
      "longitude": -2.791617
   },
   "967": {
      "postcode": "SL5",
      "latitude": 51.4056392,
      "longitude": -0.6638405
   },
   "968": {
      "postcode": "CV5",
      "latitude": 52.412484,
      "longitude": -1.555389
   },
   "969": {
      "postcode": "DD4",
      "latitude": 56.4821151,
      "longitude": -2.935612
   },
   "970": {
      "postcode": "DY8",
      "latitude": 52.460812,
      "longitude": -2.1557543
   },
   "971": {
      "postcode": "EH99",
      "latitude": 55.947641,
      "longitude": -3.2037715
   },
   "972": {
      "postcode": "CR3",
      "latitude": 51.2881312,
      "longitude": -0.0824599
   },
   "973": {
      "postcode": "BA10",
      "latitude": 51.1131761,
      "longitude": -2.4478513
   },
   "974": {
      "postcode": "ME10",
      "latitude": 51.3436099,
      "longitude": 0.735349
   },
   "975": {
      "postcode": "SM5",
      "latitude": 51.3686674,
      "longitude": -0.168793
   },
   "976": {
      "postcode": "PL22",
      "latitude": 50.403456,
      "longitude": -4.6518896
   },
   "977": {
      "postcode": "L1",
      "latitude": 53.4023772,
      "longitude": -2.9804999
   },
   "978": {
      "postcode": "BD20",
      "latitude": 53.8982751,
      "longitude": -1.9501915
   },
   "979": {
      "postcode": "PL28",
      "latitude": 50.5327501,
      "longitude": -4.9673308
   },
   "980": {
      "postcode": "LL69",
      "latitude": 53.3860502,
      "longitude": -4.3192563
   },
   "981": {
      "postcode": "B74",
      "latitude": 52.5843126,
      "longitude": -1.8621609
   },
   "982": {
      "postcode": "HP8",
      "latitude": 51.6384149,
      "longitude": -0.5700237
   },
   "983": {
      "postcode": "CM1",
      "latitude": 51.7467319,
      "longitude": 0.4577894
   },
   "984": {
      "postcode": "ZE3",
      "latitude": 59.8829471,
      "longitude": -1.3043577
   },
   "985": {
      "postcode": "BT60",
      "latitude": 54.2928226,
      "longitude": -6.6487383
   },
   "986": {
      "postcode": "AL2",
      "latitude": 51.7191035,
      "longitude": -0.3354863
   },
   "987": {
      "postcode": "BA12",
      "latitude": 51.1708259,
      "longitude": -2.1888898
   },
   "988": {
      "postcode": "EC2N",
      "latitude": 51.5157712,
      "longitude": -0.0855193
   },
   "989": {
      "postcode": "MK10",
      "latitude": 52.0410506,
      "longitude": -0.6982522
   },
   "990": {
      "postcode": "IP19",
      "latitude": 52.3402509,
      "longitude": 1.4942442
   },
   "991": {
      "postcode": "RM9",
      "latitude": 51.5409021,
      "longitude": 0.1338079
   },
   "992": {
      "postcode": "IP13",
      "latitude": 52.18917,
      "longitude": 1.3206039
   },
   "993": {
      "postcode": "BT21",
      "latitude": 54.6400923,
      "longitude": -5.54674
   },
   "994": {
      "postcode": "RG45",
      "latitude": 51.3715067,
      "longitude": -0.7995721
   },
   "995": {
      "postcode": "IP14",
      "latitude": 52.206002,
      "longitude": 1.0312375
   },
   "996": {
      "postcode": "OX13",
      "latitude": 51.6758174,
      "longitude": -1.3577318
   },
   "997": {
      "postcode": "HR6",
      "latitude": 52.2333219,
      "longitude": -2.7731407
   },
   "998": {
      "postcode": "BS40",
      "latitude": 51.346529,
      "longitude": -2.6919383
   },
   "999": {
      "postcode": "KY6",
      "latitude": 56.1974394,
      "longitude": -3.200491
   },
   "1000": {
      "postcode": "IG11",
      "latitude": 51.5350133,
      "longitude": 0.0932901
   },
   "1001": {
      "postcode": "B80",
      "latitude": 52.2735522,
      "longitude": -1.8923001
   },
   "1002": {
      "postcode": "G62",
      "latitude": 55.9426842,
      "longitude": -4.3208961
   },
   "1003": {
      "postcode": "W1K",
      "latitude": 51.5111191,
      "longitude": -0.1510369
   },
   "1004": {
      "postcode": "GU12",
      "latitude": 51.2517147,
      "longitude": -0.7297556
   },
   "1005": {
      "postcode": "OX11",
      "latitude": 51.5995807,
      "longitude": -1.2522494
   },
   "1006": {
      "postcode": "E15",
      "latitude": 51.5402208,
      "longitude": 0.0032141
   },
   "1007": {
      "postcode": "S6",
      "latitude": 53.4028113,
      "longitude": -1.5130984
   },
   "1008": {
      "postcode": "EX34",
      "latitude": 51.1983243,
      "longitude": -4.1058651
   },
   "1009": {
      "postcode": "SA9",
      "latitude": 51.7812869,
      "longitude": -3.7689001
   },
   "1010": {
      "postcode": "CO1",
      "latitude": 51.8840222,
      "longitude": 0.8963748
   },
   "1011": {
      "postcode": "TS7",
      "latitude": 54.5339607,
      "longitude": -1.1831961
   },
   "1012": {
      "postcode": "L22",
      "latitude": 53.4772218,
      "longitude": -3.0279256
   },
   "1013": {
      "postcode": "SS4",
      "latitude": 51.5930469,
      "longitude": 0.7118562
   },
   "1014": {
      "postcode": "BA21",
      "latitude": 50.9520712,
      "longitude": -2.6336799
   },
   "1015": {
      "postcode": "CH27",
      "latitude": 53.4197266,
      "longitude": -3.0367611
   },
   "1016": {
      "postcode": "KA6",
      "latitude": 55.416235,
      "longitude": -4.504737
   },
   "1017": {
      "postcode": "SA71",
      "latitude": 51.6679926,
      "longitude": -4.9293245
   },
   "1018": {
      "postcode": "WV12",
      "latitude": 52.6058407,
      "longitude": -2.0403978
   },
   "1019": {
      "postcode": "CR2",
      "latitude": 51.3480184,
      "longitude": -0.0820678
   },
   "1020": {
      "postcode": "G20",
      "latitude": 55.8858609,
      "longitude": -4.2826493
   },
   "1021": {
      "postcode": "CB4",
      "latitude": 52.2229046,
      "longitude": 0.1298349
   },
   "1022": {
      "postcode": "RH6",
      "latitude": 51.1730206,
      "longitude": -0.1641717
   },
   "1023": {
      "postcode": "AB44",
      "latitude": 57.6682668,
      "longitude": -2.4922135
   },
   "1024": {
      "postcode": "OX49",
      "latitude": 51.6506644,
      "longitude": -1.0011957
   },
   "1025": {
      "postcode": "LL66",
      "latitude": 53.3797968,
      "longitude": -4.4083964
   },
   "1026": {
      "postcode": "SY14",
      "latitude": 53.0312383,
      "longitude": -2.7680979
   },
   "1027": {
      "postcode": "G69",
      "latitude": 55.8756055,
      "longitude": -4.1009988
   },
   "1028": {
      "postcode": "BT74",
      "latitude": 54.3451053,
      "longitude": -7.6650636
   },
   "1029": {
      "postcode": "WA14",
      "latitude": 53.3878102,
      "longitude": -2.3607423
   },
   "1030": {
      "postcode": "SA16",
      "latitude": 51.6893287,
      "longitude": -4.2569858
   },
   "1031": {
      "postcode": "BD99",
      "latitude": 53.7947563,
      "longitude": -1.7663604
   },
   "1032": {
      "postcode": "LS29",
      "latitude": 53.9189109,
      "longitude": -1.800672
   },
   "1033": {
      "postcode": "G72",
      "latitude": 55.8041894,
      "longitude": -4.1294723
   },
   "1034": {
      "postcode": "PL5",
      "latitude": 50.4110853,
      "longitude": -4.1666681
   },
   "1035": {
      "postcode": "CA28",
      "latitude": 54.5435085,
      "longitude": -3.5785239
   },
   "1036": {
      "postcode": "S11",
      "latitude": 53.3607754,
      "longitude": -1.5078903
   },
   "1037": {
      "postcode": "RG41",
      "latitude": 51.4168077,
      "longitude": -0.8633653
   },
   "1038": {
      "postcode": "TS20",
      "latitude": 54.5866832,
      "longitude": -1.3138689
   },
   "1039": {
      "postcode": "TR7",
      "latitude": 50.4138677,
      "longitude": -5.0748401
   },
   "1040": {
      "postcode": "SK23",
      "latitude": 53.3277544,
      "longitude": -1.9485093
   },
   "1041": {
      "postcode": "B2",
      "latitude": 52.4893361,
      "longitude": -1.8965236
   },
   "1042": {
      "postcode": "M21",
      "latitude": 53.4380163,
      "longitude": -2.2729543
   },
   "1043": {
      "postcode": "B19",
      "latitude": 52.4971338,
      "longitude": -1.9057716
   },
   "1044": {
      "postcode": "PO4",
      "latitude": 50.7901751,
      "longitude": -1.0620764
   },
   "1045": {
      "postcode": "CF34",
      "latitude": 51.610543,
      "longitude": -3.6520832
   },
   "1046": {
      "postcode": "TN17",
      "latitude": 51.0962819,
      "longitude": 0.5367581
   },
   "1047": {
      "postcode": "PA29",
      "latitude": 55.8065512,
      "longitude": -5.4754053
   },
   "1048": {
      "postcode": "LE4",
      "latitude": 52.6646001,
      "longitude": -1.1247758
   },
   "1049": {
      "postcode": "HP1",
      "latitude": 51.7566422,
      "longitude": -0.4869619
   },
   "1050": {
      "postcode": "NG12",
      "latitude": 52.9088921,
      "longitude": -1.0522853
   },
   "1051": {
      "postcode": "SA46",
      "latitude": 52.2377669,
      "longitude": -4.2574871
   },
   "1052": {
      "postcode": "IP4",
      "latitude": 52.0604324,
      "longitude": 1.1802287
   },
   "1053": {
      "postcode": "LS99",
      "latitude": 53.7758971,
      "longitude": -1.5465407
   },
   "1054": {
      "postcode": "KT4",
      "latitude": 51.3784115,
      "longitude": -0.243017
   },
   "1055": {
      "postcode": "CT20",
      "latitude": 51.0798258,
      "longitude": 1.1630593
   },
   "1056": {
      "postcode": "CH4",
      "latitude": 53.165525,
      "longitude": -2.9481695
   },
   "1057": {
      "postcode": "DT10",
      "latitude": 50.9376061,
      "longitude": -2.3343561
   },
   "1058": {
      "postcode": "SY25",
      "latitude": 52.2379435,
      "longitude": -3.9371965
   },
   "1059": {
      "postcode": "E7",
      "latitude": 51.5471369,
      "longitude": 0.027572
   },
   "1060": {
      "postcode": "TW8",
      "latitude": 51.4873197,
      "longitude": -0.3063655
   },
   "1061": {
      "postcode": "NR19",
      "latitude": 52.6751626,
      "longitude": 0.9300324
   },
   "1062": {
      "postcode": "CW1",
      "latitude": 53.1036281,
      "longitude": -2.4360889
   },
   "1063": {
      "postcode": "LS21",
      "latitude": 53.9116086,
      "longitude": -1.6804367
   },
   "1064": {
      "postcode": "DA11",
      "latitude": 51.4344917,
      "longitude": 0.3506663
   },
   "1065": {
      "postcode": "ST12",
      "latitude": 52.946949,
      "longitude": -2.1727546
   },
   "1066": {
      "postcode": "EC4N",
      "latitude": 51.5128988,
      "longitude": -0.0914843
   },
   "1067": {
      "postcode": "TN14",
      "latitude": 51.2978503,
      "longitude": 0.1574783
   },
   "1068": {
      "postcode": "BS34",
      "latitude": 51.523502,
      "longitude": -2.5667207
   },
   "1069": {
      "postcode": "PA69",
      "latitude": 56.3796685,
      "longitude": -6.0774753
   },
   "1070": {
      "postcode": "BS2",
      "latitude": 51.4599036,
      "longitude": -2.5819782
   },
   "1071": {
      "postcode": "PL25",
      "latitude": 50.3413052,
      "longitude": -4.7782631
   },
   "1072": {
      "postcode": "LA23",
      "latitude": 54.3713964,
      "longitude": -2.9129454
   },
   "1073": {
      "postcode": "LA3",
      "latitude": 54.0498853,
      "longitude": -2.8793403
   },
   "1074": {
      "postcode": "WR3",
      "latitude": 52.2169397,
      "longitude": -2.2139652
   },
   "1075": {
      "postcode": "EC2V",
      "latitude": 51.5155673,
      "longitude": -0.0937819
   },
   "1076": {
      "postcode": "IV48",
      "latitude": 57.3130105,
      "longitude": -6.1104379
   },
   "1077": {
      "postcode": "YO13",
      "latitude": 54.287425,
      "longitude": -0.4992911
   },
   "1078": {
      "postcode": "BD10",
      "latitude": 53.8329365,
      "longitude": -1.7248454
   },
   "1079": {
      "postcode": "EH49",
      "latitude": 55.9759491,
      "longitude": -3.5978664
   },
   "1080": {
      "postcode": "GL10",
      "latitude": 51.7436973,
      "longitude": -2.2870616
   },
   "1081": {
      "postcode": "LE5",
      "latitude": 52.6383444,
      "longitude": -1.0850557
   },
   "1082": {
      "postcode": "PA32",
      "latitude": 56.197567,
      "longitude": -5.1253583
   },
   "1083": {
      "postcode": "OL14",
      "latitude": 53.7144173,
      "longitude": -2.1009851
   },
   "1084": {
      "postcode": "WA7",
      "latitude": 53.3305871,
      "longitude": -2.7036909
   },
   "1085": {
      "postcode": "BL7",
      "latitude": 53.6317625,
      "longitude": -2.4223993
   },
   "1086": {
      "postcode": "BT28",
      "latitude": 54.5227918,
      "longitude": -6.0866891
   },
   "1087": {
      "postcode": "BT4",
      "latitude": 54.6025629,
      "longitude": -5.869615
   },
   "1088": {
      "postcode": "HD3",
      "latitude": 53.6536196,
      "longitude": -1.8320544
   },
   "1089": {
      "postcode": "BS27",
      "latitude": 51.272182,
      "longitude": -2.7717346
   },
   "1090": {
      "postcode": "BT11",
      "latitude": 54.5762546,
      "longitude": -5.9981326
   },
   "1091": {
      "postcode": "EH12",
      "latitude": 55.9418955,
      "longitude": -3.279118
   },
   "1092": {
      "postcode": "SW20",
      "latitude": 51.4109597,
      "longitude": -0.2277548
   },
   "1093": {
      "postcode": "BT64",
      "latitude": 54.4490883,
      "longitude": -6.3901653
   },
   "1094": {
      "postcode": "IV56",
      "latitude": 57.3655388,
      "longitude": -6.4303864
   },
   "1095": {
      "postcode": "PA31",
      "latitude": 56.0525103,
      "longitude": -5.4583508
   },
   "1096": {
      "postcode": "NE34",
      "latitude": 54.9717889,
      "longitude": -1.422479
   },
   "1097": {
      "postcode": "SN1",
      "latitude": 51.5565291,
      "longitude": -1.783169
   },
   "1098": {
      "postcode": "UB11",
      "latitude": 51.5113205,
      "longitude": -0.4469162
   },
   "1099": {
      "postcode": "CV8",
      "latitude": 52.3519562,
      "longitude": -1.5420194
   },
   "1100": {
      "postcode": "RM3",
      "latitude": 51.6019384,
      "longitude": 0.2244542
   },
   "1101": {
      "postcode": "LN6",
      "latitude": 53.2002374,
      "longitude": -0.6001511
   },
   "1102": {
      "postcode": "FK6",
      "latitude": 56.0212698,
      "longitude": -3.9154287
   },
   "1103": {
      "postcode": "LU1",
      "latitude": 51.8744779,
      "longitude": -0.4270575
   },
   "1104": {
      "postcode": "AL1",
      "latitude": 51.7489129,
      "longitude": -0.323756
   },
   "1105": {
      "postcode": "HA9",
      "latitude": 51.5607305,
      "longitude": -0.2857817
   },
   "1106": {
      "postcode": "BT44",
      "latitude": 54.9722864,
      "longitude": -6.287524
   },
   "1107": {
      "postcode": "SE2",
      "latitude": 51.4896972,
      "longitude": 0.1159327
   },
   "1108": {
      "postcode": "SA45",
      "latitude": 52.2081814,
      "longitude": -4.3582137
   },
   "1109": {
      "postcode": "LL71",
      "latitude": 53.3295165,
      "longitude": -4.3709519
   },
   "1110": {
      "postcode": "NR10",
      "latitude": 52.7359335,
      "longitude": 1.2410548
   },
   "1111": {
      "postcode": "TR3",
      "latitude": 50.2174347,
      "longitude": -5.112456
   },
   "1112": {
      "postcode": "SS5",
      "latitude": 51.6077523,
      "longitude": 0.6479542
   },
   "1113": {
      "postcode": "AB10",
      "latitude": 57.1353138,
      "longitude": -2.1202461
   },
   "1114": {
      "postcode": "EC2P",
      "latitude": 51.5241889,
      "longitude": -0.1110467
   },
   "1115": {
      "postcode": "BN43",
      "latitude": 50.8360644,
      "longitude": -0.2669108
   },
   "1116": {
      "postcode": "SL95",
      "latitude": 51.4991652,
      "longitude": -0.5390536
   },
   "1117": {
      "postcode": "PL16",
      "latitude": 50.6464378,
      "longitude": -4.2640338
   },
   "1118": {
      "postcode": "KA4",
      "latitude": 55.5991418,
      "longitude": -4.3816208
   },
   "1119": {
      "postcode": "MK43",
      "latitude": 52.1119082,
      "longitude": -0.5583834
   },
   "1120": {
      "postcode": "SR4",
      "latitude": 54.9003709,
      "longitude": -1.4255904
   },
   "1121": {
      "postcode": "L72",
      "latitude": 53.4772447,
      "longitude": -2.9780099
   },
   "1122": {
      "postcode": "CH28",
      "latitude": 53.4005658,
      "longitude": -3.1119268
   },
   "1123": {
      "postcode": "AL9",
      "latitude": 51.7445903,
      "longitude": -0.1976882
   },
   "1124": {
      "postcode": "CO6",
      "latitude": 51.9252061,
      "longitude": 0.7920011
   },
   "1125": {
      "postcode": "BT1",
      "latitude": 54.5997539,
      "longitude": -5.9284735
   },
   "1126": {
      "postcode": "LL65",
      "latitude": 53.3010223,
      "longitude": -4.5703675
   },
   "1127": {
      "postcode": "LE55",
      "latitude": 52.6327983,
      "longitude": -1.1253367
   },
   "1128": {
      "postcode": "B62",
      "latitude": 52.4571593,
      "longitude": -2.0337937
   },
   "1129": {
      "postcode": "B75",
      "latitude": 52.578728,
      "longitude": -1.808515
   },
   "1130": {
      "postcode": "CB10",
      "latitude": 52.028753,
      "longitude": 0.2627396
   },
   "1131": {
      "postcode": "WA13",
      "latitude": 53.3823451,
      "longitude": -2.4693236
   },
   "1132": {
      "postcode": "SW2",
      "latitude": 51.4493013,
      "longitude": -0.1198466
   },
   "1133": {
      "postcode": "TQ9",
      "latitude": 50.4165597,
      "longitude": -3.6910718
   },
   "1134": {
      "postcode": "AB25",
      "latitude": 57.1527168,
      "longitude": -2.1140756
   },
   "1135": {
      "postcode": "PA18",
      "latitude": 55.8884779,
      "longitude": -4.8880972
   },
   "1136": {
      "postcode": "N11",
      "latitude": 51.6137464,
      "longitude": -0.1388912
   },
   "1137": {
      "postcode": "SW9",
      "latitude": 51.4693401,
      "longitude": -0.1138947
   },
   "1138": {
      "postcode": "CA27",
      "latitude": 54.4910171,
      "longitude": -3.5934811
   },
   "1139": {
      "postcode": "SK13",
      "latitude": 53.4486314,
      "longitude": -1.9643687
   },
   "1140": {
      "postcode": "GU7",
      "latitude": 51.1896186,
      "longitude": -0.6121645
   },
   "1141": {
      "postcode": "CM22",
      "latitude": 51.8657844,
      "longitude": 0.2271806
   },
   "1142": {
      "postcode": "FK14",
      "latitude": 56.1671323,
      "longitude": -3.6556229
   },
   "1143": {
      "postcode": "HR9",
      "latitude": 51.9077349,
      "longitude": -2.5827297
   },
   "1144": {
      "postcode": "W5",
      "latitude": 51.5131903,
      "longitude": -0.3024217
   },
   "1145": {
      "postcode": "PE4",
      "latitude": 52.6119535,
      "longitude": -0.2626267
   },
   "1146": {
      "postcode": "OX44",
      "latitude": 51.6975079,
      "longitude": -1.1223775
   },
   "1147": {
      "postcode": "IV21",
      "latitude": 57.7243122,
      "longitude": -5.7211462
   },
   "1148": {
      "postcode": "UB6",
      "latitude": 51.538982,
      "longitude": -0.3406322
   },
   "1149": {
      "postcode": "CM0",
      "latitude": 51.6627266,
      "longitude": 0.8342244
   },
   "1150": {
      "postcode": "BT19",
      "latitude": 54.6513331,
      "longitude": -5.6671749
   },
   "1151": {
      "postcode": "TN29",
      "latitude": 50.9938289,
      "longitude": 0.9325174
   },
   "1152": {
      "postcode": "GU17",
      "latitude": 51.3288028,
      "longitude": -0.7891564
   },
   "1153": {
      "postcode": "M14",
      "latitude": 53.4484029,
      "longitude": -2.2258291
   },
   "1154": {
      "postcode": "LL27",
      "latitude": 53.1485258,
      "longitude": -3.8275336
   },
   "1155": {
      "postcode": "CF10",
      "latitude": 51.4748057,
      "longitude": -3.1731995
   },
   "1156": {
      "postcode": "DH97",
      "latitude": 54.7927104,
      "longitude": -1.5351133
   },
   "1157": {
      "postcode": "CT7",
      "latitude": 51.3704017,
      "longitude": 1.2964069
   },
   "1158": {
      "postcode": "B37",
      "latitude": 52.4784345,
      "longitude": -1.7421791
   },
   "1159": {
      "postcode": "PO19",
      "latitude": 50.8382074,
      "longitude": -0.7783183
   },
   "1160": {
      "postcode": "UB9",
      "latitude": 51.5862858,
      "longitude": -0.4926586
   },
   "1161": {
      "postcode": "CB5",
      "latitude": 52.2123417,
      "longitude": 0.1539646
   },
   "1162": {
      "postcode": "SE9",
      "latitude": 51.4451387,
      "longitude": 0.0548051
   },
   "1163": {
      "postcode": "EC4P",
      "latitude": 51.5245399,
      "longitude": -0.1120477
   },
   "1164": {
      "postcode": "LA1",
      "latitude": 54.0467054,
      "longitude": -2.7994612
   },
   "1165": {
      "postcode": "M40",
      "latitude": 53.5041026,
      "longitude": -2.1909788
   },
   "1166": {
      "postcode": "CT11",
      "latitude": 51.3360593,
      "longitude": 1.4132445
   },
   "1167": {
      "postcode": "MK12",
      "latitude": 52.0583718,
      "longitude": -0.8166917
   },
   "1168": {
      "postcode": "E98",
      "latitude": 51.5080232,
      "longitude": -0.0644425
   },
   "1169": {
      "postcode": "LE94",
      "latitude": 52.4836845,
      "longitude": -0.9055232
   },
   "1170": {
      "postcode": "G64",
      "latitude": 55.9114153,
      "longitude": -4.2170017
   },
   "1171": {
      "postcode": "EN7",
      "latitude": 51.7123101,
      "longitude": -0.0696748
   },
   "1172": {
      "postcode": "DN35",
      "latitude": 53.5545579,
      "longitude": -0.036351
   },
   "1173": {
      "postcode": "TR11",
      "latitude": 50.1498016,
      "longitude": -5.0876959
   },
   "1174": {
      "postcode": "TR23",
      "latitude": 49.9536038,
      "longitude": -6.3526466
   },
   "1175": {
      "postcode": "NE36",
      "latitude": 54.9454581,
      "longitude": -1.4414688
   },
   "1176": {
      "postcode": "PA37",
      "latitude": 56.4668384,
      "longitude": -5.3919661
   },
   "1177": {
      "postcode": "PA12",
      "latitude": 55.7942177,
      "longitude": -4.6265019
   },
   "1178": {
      "postcode": "TS15",
      "latitude": 54.4872991,
      "longitude": -1.3351828
   },
   "1179": {
      "postcode": "EX12",
      "latitude": 50.7068721,
      "longitude": -3.0818842
   },
   "1180": {
      "postcode": "AB36",
      "latitude": 57.1971865,
      "longitude": -3.0683197
   },
   "1181": {
      "postcode": "E12",
      "latitude": 51.5507498,
      "longitude": 0.0529473
   },
   "1182": {
      "postcode": "NG16",
      "latitude": 53.0273823,
      "longitude": -1.2949848
   },
   "1183": {
      "postcode": "LS16",
      "latitude": 53.852089,
      "longitude": -1.6036383
   },
   "1184": {
      "postcode": "WS8",
      "latitude": 52.6474687,
      "longitude": -1.9332437
   },
   "1185": {
      "postcode": "LE11",
      "latitude": 52.7680459,
      "longitude": -1.2191752
   },
   "1186": {
      "postcode": "SE22",
      "latitude": 51.4544389,
      "longitude": -0.0724071
   },
   "1187": {
      "postcode": "TR6",
      "latitude": 50.3419388,
      "longitude": -5.1530283
   },
   "1188": {
      "postcode": "TS8",
      "latitude": 54.5216751,
      "longitude": -1.2327726
   },
   "1189": {
      "postcode": "L21",
      "latitude": 53.4713811,
      "longitude": -3.0003559
   },
   "1190": {
      "postcode": "SW10",
      "latitude": 51.483784,
      "longitude": -0.1827911
   },
   "1191": {
      "postcode": "SE18",
      "latitude": 51.4843462,
      "longitude": 0.0726765
   },
   "1192": {
      "postcode": "AB54",
      "latitude": 57.4540447,
      "longitude": -2.761688
   },
   "1193": {
      "postcode": "PA21",
      "latitude": 55.9022321,
      "longitude": -5.2508811
   },
   "1194": {
      "postcode": "CO2",
      "latitude": 51.8697798,
      "longitude": 0.8943735
   },
   "1195": {
      "postcode": "LN4",
      "latitude": 53.1484011,
      "longitude": -0.3799049
   },
   "1196": {
      "postcode": "OX10",
      "latitude": 51.6073094,
      "longitude": -1.1287254
   },
   "1197": {
      "postcode": "DY1",
      "latitude": 52.5164236,
      "longitude": -2.0965765
   },
   "1198": {
      "postcode": "EX33",
      "latitude": 51.1152054,
      "longitude": -4.1742651
   },
   "1199": {
      "postcode": "NP20",
      "latitude": 51.5904204,
      "longitude": -3.0065286
   },
   "1200": {
      "postcode": "HD7",
      "latitude": 53.6239529,
      "longitude": -1.8779019
   },
   "1201": {
      "postcode": "SR8",
      "latitude": 54.7667388,
      "longitude": -1.3365695
   },
   "1202": {
      "postcode": "EH29",
      "latitude": 55.9568445,
      "longitude": -3.4034273
   },
   "1203": {
      "postcode": "NE33",
      "latitude": 54.9912555,
      "longitude": -1.4295666
   },
   "1204": {
      "postcode": "LL23",
      "latitude": 52.9052232,
      "longitude": -3.6018542
   },
   "1205": {
      "postcode": "HS9",
      "latitude": 56.9730005,
      "longitude": -7.4722587
   },
   "1206": {
      "postcode": "CF44",
      "latitude": 51.7182832,
      "longitude": -3.4588338
   },
   "1207": {
      "postcode": "WF12",
      "latitude": 53.6833333,
      "longitude": -1.6199223
   },
   "1208": {
      "postcode": "BH2",
      "latitude": 50.7210819,
      "longitude": -1.8840411
   },
   "1209": {
      "postcode": "BT34",
      "latitude": 54.1531164,
      "longitude": -6.1774814
   },
   "1210": {
      "postcode": "WA5",
      "latitude": 53.3990847,
      "longitude": -2.6388726
   },
   "1211": {
      "postcode": "BN1",
      "latitude": 50.8423629,
      "longitude": -0.1395112
   },
   "1212": {
      "postcode": "BS31",
      "latitude": 51.4087555,
      "longitude": -2.4924616
   },
   "1213": {
      "postcode": "CM2",
      "latitude": 51.7208592,
      "longitude": 0.4866343
   },
   "1214": {
      "postcode": "BT43",
      "latitude": 54.8926899,
      "longitude": -6.2647155
   },
   "1215": {
      "postcode": "EX35",
      "latitude": 51.2239866,
      "longitude": -3.8274296
   },
   "1216": {
      "postcode": "GU32",
      "latitude": 51.0090053,
      "longitude": -0.9681798
   },
   "1217": {
      "postcode": "TD3",
      "latitude": 55.7018161,
      "longitude": -2.5737927
   },
   "1218": {
      "postcode": "TR20",
      "latitude": 50.1318144,
      "longitude": -5.4879968
   },
   "1219": {
      "postcode": "TR26",
      "latitude": 50.2028293,
      "longitude": -5.4789995
   },
   "1220": {
      "postcode": "CO14",
      "latitude": 51.8502715,
      "longitude": 1.2671935
   },
   "1221": {
      "postcode": "PL8",
      "latitude": 50.3354884,
      "longitude": -4.0107277
   },
   "1222": {
      "postcode": "S45",
      "latitude": 53.1656275,
      "longitude": -1.4213229
   },
   "1223": {
      "postcode": "WS3",
      "latitude": 52.6197704,
      "longitude": -1.9920867
   },
   "1224": {
      "postcode": "SA11",
      "latitude": 51.6748529,
      "longitude": -3.7614044
   },
   "1225": {
      "postcode": "CM99",
      "latitude": 51.7424938,
      "longitude": 0.5005836
   },
   "1226": {
      "postcode": "TN3",
      "latitude": 51.1208107,
      "longitude": 0.2480518
   },
   "1227": {
      "postcode": "W1H",
      "latitude": 51.517687,
      "longitude": -0.1611043
   },
   "1228": {
      "postcode": "BT63",
      "latitude": 54.4072137,
      "longitude": -6.3906387
   },
   "1229": {
      "postcode": "TS10",
      "latitude": 54.6067666,
      "longitude": -1.0693075
   },
   "1230": {
      "postcode": "TS23",
      "latitude": 54.6094056,
      "longitude": -1.2851796
   },
   "1231": {
      "postcode": "EH1",
      "latitude": 55.9506608,
      "longitude": -3.192931
   },
   "1232": {
      "postcode": "TR25",
      "latitude": 49.9642737,
      "longitude": -6.2933395
   },
   "1233": {
      "postcode": "AB35",
      "latitude": 57.0384103,
      "longitude": -3.1496008
   },
   "1234": {
      "postcode": "DE56",
      "latitude": 53.0219424,
      "longitude": -1.4750676
   },
   "1235": {
      "postcode": "SR6",
      "latitude": 54.9355496,
      "longitude": -1.379168
   },
   "1236": {
      "postcode": "BS24",
      "latitude": 51.3303607,
      "longitude": -2.9292938
   },
   "1237": {
      "postcode": "NN11",
      "latitude": 52.2417044,
      "longitude": -1.1794055
   },
   "1238": {
      "postcode": "G13",
      "latitude": 55.893611,
      "longitude": -4.3477509
   },
   "1239": {
      "postcode": "WN6",
      "latitude": 53.5752593,
      "longitude": -2.6718
   },
   "1240": {
      "postcode": "BN51",
      "latitude": 50.8048207,
      "longitude": -0.0586638
   },
   "1241": {
      "postcode": "S40",
      "latitude": 53.2341072,
      "longitude": -1.4461714
   },
   "1242": {
      "postcode": "LA13",
      "latitude": 54.1182576,
      "longitude": -3.1983726
   },
   "1243": {
      "postcode": "NW10",
      "latitude": 51.5412842,
      "longitude": -0.2480596
   },
   "1244": {
      "postcode": "LA14",
      "latitude": 54.1182959,
      "longitude": -3.2311912
   },
   "1245": {
      "postcode": "CH34",
      "latitude": 53.2790404,
      "longitude": -2.9050848
   },
   "1246": {
      "postcode": "HP2",
      "latitude": 51.7643313,
      "longitude": -0.4522784
   },
   "1247": {
      "postcode": "KW15",
      "latitude": 58.9800047,
      "longitude": -2.9597106
   },
   "1248": {
      "postcode": "WN1",
      "latitude": 53.5533114,
      "longitude": -2.6281505
   },
   "1249": {
      "postcode": "CW2",
      "latitude": 53.0798218,
      "longitude": -2.4465966
   },
   "1250": {
      "postcode": "YO11",
      "latitude": 54.2639772,
      "longitude": -0.3963875
   },
   "1251": {
      "postcode": "EX19",
      "latitude": 50.8780171,
      "longitude": -4.005588
   },
   "1252": {
      "postcode": "S41",
      "latitude": 53.2472723,
      "longitude": -1.428409
   },
   "1253": {
      "postcode": "PE9",
      "latitude": 52.6545544,
      "longitude": -0.4804678
   },
   "1254": {
      "postcode": "PL10",
      "latitude": 50.3452071,
      "longitude": -4.2112874
   },
   "1255": {
      "postcode": "DN33",
      "latitude": 53.5394663,
      "longitude": -0.0990748
   },
   "1256": {
      "postcode": "WV99",
      "latitude": 52.6713503,
      "longitude": -2.4202904
   },
   "1257": {
      "postcode": "TR8",
      "latitude": 50.4004251,
      "longitude": -5.039462
   },
   "1258": {
      "postcode": "WC2H",
      "latitude": 51.5133603,
      "longitude": -0.1273492
   },
   "1259": {
      "postcode": "LL17",
      "latitude": 53.2523853,
      "longitude": -3.4370183
   },
   "1260": {
      "postcode": "BH15",
      "latitude": 50.7223607,
      "longitude": -1.985506
   },
   "1261": {
      "postcode": "NG25",
      "latitude": 53.0742802,
      "longitude": -0.9627263
   },
   "1262": {
      "postcode": "PA65",
      "latitude": 56.4691539,
      "longitude": -5.7255045
   },
   "1263": {
      "postcode": "PR3",
      "latitude": 53.8688401,
      "longitude": -2.7203057
   },
   "1264": {
      "postcode": "CB7",
      "latitude": 52.3612799,
      "longitude": 0.3252127
   },
   "1265": {
      "postcode": "KT8",
      "latitude": 51.4015316,
      "longitude": -0.3631647
   },
   "1266": {
      "postcode": "SL6",
      "latitude": 51.5239786,
      "longitude": -0.7292167
   },
   "1267": {
      "postcode": "S2",
      "latitude": 53.369613,
      "longitude": -1.4480046
   },
   "1268": {
      "postcode": "BA7",
      "latitude": 51.0894942,
      "longitude": -2.5194603
   },
   "1269": {
      "postcode": "GL18",
      "latitude": 51.9416934,
      "longitude": -2.4150411
   },
   "1270": {
      "postcode": "W1C",
      "latitude": 51.5144348,
      "longitude": -0.1491314
   },
   "1271": {
      "postcode": "WV10",
      "latitude": 52.6191468,
      "longitude": -2.1134738
   },
   "1272": {
      "postcode": "L68",
      "latitude": 53.4730536,
      "longitude": -2.9606906
   },
   "1273": {
      "postcode": "TN36",
      "latitude": 50.920303,
      "longitude": 0.6990613
   },
   "1274": {
      "postcode": "SK7",
      "latitude": 53.3695112,
      "longitude": -2.1434037
   },
   "1275": {
      "postcode": "CF64",
      "latitude": 51.4332091,
      "longitude": -3.1917807
   },
   "1276": {
      "postcode": "EC1N",
      "latitude": 51.5198912,
      "longitude": -0.1087995
   },
   "1277": {
      "postcode": "CM9",
      "latitude": 51.7408752,
      "longitude": 0.7010671
   },
   "1278": {
      "postcode": "HA0",
      "latitude": 51.5513241,
      "longitude": -0.3056919
   },
   "1279": {
      "postcode": "SL2",
      "latitude": 51.5356977,
      "longitude": -0.6058076
   },
   "1280": {
      "postcode": "PA13",
      "latitude": 55.8934699,
      "longitude": -4.6315923
   },
   "1281": {
      "postcode": "ML11",
      "latitude": 55.6671734,
      "longitude": -3.7891903
   },
   "1282": {
      "postcode": "ST21",
      "latitude": 52.8725507,
      "longitude": -2.2694515
   },
   "1283": {
      "postcode": "SL9",
      "latitude": 51.5978678,
      "longitude": -0.5557695
   },
   "1284": {
      "postcode": "EH18",
      "latitude": 55.8768124,
      "longitude": -3.122531
   },
   "1285": {
      "postcode": "WA3",
      "latitude": 53.456371,
      "longitude": -2.5477451
   },
   "1286": {
      "postcode": "IV31",
      "latitude": 57.7169577,
      "longitude": -3.2907466
   },
   "1287": {
      "postcode": "CA20",
      "latitude": 54.4104053,
      "longitude": -3.4622406
   },
   "1288": {
      "postcode": "KT18",
      "latitude": 51.3160216,
      "longitude": -0.2633727
   },
   "1289": {
      "postcode": "CM24",
      "latitude": 51.8992323,
      "longitude": 0.2039133
   },
   "1290": {
      "postcode": "G68",
      "latitude": 55.9529877,
      "longitude": -4.0160663
   },
   "1291": {
      "postcode": "NP19",
      "latitude": 51.5882819,
      "longitude": -2.963588
   },
   "1292": {
      "postcode": "EX37",
      "latitude": 50.9786853,
      "longitude": -3.9538059
   },
   "1293": {
      "postcode": "L70",
      "latitude": 53.4040997,
      "longitude": -2.9567513
   },
   "1294": {
      "postcode": "SO23",
      "latitude": 51.0685878,
      "longitude": -1.3082473
   },
   "1295": {
      "postcode": "BT46",
      "latitude": 54.8654569,
      "longitude": -6.6634111
   },
   "1296": {
      "postcode": "LL49",
      "latitude": 52.9290448,
      "longitude": -4.1379154
   },
   "1297": {
      "postcode": "TN23",
      "latitude": 51.1399102,
      "longitude": 0.8570045
   },
   "1298": {
      "postcode": "S7",
      "latitude": 53.3551559,
      "longitude": -1.4910563
   },
   "1299": {
      "postcode": "IP8",
      "latitude": 52.0630417,
      "longitude": 1.0792503
   },
   "1300": {
      "postcode": "WR7",
      "latitude": 52.1965989,
      "longitude": -2.0491854
   },
   "1301": {
      "postcode": "PO8",
      "latitude": 50.9135161,
      "longitude": -1.0116749
   },
   "1302": {
      "postcode": "PA4",
      "latitude": 55.874849,
      "longitude": -4.3953267
   },
   "1303": {
      "postcode": "PA73",
      "latitude": 56.4966381,
      "longitude": -6.1836106
   },
   "1304": {
      "postcode": "EC4Y",
      "latitude": 51.512938,
      "longitude": -0.1088079
   },
   "1305": {
      "postcode": "CF36",
      "latitude": 51.4850992,
      "longitude": -3.6994938
   },
   "1306": {
      "postcode": "CO9",
      "latitude": 51.9689789,
      "longitude": 0.6094407
   },
   "1307": {
      "postcode": "HS7",
      "latitude": 57.4472485,
      "longitude": -7.340699
   },
   "1308": {
      "postcode": "LN13",
      "latitude": 53.265048,
      "longitude": 0.1836393
   },
   "1309": {
      "postcode": "SG18",
      "latitude": 52.0825989,
      "longitude": -0.2645551
   },
   "1310": {
      "postcode": "CF37",
      "latitude": 51.6033134,
      "longitude": -3.3343249
   },
   "1311": {
      "postcode": "NE3",
      "latitude": 55.0104241,
      "longitude": -1.6354989
   },
   "1312": {
      "postcode": "KA15",
      "latitude": 55.7484284,
      "longitude": -4.6263497
   },
   "1313": {
      "postcode": "SP1",
      "latitude": 51.075221,
      "longitude": -1.7887748
   },
   "1314": {
      "postcode": "LL37",
      "latitude": 52.6659968,
      "longitude": -4.0837468
   },
   "1315": {
      "postcode": "EH47",
      "latitude": 55.8586358,
      "longitude": -3.6661035
   },
   "1316": {
      "postcode": "EC2Y",
      "latitude": 51.5194073,
      "longitude": -0.0935545
   },
   "1317": {
      "postcode": "LL57",
      "latitude": 53.2068931,
      "longitude": -4.1118949
   },
   "1318": {
      "postcode": "FK13",
      "latitude": 56.1519068,
      "longitude": -3.7398856
   },
   "1319": {
      "postcode": "DH6",
      "latitude": 54.7527793,
      "longitude": -1.4640636
   },
   "1320": {
      "postcode": "B60",
      "latitude": 52.3240959,
      "longitude": -2.0491825
   },
   "1321": {
      "postcode": "CA22",
      "latitude": 54.4806529,
      "longitude": -3.5329009
   },
   "1322": {
      "postcode": "TW5",
      "latitude": 51.4824354,
      "longitude": -0.3862521
   },
   "1323": {
      "postcode": "S63",
      "latitude": 53.5185718,
      "longitude": -1.3305698
   },
   "1324": {
      "postcode": "WA55",
      "latitude": 53.3912093,
      "longitude": -2.6088591
   },
   "1325": {
      "postcode": "BN24",
      "latitude": 50.8167744,
      "longitude": 0.3261108
   },
   "1326": {
      "postcode": "CH7",
      "latitude": 53.1699651,
      "longitude": -3.1322347
   },
   "1327": {
      "postcode": "LS13",
      "latitude": 53.8108069,
      "longitude": -1.635379
   },
   "1328": {
      "postcode": "LE15",
      "latitude": 52.6564368,
      "longitude": -0.7019964
   },
   "1329": {
      "postcode": "SA61",
      "latitude": 51.8001658,
      "longitude": -4.9741219
   },
   "1330": {
      "postcode": "SM1",
      "latitude": 51.3669805,
      "longitude": -0.1928536
   },
   "1331": {
      "postcode": "KA30",
      "latitude": 55.7972875,
      "longitude": -4.8634584
   },
   "1332": {
      "postcode": "PH2",
      "latitude": 56.387089,
      "longitude": -3.4038513
   },
   "1333": {
      "postcode": "PA26",
      "latitude": 56.2605328,
      "longitude": -4.9351065
   },
   "1334": {
      "postcode": "ST4",
      "latitude": 52.9945102,
      "longitude": -2.1854192
   },
   "1335": {
      "postcode": "BT41",
      "latitude": 54.7322694,
      "longitude": -6.2572788
   },
   "1336": {
      "postcode": "NG6",
      "latitude": 52.9985112,
      "longitude": -1.1921785
   },
   "1337": {
      "postcode": "CW9",
      "latitude": 53.2584003,
      "longitude": -2.5017811
   },
   "1338": {
      "postcode": "LL55",
      "latitude": 53.1332669,
      "longitude": -4.2035215
   },
   "1339": {
      "postcode": "PA24",
      "latitude": 56.1584351,
      "longitude": -4.9044299
   },
   "1340": {
      "postcode": "BS11",
      "latitude": 51.4973558,
      "longitude": -2.6752683
   },
   "1341": {
      "postcode": "LL46",
      "latitude": 52.8552904,
      "longitude": -4.1072866
   },
   "1342": {
      "postcode": "BR2",
      "latitude": 51.387269,
      "longitude": 0.0224568
   },
   "1343": {
      "postcode": "TS14",
      "latitude": 54.5324596,
      "longitude": -1.0625812
   },
   "1344": {
      "postcode": "SA2",
      "latitude": 51.6191141,
      "longitude": -3.9979674
   },
   "1345": {
      "postcode": "DN21",
      "latitude": 53.4200117,
      "longitude": -0.7020715
   },
   "1346": {
      "postcode": "DE45",
      "latitude": 53.2147846,
      "longitude": -1.6782889
   },
   "1347": {
      "postcode": "PE7",
      "latitude": 52.5371201,
      "longitude": -0.2061648
   },
   "1348": {
      "postcode": "DG12",
      "latitude": 54.9901401,
      "longitude": -3.2513519
   },
   "1349": {
      "postcode": "LL61",
      "latitude": 53.1959058,
      "longitude": -4.262625
   },
   "1350": {
      "postcode": "KY10",
      "latitude": 56.2307947,
      "longitude": -2.700065
   },
   "1351": {
      "postcode": "RM13",
      "latitude": 51.5252467,
      "longitude": 0.1931007
   },
   "1352": {
      "postcode": "B97",
      "latitude": 52.2996987,
      "longitude": -1.9545616
   },
   "1353": {
      "postcode": "PR1",
      "latitude": 53.7573394,
      "longitude": -2.7017204
   },
   "1354": {
      "postcode": "BN5",
      "latitude": 50.9270143,
      "longitude": -0.2687648
   },
   "1355": {
      "postcode": "KT6",
      "latitude": 51.38741,
      "longitude": -0.3026903
   },
   "1356": {
      "postcode": "HG1",
      "latitude": 53.9999818,
      "longitude": -1.5353201
   },
   "1357": {
      "postcode": "SM7",
      "latitude": 51.3229202,
      "longitude": -0.2014229
   },
   "1358": {
      "postcode": "B36",
      "latitude": 52.5042044,
      "longitude": -1.7784585
   },
   "1359": {
      "postcode": "TN13",
      "latitude": 51.2768935,
      "longitude": 0.1838655
   },
   "1360": {
      "postcode": "SO19",
      "latitude": 50.9019834,
      "longitude": -1.354918
   },
   "1361": {
      "postcode": "SN12",
      "latitude": 51.3722003,
      "longitude": -2.1366155
   },
   "1362": {
      "postcode": "PE25",
      "latitude": 53.1539916,
      "longitude": 0.3342567
   },
   "1363": {
      "postcode": "BH12",
      "latitude": 50.7374063,
      "longitude": -1.9273505
   },
   "1364": {
      "postcode": "YO43",
      "latitude": 53.8493882,
      "longitude": -0.6843122
   },
   "1365": {
      "postcode": "B7",
      "latitude": 52.4941549,
      "longitude": -1.8723775
   },
   "1366": {
      "postcode": "CH25",
      "latitude": 53.3970307,
      "longitude": -3.01145
   },
   "1367": {
      "postcode": "DY9",
      "latitude": 52.4332065,
      "longitude": -2.122508
   },
   "1368": {
      "postcode": "NR5",
      "latitude": 52.6407866,
      "longitude": 1.2286953
   },
   "1369": {
      "postcode": "ST3",
      "latitude": 52.9807695,
      "longitude": -2.1231617
   },
   "1370": {
      "postcode": "GU34",
      "latitude": 51.138975,
      "longitude": -0.9871214
   },
   "1371": {
      "postcode": "CF95",
      "latitude": 51.4811947,
      "longitude": -3.1710394
   },
   "1372": {
      "postcode": "CF47",
      "latitude": 51.7515033,
      "longitude": -3.3750262
   },
   "1373": {
      "postcode": "PH26",
      "latitude": 57.3300387,
      "longitude": -3.6062492
   },
   "1374": {
      "postcode": "UB5",
      "latitude": 51.5431381,
      "longitude": -0.3764324
   },
   "1375": {
      "postcode": "PL27",
      "latitude": 50.5237028,
      "longitude": -4.875155
   },
   "1376": {
      "postcode": "LL73",
      "latitude": 53.3352368,
      "longitude": -4.2449087
   },
   "1377": {
      "postcode": "NR7",
      "latitude": 52.6444333,
      "longitude": 1.3363787
   },
   "1378": {
      "postcode": "RM2",
      "latitude": 51.5843336,
      "longitude": 0.2033607
   },
   "1379": {
      "postcode": "RG5",
      "latitude": 51.4520535,
      "longitude": -0.8996446
   },
   "1380": {
      "postcode": "FK1",
      "latitude": 55.9851464,
      "longitude": -3.7946922
   },
   "1381": {
      "postcode": "CF72",
      "latitude": 51.5298928,
      "longitude": -3.4021313
   },
   "1382": {
      "postcode": "EN3",
      "latitude": 51.6604157,
      "longitude": -0.0366574
   },
   "1383": {
      "postcode": "FK7",
      "latitude": 56.0964876,
      "longitude": -3.9179582
   },
   "1384": {
      "postcode": "FK2",
      "latitude": 56.0050252,
      "longitude": -3.7562534
   },
   "1385": {
      "postcode": "G79",
      "latitude": 55.7710036,
      "longitude": -4.2230758
   },
   "1386": {
      "postcode": "BT70",
      "latitude": 54.5139825,
      "longitude": -6.8875077
   },
   "1387": {
      "postcode": "KY15",
      "latitude": 56.2993375,
      "longitude": -3.05442
   },
   "1388": {
      "postcode": "CO12",
      "latitude": 51.9312042,
      "longitude": 1.2528957
   },
   "1389": {
      "postcode": "SR5",
      "latitude": 54.9226017,
      "longitude": -1.4241884
   },
   "1390": {
      "postcode": "SN16",
      "latitude": 51.5920459,
      "longitude": -2.084858
   },
   "1391": {
      "postcode": "CA5",
      "latitude": 54.85508,
      "longitude": -3.0194131
   },
   "1392": {
      "postcode": "SG17",
      "latitude": 52.0345727,
      "longitude": -0.3353918
   },
   "1393": {
      "postcode": "CA7",
      "latitude": 54.8076079,
      "longitude": -3.2392072
   },
   "1394": {
      "postcode": "LS28",
      "latitude": 53.8023004,
      "longitude": -1.6700027
   },
   "1395": {
      "postcode": "GL8",
      "latitude": 51.6425527,
      "longitude": -2.1709169
   },
   "1396": {
      "postcode": "UB4",
      "latitude": 51.5259518,
      "longitude": -0.4084729
   },
   "1397": {
      "postcode": "RM20",
      "latitude": 51.4784335,
      "longitude": 0.2847884
   },
   "1398": {
      "postcode": "TS5",
      "latitude": 54.5503419,
      "longitude": -1.2523379
   },
   "1399": {
      "postcode": "CR0",
      "latitude": 51.3732242,
      "longitude": -0.0775432
   },
   "1400": {
      "postcode": "SK14",
      "latitude": 53.4520427,
      "longitude": -2.0566162
   },
   "1401": {
      "postcode": "BS37",
      "latitude": 51.5409765,
      "longitude": -2.4141076
   },
   "1402": {
      "postcode": "HA4",
      "latitude": 51.5704138,
      "longitude": -0.4107522
   },
   "1403": {
      "postcode": "RG7",
      "latitude": 51.3976703,
      "longitude": -1.0774783
   },
   "1404": {
      "postcode": "CM77",
      "latitude": 51.8667384,
      "longitude": 0.5523052
   },
   "1405": {
      "postcode": "B71",
      "latitude": 52.5360066,
      "longitude": -1.9904942
   },
   "1406": {
      "postcode": "SS0",
      "latitude": 51.546671,
      "longitude": 0.6877161
   },
   "1407": {
      "postcode": "G65",
      "latitude": 55.9734685,
      "longitude": -4.0575613
   },
   "1408": {
      "postcode": "GL6",
      "latitude": 51.7343681,
      "longitude": -2.1938197
   },
   "1409": {
      "postcode": "WS5",
      "latitude": 52.5659951,
      "longitude": -1.9583275
   },
   "1410": {
      "postcode": "HU11",
      "latitude": 53.8275962,
      "longitude": -0.2216762
   },
   "1411": {
      "postcode": "S18",
      "latitude": 53.299467,
      "longitude": -1.4743449
   },
   "1412": {
      "postcode": "EH10",
      "latitude": 55.9198652,
      "longitude": -3.2111151
   },
   "1413": {
      "postcode": "DA16",
      "latitude": 51.4648617,
      "longitude": 0.1062654
   },
   "1414": {
      "postcode": "AB43",
      "latitude": 57.6572238,
      "longitude": -2.0442865
   },
   "1415": {
      "postcode": "HU7",
      "latitude": 53.7909078,
      "longitude": -0.3292706
   },
   "1416": {
      "postcode": "SW15",
      "latitude": 51.4570342,
      "longitude": -0.2284869
   },
   "1417": {
      "postcode": "SY19",
      "latitude": 52.5793884,
      "longitude": -3.6346543
   },
   "1418": {
      "postcode": "PH41",
      "latitude": 57.0035759,
      "longitude": -5.832467
   },
   "1419": {
      "postcode": "NR18",
      "latitude": 52.5706689,
      "longitude": 1.1079084
   },
   "1420": {
      "postcode": "EX3",
      "latitude": 50.6868408,
      "longitude": -3.4596319
   },
   "1421": {
      "postcode": "NP23",
      "latitude": 51.785403,
      "longitude": -3.1974216
   },
   "1422": {
      "postcode": "UB7",
      "latitude": 51.5044432,
      "longitude": -0.4691618
   },
   "1423": {
      "postcode": "WF10",
      "latitude": 53.7240007,
      "longitude": -1.347783
   },
   "1424": {
      "postcode": "UB1",
      "latitude": 51.5155606,
      "longitude": -0.3733091
   },
   "1425": {
      "postcode": "DN39",
      "latitude": 53.6166111,
      "longitude": -0.3355842
   },
   "1426": {
      "postcode": "SS15",
      "latitude": 51.577489,
      "longitude": 0.4281305
   },
   "1427": {
      "postcode": "TR27",
      "latitude": 50.1828787,
      "longitude": -5.4037493
   },
   "1428": {
      "postcode": "PO18",
      "latitude": 50.8649547,
      "longitude": -0.81514
   },
   "1429": {
      "postcode": "BN88",
      "latitude": 50.8274838,
      "longitude": -0.1400575
   },
   "1430": {
      "postcode": "IV13",
      "latitude": 57.3421909,
      "longitude": -4.0206217
   },
   "1431": {
      "postcode": "BT26",
      "latitude": 54.4542746,
      "longitude": -6.0639346
   },
   "1432": {
      "postcode": "CH64",
      "latitude": 53.2882069,
      "longitude": -3.0476231
   },
   "1433": {
      "postcode": "CF46",
      "latitude": 51.6647879,
      "longitude": -3.300659
   },
   "1434": {
      "postcode": "SK15",
      "latitude": 53.4870446,
      "longitude": -2.0469859
   },
   "1435": {
      "postcode": "TN39",
      "latitude": 50.8468689,
      "longitude": 0.4514689
   },
   "1436": {
      "postcode": "KY2",
      "latitude": 56.1240311,
      "longitude": -3.1846279
   },
   "1437": {
      "postcode": "KW8",
      "latitude": 58.1152848,
      "longitude": -3.6650988
   },
   "1438": {
      "postcode": "L80",
      "latitude": 53.4692073,
      "longitude": -2.9690856
   },
   "1439": {
      "postcode": "YO31",
      "latitude": 53.9699082,
      "longitude": -1.0644173
   },
   "1440": {
      "postcode": "SA31",
      "latitude": 51.8567444,
      "longitude": -4.3082937
   },
   "1441": {
      "postcode": "LS98",
      "latitude": 53.7852835,
      "longitude": -1.538512
   },
   "1442": {
      "postcode": "TR5",
      "latitude": 50.31016,
      "longitude": -5.196735
   },
   "1443": {
      "postcode": "IV30",
      "latitude": 57.6524753,
      "longitude": -3.3254479
   },
   "1444": {
      "postcode": "S12",
      "latitude": 53.3482005,
      "longitude": -1.4064871
   },
   "1445": {
      "postcode": "N12",
      "latitude": 51.6149237,
      "longitude": -0.1776502
   },
   "1446": {
      "postcode": "YO1",
      "latitude": 53.9586237,
      "longitude": -1.0828142
   },
   "1447": {
      "postcode": "GU6",
      "latitude": 51.1405502,
      "longitude": -0.4841941
   },
   "1448": {
      "postcode": "RG19",
      "latitude": 51.3912084,
      "longitude": -1.2443747
   },
   "1449": {
      "postcode": "CF42",
      "latitude": 51.667356,
      "longitude": -3.5238408
   },
   "1450": {
      "postcode": "SA3",
      "latitude": 51.5817133,
      "longitude": -4.0513777
   },
   "1451": {
      "postcode": "DE65",
      "latitude": 52.8669174,
      "longitude": -1.6116951
   },
   "1452": {
      "postcode": "DA17",
      "latitude": 51.4861908,
      "longitude": 0.1491035
   },
   "1453": {
      "postcode": "HX3",
      "latitude": 53.7267217,
      "longitude": -1.844259
   },
   "1454": {
      "postcode": "HU18",
      "latitude": 53.9099131,
      "longitude": -0.1689549
   },
   "1455": {
      "postcode": "EH13",
      "latitude": 55.9067795,
      "longitude": -3.2429491
   },
   "1456": {
      "postcode": "PA76",
      "latitude": 56.3340203,
      "longitude": -6.3943735
   },
   "1457": {
      "postcode": "DT2",
      "latitude": 50.7497424,
      "longitude": -2.4509175
   },
   "1458": {
      "postcode": "G78",
      "latitude": 55.7929059,
      "longitude": -4.4098882
   },
   "1459": {
      "postcode": "IV45",
      "latitude": 57.0717262,
      "longitude": -5.9065595
   },
   "1460": {
      "postcode": "TR15",
      "latitude": 50.2331276,
      "longitude": -5.2380409
   },
   "1461": {
      "postcode": "NR9",
      "latitude": 52.6336604,
      "longitude": 1.1078046
   },
   "1462": {
      "postcode": "YO8",
      "latitude": 53.7812636,
      "longitude": -1.0606474
   },
   "1463": {
      "postcode": "PA14",
      "latitude": 55.92732,
      "longitude": -4.6642031
   },
   "1464": {
      "postcode": "GU14",
      "latitude": 51.2939331,
      "longitude": -0.763558
   },
   "1465": {
      "postcode": "BS21",
      "latitude": 51.4350533,
      "longitude": -2.8498455
   },
   "1466": {
      "postcode": "CV36",
      "latitude": 52.0590955,
      "longitude": -1.6218655
   },
   "1467": {
      "postcode": "WV16",
      "latitude": 52.5095974,
      "longitude": -2.4409185
   },
   "1468": {
      "postcode": "MK14",
      "latitude": 52.0632325,
      "longitude": -0.7553798
   },
   "1469": {
      "postcode": "GU3",
      "latitude": 51.2467422,
      "longitude": -0.6286183
   },
   "1470": {
      "postcode": "N9",
      "latitude": 51.6285027,
      "longitude": -0.0580156
   },
   "1471": {
      "postcode": "TS26",
      "latitude": 54.688955,
      "longitude": -1.2326907
   },
   "1472": {
      "postcode": "IV32",
      "latitude": 57.630793,
      "longitude": -3.1048715
   },
   "1473": {
      "postcode": "TW6",
      "latitude": 51.4709495,
      "longitude": -0.4483159
   },
   "1474": {
      "postcode": "SE24",
      "latitude": 51.4563048,
      "longitude": -0.1002302
   },
   "1475": {
      "postcode": "DD11",
      "latitude": 56.5735539,
      "longitude": -2.5990122
   },
   "1476": {
      "postcode": "SE10",
      "latitude": 51.4846226,
      "longitude": 0.0003716
   },
   "1477": {
      "postcode": "UB18",
      "latitude": 51.5007178,
      "longitude": -0.4026841
   },
   "1478": {
      "postcode": "B13",
      "latitude": 52.4375032,
      "longitude": -1.8790028
   },
   "1479": {
      "postcode": "KA28",
      "latitude": 55.7540267,
      "longitude": -4.925425
   },
   "1480": {
      "postcode": "CH44",
      "latitude": 53.415302,
      "longitude": -3.0370999
   },
   "1481": {
      "postcode": "DN3",
      "latitude": 53.546061,
      "longitude": -1.059325
   },
   "1482": {
      "postcode": "TR13",
      "latitude": 50.1095854,
      "longitude": -5.2866459
   },
   "1483": {
      "postcode": "BT55",
      "latitude": 55.179239,
      "longitude": -6.7104568
   },
   "1484": {
      "postcode": "BB1",
      "latitude": 53.7567872,
      "longitude": -2.462979
   },
   "1485": {
      "postcode": "HD4",
      "latitude": 53.6256253,
      "longitude": -1.797853
   },
   "1486": {
      "postcode": "NE82",
      "latitude": 54.93464,
      "longitude": -1.6151031
   },
   "1487": {
      "postcode": "PL95",
      "latitude": 50.3644065,
      "longitude": -4.1044393
   },
   "1488": {
      "postcode": "NE23",
      "latitude": 55.0800801,
      "longitude": -1.582986
   },
   "1489": {
      "postcode": "DT11",
      "latitude": 50.8615403,
      "longitude": -2.1834102
   },
   "1490": {
      "postcode": "BR4",
      "latitude": 51.3750032,
      "longitude": -0.0083853
   },
   "1491": {
      "postcode": "SK2",
      "latitude": 53.3943065,
      "longitude": -2.1323676
   },
   "1492": {
      "postcode": "G90",
      "latitude": 55.8689906,
      "longitude": -4.2410555
   },
   "1493": {
      "postcode": "BD3",
      "latitude": 53.7984863,
      "longitude": -1.7267147
   },
   "1494": {
      "postcode": "TN31",
      "latitude": 50.962869,
      "longitude": 0.6855793
   },
   "1495": {
      "postcode": "L11",
      "latitude": 53.4478258,
      "longitude": -2.9154238
   },
   "1496": {
      "postcode": "DN20",
      "latitude": 53.5580271,
      "longitude": -0.5063124
   },
   "1497": {
      "postcode": "SW17",
      "latitude": 51.4307971,
      "longitude": -0.1648874
   },
   "1498": {
      "postcode": "M3",
      "latitude": 53.4836687,
      "longitude": -2.2528623
   },
   "1499": {
      "postcode": "BT32",
      "latitude": 54.3355257,
      "longitude": -6.2456426
   },
   "1500": {
      "postcode": "UB3",
      "latitude": 51.5052003,
      "longitude": -0.4245561
   },
   "1501": {
      "postcode": "PO10",
      "latitude": 50.8522374,
      "longitude": -0.9293902
   },
   "1502": {
      "postcode": "WS11",
      "latitude": 52.6880429,
      "longitude": -2.0173886
   },
   "1503": {
      "postcode": "BN18",
      "latitude": 50.8476816,
      "longitude": -0.5840822
   },
   "1504": {
      "postcode": "PO5",
      "latitude": 50.7886425,
      "longitude": -1.0861972
   },
   "1505": {
      "postcode": "KY14",
      "latitude": 56.3108245,
      "longitude": -3.2419856
   },
   "1506": {
      "postcode": "NG17",
      "latitude": 53.1160576,
      "longitude": -1.2615156
   },
   "1507": {
      "postcode": "SA7",
      "latitude": 51.6647175,
      "longitude": -3.8881517
   },
   "1508": {
      "postcode": "PR6",
      "latitude": 53.6677742,
      "longitude": -2.6119293
   },
   "1509": {
      "postcode": "G21",
      "latitude": 55.8822282,
      "longitude": -4.2201317
   },
   "1510": {
      "postcode": "HS3",
      "latitude": 57.8774467,
      "longitude": -6.8512421
   },
   "1511": {
      "postcode": "DL14",
      "latitude": 54.6515089,
      "longitude": -1.6921535
   },
   "1512": {
      "postcode": "B24",
      "latitude": 52.5196415,
      "longitude": -1.8271375
   },
   "1513": {
      "postcode": "BT14",
      "latitude": 54.621457,
      "longitude": -5.9626627
   },
   "1514": {
      "postcode": "AB24",
      "latitude": 57.1639292,
      "longitude": -2.1079218
   },
   "1515": {
      "postcode": "B45",
      "latitude": 52.3885168,
      "longitude": -2.0090938
   },
   "1516": {
      "postcode": "BD16",
      "latitude": 53.8484508,
      "longitude": -1.8331337
   },
   "1517": {
      "postcode": "CH88",
      "latitude": 53.1945673,
      "longitude": -2.874551
   },
   "1518": {
      "postcode": "BN13",
      "latitude": 50.8326835,
      "longitude": -0.4113838
   },
   "1519": {
      "postcode": "CV22",
      "latitude": 52.359079,
      "longitude": -1.2784656
   },
   "1520": {
      "postcode": "IG2",
      "latitude": 51.5760405,
      "longitude": 0.0815331
   },
   "1521": {
      "postcode": "BT23",
      "latitude": 54.564476,
      "longitude": -5.7153624
   },
   "1522": {
      "postcode": "PA16",
      "latitude": 55.9425162,
      "longitude": -4.8009273
   },
   "1523": {
      "postcode": "W2",
      "latitude": 51.5151251,
      "longitude": -0.1854875
   },
   "1524": {
      "postcode": "CV1",
      "latitude": 52.4094028,
      "longitude": -1.5065272
   },
   "1525": {
      "postcode": "PA25",
      "latitude": 56.2143195,
      "longitude": -5.0433625
   },
   "1526": {
      "postcode": "NN16",
      "latitude": 52.4046781,
      "longitude": -0.7057147
   },
   "1527": {
      "postcode": "SL7",
      "latitude": 51.5753276,
      "longitude": -0.777869
   },
   "1528": {
      "postcode": "NW6",
      "latitude": 51.542172,
      "longitude": -0.1962878
   },
   "1529": {
      "postcode": "S10",
      "latitude": 53.3767062,
      "longitude": -1.5185445
   },
   "1530": {
      "postcode": "CB25",
      "latitude": 52.2608073,
      "longitude": 0.2541302
   },
   "1531": {
      "postcode": "IG3",
      "latitude": 51.5631159,
      "longitude": 0.1029088
   },
   "1532": {
      "postcode": "IV2",
      "latitude": 57.4680582,
      "longitude": -4.1860306
   },
   "1533": {
      "postcode": "PO12",
      "latitude": 50.7979491,
      "longitude": -1.1418001
   },
   "1534": {
      "postcode": "PH9",
      "latitude": 56.6480509,
      "longitude": -3.6899621
   },
   "1535": {
      "postcode": "CM20",
      "latitude": 51.7753987,
      "longitude": 0.1026721
   },
   "1536": {
      "postcode": "GU15",
      "latitude": 51.3355019,
      "longitude": -0.7376588
   },
   "1537": {
      "postcode": "CB21",
      "latitude": 52.128038,
      "longitude": 0.2815412
   },
   "1538": {
      "postcode": "AL10",
      "latitude": 51.7604054,
      "longitude": -0.2323864
   },
   "1539": {
      "postcode": "SM2",
      "latitude": 51.3518298,
      "longitude": -0.1987871
   },
   "1540": {
      "postcode": "NW7",
      "latitude": 51.6148052,
      "longitude": -0.2348917
   },
   "1541": {
      "postcode": "PA80",
      "latitude": 56.5659697,
      "longitude": -5.786465
   },
   "1542": {
      "postcode": "LL24",
      "latitude": 53.0577084,
      "longitude": -3.7859794
   },
   "1543": {
      "postcode": "PA45",
      "latitude": 55.8196554,
      "longitude": -6.1668358
   },
   "1544": {
      "postcode": "BT71",
      "latitude": 54.5128046,
      "longitude": -6.7043034
   },
   "1545": {
      "postcode": "NR13",
      "latitude": 52.6338547,
      "longitude": 1.4697849
   },
   "1546": {
      "postcode": "CR6",
      "latitude": 51.3092312,
      "longitude": -0.0527574
   },
   "1547": {
      "postcode": "LN12",
      "latitude": 53.3292696,
      "longitude": 0.2640547
   },
   "1548": {
      "postcode": "BH8",
      "latitude": 50.7419912,
      "longitude": -1.8519359
   },
   "1549": {
      "postcode": "DD5",
      "latitude": 56.4799789,
      "longitude": -2.8580673
   },
   "1550": {
      "postcode": "L3",
      "latitude": 53.4084083,
      "longitude": -2.984451
   },
   "1551": {
      "postcode": "PH50",
      "latitude": 56.7145473,
      "longitude": -4.964924
   },
   "1552": {
      "postcode": "IV41",
      "latitude": 57.2728062,
      "longitude": -5.7361569
   },
   "1553": {
      "postcode": "ST6",
      "latitude": 53.0579381,
      "longitude": -2.1895987
   },
   "1554": {
      "postcode": "CM92",
      "latitude": 51.7693558,
      "longitude": 0.0612532
   },
   "1555": {
      "postcode": "WV9",
      "latitude": 52.6376624,
      "longitude": -2.1435341
   },
   "1556": {
      "postcode": "PH16",
      "latitude": 56.7067956,
      "longitude": -3.8062465
   },
   "1557": {
      "postcode": "NN6",
      "latitude": 52.3269298,
      "longitude": -0.9458447
   },
   "1558": {
      "postcode": "MK2",
      "latitude": 51.990521,
      "longitude": -0.7252031
   },
   "1559": {
      "postcode": "PL32",
      "latitude": 50.6332624,
      "longitude": -4.6619385
   },
   "1560": {
      "postcode": "OX16",
      "latitude": 52.0625051,
      "longitude": -1.3425431
   },
   "1561": {
      "postcode": "NP18",
      "latitude": 51.6087786,
      "longitude": -2.9423237
   },
   "1562": {
      "postcode": "TR14",
      "latitude": 50.2107232,
      "longitude": -5.2967361
   },
   "1563": {
      "postcode": "RH18",
      "latitude": 51.0932269,
      "longitude": 0.035663
   },
   "1564": {
      "postcode": "BS1",
      "latitude": 51.4532627,
      "longitude": -2.5935387
   },
   "1565": {
      "postcode": "NR21",
      "latitude": 52.8414338,
      "longitude": 0.8522567
   },
   "1566": {
      "postcode": "CT21",
      "latitude": 51.0725975,
      "longitude": 1.0760693
   },
   "1567": {
      "postcode": "CF32",
      "latitude": 51.5599583,
      "longitude": -3.5842696
   },
   "1568": {
      "postcode": "BD19",
      "latitude": 53.7273298,
      "longitude": -1.7141196
   },
   "1569": {
      "postcode": "N20",
      "latitude": 51.6292552,
      "longitude": -0.1743686
   },
   "1570": {
      "postcode": "SO43",
      "latitude": 50.8862421,
      "longitude": -1.5893747
   },
   "1571": {
      "postcode": "SY18",
      "latitude": 52.4415588,
      "longitude": -3.5494041
   },
   "1572": {
      "postcode": "BH7",
      "latitude": 50.7364005,
      "longitude": -1.8263105
   },
   "1573": {
      "postcode": "BD1",
      "latitude": 53.7966616,
      "longitude": -1.7545344
   },
   "1574": {
      "postcode": "LS24",
      "latitude": 53.8687779,
      "longitude": -1.2530036
   },
   "1575": {
      "postcode": "KA14",
      "latitude": 55.7401813,
      "longitude": -4.6733417
   },
   "1576": {
      "postcode": "FK16",
      "latitude": 56.1911637,
      "longitude": -4.0610009
   },
   "1577": {
      "postcode": "WV4",
      "latitude": 52.5614099,
      "longitude": -2.1447119
   },
   "1578": {
      "postcode": "ME3",
      "latitude": 51.4354568,
      "longitude": 0.5468331
   },
   "1579": {
      "postcode": "SS2",
      "latitude": 51.5508903,
      "longitude": 0.7167546
   },
   "1580": {
      "postcode": "LA5",
      "latitude": 54.1438808,
      "longitude": -2.7918796
   },
   "1581": {
      "postcode": "BT69",
      "latitude": 54.4199975,
      "longitude": -6.9502828
   },
   "1582": {
      "postcode": "ME16",
      "latitude": 51.273831,
      "longitude": 0.4960741
   },
   "1583": {
      "postcode": "BL9",
      "latitude": 53.5918117,
      "longitude": -2.2870531
   },
   "1584": {
      "postcode": "E5",
      "latitude": 51.5588861,
      "longitude": -0.0537874
   },
   "1585": {
      "postcode": "TN24",
      "latitude": 51.1497728,
      "longitude": 0.8877433
   },
   "1586": {
      "postcode": "DY14",
      "latitude": 52.3804492,
      "longitude": -2.4685572
   },
   "1587": {
      "postcode": "KA10",
      "latitude": 55.550437,
      "longitude": -4.6476679
   },
   "1588": {
      "postcode": "NG4",
      "latitude": 52.9710572,
      "longitude": -1.0877171
   },
   "1589": {
      "postcode": "NG19",
      "latitude": 53.1605766,
      "longitude": -1.1983361
   },
   "1590": {
      "postcode": "BT61",
      "latitude": 54.3687705,
      "longitude": -6.6224601
   },
   "1591": {
      "postcode": "SA35",
      "latitude": 51.9710664,
      "longitude": -4.5582429
   },
   "1592": {
      "postcode": "KA25",
      "latitude": 55.7533969,
      "longitude": -4.6885437
   },
   "1593": {
      "postcode": "HS1",
      "latitude": 58.2126144,
      "longitude": -6.3814786
   },
   "1594": {
      "postcode": "CH47",
      "latitude": 53.3964675,
      "longitude": -3.1691925
   },
   "1595": {
      "postcode": "BT48",
      "latitude": 55.0103984,
      "longitude": -7.3273919
   },
   "1596": {
      "postcode": "IG1",
      "latitude": 51.5594197,
      "longitude": 0.0733642
   },
   "1597": {
      "postcode": "BT31",
      "latitude": 54.2769937,
      "longitude": -5.9689188
   },
   "1598": {
      "postcode": "NE68",
      "latitude": 55.5798149,
      "longitude": -1.6589189
   },
   "1599": {
      "postcode": "NP15",
      "latitude": 51.7263322,
      "longitude": -2.8867108
   },
   "1600": {
      "postcode": "PH11",
      "latitude": 56.6381789,
      "longitude": -3.2349256
   },
   "1601": {
      "postcode": "PH35",
      "latitude": 57.0755394,
      "longitude": -4.9027758
   },
   "1602": {
      "postcode": "CF33",
      "latitude": 51.5255628,
      "longitude": -3.6931827
   },
   "1603": {
      "postcode": "RG23",
      "latitude": 51.2582357,
      "longitude": -1.1500593
   },
   "1604": {
      "postcode": "IV28",
      "latitude": 58.0097064,
      "longitude": -4.1581729
   },
   "1605": {
      "postcode": "BN21",
      "latitude": 50.7726897,
      "longitude": 0.2765565
   },
   "1606": {
      "postcode": "LL33",
      "latitude": 53.2507498,
      "longitude": -3.9789879
   },
   "1607": {
      "postcode": "TN38",
      "latitude": 50.8637392,
      "longitude": 0.543696
   },
   "1608": {
      "postcode": "LN11",
      "latitude": 53.3730382,
      "longitude": 0.0260752
   },
   "1609": {
      "postcode": "LL45",
      "latitude": 52.8220907,
      "longitude": -4.0961914
   },
   "1610": {
      "postcode": "WC1E",
      "latitude": 51.5217107,
      "longitude": -0.1328422
   },
   "1611": {
      "postcode": "FY8",
      "latitude": 53.7508559,
      "longitude": -3.0027549
   },
   "1612": {
      "postcode": "BD21",
      "latitude": 53.864231,
      "longitude": -1.9076629
   },
   "1613": {
      "postcode": "CF35",
      "latitude": 51.5227048,
      "longitude": -3.5254789
   },
   "1614": {
      "postcode": "HD5",
      "latitude": 53.6474167,
      "longitude": -1.7462168
   },
   "1615": {
      "postcode": "GU20",
      "latitude": 51.3687408,
      "longitude": -0.6579475
   },
   "1616": {
      "postcode": "WR5",
      "latitude": 52.1748639,
      "longitude": -2.2020856
   },
   "1617": {
      "postcode": "G44",
      "latitude": 55.8141896,
      "longitude": -4.2556442
   },
   "1618": {
      "postcode": "KW11",
      "latitude": 58.3080468,
      "longitude": -4.1362061
   },
   "1619": {
      "postcode": "GL53",
      "latitude": 51.8795927,
      "longitude": -2.0676025
   },
   "1620": {
      "postcode": "DG11",
      "latitude": 55.113619,
      "longitude": -3.3386407
   },
   "1621": {
      "postcode": "MK6",
      "latitude": 52.0295557,
      "longitude": -0.7429696
   },
   "1622": {
      "postcode": "CV6",
      "latitude": 52.4341647,
      "longitude": -1.5074757
   },
   "1623": {
      "postcode": "DH2",
      "latitude": 54.8597025,
      "longitude": -1.5995581
   },
   "1624": {
      "postcode": "L14",
      "latitude": 53.4179489,
      "longitude": -2.8808404
   },
   "1625": {
      "postcode": "DL12",
      "latitude": 54.5721304,
      "longitude": -1.9855857
   },
   "1626": {
      "postcode": "EX24",
      "latitude": 50.7404493,
      "longitude": -3.0893775
   },
   "1627": {
      "postcode": "GU24",
      "latitude": 51.3303573,
      "longitude": -0.6282203
   },
   "1628": {
      "postcode": "GU9",
      "latitude": 51.219137,
      "longitude": -0.7942479
   },
   "1629": {
      "postcode": "KW3",
      "latitude": 58.3064884,
      "longitude": -3.2804565
   },
   "1630": {
      "postcode": "CF99",
      "latitude": 51.464505,
      "longitude": -3.16135
   },
   "1631": {
      "postcode": "EX2",
      "latitude": 50.7095079,
      "longitude": -3.5143056
   },
   "1632": {
      "postcode": "BS28",
      "latitude": 51.2260512,
      "longitude": -2.8149367
   },
   "1633": {
      "postcode": "LL53",
      "latitude": 52.8841626,
      "longitude": -4.4927499
   },
   "1634": {
      "postcode": "BS16",
      "latitude": 51.4868114,
      "longitude": -2.5100273
   },
   "1635": {
      "postcode": "BL3",
      "latitude": 53.5646619,
      "longitude": -2.4321772
   },
   "1636": {
      "postcode": "NE11",
      "latitude": 54.9399167,
      "longitude": -1.6358329
   },
   "1637": {
      "postcode": "BT94",
      "latitude": 54.3760757,
      "longitude": -7.5336959
   },
   "1638": {
      "postcode": "PA9",
      "latitude": 55.8072925,
      "longitude": -4.5569521
   },
   "1639": {
      "postcode": "IV26",
      "latitude": 57.9267694,
      "longitude": -5.193821
   },
   "1640": {
      "postcode": "LS17",
      "latitude": 53.8600575,
      "longitude": -1.5277566
   },
   "1641": {
      "postcode": "CB24",
      "latitude": 52.2782051,
      "longitude": 0.0817273
   },
   "1642": {
      "postcode": "KA22",
      "latitude": 55.6499957,
      "longitude": -4.8088415
   },
   "1643": {
      "postcode": "IP20",
      "latitude": 52.4065354,
      "longitude": 1.3191966
   },
   "1644": {
      "postcode": "SE21",
      "latitude": 51.438989,
      "longitude": -0.0887527
   },
   "1645": {
      "postcode": "SE13",
      "latitude": 51.4594042,
      "longitude": -0.0095672
   },
   "1646": {
      "postcode": "PA63",
      "latitude": 56.3817723,
      "longitude": -5.7158719
   },
   "1647": {
      "postcode": "BT35",
      "latitude": 54.1620226,
      "longitude": -6.4418816
   },
   "1648": {
      "postcode": "E1W",
      "latitude": 51.5091122,
      "longitude": -0.0589168
   },
   "1649": {
      "postcode": "N15",
      "latitude": 51.5826261,
      "longitude": -0.081173
   },
   "1650": {
      "postcode": "WV3",
      "latitude": 52.5790352,
      "longitude": -2.1565201
   },
   "1651": {
      "postcode": "TF4",
      "latitude": 52.6626967,
      "longitude": -2.4715605
   },
   "1652": {
      "postcode": "SW5",
      "latitude": 51.4915827,
      "longitude": -0.1919239
   },
   "1653": {
      "postcode": "RG26",
      "latitude": 51.3401022,
      "longitude": -1.1297305
   },
   "1654": {
      "postcode": "NN2",
      "latitude": 52.2625668,
      "longitude": -0.8886515
   },
   "1655": {
      "postcode": "B33",
      "latitude": 52.4802868,
      "longitude": -1.7884156
   },
   "1656": {
      "postcode": "OL95",
      "latitude": 53.5563368,
      "longitude": -2.1054013
   },
   "1657": {
      "postcode": "YO42",
      "latitude": 53.9238079,
      "longitude": -0.7902264
   },
   "1658": {
      "postcode": "PH37",
      "latitude": 56.8356654,
      "longitude": -5.501676
   },
   "1659": {
      "postcode": "NN3",
      "latitude": 52.2639662,
      "longitude": -0.8422004
   },
   "1660": {
      "postcode": "SN9",
      "latitude": 51.3242371,
      "longitude": -1.7880126
   },
   "1661": {
      "postcode": "TQ5",
      "latitude": 50.391781,
      "longitude": -3.5234852
   },
   "1662": {
      "postcode": "TA13",
      "latitude": 50.9466906,
      "longitude": -2.8102347
   },
   "1663": {
      "postcode": "B11",
      "latitude": 52.4544936,
      "longitude": -1.8581324
   },
   "1664": {
      "postcode": "G3",
      "latitude": 55.8658506,
      "longitude": -4.2778116
   },
   "1665": {
      "postcode": "CT13",
      "latitude": 51.2664408,
      "longitude": 1.327004
   },
   "1666": {
      "postcode": "L34",
      "latitude": 53.435385,
      "longitude": -2.8154652
   },
   "1667": {
      "postcode": "MK13",
      "latitude": 52.0532824,
      "longitude": -0.7825057
   },
   "1668": {
      "postcode": "B66",
      "latitude": 52.4926661,
      "longitude": -1.9647632
   },
   "1669": {
      "postcode": "IP11",
      "latitude": 51.9675191,
      "longitude": 1.3411933
   },
   "1670": {
      "postcode": "CH1",
      "latitude": 53.2022603,
      "longitude": -2.9089758
   },
   "1671": {
      "postcode": "W14",
      "latitude": 51.494691,
      "longitude": -0.2102541
   },
   "1672": {
      "postcode": "WC1H",
      "latitude": 51.5268445,
      "longitude": -0.1256084
   },
   "1673": {
      "postcode": "M15",
      "latitude": 53.4673852,
      "longitude": -2.2514891
   },
   "1674": {
      "postcode": "NR30",
      "latitude": 52.6197388,
      "longitude": 1.7277361
   },
   "1675": {
      "postcode": "KW2",
      "latitude": 58.3483934,
      "longitude": -3.1636573
   },
   "1676": {
      "postcode": "SA62",
      "latitude": 51.841175,
      "longitude": -5.0642757
   },
   "1677": {
      "postcode": "PE38",
      "latitude": 52.5881901,
      "longitude": 0.3752984
   },
   "1678": {
      "postcode": "CV4",
      "latitude": 52.3972327,
      "longitude": -1.5714648
   },
   "1679": {
      "postcode": "LS12",
      "latitude": 53.7912186,
      "longitude": -1.5972635
   },
   "1680": {
      "postcode": "MK44",
      "latitude": 52.1965903,
      "longitude": -0.4242789
   },
   "1681": {
      "postcode": "L29",
      "latitude": 53.5075951,
      "longitude": -2.9855216
   },
   "1682": {
      "postcode": "BT5",
      "latitude": 54.5891629,
      "longitude": -5.871144
   },
   "1683": {
      "postcode": "G43",
      "latitude": 55.8184976,
      "longitude": -4.2918152
   },
   "1684": {
      "postcode": "SK12",
      "latitude": 53.3514172,
      "longitude": -2.0924709
   },
   "1685": {
      "postcode": "B77",
      "latitude": 52.6185928,
      "longitude": -1.66868
   },
   "1686": {
      "postcode": "BA14",
      "latitude": 51.3191164,
      "longitude": -2.2025658
   },
   "1687": {
      "postcode": "NE67",
      "latitude": 55.536534,
      "longitude": -1.6919416
   },
   "1688": {
      "postcode": "CF15",
      "latitude": 51.5333849,
      "longitude": -3.271715
   },
   "1689": {
      "postcode": "SW19",
      "latitude": 51.4241552,
      "longitude": -0.2029208
   },
   "1690": {
      "postcode": "CF5",
      "latitude": 51.4829052,
      "longitude": -3.2447881
   },
   "1691": {
      "postcode": "KT10",
      "latitude": 51.3695018,
      "longitude": -0.3543868
   },
   "1692": {
      "postcode": "KA20",
      "latitude": 55.6413789,
      "longitude": -4.7511586
   },
   "1693": {
      "postcode": "TW20",
      "latitude": 51.4274804,
      "longitude": -0.5525407
   },
   "1694": {
      "postcode": "FY2",
      "latitude": 53.8459338,
      "longitude": -3.0396623
   },
   "1695": {
      "postcode": "SO24",
      "latitude": 51.0844741,
      "longitude": -1.1471161
   },
   "1696": {
      "postcode": "SE19",
      "latitude": 51.4179954,
      "longitude": -0.0861287
   },
   "1697": {
      "postcode": "LL77",
      "latitude": 53.2605503,
      "longitude": -4.3124692
   },
   "1698": {
      "postcode": "DE6",
      "latitude": 52.9922845,
      "longitude": -1.7179509
   },
   "1699": {
      "postcode": "LS2",
      "latitude": 53.8028065,
      "longitude": -1.5463049
   },
   "1700": {
      "postcode": "OL8",
      "latitude": 53.5258859,
      "longitude": -2.1173031
   },
   "1701": {
      "postcode": "ST2",
      "latitude": 53.028141,
      "longitude": -2.1354237
   },
   "1702": {
      "postcode": "PO38",
      "latitude": 50.6053631,
      "longitude": -1.2432132
   },
   "1703": {
      "postcode": "WA15",
      "latitude": 53.3845913,
      "longitude": -2.3259397
   },
   "1704": {
      "postcode": "W9",
      "latitude": 51.5247242,
      "longitude": -0.1926416
   },
   "1705": {
      "postcode": "NG24",
      "latitude": 53.0696884,
      "longitude": -0.7990824
   },
   "1706": {
      "postcode": "DE15",
      "latitude": 52.7980963,
      "longitude": -1.6087583
   },
   "1707": {
      "postcode": "CB1",
      "latitude": 52.1953297,
      "longitude": 0.1420534
   },
   "1708": {
      "postcode": "DN17",
      "latitude": 53.5727238,
      "longitude": -0.7059175
   },
   "1709": {
      "postcode": "G81",
      "latitude": 55.9138295,
      "longitude": -4.4077065
   },
   "1710": {
      "postcode": "BT78",
      "latitude": 54.5709348,
      "longitude": -7.3760979
   },
   "1711": {
      "postcode": "BB9",
      "latitude": 53.8374035,
      "longitude": -2.2156194
   },
   "1712": {
      "postcode": "EN2",
      "latitude": 51.6599921,
      "longitude": -0.0941879
   },
   "1713": {
      "postcode": "DH3",
      "latitude": 54.8727478,
      "longitude": -1.5679921
   },
   "1714": {
      "postcode": "BB7",
      "latitude": 53.8708936,
      "longitude": -2.3888971
   },
   "1715": {
      "postcode": "PE22",
      "latitude": 53.0501008,
      "longitude": 0.0445584
   },
   "1716": {
      "postcode": "KW12",
      "latitude": 58.5057403,
      "longitude": -3.4926733
   },
   "1717": {
      "postcode": "M18",
      "latitude": 53.4613132,
      "longitude": -2.1703934
   },
   "1718": {
      "postcode": "YO22",
      "latitude": 54.4508006,
      "longitude": -0.6217825
   },
   "1719": {
      "postcode": "AL8",
      "latitude": 51.803623,
      "longitude": -0.2117607
   },
   "1720": {
      "postcode": "RM4",
      "latitude": 51.6410737,
      "longitude": 0.1587939
   },
   "1721": {
      "postcode": "KA5",
      "latitude": 55.5104356,
      "longitude": -4.3878367
   },
   "1722": {
      "postcode": "ME20",
      "latitude": 51.3033514,
      "longitude": 0.4598919
   },
   "1723": {
      "postcode": "IV46",
      "latitude": 57.111871,
      "longitude": -5.9840485
   },
   "1724": {
      "postcode": "DG13",
      "latitude": 55.1733051,
      "longitude": -3.0305281
   },
   "1725": {
      "postcode": "ME5",
      "latitude": 51.348554,
      "longitude": 0.532612
   },
   "1726": {
      "postcode": "ME19",
      "latitude": 51.2904715,
      "longitude": 0.407949
   },
   "1727": {
      "postcode": "HP15",
      "latitude": 51.6585214,
      "longitude": -0.7117144
   },
   "1728": {
      "postcode": "SA15",
      "latitude": 51.6995488,
      "longitude": -4.1678401
   },
   "1729": {
      "postcode": "S32",
      "latitude": 53.2945357,
      "longitude": -1.6515465
   },
   "1730": {
      "postcode": "NW1W",
      "latitude": 51.5307841,
      "longitude": -0.1354264
   },
   "1731": {
      "postcode": "BS98",
      "latitude": 51.4597488,
      "longitude": -2.5889635
   },
   "1732": {
      "postcode": "N2",
      "latitude": 51.5900894,
      "longitude": -0.1692626
   },
   "1733": {
      "postcode": "BD24",
      "latitude": 54.080044,
      "longitude": -2.2841297
   },
   "1734": {
      "postcode": "IP17",
      "latitude": 52.2304463,
      "longitude": 1.5018473
   },
   "1735": {
      "postcode": "TR22",
      "latitude": 49.895171,
      "longitude": -6.340873
   },
   "1736": {
      "postcode": "KT12",
      "latitude": 51.3773192,
      "longitude": -0.4083965
   },
   "1737": {
      "postcode": "BD2",
      "latitude": 53.8152428,
      "longitude": -1.7344633
   },
   "1738": {
      "postcode": "LN8",
      "latitude": 53.374899,
      "longitude": -0.3265738
   },
   "1739": {
      "postcode": "KW17",
      "latitude": 59.0364329,
      "longitude": -3.0093093
   },
   "1740": {
      "postcode": "HU19",
      "latitude": 53.7233393,
      "longitude": 0.0344319
   },
   "1741": {
      "postcode": "LN2",
      "latitude": 53.2571394,
      "longitude": -0.5062171
   },
   "1742": {
      "postcode": "BN26",
      "latitude": 50.8211682,
      "longitude": 0.2228173
   },
   "1743": {
      "postcode": "LL16",
      "latitude": 53.185191,
      "longitude": -3.4330517
   },
   "1744": {
      "postcode": "PH14",
      "latitude": 56.4528883,
      "longitude": -3.1808965
   },
   "1745": {
      "postcode": "KY5",
      "latitude": 56.145365,
      "longitude": -3.2948408
   },
   "1746": {
      "postcode": "SA72",
      "latitude": 51.6917901,
      "longitude": -4.9355542
   },
   "1747": {
      "postcode": "PL11",
      "latitude": 50.372956,
      "longitude": -4.2549194
   },
   "1748": {
      "postcode": "EC3A",
      "latitude": 51.5147892,
      "longitude": -0.0802178
   },
   "1749": {
      "postcode": "PR7",
      "latitude": 53.6486409,
      "longitude": -2.655302
   },
   "1750": {
      "postcode": "S36",
      "latitude": 53.5054492,
      "longitude": -1.616598
   },
   "1751": {
      "postcode": "KT17",
      "latitude": 51.3412,
      "longitude": -0.2495666
   },
   "1752": {
      "postcode": "ST16",
      "latitude": 52.8135538,
      "longitude": -2.1201818
   },
   "1753": {
      "postcode": "CF3",
      "latitude": 51.5203429,
      "longitude": -3.1110728
   },
   "1754": {
      "postcode": "SA44",
      "latitude": 52.0874643,
      "longitude": -4.3732402
   },
   "1755": {
      "postcode": "TS18",
      "latitude": 54.5609693,
      "longitude": -1.3240632
   },
   "1756": {
      "postcode": "SN7",
      "latitude": 51.6484265,
      "longitude": -1.5662623
   },
   "1757": {
      "postcode": "IP23",
      "latitude": 52.3073907,
      "longitude": 1.1200031
   },
   "1758": {
      "postcode": "BD23",
      "latitude": 53.993339,
      "longitude": -2.0569312
   },
   "1759": {
      "postcode": "PL3",
      "latitude": 50.3882426,
      "longitude": -4.1272702
   },
   "1760": {
      "postcode": "YO51",
      "latitude": 54.0900779,
      "longitude": -1.3947245
   },
   "1761": {
      "postcode": "GU2",
      "latitude": 51.2457661,
      "longitude": -0.5942024
   },
   "1762": {
      "postcode": "CA10",
      "latitude": 54.6118806,
      "longitude": -2.6584077
   },
   "1763": {
      "postcode": "CM14",
      "latitude": 51.6186789,
      "longitude": 0.2921453
   },
   "1764": {
      "postcode": "SN14",
      "latitude": 51.4755423,
      "longitude": -2.1991424
   },
   "1765": {
      "postcode": "SY16",
      "latitude": 52.5206495,
      "longitude": -3.3122813
   },
   "1766": {
      "postcode": "PE3",
      "latitude": 52.5843494,
      "longitude": -0.2752554
   },
   "1767": {
      "postcode": "BN8",
      "latitude": 50.9166625,
      "longitude": 0.0527321
   },
   "1768": {
      "postcode": "DN10",
      "latitude": 53.424485,
      "longitude": -0.9350013
   },
   "1769": {
      "postcode": "HP18",
      "latitude": 51.8202707,
      "longitude": -0.9688388
   },
   "1770": {
      "postcode": "N3",
      "latitude": 51.6002281,
      "longitude": -0.193929
   },
   "1771": {
      "postcode": "PH32",
      "latitude": 57.1445763,
      "longitude": -4.6835593
   },
   "1772": {
      "postcode": "W1F",
      "latitude": 51.5134975,
      "longitude": -0.1364725
   },
   "1773": {
      "postcode": "G73",
      "latitude": 55.8195192,
      "longitude": -4.2065974
   },
   "1774": {
      "postcode": "PO34",
      "latitude": 50.7159013,
      "longitude": -1.1134555
   },
   "1775": {
      "postcode": "FK4",
      "latitude": 55.9964986,
      "longitude": -3.9074569
   },
   "1776": {
      "postcode": "EC1R",
      "latitude": 51.5249491,
      "longitude": -0.1083725
   },
   "1777": {
      "postcode": "M5",
      "latitude": 53.479221,
      "longitude": -2.2837555
   },
   "1778": {
      "postcode": "G63",
      "latitude": 56.0430198,
      "longitude": -4.3655688
   },
   "1779": {
      "postcode": "PA7",
      "latitude": 55.9073289,
      "longitude": -4.5040855
   },
   "1780": {
      "postcode": "DL15",
      "latitude": 54.7109706,
      "longitude": -1.7302545
   },
   "1781": {
      "postcode": "LL38",
      "latitude": 52.6953036,
      "longitude": -4.0503008
   },
   "1782": {
      "postcode": "TR1",
      "latitude": 50.2626097,
      "longitude": -5.0541868
   },
   "1783": {
      "postcode": "UB2",
      "latitude": 51.4995871,
      "longitude": -0.3791468
   },
   "1784": {
      "postcode": "S66",
      "latitude": 53.4201548,
      "longitude": -1.2439946
   },
   "1785": {
      "postcode": "LL58",
      "latitude": 53.2820716,
      "longitude": -4.0992684
   },
   "1786": {
      "postcode": "HA8",
      "latitude": 51.6113532,
      "longitude": -0.2739101
   },
   "1787": {
      "postcode": "KY4",
      "latitude": 56.1140341,
      "longitude": -3.3630354
   },
   "1788": {
      "postcode": "HA2",
      "latitude": 51.5736982,
      "longitude": -0.3612317
   },
   "1789": {
      "postcode": "PE30",
      "latitude": 52.7597146,
      "longitude": 0.4165056
   },
   "1790": {
      "postcode": "TW11",
      "latitude": 51.4263148,
      "longitude": -0.3317674
   },
   "1791": {
      "postcode": "L27",
      "latitude": 53.3877426,
      "longitude": -2.838985
   },
   "1792": {
      "postcode": "LL54",
      "latitude": 53.0580643,
      "longitude": -4.2875015
   },
   "1793": {
      "postcode": "BH13",
      "latitude": 50.7088605,
      "longitude": -1.920442
   },
   "1794": {
      "postcode": "BT47",
      "latitude": 54.9739997,
      "longitude": -7.2126901
   },
   "1795": {
      "postcode": "WF13",
      "latitude": 53.6923035,
      "longitude": -1.6467249
   },
   "1796": {
      "postcode": "EC4V",
      "latitude": 51.5124476,
      "longitude": -0.099878
   },
   "1797": {
      "postcode": "DE55",
      "latitude": 53.1022937,
      "longitude": -1.3722605
   },
   "1798": {
      "postcode": "TS1",
      "latitude": 54.5719344,
      "longitude": -1.2392024
   },
   "1799": {
      "postcode": "EN10",
      "latitude": 51.7381929,
      "longitude": -0.023162
   },
   "1800": {
      "postcode": "NE39",
      "latitude": 54.9234877,
      "longitude": -1.7611063
   },
   "1801": {
      "postcode": "PA78",
      "latitude": 56.6264192,
      "longitude": -6.5458652
   },
   "1802": {
      "postcode": "LS11",
      "latitude": 53.776223,
      "longitude": -1.5573555
   },
   "1803": {
      "postcode": "N13",
      "latitude": 51.618112,
      "longitude": -0.1042702
   },
   "1804": {
      "postcode": "SA70",
      "latitude": 51.6725248,
      "longitude": -4.7416638
   },
   "1805": {
      "postcode": "RM17",
      "latitude": 51.479725,
      "longitude": 0.3283265
   },
   "1806": {
      "postcode": "PH19",
      "latitude": 56.9262864,
      "longitude": -4.2556793
   },
   "1807": {
      "postcode": "HD1",
      "latitude": 53.6468691,
      "longitude": -1.788934
   },
   "1808": {
      "postcode": "WA11",
      "latitude": 53.4780797,
      "longitude": -2.7197662
   },
   "1809": {
      "postcode": "TA5",
      "latitude": 51.1428039,
      "longitude": -3.094884
   },
   "1810": {
      "postcode": "DY7",
      "latitude": 52.466416,
      "longitude": -2.2308062
   },
   "1811": {
      "postcode": "BA9",
      "latitude": 51.0576908,
      "longitude": -2.4101382
   },
   "1812": {
      "postcode": "BS5",
      "latitude": 51.4620533,
      "longitude": -2.5517422
   },
   "1813": {
      "postcode": "NR3",
      "latitude": 52.6432723,
      "longitude": 1.2917283
   },
   "1814": {
      "postcode": "CF81",
      "latitude": 51.7017292,
      "longitude": -3.2446317
   },
   "1815": {
      "postcode": "SK9",
      "latitude": 53.3278962,
      "longitude": -2.2304439
   },
   "1816": {
      "postcode": "CW6",
      "latitude": 53.1625246,
      "longitude": -2.6672351
   },
   "1817": {
      "postcode": "LL78",
      "latitude": 53.3174138,
      "longitude": -4.2630432
   },
   "1818": {
      "postcode": "GU28",
      "latitude": 50.9910457,
      "longitude": -0.6327655
   },
   "1819": {
      "postcode": "YO25",
      "latitude": 54.0040772,
      "longitude": -0.4163603
   },
   "1820": {
      "postcode": "EC1M",
      "latitude": 51.5213505,
      "longitude": -0.1023129
   },
   "1821": {
      "postcode": "HU4",
      "latitude": 53.7362344,
      "longitude": -0.4040642
   },
   "1822": {
      "postcode": "AB13",
      "latitude": 57.1082022,
      "longitude": -2.2368915
   },
   "1823": {
      "postcode": "YO23",
      "latitude": 53.9234845,
      "longitude": -1.1234069
   },
   "1824": {
      "postcode": "AB21",
      "latitude": 57.2093798,
      "longitude": -2.2016004
   },
   "1825": {
      "postcode": "NE12",
      "latitude": 55.0243325,
      "longitude": -1.5705744
   },
   "1826": {
      "postcode": "BS30",
      "latitude": 51.4447118,
      "longitude": -2.4713845
   },
   "1827": {
      "postcode": "M27",
      "latitude": 53.5121147,
      "longitude": -2.3364528
   },
   "1828": {
      "postcode": "PL13",
      "latitude": 50.3587383,
      "longitude": -4.4757544
   },
   "1829": {
      "postcode": "PL21",
      "latitude": 50.3852736,
      "longitude": -3.9184514
   },
   "1830": {
      "postcode": "LS25",
      "latitude": 53.7858344,
      "longitude": -1.3250023
   },
   "1831": {
      "postcode": "IP5",
      "latitude": 52.0619388,
      "longitude": 1.245372
   },
   "1832": {
      "postcode": "S17",
      "latitude": 53.3213081,
      "longitude": -1.5289135
   },
   "1833": {
      "postcode": "LE9",
      "latitude": 52.5730928,
      "longitude": -1.2811778
   },
   "1834": {
      "postcode": "NN17",
      "latitude": 52.5010487,
      "longitude": -0.6842686
   },
   "1835": {
      "postcode": "CA25",
      "latitude": 54.5231026,
      "longitude": -3.5191491
   },
   "1836": {
      "postcode": "SE17",
      "latitude": 51.4882787,
      "longitude": -0.0933945
   },
   "1837": {
      "postcode": "SE15",
      "latitude": 51.4727365,
      "longitude": -0.0656967
   },
   "1838": {
      "postcode": "ST55",
      "latitude": 53.0141598,
      "longitude": -2.2380231
   },
   "1839": {
      "postcode": "HU2",
      "latitude": 53.7507551,
      "longitude": -0.3406848
   },
   "1840": {
      "postcode": "PE19",
      "latitude": 52.2359693,
      "longitude": -0.2636521
   },
   "1841": {
      "postcode": "BA3",
      "latitude": 51.2717539,
      "longitude": -2.4785029
   },
   "1842": {
      "postcode": "NE31",
      "latitude": 54.9708203,
      "longitude": -1.5132819
   },
   "1843": {
      "postcode": "LA7",
      "latitude": 54.2257341,
      "longitude": -2.7730264
   },
   "1844": {
      "postcode": "WS4",
      "latitude": 52.6068687,
      "longitude": -1.9587114
   },
   "1845": {
      "postcode": "NN10",
      "latitude": 52.2928622,
      "longitude": -0.5977197
   },
   "1846": {
      "postcode": "B93",
      "latitude": 52.3804941,
      "longitude": -1.7438511
   },
   "1847": {
      "postcode": "BN50",
      "latitude": 50.8263299,
      "longitude": -0.1408006
   },
   "1848": {
      "postcode": "G14",
      "latitude": 55.8804359,
      "longitude": -4.350756
   },
   "1849": {
      "postcode": "RG2",
      "latitude": 51.4201494,
      "longitude": -0.9517094
   },
   "1850": {
      "postcode": "OX15",
      "latitude": 52.0303387,
      "longitude": -1.4113905
   },
   "1851": {
      "postcode": "DE12",
      "latitude": 52.7233343,
      "longitude": -1.5535436
   },
   "1852": {
      "postcode": "SW8",
      "latitude": 51.4765695,
      "longitude": -0.1320148
   },
   "1853": {
      "postcode": "CA2",
      "latitude": 54.8838592,
      "longitude": -2.9512475
   },
   "1854": {
      "postcode": "MK19",
      "latitude": 52.0751348,
      "longitude": -0.8552011
   },
   "1855": {
      "postcode": "GU23",
      "latitude": 51.2940938,
      "longitude": -0.5060248
   },
   "1856": {
      "postcode": "MK17",
      "latitude": 51.997579,
      "longitude": -0.6993948
   },
   "1857": {
      "postcode": "PH44",
      "latitude": 57.0567966,
      "longitude": -6.503266
   },
   "1858": {
      "postcode": "PH22",
      "latitude": 57.1941031,
      "longitude": -3.8202505
   },
   "1859": {
      "postcode": "TQ8",
      "latitude": 50.2366074,
      "longitude": -3.7718704
   },
   "1860": {
      "postcode": "HP13",
      "latitude": 51.6344818,
      "longitude": -0.7404825
   },
   "1861": {
      "postcode": "N1P",
      "latitude": 51.5389749,
      "longitude": -0.1030615
   },
   "1862": {
      "postcode": "PE20",
      "latitude": 52.9312795,
      "longitude": -0.1038179
   },
   "1863": {
      "postcode": "EH52",
      "latitude": 55.9383479,
      "longitude": -3.485057
   },
   "1864": {
      "postcode": "PL26",
      "latitude": 50.3449922,
      "longitude": -4.827501
   },
   "1865": {
      "postcode": "LL72",
      "latitude": 53.352291,
      "longitude": -4.2400479
   },
   "1866": {
      "postcode": "PE8",
      "latitude": 52.5217429,
      "longitude": -0.4539945
   },
   "1867": {
      "postcode": "EH51",
      "latitude": 56.0110331,
      "longitude": -3.6055066
   },
   "1868": {
      "postcode": "CM3",
      "latitude": 51.7211161,
      "longitude": 0.5842087
   },
   "1869": {
      "postcode": "EX7",
      "latitude": 50.5843718,
      "longitude": -3.4706752
   },
   "1870": {
      "postcode": "EH23",
      "latitude": 55.8394658,
      "longitude": -3.0509226
   },
   "1871": {
      "postcode": "WV7",
      "latitude": 52.6354827,
      "longitude": -2.2794354
   },
   "1872": {
      "postcode": "G76",
      "latitude": 55.7770362,
      "longitude": -4.2730765
   },
   "1873": {
      "postcode": "CH29",
      "latitude": 53.3901667,
      "longitude": -3.1794125
   },
   "1874": {
      "postcode": "SE8",
      "latitude": 51.4819486,
      "longitude": -0.0294902
   },
   "1875": {
      "postcode": "DL10",
      "latitude": 54.4138943,
      "longitude": -1.6913727
   },
   "1876": {
      "postcode": "SK11",
      "latitude": 53.245315,
      "longitude": -2.1463212
   },
   "1877": {
      "postcode": "WS9",
      "latitude": 52.6099899,
      "longitude": -1.9184422
   },
   "1878": {
      "postcode": "G58",
      "latitude": 55.8423713,
      "longitude": -4.2906685
   },
   "1879": {
      "postcode": "KA8",
      "latitude": 55.4717538,
      "longitude": -4.612459
   },
   "1880": {
      "postcode": "PA28",
      "latitude": 55.4376036,
      "longitude": -5.6038598
   },
   "1881": {
      "postcode": "DE99",
      "latitude": 52.9150384,
      "longitude": -1.4661393
   },
   "1882": {
      "postcode": "IV36",
      "latitude": 57.6097384,
      "longitude": -3.6074174
   },
   "1883": {
      "postcode": "ML3",
      "latitude": 55.7699883,
      "longitude": -4.0550162
   },
   "1884": {
      "postcode": "RM7",
      "latitude": 51.5748451,
      "longitude": 0.1687782
   },
   "1885": {
      "postcode": "DA6",
      "latitude": 51.4551736,
      "longitude": 0.1388193
   },
   "1886": {
      "postcode": "LE18",
      "latitude": 52.5832335,
      "longitude": -1.111972
   },
   "1887": {
      "postcode": "SW6",
      "latitude": 51.4766351,
      "longitude": -0.2012224
   },
   "1888": {
      "postcode": "SS11",
      "latitude": 51.6172491,
      "longitude": 0.537807
   },
   "1889": {
      "postcode": "ST10",
      "latitude": 52.9885754,
      "longitude": -1.9646762
   },
   "1890": {
      "postcode": "PA17",
      "latitude": 55.8633832,
      "longitude": -4.8851597
   },
   "1891": {
      "postcode": "CF62",
      "latitude": 51.4039362,
      "longitude": -3.310979
   },
   "1892": {
      "postcode": "ME12",
      "latitude": 51.4223196,
      "longitude": 0.8043021
   },
   "1893": {
      "postcode": "PH40",
      "latitude": 56.9633163,
      "longitude": -5.8017491
   },
   "1894": {
      "postcode": "IP30",
      "latitude": 52.209224,
      "longitude": 0.8464525
   },
   "1895": {
      "postcode": "SP4",
      "latitude": 51.1660243,
      "longitude": -1.7660031
   },
   "1896": {
      "postcode": "LL48",
      "latitude": 52.9360472,
      "longitude": -4.0696243
   },
   "1897": {
      "postcode": "ST5",
      "latitude": 53.0153757,
      "longitude": -2.2395729
   },
   "1898": {
      "postcode": "CA3",
      "latitude": 54.9093172,
      "longitude": -2.9402815
   },
   "1899": {
      "postcode": "HU3",
      "latitude": 53.7423203,
      "longitude": -0.3676664
   },
   "1900": {
      "postcode": "PE34",
      "latitude": 52.7249832,
      "longitude": 0.3373637
   },
   "1901": {
      "postcode": "EC3N",
      "latitude": 51.5119304,
      "longitude": -0.0770379
   },
   "1902": {
      "postcode": "B72",
      "latitude": 52.5501949,
      "longitude": -1.8219989
   },
   "1903": {
      "postcode": "B27",
      "latitude": 52.4445575,
      "longitude": -1.8228123
   },
   "1904": {
      "postcode": "OX29",
      "latitude": 51.7940797,
      "longitude": -1.435656
   },
   "1905": {
      "postcode": "SS16",
      "latitude": 51.5625971,
      "longitude": 0.4520758
   },
   "1906": {
      "postcode": "TW16",
      "latitude": 51.4157677,
      "longitude": -0.4169227
   },
   "1907": {
      "postcode": "OL1",
      "latitude": 53.5497377,
      "longitude": -2.1069922
   },
   "1908": {
      "postcode": "HX7",
      "latitude": 53.7392443,
      "longitude": -2.0085802
   },
   "1909": {
      "postcode": "BH18",
      "latitude": 50.7595167,
      "longitude": -1.9984276
   },
   "1910": {
      "postcode": "L7",
      "latitude": 53.4057417,
      "longitude": -2.9499885
   },
   "1911": {
      "postcode": "L67",
      "latitude": 53.4499811,
      "longitude": -2.9424012
   },
   "1912": {
      "postcode": "CF24",
      "latitude": 51.4880332,
      "longitude": -3.1619481
   },
   "1913": {
      "postcode": "WC1N",
      "latitude": 51.5229255,
      "longitude": -0.1197316
   },
   "1914": {
      "postcode": "PL19",
      "latitude": 50.5565609,
      "longitude": -4.1547903
   },
   "1915": {
      "postcode": "NE2",
      "latitude": 54.9870836,
      "longitude": -1.6061088
   },
   "1916": {
      "postcode": "CB3",
      "latitude": 52.212482,
      "longitude": 0.0981705
   },
   "1917": {
      "postcode": "TD13",
      "latitude": 55.929849,
      "longitude": -2.3714898
   },
   "1918": {
      "postcode": "CF71",
      "latitude": 51.4609003,
      "longitude": -3.4589993
   },
   "1919": {
      "postcode": "LL56",
      "latitude": 53.1843564,
      "longitude": -4.2059205
   },
   "1920": {
      "postcode": "NG11",
      "latitude": 52.8991198,
      "longitude": -1.1741527
   },
   "1921": {
      "postcode": "SS8",
      "latitude": 51.5221057,
      "longitude": 0.5895804
   },
   "1922": {
      "postcode": "CT4",
      "latitude": 51.2238425,
      "longitude": 1.0647403
   },
   "1923": {
      "postcode": "DL11",
      "latitude": 54.4394631,
      "longitude": -1.876604
   },
   "1924": {
      "postcode": "TQ14",
      "latitude": 50.5507921,
      "longitude": -3.5078648
   },
   "1925": {
      "postcode": "EH22",
      "latitude": 55.8850462,
      "longitude": -3.0607492
   },
   "1926": {
      "postcode": "NN1",
      "latitude": 52.2416489,
      "longitude": -0.8883002
   },
   "1927": {
      "postcode": "NE41",
      "latitude": 54.9760829,
      "longitude": -1.8201262
   },
   "1928": {
      "postcode": "RG30",
      "latitude": 51.4511542,
      "longitude": -1.0147746
   },
   "1929": {
      "postcode": "NR32",
      "latitude": 52.489723,
      "longitude": 1.7315777
   },
   "1930": {
      "postcode": "B46",
      "latitude": 52.5088835,
      "longitude": -1.6949788
   },
   "1931": {
      "postcode": "PE23",
      "latitude": 53.1727258,
      "longitude": 0.0887887
   },
   "1932": {
      "postcode": "IV63",
      "latitude": 57.3047579,
      "longitude": -4.5326314
   },
   "1933": {
      "postcode": "SS14",
      "latitude": 51.5760335,
      "longitude": 0.4746395
   },
   "1934": {
      "postcode": "NP16",
      "latitude": 51.6504671,
      "longitude": -2.6898185
   },
   "1935": {
      "postcode": "SR3",
      "latitude": 54.8766731,
      "longitude": -1.4168469
   },
   "1936": {
      "postcode": "BN42",
      "latitude": 50.8376298,
      "longitude": -0.2347507
   },
   "1937": {
      "postcode": "LL21",
      "latitude": 52.9900548,
      "longitude": -3.4102899
   },
   "1938": {
      "postcode": "BS10",
      "latitude": 51.5067451,
      "longitude": -2.610823
   },
   "1939": {
      "postcode": "BT56",
      "latitude": 55.197616,
      "longitude": -6.6503827
   },
   "1940": {
      "postcode": "LL59",
      "latitude": 53.2357839,
      "longitude": -4.1631557
   },
   "1941": {
      "postcode": "G83",
      "latitude": 56.0121497,
      "longitude": -4.5869607
   },
   "1942": {
      "postcode": "CA13",
      "latitude": 54.6598623,
      "longitude": -3.3683706
   },
   "1943": {
      "postcode": "PA6",
      "latitude": 55.8658238,
      "longitude": -4.5371164
   },
   "1944": {
      "postcode": "TF1",
      "latitude": 52.7031424,
      "longitude": -2.5029461
   },
   "1945": {
      "postcode": "DL6",
      "latitude": 54.371022,
      "longitude": -1.3904975
   },
   "1946": {
      "postcode": "BD12",
      "latitude": 53.7456818,
      "longitude": -1.7626592
   },
   "1947": {
      "postcode": "KY11",
      "latitude": 56.0485491,
      "longitude": -3.4139256
   },
   "1948": {
      "postcode": "PO15",
      "latitude": 50.8676994,
      "longitude": -1.2281695
   },
   "1949": {
      "postcode": "TR24",
      "latitude": 49.9554022,
      "longitude": -6.3353021
   },
   "1950": {
      "postcode": "NR15",
      "latitude": 52.5032686,
      "longitude": 1.2663003
   },
   "1951": {
      "postcode": "CO16",
      "latitude": 51.8219619,
      "longitude": 1.1229273
   },
   "1952": {
      "postcode": "SY4",
      "latitude": 52.7980636,
      "longitude": -2.753822
   },
   "1953": {
      "postcode": "BH31",
      "latitude": 50.8760396,
      "longitude": -1.872606
   },
   "1954": {
      "postcode": "WC2A",
      "latitude": 51.5162229,
      "longitude": -0.1142197
   },
   "1955": {
      "postcode": "SA65",
      "latitude": 51.9881184,
      "longitude": -4.9697965
   },
   "1956": {
      "postcode": "DE1",
      "latitude": 52.9221535,
      "longitude": -1.4774894
   },
   "1957": {
      "postcode": "EC2R",
      "latitude": 51.5160606,
      "longitude": -0.0909709
   },
   "1958": {
      "postcode": "MK11",
      "latitude": 52.0510771,
      "longitude": -0.8404949
   },
   "1959": {
      "postcode": "HX5",
      "latitude": 53.6845992,
      "longitude": -1.8352938
   },
   "1960": {
      "postcode": "L2",
      "latitude": 53.4068628,
      "longitude": -2.9899412
   },
   "1961": {
      "postcode": "EH4",
      "latitude": 55.9624129,
      "longitude": -3.2608608
   },
   "1962": {
      "postcode": "EC1A",
      "latitude": 51.5203315,
      "longitude": -0.1039346
   },
   "1963": {
      "postcode": "PO7",
      "latitude": 50.8829409,
      "longitude": -1.0406889
   },
   "1964": {
      "postcode": "OL6",
      "latitude": 53.4943593,
      "longitude": -2.0861171
   },
   "1965": {
      "postcode": "IV27",
      "latitude": 58.2764191,
      "longitude": -4.7971051
   },
   "1966": {
      "postcode": "OX26",
      "latitude": 51.901173,
      "longitude": -1.1544766
   },
   "1967": {
      "postcode": "SN38",
      "latitude": 51.5627924,
      "longitude": -1.806599
   },
   "1968": {
      "postcode": "CW10",
      "latitude": 53.1887768,
      "longitude": -2.4436061
   },
   "1969": {
      "postcode": "NN29",
      "latitude": 52.2580421,
      "longitude": -0.6648146
   },
   "1970": {
      "postcode": "G41",
      "latitude": 55.8376134,
      "longitude": -4.2844564
   },
   "1971": {
      "postcode": "LL36",
      "latitude": 52.6042624,
      "longitude": -4.0644733
   },
   "1972": {
      "postcode": "TS13",
      "latitude": 54.5496921,
      "longitude": -0.8541928
   },
   "1973": {
      "postcode": "HS2",
      "latitude": 58.2483484,
      "longitude": -6.4631996
   },
   "1974": {
      "postcode": "NG80",
      "latitude": 52.9300984,
      "longitude": -1.1917297
   },
   "1975": {
      "postcode": "PO37",
      "latitude": 50.6314255,
      "longitude": -1.1796299
   },
   "1976": {
      "postcode": "KT16",
      "latitude": 51.3825678,
      "longitude": -0.516428
   },
   "1977": {
      "postcode": "AL4",
      "latitude": 51.7739838,
      "longitude": -0.295024
   },
   "1978": {
      "postcode": "BB5",
      "latitude": 53.754299,
      "longitude": -2.37346
   },
   "1979": {
      "postcode": "PO2",
      "latitude": 50.8178415,
      "longitude": -1.0774067
   },
   "1980": {
      "postcode": "PR5",
      "latitude": 53.731555,
      "longitude": -2.6577319
   },
   "1981": {
      "postcode": "EN6",
      "latitude": 51.699489,
      "longitude": -0.176714
   },
   "1982": {
      "postcode": "BH10",
      "latitude": 50.7595614,
      "longitude": -1.8929555
   },
   "1983": {
      "postcode": "HU20",
      "latitude": 53.787867,
      "longitude": -0.5117995
   },
   "1984": {
      "postcode": "PE16",
      "latitude": 52.4548843,
      "longitude": 0.0493714
   },
   "1985": {
      "postcode": "CF82",
      "latitude": 51.6509975,
      "longitude": -3.2379255
   },
   "1986": {
      "postcode": "PO32",
      "latitude": 50.7511908,
      "longitude": -1.2810514
   },
   "1987": {
      "postcode": "CA16",
      "latitude": 54.5740293,
      "longitude": -2.4838426
   },
   "1988": {
      "postcode": "LE2",
      "latitude": 52.6073868,
      "longitude": -1.1169519
   },
   "1989": {
      "postcode": "DN37",
      "latitude": 53.5399911,
      "longitude": -0.1383433
   },
   "1990": {
      "postcode": "SY10",
      "latitude": 52.8394661,
      "longitude": -3.1235551
   },
   "1991": {
      "postcode": "CH2",
      "latitude": 53.2178821,
      "longitude": -2.8689752
   },
   "1992": {
      "postcode": "NR27",
      "latitude": 52.9242431,
      "longitude": 1.2998419
   },
   "1993": {
      "postcode": "WD5",
      "latitude": 51.7026256,
      "longitude": -0.4163911
   },
   "1994": {
      "postcode": "OX12",
      "latitude": 51.5964061,
      "longitude": -1.425191
   },
   "1995": {
      "postcode": "KT2",
      "latitude": 51.4189252,
      "longitude": -0.2906684
   },
   "1996": {
      "postcode": "B1",
      "latitude": 52.4799811,
      "longitude": -1.9091472
   },
   "1997": {
      "postcode": "DY4",
      "latitude": 52.5328792,
      "longitude": -2.0552638
   },
   "1998": {
      "postcode": "CT10",
      "latitude": 51.3631369,
      "longitude": 1.4294367
   },
   "1999": {
      "postcode": "PA36",
      "latitude": 56.5241284,
      "longitude": -4.7696606
   },
   "2000": {
      "postcode": "NN13",
      "latitude": 52.0340435,
      "longitude": -1.1480035
   },
   "2001": {
      "postcode": "FY5",
      "latitude": 53.8752307,
      "longitude": -3.0218705
   },
   "2002": {
      "postcode": "NN8",
      "latitude": 52.3032613,
      "longitude": -0.6996321
   },
   "2003": {
      "postcode": "ML5",
      "latitude": 55.8597936,
      "longitude": -4.0317112
   },
   "2004": {
      "postcode": "HR3",
      "latitude": 52.0939594,
      "longitude": -3.0850031
   },
   "2005": {
      "postcode": "TD11",
      "latitude": 55.7877855,
      "longitude": -2.3139948
   },
   "2006": {
      "postcode": "BR5",
      "latitude": 51.3917166,
      "longitude": 0.1033934
   },
   "2007": {
      "postcode": "S25",
      "latitude": 53.3658458,
      "longitude": -1.2168611
   },
   "2008": {
      "postcode": "IP16",
      "latitude": 52.2041101,
      "longitude": 1.5840513
   },
   "2009": {
      "postcode": "WS7",
      "latitude": 52.6797404,
      "longitude": -1.9216495
   },
   "2010": {
      "postcode": "B64",
      "latitude": 52.4725264,
      "longitude": -2.0694635
   },
   "2011": {
      "postcode": "EC1P",
      "latitude": 51.524516,
      "longitude": -0.1120727
   },
   "2012": {
      "postcode": "DD2",
      "latitude": 56.4703225,
      "longitude": -3.0317411
   },
   "2013": {
      "postcode": "BS26",
      "latitude": 51.2788645,
      "longitude": -2.8569371
   },
   "2014": {
      "postcode": "NE21",
      "latitude": 54.9575809,
      "longitude": -1.7214224
   },
   "2015": {
      "postcode": "DA8",
      "latitude": 51.4757724,
      "longitude": 0.1758771
   },
   "2016": {
      "postcode": "PA64",
      "latitude": 56.437876,
      "longitude": -5.6860385
   },
   "2017": {
      "postcode": "WA4",
      "latitude": 53.3653734,
      "longitude": -2.5758118
   },
   "2018": {
      "postcode": "CW8",
      "latitude": 53.2534481,
      "longitude": -2.5652379
   },
   "2019": {
      "postcode": "S49",
      "latitude": 53.2350543,
      "longitude": -1.434735
   },
   "2020": {
      "postcode": "WS15",
      "latitude": 52.7585909,
      "longitude": -1.9173233
   },
   "2021": {
      "postcode": "IV55",
      "latitude": 57.4561945,
      "longitude": -6.6097781
   },
   "2022": {
      "postcode": "BH21",
      "latitude": 50.8125355,
      "longitude": -1.974537
   },
   "2023": {
      "postcode": "KA27",
      "latitude": 55.5386053,
      "longitude": -5.174569
   },
   "2024": {
      "postcode": "CH45",
      "latitude": 53.4289247,
      "longitude": -3.0517282
   },
   "2025": {
      "postcode": "MK8",
      "latitude": 52.0330526,
      "longitude": -0.8047638
   },
   "2026": {
      "postcode": "WR12",
      "latitude": 52.0414013,
      "longitude": -1.8704376
   },
   "2027": {
      "postcode": "DG4",
      "latitude": 55.3754906,
      "longitude": -3.9527786
   },
   "2028": {
      "postcode": "NE1",
      "latitude": 54.972442,
      "longitude": -1.6115224
   },
   "2029": {
      "postcode": "BS4",
      "latitude": 51.435356,
      "longitude": -2.5636106
   },
   "2030": {
      "postcode": "RM18",
      "latitude": 51.4674524,
      "longitude": 0.37594
   },
   "2031": {
      "postcode": "NW9",
      "latitude": 51.5881194,
      "longitude": -0.2552637
   },
   "2032": {
      "postcode": "WR11",
      "latitude": 52.0958405,
      "longitude": -1.9290168
   },
   "2033": {
      "postcode": "RH10",
      "latitude": 51.1183435,
      "longitude": -0.1547527
   },
   "2034": {
      "postcode": "E17",
      "latitude": 51.5869039,
      "longitude": -0.0207805
   },
   "2035": {
      "postcode": "LL68",
      "latitude": 53.3977575,
      "longitude": -4.3794888
   },
   "2036": {
      "postcode": "PO20",
      "latitude": 50.7837114,
      "longitude": -0.7846263
   },
   "2037": {
      "postcode": "SN10",
      "latitude": 51.3370397,
      "longitude": -1.9869176
   },
   "2038": {
      "postcode": "LE3",
      "latitude": 52.6315445,
      "longitude": -1.1772298
   },
   "2039": {
      "postcode": "YO17",
      "latitude": 54.1367836,
      "longitude": -0.7568135
   },
   "2040": {
      "postcode": "L25",
      "latitude": 53.3788522,
      "longitude": -2.8636656
   },
   "2041": {
      "postcode": "S42",
      "latitude": 53.1996406,
      "longitude": -1.4217945
   },
   "2042": {
      "postcode": "EH31",
      "latitude": 56.0365209,
      "longitude": -2.8267129
   },
   "2043": {
      "postcode": "L69",
      "latitude": 53.3874418,
      "longitude": -2.9746703
   },
   "2044": {
      "postcode": "GL12",
      "latitude": 51.6242009,
      "longitude": -2.3889711
   },
   "2045": {
      "postcode": "AB32",
      "latitude": 57.1550293,
      "longitude": -2.317922
   },
   "2046": {
      "postcode": "TA19",
      "latitude": 50.9351637,
      "longitude": -2.9154632
   },
   "2047": {
      "postcode": "WA9",
      "latitude": 53.4361271,
      "longitude": -2.7192438
   },
   "2048": {
      "postcode": "SP3",
      "latitude": 51.1021334,
      "longitude": -2.0158963
   },
   "2049": {
      "postcode": "IP3",
      "latitude": 52.04135,
      "longitude": 1.18801
   },
   "2050": {
      "postcode": "N1",
      "latitude": 51.5377218,
      "longitude": -0.0970473
   },
   "2051": {
      "postcode": "DY5",
      "latitude": 52.4804556,
      "longitude": -2.1239401
   },
   "2052": {
      "postcode": "PO36",
      "latitude": 50.6585816,
      "longitude": -1.163679
   },
   "2053": {
      "postcode": "CT17",
      "latitude": 51.1291169,
      "longitude": 1.2937687
   },
   "2054": {
      "postcode": "LE7",
      "latitude": 52.6800581,
      "longitude": -1.0709886
   },
   "2055": {
      "postcode": "B25",
      "latitude": 52.4649901,
      "longitude": -1.8219999
   },
   "2056": {
      "postcode": "DY13",
      "latitude": 52.3367283,
      "longitude": -2.2813551
   },
   "2057": {
      "postcode": "KT3",
      "latitude": 51.3995791,
      "longitude": -0.2574604
   },
   "2058": {
      "postcode": "LS22",
      "latitude": 53.9317926,
      "longitude": -1.3956826
   },
   "2059": {
      "postcode": "BA15",
      "latitude": 51.3482711,
      "longitude": -2.2580986
   },
   "2060": {
      "postcode": "EH2",
      "latitude": 55.9522871,
      "longitude": -3.2022387
   },
   "2061": {
      "postcode": "PO9",
      "latitude": 50.8634319,
      "longitude": -0.9839667
   },
   "2062": {
      "postcode": "AB45",
      "latitude": 57.6517031,
      "longitude": -2.5676286
   },
   "2063": {
      "postcode": "EX11",
      "latitude": 50.7468054,
      "longitude": -3.2895514
   },
   "2064": {
      "postcode": "RG24",
      "latitude": 51.2807785,
      "longitude": -1.0794987
   },
   "2065": {
      "postcode": "B5",
      "latitude": 52.4694163,
      "longitude": -1.8975868
   },
   "2066": {
      "postcode": "IV9",
      "latitude": 57.5690237,
      "longitude": -4.1786419
   },
   "2067": {
      "postcode": "EC4M",
      "latitude": 51.5142792,
      "longitude": -0.0993846
   },
   "2068": {
      "postcode": "BN2",
      "latitude": 50.8250741,
      "longitude": -0.1010175
   },
   "2069": {
      "postcode": "TF11",
      "latitude": 52.6651286,
      "longitude": -2.3582963
   },
   "2070": {
      "postcode": "TN30",
      "latitude": 51.0622974,
      "longitude": 0.6967544
   },
   "2071": {
      "postcode": "DN7",
      "latitude": 53.5833786,
      "longitude": -1.01316
   },
   "2072": {
      "postcode": "ST8",
      "latitude": 53.1155274,
      "longitude": -2.167896
   },
   "2073": {
      "postcode": "LL70",
      "latitude": 53.3638741,
      "longitude": -4.2877619
   },
   "2074": {
      "postcode": "PE26",
      "latitude": 52.4532813,
      "longitude": -0.116638
   },
   "2075": {
      "postcode": "LL14",
      "latitude": 52.9909507,
      "longitude": -3.0533052
   },
   "2076": {
      "postcode": "MK42",
      "latitude": 52.1173913,
      "longitude": -0.4724081
   },
   "2077": {
      "postcode": "BL6",
      "latitude": 53.5917532,
      "longitude": -2.5408608
   },
   "2078": {
      "postcode": "SK22",
      "latitude": 53.3725343,
      "longitude": -1.9846946
   },
   "2079": {
      "postcode": "BT79",
      "latitude": 54.623159,
      "longitude": -7.200907
   },
   "2080": {
      "postcode": "EC1V",
      "latitude": 51.5268168,
      "longitude": -0.0978016
   },
   "2081": {
      "postcode": "PA44",
      "latitude": 55.7994182,
      "longitude": -6.2935908
   },
   "2082": {
      "postcode": "BH16",
      "latitude": 50.740203,
      "longitude": -2.0474413
   },
   "2083": {
      "postcode": "LL75",
      "latitude": 53.2849805,
      "longitude": -4.2166075
   },
   "2084": {
      "postcode": "LE65",
      "latitude": 52.7486524,
      "longitude": -1.4694618
   },
   "2085": {
      "postcode": "SY23",
      "latitude": 52.3800111,
      "longitude": -4.051249
   },
   "2086": {
      "postcode": "HG3",
      "latitude": 54.0300146,
      "longitude": -1.6178422
   },
   "2087": {
      "postcode": "RH12",
      "latitude": 51.0771886,
      "longitude": -0.332156
   },
   "2088": {
      "postcode": "DL2",
      "latitude": 54.5282376,
      "longitude": -1.5973398
   },
   "2089": {
      "postcode": "PL29",
      "latitude": 50.5861971,
      "longitude": -4.8301107
   },
   "2090": {
      "postcode": "SL4",
      "latitude": 51.4752709,
      "longitude": -0.6274221
   },
   "2091": {
      "postcode": "M60",
      "latitude": 53.4844452,
      "longitude": -2.2348172
   },
   "2092": {
      "postcode": "WV14",
      "latitude": 52.5572984,
      "longitude": -2.0789308
   },
   "2093": {
      "postcode": "TD15",
      "latitude": 55.7473641,
      "longitude": -2.0146884
   },
   "2094": {
      "postcode": "TA14",
      "latitude": 50.9468145,
      "longitude": -2.7515634
   },
   "2095": {
      "postcode": "BT65",
      "latitude": 54.4445858,
      "longitude": -6.3654149
   },
   "2096": {
      "postcode": "PR9",
      "latitude": 53.659666,
      "longitude": -2.9686373
   },
   "2097": {
      "postcode": "WN5",
      "latitude": 53.5319036,
      "longitude": -2.6873957
   },
   "2098": {
      "postcode": "NE35",
      "latitude": 54.9510139,
      "longitude": -1.460656
   },
   "2099": {
      "postcode": "DG3",
      "latitude": 55.237439,
      "longitude": -3.799286
   },
   "2100": {
      "postcode": "M33",
      "latitude": 53.4209662,
      "longitude": -2.3262749
   },
   "2101": {
      "postcode": "GU52",
      "latitude": 51.2636841,
      "longitude": -0.8386174
   },
   "2102": {
      "postcode": "EX21",
      "latitude": 50.8057129,
      "longitude": -4.2086933
   },
   "2103": {
      "postcode": "DN36",
      "latitude": 53.5114674,
      "longitude": -0.039586
   },
   "2104": {
      "postcode": "HA7",
      "latitude": 51.6113081,
      "longitude": -0.3106331
   },
   "2105": {
      "postcode": "CH65",
      "latitude": 53.2771085,
      "longitude": -2.9018402
   },
   "2106": {
      "postcode": "EC2A",
      "latitude": 51.5237066,
      "longitude": -0.0855916
   },
   "2107": {
      "postcode": "TA4",
      "latitude": 51.074692,
      "longitude": -3.2714873
   },
   "2108": {
      "postcode": "L23",
      "latitude": 53.4909653,
      "longitude": -3.023793
   },
   "2109": {
      "postcode": "PH13",
      "latitude": 56.5371048,
      "longitude": -3.2746989
   },
   "2110": {
      "postcode": "S9",
      "latitude": 53.3981645,
      "longitude": -1.4178388
   },
   "2111": {
      "postcode": "S4",
      "latitude": 53.4009143,
      "longitude": -1.4496573
   },
   "2112": {
      "postcode": "PE12",
      "latitude": 52.7851801,
      "longitude": 0.0279957
   },
   "2113": {
      "postcode": "KT23",
      "latitude": 51.2801634,
      "longitude": -0.3756767
   },
   "2114": {
      "postcode": "EX36",
      "latitude": 51.0166843,
      "longitude": -3.796052
   },
   "2115": {
      "postcode": "DN4",
      "latitude": 53.504999,
      "longitude": -1.1211527
   },
   "2116": {
      "postcode": "PL35",
      "latitude": 50.6847541,
      "longitude": -4.6853135
   },
   "2117": {
      "postcode": "PE28",
      "latitude": 52.3588328,
      "longitude": -0.1906381
   },
   "2118": {
      "postcode": "KT24",
      "latitude": 51.2701574,
      "longitude": -0.4298101
   },
   "2119": {
      "postcode": "CF43",
      "latitude": 51.6576285,
      "longitude": -3.4504756
   },
   "2120": {
      "postcode": "SM6",
      "latitude": 51.3614689,
      "longitude": -0.1445371
   },
   "2121": {
      "postcode": "SE7",
      "latitude": 51.4842259,
      "longitude": 0.0340854
   },
   "2122": {
      "postcode": "CH8",
      "latitude": 53.2830042,
      "longitude": -3.2465239
   },
   "2123": {
      "postcode": "PL6",
      "latitude": 50.418712,
      "longitude": -4.1156868
   },
   "2124": {
      "postcode": "BT29",
      "latitude": 54.6209431,
      "longitude": -6.196934
   },
   "2125": {
      "postcode": "NR12",
      "latitude": 52.7597763,
      "longitude": 1.4720163
   },
   "2126": {
      "postcode": "CV37",
      "latitude": 52.1827385,
      "longitude": -1.715127
   },
   "2127": {
      "postcode": "SW7",
      "latitude": 51.4962781,
      "longitude": -0.1770136
   },
   "2128": {
      "postcode": "HP11",
      "latitude": 51.6239518,
      "longitude": -0.7453006
   },
   "2129": {
      "postcode": "LS9",
      "latitude": 53.7995059,
      "longitude": -1.510182
   },
   "2130": {
      "postcode": "TN25",
      "latitude": 51.1412359,
      "longitude": 0.9384339
   },
   "2131": {
      "postcode": "NG31",
      "latitude": 52.9144482,
      "longitude": -0.6420228
   },
   "2132": {
      "postcode": "TQ7",
      "latitude": 50.2826457,
      "longitude": -3.7844126
   },
   "2133": {
      "postcode": "DY2",
      "latitude": 52.4963087,
      "longitude": -2.0814401
   },
   "2134": {
      "postcode": "DT6",
      "latitude": 50.7391695,
      "longitude": -2.7754498
   },
   "2135": {
      "postcode": "SA69",
      "latitude": 51.710974,
      "longitude": -4.706798
   },
   "2136": {
      "postcode": "IP24",
      "latitude": 52.419832,
      "longitude": 0.757916
   },
   "2137": {
      "postcode": "DY3",
      "latitude": 52.5308396,
      "longitude": -2.1312352
   },
   "2138": {
      "postcode": "GU31",
      "latitude": 50.9969882,
      "longitude": -0.90349
   },
   "2139": {
      "postcode": "PO33",
      "latitude": 50.7216598,
      "longitude": -1.1700685
   },
   "2140": {
      "postcode": "M28",
      "latitude": 53.5147094,
      "longitude": -2.3993412
   },
   "2141": {
      "postcode": "E16",
      "latitude": 51.5105927,
      "longitude": 0.0289721
   },
   "2142": {
      "postcode": "DD3",
      "latitude": 56.4831651,
      "longitude": -2.9898945
   },
   "2143": {
      "postcode": "CH46",
      "latitude": 53.4039828,
      "longitude": -3.1108625
   },
   "2144": {
      "postcode": "PR26",
      "latitude": 53.6876888,
      "longitude": -2.7410845
   },
   "2145": {
      "postcode": "TD1",
      "latitude": 55.6231746,
      "longitude": -2.810917
   },
   "2146": {
      "postcode": "CF45",
      "latitude": 51.6696017,
      "longitude": -3.3622637
   },
   "2147": {
      "postcode": "NG20",
      "latitude": 53.2100156,
      "longitude": -1.1858804
   },
   "2148": {
      "postcode": "SN13",
      "latitude": 51.4245832,
      "longitude": -2.2124861
   },
   "2149": {
      "postcode": "SW16",
      "latitude": 51.4212906,
      "longitude": -0.1292383
   },
   "2150": {
      "postcode": "G11",
      "latitude": 55.8733357,
      "longitude": -4.3129733
   },
   "2151": {
      "postcode": "L39",
      "latitude": 53.5617461,
      "longitude": -2.8964099
   },
   "2152": {
      "postcode": "MK9",
      "latitude": 52.0404,
      "longitude": -0.754928
   },
   "2153": {
      "postcode": "MK15",
      "latitude": 52.0568594,
      "longitude": -0.729772
   },
   "2154": {
      "postcode": "TN1",
      "latitude": 51.1346687,
      "longitude": 0.2665338
   },
   "2155": {
      "postcode": "BR8",
      "latitude": 51.3985498,
      "longitude": 0.1743791
   },
   "2156": {
      "postcode": "HU8",
      "latitude": 53.7694364,
      "longitude": -0.2996667
   },
   "2157": {
      "postcode": "N8",
      "latitude": 51.5829293,
      "longitude": -0.1198918
   },
   "2158": {
      "postcode": "IG6",
      "latitude": 51.5960763,
      "longitude": 0.0877543
   },
   "2159": {
      "postcode": "DL17",
      "latitude": 54.6805221,
      "longitude": -1.5410837
   },
   "2160": {
      "postcode": "NP13",
      "latitude": 51.7353588,
      "longitude": -3.1414332
   },
   "2161": {
      "postcode": "IV6",
      "latitude": 57.5251331,
      "longitude": -4.4589452
   },
   "2162": {
      "postcode": "LE87",
      "latitude": 52.6277023,
      "longitude": -1.1336672
   },
   "2163": {
      "postcode": "BT53",
      "latitude": 55.0857068,
      "longitude": -6.4749555
   },
   "2164": {
      "postcode": "ME4",
      "latitude": 51.3814348,
      "longitude": 0.5288721
   },
   "2165": {
      "postcode": "DT8",
      "latitude": 50.8199071,
      "longitude": -2.7589018
   },
   "2166": {
      "postcode": "HA5",
      "latitude": 51.5949876,
      "longitude": -0.3862778
   },
   "2167": {
      "postcode": "CA26",
      "latitude": 54.5445875,
      "longitude": -3.4825948
   },
   "2168": {
      "postcode": "B48",
      "latitude": 52.3547623,
      "longitude": -1.9470221
   },
   "2169": {
      "postcode": "IV22",
      "latitude": 57.7387245,
      "longitude": -5.5136528
   },
   "2170": {
      "postcode": "IG9",
      "latitude": 51.6258577,
      "longitude": 0.0402651
   },
   "2171": {
      "postcode": "HR7",
      "latitude": 52.1855201,
      "longitude": -2.5236492
   },
   "2172": {
      "postcode": "HP23",
      "latitude": 51.7954966,
      "longitude": -0.6612615
   },
   "2173": {
      "postcode": "CM98",
      "latitude": 51.7521007,
      "longitude": 0.5184271
   },
   "2174": {
      "postcode": "ML12",
      "latitude": 55.5680243,
      "longitude": -3.5951775
   },
   "2175": {
      "postcode": "WF9",
      "latitude": 53.6063404,
      "longitude": -1.3212719
   },
   "2176": {
      "postcode": "SG3",
      "latitude": 51.8604038,
      "longitude": -0.1822612
   },
   "2177": {
      "postcode": "B28",
      "latitude": 52.4272318,
      "longitude": -1.8432114
   },
   "2178": {
      "postcode": "DE23",
      "latitude": 52.9003792,
      "longitude": -1.4978936
   },
   "2179": {
      "postcode": "NR8",
      "latitude": 52.6767458,
      "longitude": 1.2047578
   },
   "2180": {
      "postcode": "TW19",
      "latitude": 51.4543018,
      "longitude": -0.4985225
   },
   "2181": {
      "postcode": "PH30",
      "latitude": 56.788984,
      "longitude": -4.599829
   },
   "2182": {
      "postcode": "TW13",
      "latitude": 51.4389898,
      "longitude": -0.4020137
   },
   "2183": {
      "postcode": "LL20",
      "latitude": 52.9588899,
      "longitude": -3.1607087
   },
   "2184": {
      "postcode": "EH11",
      "latitude": 55.932686,
      "longitude": -3.2518031
   },
   "2185": {
      "postcode": "SA47",
      "latitude": 52.1922116,
      "longitude": -4.2996604
   },
   "2186": {
      "postcode": "SO22",
      "latitude": 51.0665077,
      "longitude": -1.3356583
   },
   "2187": {
      "postcode": "KT13",
      "latitude": 51.368034,
      "longitude": -0.4493546
   },
   "2188": {
      "postcode": "ST9",
      "latitude": 53.0528082,
      "longitude": -2.0960983
   },
   "2189": {
      "postcode": "SA80",
      "latitude": 51.6479391,
      "longitude": -3.9242947
   },
   "2190": {
      "postcode": "DA12",
      "latitude": 51.4278035,
      "longitude": 0.3871907
   },
   "2191": {
      "postcode": "L19",
      "latitude": 53.3589357,
      "longitude": -2.9033178
   },
   "2192": {
      "postcode": "B95",
      "latitude": 52.2859172,
      "longitude": -1.7806898
   },
   "2193": {
      "postcode": "WF5",
      "latitude": 53.6804698,
      "longitude": -1.5764287
   },
   "2194": {
      "postcode": "DT4",
      "latitude": 50.6095897,
      "longitude": -2.4654498
   },
   "2195": {
      "postcode": "DN32",
      "latitude": 53.5621163,
      "longitude": -0.070213
   },
   "2196": {
      "postcode": "DN31",
      "latitude": 53.5699931,
      "longitude": -0.0891049
   },
   "2197": {
      "postcode": "EH36",
      "latitude": 55.8555977,
      "longitude": -2.8533193
   },
   "2198": {
      "postcode": "B69",
      "latitude": 52.5027111,
      "longitude": -2.030311
   },
   "2199": {
      "postcode": "TN4",
      "latitude": 51.1455609,
      "longitude": 0.254806
   },
   "2200": {
      "postcode": "L71",
      "latitude": 53.4346302,
      "longitude": -2.9747137
   },
   "2201": {
      "postcode": "BH11",
      "latitude": 50.7622035,
      "longitude": -1.9198635
   },
   "2202": {
      "postcode": "LU2",
      "latitude": 51.8932427,
      "longitude": -0.3944578
   },
   "2203": {
      "postcode": "HR4",
      "latitude": 52.0905547,
      "longitude": -2.7712966
   },
   "2204": {
      "postcode": "EC3M",
      "latitude": 51.5118135,
      "longitude": -0.0821665
   },
   "2205": {
      "postcode": "SS9",
      "latitude": 51.5547671,
      "longitude": 0.651723
   },
   "2206": {
      "postcode": "KW10",
      "latitude": 57.9740723,
      "longitude": -3.9787883
   },
   "2207": {
      "postcode": "CM16",
      "latitude": 51.7002877,
      "longitude": 0.1200906
   },
   "2208": {
      "postcode": "TS2",
      "latitude": 54.5853647,
      "longitude": -1.2376261
   },
   "2209": {
      "postcode": "M11",
      "latitude": 53.4788514,
      "longitude": -2.1812356
   },
   "2210": {
      "postcode": "IP15",
      "latitude": 52.1562567,
      "longitude": 1.595477
   },
   "2211": {
      "postcode": "BL8",
      "latitude": 53.6048216,
      "longitude": -2.3275802
   },
   "2212": {
      "postcode": "BT39",
      "latitude": 54.745645,
      "longitude": -6.0174462
   },
   "2213": {
      "postcode": "M22",
      "latitude": 53.3858702,
      "longitude": -2.2600788
   },
   "2214": {
      "postcode": "BA22",
      "latitude": 50.9695037,
      "longitude": -2.6381055
   },
   "2215": {
      "postcode": "LD4",
      "latitude": 52.1178244,
      "longitude": -3.5568359
   },
   "2216": {
      "postcode": "PH5",
      "latitude": 56.3282762,
      "longitude": -3.8298735
   },
   "2217": {
      "postcode": "BH9",
      "latitude": 50.749635,
      "longitude": -1.8727345
   },
   "2218": {
      "postcode": "HU5",
      "latitude": 53.7599562,
      "longitude": -0.3761886
   },
   "2219": {
      "postcode": "LE17",
      "latitude": 52.4675874,
      "longitude": -1.1778293
   },
   "2220": {
      "postcode": "SP10",
      "latitude": 51.211413,
      "longitude": -1.4845424
   },
   "2221": {
      "postcode": "RH8",
      "latitude": 51.2508257,
      "longitude": 0.0023834
   },
   "2222": {
      "postcode": "IP32",
      "latitude": 52.2546724,
      "longitude": 0.7191907
   },
   "2223": {
      "postcode": "KA13",
      "latitude": 55.6556626,
      "longitude": -4.7001607
   },
   "2224": {
      "postcode": "FK5",
      "latitude": 56.0272594,
      "longitude": -3.8224587
   },
   "2225": {
      "postcode": "NP44",
      "latitude": 51.6512296,
      "longitude": -3.0279524
   },
   "2226": {
      "postcode": "SS6",
      "latitude": 51.5886238,
      "longitude": 0.6074751
   },
   "2227": {
      "postcode": "IP21",
      "latitude": 52.3648604,
      "longitude": 1.2367254
   },
   "2228": {
      "postcode": "NP24",
      "latitude": 51.7189914,
      "longitude": -3.2385423
   },
   "2229": {
      "postcode": "NR22",
      "latitude": 52.8944462,
      "longitude": 0.8651737
   },
   "2230": {
      "postcode": "WN7",
      "latitude": 53.4980465,
      "longitude": -2.5184534
   },
   "2231": {
      "postcode": "BH6",
      "latitude": 50.7276493,
      "longitude": -1.8019536
   },
   "2232": {
      "postcode": "BB11",
      "latitude": 53.7826402,
      "longitude": -2.2539059
   },
   "2233": {
      "postcode": "WD7",
      "latitude": 51.6870763,
      "longitude": -0.309921
   },
   "2234": {
      "postcode": "EC4A",
      "latitude": 51.5157778,
      "longitude": -0.1082509
   },
   "2235": {
      "postcode": "CM5",
      "latitude": 51.7217242,
      "longitude": 0.2482353
   },
   "2236": {
      "postcode": "TA1",
      "latitude": 51.0132224,
      "longitude": -3.1028526
   },
   "2237": {
      "postcode": "RM16",
      "latitude": 51.4929827,
      "longitude": 0.3410404
   },
   "2238": {
      "postcode": "PH7",
      "latitude": 56.3730997,
      "longitude": -3.8270302
   },
   "2239": {
      "postcode": "SW1A",
      "latitude": 51.5044592,
      "longitude": -0.1321624
   },
   "2240": {
      "postcode": "CT12",
      "latitude": 51.3433748,
      "longitude": 1.369083
   },
   "2241": {
      "postcode": "LS3",
      "latitude": 53.8023697,
      "longitude": -1.5634257
   },
   "2242": {
      "postcode": "S21",
      "latitude": 53.3120546,
      "longitude": -1.3396584
   },
   "2243": {
      "postcode": "B38",
      "latitude": 52.3999018,
      "longitude": -1.9347197
   },
   "2244": {
      "postcode": "S35",
      "latitude": 53.4586541,
      "longitude": -1.4979375
   },
   "2245": {
      "postcode": "WF4",
      "latitude": 53.6466346,
      "longitude": -1.5193831
   },
   "2246": {
      "postcode": "SK16",
      "latitude": 53.4746223,
      "longitude": -2.0827362
   },
   "2247": {
      "postcode": "LE41",
      "latitude": 52.6129239,
      "longitude": -1.1949066
   },
   "2248": {
      "postcode": "DE74",
      "latitude": 52.8395922,
      "longitude": -1.3258768
   },
   "2249": {
      "postcode": "L4",
      "latitude": 53.437841,
      "longitude": -2.9612931
   },
   "2250": {
      "postcode": "L9",
      "latitude": 53.4613892,
      "longitude": -2.9536021
   },
   "2251": {
      "postcode": "CA95",
      "latitude": 54.6446666,
      "longitude": -3.5664497
   },
   "2252": {
      "postcode": "IV47",
      "latitude": 57.2952228,
      "longitude": -6.3443887
   },
   "2253": {
      "postcode": "G33",
      "latitude": 55.8741808,
      "longitude": -4.1653486
   },
   "2254": {
      "postcode": "CM11",
      "latitude": 51.6235893,
      "longitude": 0.4459616
   },
   "2255": {
      "postcode": "OL10",
      "latitude": 53.5904693,
      "longitude": -2.223154
   },
   "2256": {
      "postcode": "G40",
      "latitude": 55.8474967,
      "longitude": -4.2211184
   },
   "2257": {
      "postcode": "HP16",
      "latitude": 51.7022351,
      "longitude": -0.7196191
   },
   "2258": {
      "postcode": "BR7",
      "latitude": 51.4148588,
      "longitude": 0.0645782
   },
   "2259": {
      "postcode": "RG28",
      "latitude": 51.2341195,
      "longitude": -1.3359686
   },
   "2260": {
      "postcode": "BH23",
      "latitude": 50.7475595,
      "longitude": -1.7543605
   },
   "2261": {
      "postcode": "CM7",
      "latitude": 51.897274,
      "longitude": 0.5373554
   },
   "2262": {
      "postcode": "DE24",
      "latitude": 52.8891675,
      "longitude": -1.4528507
   },
   "2263": {
      "postcode": "CR9",
      "latitude": 51.3740708,
      "longitude": -0.098286
   },
   "2264": {
      "postcode": "N18",
      "latitude": 51.6138819,
      "longitude": -0.0665839
   },
   "2265": {
      "postcode": "CW7",
      "latitude": 53.1899294,
      "longitude": -2.5290755
   },
   "2266": {
      "postcode": "CO10",
      "latitude": 52.058478,
      "longitude": 0.7211086
   },
   "2267": {
      "postcode": "B79",
      "latitude": 52.6506131,
      "longitude": -1.6815794
   },
   "2268": {
      "postcode": "PL2",
      "latitude": 50.389557,
      "longitude": -4.1630645
   },
   "2269": {
      "postcode": "LA8",
      "latitude": 54.3238097,
      "longitude": -2.7619094
   },
   "2270": {
      "postcode": "SO53",
      "latitude": 50.9860424,
      "longitude": -1.383629
   },
   "2271": {
      "postcode": "BN7",
      "latitude": 50.877372,
      "longitude": -0.0008331
   },
   "2272": {
      "postcode": "MK41",
      "latitude": 52.1526153,
      "longitude": -0.4477354
   },
   "2273": {
      "postcode": "KA21",
      "latitude": 55.6421009,
      "longitude": -4.7844006
   },
   "2274": {
      "postcode": "NE48",
      "latitude": 55.1317811,
      "longitude": -2.2582022
   },
   "2275": {
      "postcode": "NW3",
      "latitude": 51.5523422,
      "longitude": -0.1725058
   },
   "2276": {
      "postcode": "EH14",
      "latitude": 55.9088677,
      "longitude": -3.2859923
   },
   "2277": {
      "postcode": "HD8",
      "latitude": 53.5995424,
      "longitude": -1.6750146
   },
   "2278": {
      "postcode": "NE45",
      "latitude": 54.9766604,
      "longitude": -2.0147337
   },
   "2279": {
      "postcode": "SN8",
      "latitude": 51.4063157,
      "longitude": -1.6857426
   },
   "2280": {
      "postcode": "S65",
      "latitude": 53.436171,
      "longitude": -1.3185879
   },
   "2281": {
      "postcode": "M34",
      "latitude": 53.4565302,
      "longitude": -2.1185355
   },
   "2282": {
      "postcode": "NE28",
      "latitude": 55.0001992,
      "longitude": -1.5207301
   },
   "2283": {
      "postcode": "NE25",
      "latitude": 55.0523507,
      "longitude": -1.4893199
   },
   "2284": {
      "postcode": "GL17",
      "latitude": 51.8552806,
      "longitude": -2.5103348
   },
   "2285": {
      "postcode": "WV11",
      "latitude": 52.6105811,
      "longitude": -2.0719935
   },
   "2286": {
      "postcode": "TD4",
      "latitude": 55.642449,
      "longitude": -2.6720572
   },
   "2287": {
      "postcode": "HU10",
      "latitude": 53.7515019,
      "longitude": -0.4418264
   },
   "2288": {
      "postcode": "NR11",
      "latitude": 52.8409073,
      "longitude": 1.2737841
   },
   "2289": {
      "postcode": "LN1",
      "latitude": 53.2609265,
      "longitude": -0.5924173
   },
   "2290": {
      "postcode": "FK12",
      "latitude": 56.1525705,
      "longitude": -3.8017465
   },
   "2291": {
      "postcode": "LA18",
      "latitude": 54.2154222,
      "longitude": -3.2760572
   },
   "2292": {
      "postcode": "DG14",
      "latitude": 55.0819733,
      "longitude": -2.9826094
   },
   "2293": {
      "postcode": "B43",
      "latitude": 52.5485092,
      "longitude": -1.9307835
   },
   "2294": {
      "postcode": "NE6",
      "latitude": 54.9774742,
      "longitude": -1.5658577
   },
   "2295": {
      "postcode": "WR10",
      "latitude": 52.1149851,
      "longitude": -2.0671085
   },
   "2296": {
      "postcode": "NE63",
      "latitude": 55.1782267,
      "longitude": -1.5632732
   },
   "2297": {
      "postcode": "AB31",
      "latitude": 57.0729813,
      "longitude": -2.522251
   },
   "2298": {
      "postcode": "PA70",
      "latitude": 56.3649649,
      "longitude": -6.0371982
   },
   "2299": {
      "postcode": "PO11",
      "latitude": 50.7920495,
      "longitude": -0.9756968
   },
   "2300": {
      "postcode": "SE6",
      "latitude": 51.438559,
      "longitude": -0.0166543
   },
   "2301": {
      "postcode": "GU26",
      "latitude": 51.1142993,
      "longitude": -0.75038
   },
   "2302": {
      "postcode": "B47",
      "latitude": 52.3852897,
      "longitude": -1.8800827
   },
   "2303": {
      "postcode": "HS8",
      "latitude": 57.2352236,
      "longitude": -7.3470515
   },
   "2304": {
      "postcode": "PA77",
      "latitude": 56.4953995,
      "longitude": -6.8810683
   },
   "2305": {
      "postcode": "YO16",
      "latitude": 54.0956952,
      "longitude": -0.2020607
   },
   "2306": {
      "postcode": "B99",
      "latitude": 52.4959257,
      "longitude": -1.8942585
   },
   "2307": {
      "postcode": "TS4",
      "latitude": 54.5559482,
      "longitude": -1.2229129
   },
   "2308": {
      "postcode": "NR2",
      "latitude": 52.6291722,
      "longitude": 1.2800286
   },
   "2309": {
      "postcode": "CV47",
      "latitude": 52.2354306,
      "longitude": -1.3854686
   },
   "2310": {
      "postcode": "PH49",
      "latitude": 56.674888,
      "longitude": -5.1153736
   },
   "2311": {
      "postcode": "HP6",
      "latitude": 51.6783912,
      "longitude": -0.5991444
   },
   "2312": {
      "postcode": "WD23",
      "latitude": 51.6452717,
      "longitude": -0.3580507
   },
   "2313": {
      "postcode": "DN16",
      "latitude": 53.5674423,
      "longitude": -0.6397388
   },
   "2314": {
      "postcode": "L10",
      "latitude": 53.4744835,
      "longitude": -2.9266207
   },
   "2315": {
      "postcode": "CF23",
      "latitude": 51.5146202,
      "longitude": -3.1554545
   },
   "2316": {
      "postcode": "PH23",
      "latitude": 57.2837083,
      "longitude": -3.8169255
   },
   "2317": {
      "postcode": "SA12",
      "latitude": 51.6082605,
      "longitude": -3.7957976
   },
   "2318": {
      "postcode": "EH43",
      "latitude": 55.6238505,
      "longitude": -3.0113991
   },
   "2319": {
      "postcode": "KA9",
      "latitude": 55.4972272,
      "longitude": -4.6053308
   },
   "2320": {
      "postcode": "DA2",
      "latitude": 51.4320776,
      "longitude": 0.2331447
   },
   "2321": {
      "postcode": "BT18",
      "latitude": 54.6412227,
      "longitude": -5.8220028
   },
   "2322": {
      "postcode": "OX9",
      "latitude": 51.7379966,
      "longitude": -0.9839931
   },
   "2323": {
      "postcode": "IV54",
      "latitude": 57.4304314,
      "longitude": -5.6198002
   },
   "2324": {
      "postcode": "S97",
      "latitude": 53.5032475,
      "longitude": -1.3379727
   },
   "2325": {
      "postcode": "SE16",
      "latitude": 51.4965989,
      "longitude": -0.053091
   },
   "2326": {
      "postcode": "BD14",
      "latitude": 53.7821908,
      "longitude": -1.8183815
   },
   "2327": {
      "postcode": "SG1",
      "latitude": 51.913148,
      "longitude": -0.1949772
   },
   "2328": {
      "postcode": "PA41",
      "latitude": 55.6744664,
      "longitude": -5.7425879
   },
   "2329": {
      "postcode": "CM4",
      "latitude": 51.6750757,
      "longitude": 0.3903574
   },
   "2330": {
      "postcode": "YO18",
      "latitude": 54.2589315,
      "longitude": -0.7690067
   },
   "2331": {
      "postcode": "SW1V",
      "latitude": 51.4894932,
      "longitude": -0.1399734
   },
   "2332": {
      "postcode": "BS49",
      "latitude": 51.3829265,
      "longitude": -2.8123525
   },
   "2333": {
      "postcode": "BN16",
      "latitude": 50.814554,
      "longitude": -0.4957555
   },
   "2334": {
      "postcode": "KT11",
      "latitude": 51.3281995,
      "longitude": -0.4028817
   },
   "2335": {
      "postcode": "NN14",
      "latitude": 52.4110165,
      "longitude": -0.6955533
   },
   "2336": {
      "postcode": "RG6",
      "latitude": 51.4378229,
      "longitude": -0.9281585
   },
   "2337": {
      "postcode": "WF16",
      "latitude": 53.7102031,
      "longitude": -1.6692768
   },
   "2338": {
      "postcode": "EX31",
      "latitude": 51.0857144,
      "longitude": -4.068489
   },
   "2339": {
      "postcode": "SO42",
      "latitude": 50.8151761,
      "longitude": -1.5366074
   },
   "2340": {
      "postcode": "AB38",
      "latitude": 57.4863473,
      "longitude": -3.2264677
   },
   "2341": {
      "postcode": "KY8",
      "latitude": 56.1972496,
      "longitude": -3.0126117
   },
   "2342": {
      "postcode": "MK5",
      "latitude": 52.0209076,
      "longitude": -0.7846548
   },
   "2343": {
      "postcode": "CH26",
      "latitude": 53.365703,
      "longitude": -3.0659079
   },
   "2344": {
      "postcode": "G1",
      "latitude": 55.8588265,
      "longitude": -4.2488914
   },
   "2345": {
      "postcode": "SA39",
      "latitude": 52.0188701,
      "longitude": -4.2435846
   },
   "2346": {
      "postcode": "NE20",
      "latitude": 55.0526955,
      "longitude": -1.7874806
   },
   "2347": {
      "postcode": "SK4",
      "latitude": 53.4194666,
      "longitude": -2.1817251
   },
   "2348": {
      "postcode": "GU22",
      "latitude": 51.3121626,
      "longitude": -0.5517403
   },
   "2349": {
      "postcode": "HU6",
      "latitude": 53.781012,
      "longitude": -0.3713507
   },
   "2350": {
      "postcode": "NP4",
      "latitude": 51.7193671,
      "longitude": -3.0470946
   },
   "2351": {
      "postcode": "W10",
      "latitude": 51.5230766,
      "longitude": -0.2176568
   },
   "2352": {
      "postcode": "CT16",
      "latitude": 51.1421367,
      "longitude": 1.2992504
   },
   "2353": {
      "postcode": "YO14",
      "latitude": 54.1978665,
      "longitude": -0.2981294
   },
   "2354": {
      "postcode": "BT6",
      "latitude": 54.5799883,
      "longitude": -5.897917
   },
   "2355": {
      "postcode": "BA4",
      "latitude": 51.1724351,
      "longitude": -2.5320463
   },
   "2356": {
      "postcode": "CA6",
      "latitude": 54.9933146,
      "longitude": -2.8949601
   },
   "2357": {
      "postcode": "HP4",
      "latitude": 51.7678331,
      "longitude": -0.5685998
   },
   "2358": {
      "postcode": "CM15",
      "latitude": 51.6443998,
      "longitude": 0.3035113
   },
   "2359": {
      "postcode": "TD12",
      "latitude": 55.6527612,
      "longitude": -2.2410299
   },
   "2360": {
      "postcode": "TA2",
      "latitude": 51.0340308,
      "longitude": -3.1010171
   },
   "2361": {
      "postcode": "DL1",
      "latitude": 54.529558,
      "longitude": -1.5387005
   },
   "2362": {
      "postcode": "CW4",
      "latitude": 53.2088755,
      "longitude": -2.3556124
   },
   "2363": {
      "postcode": "DD1",
      "latitude": 56.4610055,
      "longitude": -2.9764463
   },
   "2364": {
      "postcode": "PA10",
      "latitude": 55.8328892,
      "longitude": -4.5514075
   },
   "2365": {
      "postcode": "TN2",
      "latitude": 51.1279359,
      "longitude": 0.2750576
   },
   "2366": {
      "postcode": "MK46",
      "latitude": 52.1557959,
      "longitude": -0.7020457
   },
   "2367": {
      "postcode": "NE40",
      "latitude": 54.9659302,
      "longitude": -1.7743389
   },
   "2368": {
      "postcode": "HG5",
      "latitude": 54.013486,
      "longitude": -1.4579043
   },
   "2369": {
      "postcode": "SA43",
      "latitude": 52.0872908,
      "longitude": -4.6280484
   },
   "2370": {
      "postcode": "M8",
      "latitude": 53.5086893,
      "longitude": -2.2401019
   },
   "2371": {
      "postcode": "TN18",
      "latitude": 51.0428062,
      "longitude": 0.5226677
   },
   "2372": {
      "postcode": "M16",
      "latitude": 53.4551078,
      "longitude": -2.2645745
   },
   "2373": {
      "postcode": "TA20",
      "latitude": 50.8735523,
      "longitude": -2.9622162
   },
   "2374": {
      "postcode": "NE98",
      "latitude": 54.9722874,
      "longitude": -1.598375
   },
   "2375": {
      "postcode": "WC2B",
      "latitude": 51.5149298,
      "longitude": -0.1204399
   },
   "2376": {
      "postcode": "RG27",
      "latitude": 51.3058876,
      "longitude": -0.9469323
   },
   "2377": {
      "postcode": "NR6",
      "latitude": 52.6619269,
      "longitude": 1.2803571
   },
   "2378": {
      "postcode": "SO16",
      "latitude": 50.936668,
      "longitude": -1.433299
   },
   "2379": {
      "postcode": "FK3",
      "latitude": 56.0107515,
      "longitude": -3.7207793
   },
   "2380": {
      "postcode": "DE75",
      "latitude": 53.0130721,
      "longitude": -1.3543073
   },
   "2381": {
      "postcode": "E13",
      "latitude": 51.5278271,
      "longitude": 0.0267009
   },
   "2382": {
      "postcode": "TN15",
      "latitude": 51.302716,
      "longitude": 0.2746409
   },
   "2383": {
      "postcode": "WD24",
      "latitude": 51.6737504,
      "longitude": -0.3981532
   },
   "2384": {
      "postcode": "AB52",
      "latitude": 57.3437877,
      "longitude": -2.6088547
   },
   "2385": {
      "postcode": "FY1",
      "latitude": 53.8152768,
      "longitude": -3.0470272
   },
   "2386": {
      "postcode": "BT52",
      "latitude": 55.134521,
      "longitude": -6.6551623
   },
   "2387": {
      "postcode": "EX38",
      "latitude": 50.9439211,
      "longitude": -4.1521992
   },
   "2388": {
      "postcode": "PH38",
      "latitude": 56.8438021,
      "longitude": -5.7438068
   },
   "2389": {
      "postcode": "SO17",
      "latitude": 50.927271,
      "longitude": -1.3926392
   },
   "2390": {
      "postcode": "WR8",
      "latitude": 52.074811,
      "longitude": -2.2066668
   },
   "2391": {
      "postcode": "SW1P",
      "latitude": 51.4900482,
      "longitude": -0.133214
   },
   "2392": {
      "postcode": "NE64",
      "latitude": 55.1846583,
      "longitude": -1.5154095
   },
   "2393": {
      "postcode": "GU5",
      "latitude": 51.198914,
      "longitude": -0.5097292
   },
   "2394": {
      "postcode": "SA20",
      "latitude": 52.0119374,
      "longitude": -3.78776
   },
   "2395": {
      "postcode": "CM19",
      "latitude": 51.7594581,
      "longitude": 0.0711651
   },
   "2396": {
      "postcode": "DN41",
      "latitude": 53.581266,
      "longitude": -0.1952465
   },
   "2397": {
      "postcode": "TW9",
      "latitude": 51.4694559,
      "longitude": -0.2927343
   },
   "2398": {
      "postcode": "G5",
      "latitude": 55.8479394,
      "longitude": -4.252235
   },
   "2399": {
      "postcode": "IP31",
      "latitude": 52.2925866,
      "longitude": 0.8356002
   },
   "2400": {
      "postcode": "L26",
      "latitude": 53.3645787,
      "longitude": -2.8330565
   },
   "2401": {
      "postcode": "ST19",
      "latitude": 52.7087806,
      "longitude": -2.1473047
   },
   "2402": {
      "postcode": "E20",
      "latitude": 51.5465858,
      "longitude": -0.0100095
   },
   "2403": {
      "postcode": "IP22",
      "latitude": 52.3759592,
      "longitude": 1.0527441
   },
   "2404": {
      "postcode": "PE36",
      "latitude": 52.9394294,
      "longitude": 0.5087246
   },
   "2405": {
      "postcode": "BL2",
      "latitude": 53.5885067,
      "longitude": -2.3950838
   },
   "2406": {
      "postcode": "NR23",
      "latitude": 52.9487974,
      "longitude": 0.8580662
   },
   "2407": {
      "postcode": "BH17",
      "latitude": 50.746875,
      "longitude": -1.9800404
   },
   "2408": {
      "postcode": "LL42",
      "latitude": 52.7257676,
      "longitude": -4.0552734
   },
   "2409": {
      "postcode": "HU16",
      "latitude": 53.7815431,
      "longitude": -0.4222631
   },
   "2410": {
      "postcode": "PA61",
      "latitude": 56.0716509,
      "longitude": -6.2030067
   },
   "2411": {
      "postcode": "BN44",
      "latitude": 50.8910892,
      "longitude": -0.322266
   },
   "2412": {
      "postcode": "IV52",
      "latitude": 57.3365804,
      "longitude": -5.6530794
   },
   "2413": {
      "postcode": "SA66",
      "latitude": 51.8836245,
      "longitude": -4.7449465
   },
   "2414": {
      "postcode": "RH15",
      "latitude": 50.9574814,
      "longitude": -0.1309943
   },
   "2415": {
      "postcode": "W7",
      "latitude": 51.5118598,
      "longitude": -0.335921
   },
   "2416": {
      "postcode": "W1A",
      "latitude": 51.5243788,
      "longitude": -0.11279
   },
   "2417": {
      "postcode": "OX17",
      "latitude": 52.07362,
      "longitude": -1.2890522
   },
   "2418": {
      "postcode": "NP12",
      "latitude": 51.6691612,
      "longitude": -3.1979409
   },
   "2419": {
      "postcode": "NE66",
      "latitude": 55.4286568,
      "longitude": -1.7296243
   },
   "2420": {
      "postcode": "TA3",
      "latitude": 50.9936898,
      "longitude": -3.037039
   },
   "2421": {
      "postcode": "BT33",
      "latitude": 54.2233393,
      "longitude": -5.8913207
   },
   "2422": {
      "postcode": "RM19",
      "latitude": 51.4828338,
      "longitude": 0.2443696
   },
   "2423": {
      "postcode": "M13",
      "latitude": 53.4604456,
      "longitude": -2.2154546
   },
   "2424": {
      "postcode": "WA88",
      "latitude": 53.3679728,
      "longitude": -2.7686736
   },
   "2425": {
      "postcode": "GL14",
      "latitude": 51.8176681,
      "longitude": -2.4811369
   },
   "2426": {
      "postcode": "G67",
      "latitude": 55.9466652,
      "longitude": -3.9871989
   },
   "2427": {
      "postcode": "TS19",
      "latitude": 54.5771805,
      "longitude": -1.3433587
   },
   "2428": {
      "postcode": "TA15",
      "latitude": 50.9511535,
      "longitude": -2.7169146
   },
   "2429": {
      "postcode": "KT21",
      "latitude": 51.3111901,
      "longitude": -0.3035835
   },
   "2430": {
      "postcode": "DT9",
      "latitude": 50.9420485,
      "longitude": -2.5162283
   },
   "2431": {
      "postcode": "PL20",
      "latitude": 50.5001025,
      "longitude": -4.100192
   },
   "2432": {
      "postcode": "G42",
      "latitude": 55.8321344,
      "longitude": -4.2574366
   },
   "2433": {
      "postcode": "NE43",
      "latitude": 54.9480295,
      "longitude": -1.9058067
   },
   "2434": {
      "postcode": "CV23",
      "latitude": 52.3683793,
      "longitude": -1.2835273
   },
   "2435": {
      "postcode": "DE7",
      "latitude": 52.9734328,
      "longitude": -1.3232261
   },
   "2436": {
      "postcode": "ML10",
      "latitude": 55.6801214,
      "longitude": -4.0692342
   },
   "2437": {
      "postcode": "BS14",
      "latitude": 51.412973,
      "longitude": -2.5632222
   },
   "2438": {
      "postcode": "TS24",
      "latitude": 54.6967403,
      "longitude": -1.2111481
   },
   "2439": {
      "postcode": "BT62",
      "latitude": 54.411752,
      "longitude": -6.4661507
   },
   "2440": {
      "postcode": "B32",
      "latitude": 52.4486238,
      "longitude": -1.9945407
   },
   "2441": {
      "postcode": "CT8",
      "latitude": 51.3799305,
      "longitude": 1.3366875
   },
   "2442": {
      "postcode": "EH40",
      "latitude": 55.9907365,
      "longitude": -2.6620483
   },
   "2443": {
      "postcode": "BT10",
      "latitude": 54.5594341,
      "longitude": -5.9851563
   },
   "2444": {
      "postcode": "IV20",
      "latitude": 57.7885407,
      "longitude": -3.9034344
   },
   "2445": {
      "postcode": "PA27",
      "latitude": 56.1553315,
      "longitude": -5.0860009
   },
   "2446": {
      "postcode": "NN12",
      "latitude": 52.1265265,
      "longitude": -0.9999332
   },
   "2447": {
      "postcode": "SK8",
      "latitude": 53.3796923,
      "longitude": -2.2090903
   },
   "2448": {
      "postcode": "LE14",
      "latitude": 52.7843462,
      "longitude": -0.8971578
   },
   "2449": {
      "postcode": "SG13",
      "latitude": 51.7877234,
      "longitude": -0.0715474
   },
   "2450": {
      "postcode": "G45",
      "latitude": 55.8049645,
      "longitude": -4.2327269
   },
   "2451": {
      "postcode": "BS32",
      "latitude": 51.5444813,
      "longitude": -2.5576565
   },
   "2452": {
      "postcode": "NE8",
      "latitude": 54.9549915,
      "longitude": -1.6065202
   },
   "2453": {
      "postcode": "HX4",
      "latitude": 53.6770659,
      "longitude": -1.8826642
   },
   "2454": {
      "postcode": "PE33",
      "latitude": 52.6459805,
      "longitude": 0.4658335
   },
   "2455": {
      "postcode": "OL4",
      "latitude": 53.5424267,
      "longitude": -2.0734838
   },
   "2456": {
      "postcode": "RH9",
      "latitude": 51.2363052,
      "longitude": -0.0630331
   },
   "2457": {
      "postcode": "PA68",
      "latitude": 56.434551,
      "longitude": -6.1426434
   },
   "2458": {
      "postcode": "BD22",
      "latitude": 53.8457607,
      "longitude": -1.9553752
   },
   "2459": {
      "postcode": "NE61",
      "latitude": 55.1782661,
      "longitude": -1.6872652
   },
   "2460": {
      "postcode": "E4",
      "latitude": 51.6218323,
      "longitude": -0.0057248
   },
   "2461": {
      "postcode": "DH1",
      "latitude": 54.7820794,
      "longitude": -1.565542
   },
   "2462": {
      "postcode": "N16",
      "latitude": 51.5625965,
      "longitude": -0.0766528
   },
   "2463": {
      "postcode": "IV17",
      "latitude": 57.6989377,
      "longitude": -4.2594791
   },
   "2464": {
      "postcode": "M2",
      "latitude": 53.4804426,
      "longitude": -2.2444104
   },
   "2465": {
      "postcode": "CT18",
      "latitude": 51.1156399,
      "longitude": 1.1492879
   },
   "2466": {
      "postcode": "SS1",
      "latitude": 51.5376959,
      "longitude": 0.7305193
   },
   "2467": {
      "postcode": "SY11",
      "latitude": 52.8699722,
      "longitude": -3.0312225
   },
   "2468": {
      "postcode": "M32",
      "latitude": 53.4508922,
      "longitude": -2.3094048
   },
   "2469": {
      "postcode": "NR25",
      "latitude": 52.9201145,
      "longitude": 1.082767
   },
   "2470": {
      "postcode": "N1C",
      "latitude": 51.5365569,
      "longitude": -0.1258562
   },
   "2471": {
      "postcode": "NG1",
      "latitude": 52.9547046,
      "longitude": -1.1485826
   },
   "2472": {
      "postcode": "M99",
      "latitude": 53.4848048,
      "longitude": -2.2310186
   },
   "2473": {
      "postcode": "CF40",
      "latitude": 51.6203262,
      "longitude": -3.4516265
   },
   "2474": {
      "postcode": "PH1",
      "latitude": 56.4224093,
      "longitude": -3.4793955
   },
   "2475": {
      "postcode": "WS12",
      "latitude": 52.7071392,
      "longitude": -2.0024555
   },
   "2476": {
      "postcode": "DL13",
      "latitude": 54.7169113,
      "longitude": -1.9573372
   },
   "2477": {
      "postcode": "DN14",
      "latitude": 53.7086376,
      "longitude": -0.9413185
   },
   "2478": {
      "postcode": "DE5",
      "latitude": 53.0449455,
      "longitude": -1.4028946
   },
   "2479": {
      "postcode": "EX16",
      "latitude": 50.9226683,
      "longitude": -3.4916806
   },
   "2480": {
      "postcode": "BS20",
      "latitude": 51.4806147,
      "longitude": -2.7535558
   },
   "2481": {
      "postcode": "M26",
      "latitude": 53.5623031,
      "longitude": -2.3348733
   },
   "2482": {
      "postcode": "N10",
      "latitude": 51.5948015,
      "longitude": -0.1450221
   },
   "2483": {
      "postcode": "M20",
      "latitude": 53.4241784,
      "longitude": -2.232693
   },
   "2484": {
      "postcode": "TR16",
      "latitude": 50.2326748,
      "longitude": -5.2212503
   },
   "2485": {
      "postcode": "B17",
      "latitude": 52.461233,
      "longitude": -1.9586781
   },
   "2486": {
      "postcode": "B4",
      "latitude": 52.4857738,
      "longitude": -1.8928567
   },
   "2487": {
      "postcode": "DL4",
      "latitude": 54.6301995,
      "longitude": -1.6443807
   },
   "2488": {
      "postcode": "AB14",
      "latitude": 57.1004493,
      "longitude": -2.2713239
   },
   "2489": {
      "postcode": "EH20",
      "latitude": 55.8788332,
      "longitude": -3.156757
   },
   "2490": {
      "postcode": "BN23",
      "latitude": 50.7976028,
      "longitude": 0.3125132
   },
   "2491": {
      "postcode": "KT15",
      "latitude": 51.3637699,
      "longitude": -0.4958004
   },
   "2492": {
      "postcode": "PA42",
      "latitude": 55.6368001,
      "longitude": -6.1894539
   },
   "2493": {
      "postcode": "BB94",
      "latitude": 53.9152416,
      "longitude": -2.1380327
   },
   "2494": {
      "postcode": "OX33",
      "latitude": 51.7583288,
      "longitude": -1.1399624
   },
   "2495": {
      "postcode": "SG11",
      "latitude": 51.8860481,
      "longitude": 0.0334702
   },
   "2496": {
      "postcode": "IP26",
      "latitude": 52.5074578,
      "longitude": 0.5727044
   },
   "2497": {
      "postcode": "M61",
      "latitude": 53.4865107,
      "longitude": -2.2290529
   },
   "2498": {
      "postcode": "NE38",
      "latitude": 54.8934927,
      "longitude": -1.5247917
   },
   "2499": {
      "postcode": "YO30",
      "latitude": 53.9871101,
      "longitude": -1.1170367
   },
   "2500": {
      "postcode": "ME15",
      "latitude": 51.2532135,
      "longitude": 0.5335779
   },
   "2501": {
      "postcode": "RG9",
      "latitude": 51.5450342,
      "longitude": -0.9260061
   },
   "2502": {
      "postcode": "LA11",
      "latitude": 54.199939,
      "longitude": -2.9260474
   },
   "2503": {
      "postcode": "M44",
      "latitude": 53.4407447,
      "longitude": -2.4271805
   },
   "2504": {
      "postcode": "IG8",
      "latitude": 51.6100214,
      "longitude": 0.0381164
   },
   "2505": {
      "postcode": "OX7",
      "latitude": 51.9104488,
      "longitude": -1.5287932
   },
   "2506": {
      "postcode": "IV8",
      "latitude": 57.5541728,
      "longitude": -4.2656627
   },
   "2507": {
      "postcode": "CA9",
      "latitude": 54.8009692,
      "longitude": -2.4136614
   },
   "2508": {
      "postcode": "SA37",
      "latitude": 52.0159313,
      "longitude": -4.5927184
   },
   "2509": {
      "postcode": "BH19",
      "latitude": 50.611489,
      "longitude": -1.97082
   },
   "2510": {
      "postcode": "BN20",
      "latitude": 50.7748096,
      "longitude": 0.2519395
   },
   "2511": {
      "postcode": "IG10",
      "latitude": 51.6484187,
      "longitude": 0.0659951
   },
   "2512": {
      "postcode": "LL11",
      "latitude": 53.0634765,
      "longitude": -3.0362413
   },
   "2513": {
      "postcode": "DH98",
      "latitude": 54.8873334,
      "longitude": -1.5884088
   },
   "2514": {
      "postcode": "DA9",
      "latitude": 51.4481337,
      "longitude": 0.2783186
   },
   "2515": {
      "postcode": "RH7",
      "latitude": 51.1746946,
      "longitude": -0.0182314
   },
   "2516": {
      "postcode": "KT1",
      "latitude": 51.4074987,
      "longitude": -0.2982129
   },
   "2517": {
      "postcode": "CF48",
      "latitude": 51.7415755,
      "longitude": -3.3715116
   },
   "2518": {
      "postcode": "B10",
      "latitude": 52.4695926,
      "longitude": -1.8523465
   },
   "2519": {
      "postcode": "SW13",
      "latitude": 51.4761464,
      "longitude": -0.2438054
   },
   "2520": {
      "postcode": "AB99",
      "latitude": 57.1113406,
      "longitude": -2.0939925
   },
   "2521": {
      "postcode": "EH95",
      "latitude": 55.9786198,
      "longitude": -3.2535203
   },
   "2522": {
      "postcode": "SY17",
      "latitude": 52.5171419,
      "longitude": -3.4690989
   },
   "2523": {
      "postcode": "LE1",
      "latitude": 52.6339706,
      "longitude": -1.1326155
   },
   "2524": {
      "postcode": "BL11",
      "latitude": 53.5723273,
      "longitude": -2.425451
   },
   "2525": {
      "postcode": "PO1",
      "latitude": 50.799499,
      "longitude": -1.0896771
   },
   "2526": {
      "postcode": "IP1",
      "latitude": 52.0668563,
      "longitude": 1.13956
   },
   "2527": {
      "postcode": "GL50",
      "latitude": 51.900632,
      "longitude": -2.0818521
   },
   "2528": {
      "postcode": "HP20",
      "latitude": 51.8200483,
      "longitude": -0.8054056
   },
   "2529": {
      "postcode": "KA7",
      "latitude": 55.4471342,
      "longitude": -4.6304833
   },
   "2530": {
      "postcode": "CT5",
      "latitude": 51.3534291,
      "longitude": 1.0349292
   },
   "2531": {
      "postcode": "EH5",
      "latitude": 55.9760767,
      "longitude": -3.2223197
   },
   "2532": {
      "postcode": "DT7",
      "latitude": 50.7294287,
      "longitude": -2.9474704
   },
   "2533": {
      "postcode": "RG20",
      "latitude": 51.4036907,
      "longitude": -1.3378722
   },
   "2534": {
      "postcode": "KA16",
      "latitude": 55.6075033,
      "longitude": -4.3282433
   },
   "2535": {
      "postcode": "IP9",
      "latitude": 51.9891921,
      "longitude": 1.1472122
   },
   "2536": {
      "postcode": "SN6",
      "latitude": 51.6215185,
      "longitude": -1.7409572
   },
   "2537": {
      "postcode": "LL22",
      "latitude": 53.2679053,
      "longitude": -3.5977386
   },
   "2538": {
      "postcode": "TQ11",
      "latitude": 50.4823197,
      "longitude": -3.7850715
   },
   "2539": {
      "postcode": "S60",
      "latitude": 53.4123073,
      "longitude": -1.3507801
   },
   "2540": {
      "postcode": "WS10",
      "latitude": 52.5606417,
      "longitude": -2.0224958
   },
   "2541": {
      "postcode": "HX2",
      "latitude": 53.7385491,
      "longitude": -1.9066236
   },
   "2542": {
      "postcode": "LS8",
      "latitude": 53.8247746,
      "longitude": -1.5094795
   },
   "2543": {
      "postcode": "OL2",
      "latitude": 53.5732655,
      "longitude": -2.1099662
   },
   "2544": {
      "postcode": "NP25",
      "latitude": 51.8025304,
      "longitude": -2.7242692
   },
   "2545": {
      "postcode": "BB6",
      "latitude": 53.7929328,
      "longitude": -2.4175001
   },
   "2546": {
      "postcode": "ZE2",
      "latitude": 60.3146317,
      "longitude": -1.2291689
   },
   "2547": {
      "postcode": "SA4",
      "latitude": 51.6732535,
      "longitude": -4.0486716
   },
   "2548": {
      "postcode": "SK3",
      "latitude": 53.3982575,
      "longitude": -2.172193
   },
   "2549": {
      "postcode": "SN25",
      "latitude": 51.5980434,
      "longitude": -1.8088878
   },
   "2550": {
      "postcode": "PA46",
      "latitude": 55.8626671,
      "longitude": -6.120776
   },
   "2551": {
      "postcode": "SA19",
      "latitude": 51.9545649,
      "longitude": -3.9481925
   },
   "2552": {
      "postcode": "B68",
      "latitude": 52.4785994,
      "longitude": -2.0014018
   },
   "2553": {
      "postcode": "CB23",
      "latitude": 52.2151042,
      "longitude": -0.0318968
   },
   "2554": {
      "postcode": "NR24",
      "latitude": 52.85878,
      "longitude": 1.0502847
   },
   "2555": {
      "postcode": "CA17",
      "latitude": 54.4800608,
      "longitude": -2.3509231
   },
   "2556": {
      "postcode": "CF41",
      "latitude": 51.64737,
      "longitude": -3.4820101
   },
   "2557": {
      "postcode": "CM8",
      "latitude": 51.8055915,
      "longitude": 0.6374042
   },
   "2558": {
      "postcode": "PA33",
      "latitude": 56.3668062,
      "longitude": -5.0642038
   },
   "2559": {
      "postcode": "N4",
      "latitude": 51.5700217,
      "longitude": -0.1043503
   },
   "2560": {
      "postcode": "S62",
      "latitude": 53.465419,
      "longitude": -1.3479048
   },
   "2561": {
      "postcode": "LS20",
      "latitude": 53.8744534,
      "longitude": -1.7157506
   },
   "2562": {
      "postcode": "RG22",
      "latitude": 51.2481133,
      "longitude": -1.1247687
   },
   "2563": {
      "postcode": "EH21",
      "latitude": 55.9385173,
      "longitude": -3.0462249
   },
   "2564": {
      "postcode": "BS3",
      "latitude": 51.4386547,
      "longitude": -2.6031568
   },
   "2565": {
      "postcode": "S80",
      "latitude": 53.2925801,
      "longitude": -1.1521193
   },
   "2566": {
      "postcode": "OL12",
      "latitude": 53.6364434,
      "longitude": -2.1653237
   },
   "2567": {
      "postcode": "CR4",
      "latitude": 51.4043894,
      "longitude": -0.1591591
   },
   "2568": {
      "postcode": "NG7",
      "latitude": 52.9579006,
      "longitude": -1.1725474
   },
   "2569": {
      "postcode": "M19",
      "latitude": 53.4364131,
      "longitude": -2.1963069
   },
   "2570": {
      "postcode": "L24",
      "latitude": 53.3434469,
      "longitude": -2.8391389
   },
   "2571": {
      "postcode": "S8",
      "latitude": 53.3398982,
      "longitude": -1.4776091
   },
   "2572": {
      "postcode": "EX5",
      "latitude": 50.7561717,
      "longitude": -3.4348553
   },
   "2573": {
      "postcode": "PE24",
      "latitude": 53.1644979,
      "longitude": 0.2645359
   },
   "2574": {
      "postcode": "TF10",
      "latitude": 52.7694651,
      "longitude": -2.3870759
   },
   "2575": {
      "postcode": "CW11",
      "latitude": 53.1431937,
      "longitude": -2.3673649
   },
   "2576": {
      "postcode": "SG15",
      "latitude": 52.013322,
      "longitude": -0.2637871
   },
   "2577": {
      "postcode": "EC4R",
      "latitude": 51.5108121,
      "longitude": -0.0904232
   },
   "2578": {
      "postcode": "SW1W",
      "latitude": 51.4925553,
      "longitude": -0.1509311
   },
   "2579": {
      "postcode": "IP98",
      "latitude": 52.3765933,
      "longitude": 1.1109271
   },
   "2580": {
      "postcode": "ME1",
      "latitude": 51.3715824,
      "longitude": 0.4975849
   },
   "2581": {
      "postcode": "BS48",
      "latitude": 51.4251376,
      "longitude": -2.7478067
   },
   "2582": {
      "postcode": "EX6",
      "latitude": 50.6765895,
      "longitude": -3.5972315
   },
   "2583": {
      "postcode": "BT75",
      "latitude": 54.3726416,
      "longitude": -7.3171652
   },
   "2584": {
      "postcode": "BS36",
      "latitude": 51.5257135,
      "longitude": -2.4864768
   },
   "2585": {
      "postcode": "DD6",
      "latitude": 56.4363293,
      "longitude": -2.9262534
   },
   "2586": {
      "postcode": "FK20",
      "latitude": 56.4054262,
      "longitude": -4.6401017
   },
   "2587": {
      "postcode": "B50",
      "latitude": 52.1683483,
      "longitude": -1.8562373
   },
   "2588": {
      "postcode": "WA16",
      "latitude": 53.3030431,
      "longitude": -2.3722288
   },
   "2589": {
      "postcode": "TA23",
      "latitude": 51.1625334,
      "longitude": -3.352683
   },
   "2590": {
      "postcode": "PO30",
      "latitude": 50.6911019,
      "longitude": -1.31348
   },
   "2591": {
      "postcode": "SA64",
      "latitude": 52.002105,
      "longitude": -5.0124731
   },
   "2592": {
      "postcode": "AB22",
      "latitude": 57.1865864,
      "longitude": -2.1223591
   },
   "2593": {
      "postcode": "WF8",
      "latitude": 53.6861759,
      "longitude": -1.3004853
   },
   "2594": {
      "postcode": "EH33",
      "latitude": 55.9415591,
      "longitude": -2.9458801
   },
   "2595": {
      "postcode": "BS29",
      "latitude": 51.3306402,
      "longitude": -2.8750405
   },
   "2596": {
      "postcode": "FY7",
      "latitude": 53.9159897,
      "longitude": -3.0273891
   },
   "2597": {
      "postcode": "NE19",
      "latitude": 55.1795745,
      "longitude": -2.0990756
   },
   "2598": {
      "postcode": "DE14",
      "latitude": 52.8047417,
      "longitude": -1.643379
   },
   "2599": {
      "postcode": "W1T",
      "latitude": 51.5202472,
      "longitude": -0.1367101
   },
   "2600": {
      "postcode": "CB2",
      "latitude": 52.1858693,
      "longitude": 0.1231567
   },
   "2601": {
      "postcode": "OL5",
      "latitude": 53.5180411,
      "longitude": -2.0385356
   },
   "2602": {
      "postcode": "FY6",
      "latitude": 53.8680398,
      "longitude": -2.981457
   },
   "2603": {
      "postcode": "RM8",
      "latitude": 51.5572096,
      "longitude": 0.1293935
   },
   "2604": {
      "postcode": "NG5",
      "latitude": 52.9972496,
      "longitude": -1.1442651
   },
   "2605": {
      "postcode": "W1J",
      "latitude": 51.5079068,
      "longitude": -0.1450205
   },
   "2606": {
      "postcode": "LA10",
      "latitude": 54.3138033,
      "longitude": -2.4939771
   },
   "2607": {
      "postcode": "B78",
      "latitude": 52.6055691,
      "longitude": -1.6733206
   },
   "2608": {
      "postcode": "BN9",
      "latitude": 50.795683,
      "longitude": 0.0498051
   },
   "2609": {
      "postcode": "EN5",
      "latitude": 51.649944,
      "longitude": -0.1975625
   },
   "2610": {
      "postcode": "WD25",
      "latitude": 51.6870777,
      "longitude": -0.3877274
   },
   "2611": {
      "postcode": "NW5",
      "latitude": 51.551787,
      "longitude": -0.1449996
   },
   "2612": {
      "postcode": "NG34",
      "latitude": 52.9871563,
      "longitude": -0.3938278
   },
   "2613": {
      "postcode": "PA1",
      "latitude": 55.8446501,
      "longitude": -4.4173443
   },
   "2614": {
      "postcode": "PL14",
      "latitude": 50.4639492,
      "longitude": -4.466271
   },
   "2615": {
      "postcode": "GL3",
      "latitude": 51.8619393,
      "longitude": -2.1760821
   },
   "2616": {
      "postcode": "CA18",
      "latitude": 54.3543145,
      "longitude": -3.3912119
   },
   "2617": {
      "postcode": "B35",
      "latitude": 52.5188542,
      "longitude": -1.7890673
   },
   "2618": {
      "postcode": "TN37",
      "latitude": 50.8723505,
      "longitude": 0.5572632
   },
   "2619": {
      "postcode": "B29",
      "latitude": 52.4376384,
      "longitude": -1.947722
   },
   "2620": {
      "postcode": "NN18",
      "latitude": 52.4779167,
      "longitude": -0.7130298
   },
   "2621": {
      "postcode": "SG16",
      "latitude": 52.0142001,
      "longitude": -0.298799
   },
   "2622": {
      "postcode": "NG90",
      "latitude": 52.9258962,
      "longitude": -1.1906952
   },
   "2623": {
      "postcode": "EN4",
      "latitude": 51.6491899,
      "longitude": -0.1605104
   },
   "2624": {
      "postcode": "G52",
      "latitude": 55.8478068,
      "longitude": -4.3502252
   },
   "2625": {
      "postcode": "IP2",
      "latitude": 52.0452602,
      "longitude": 1.1338136
   },
   "2626": {
      "postcode": "NP10",
      "latitude": 51.5780227,
      "longitude": -3.0477786
   },
   "2627": {
      "postcode": "BH20",
      "latitude": 50.6871662,
      "longitude": -2.1485991
   },
   "2628": {
      "postcode": "BN6",
      "latitude": 50.931059,
      "longitude": -0.1555778
   },
   "2629": {
      "postcode": "B49",
      "latitude": 52.2178973,
      "longitude": -1.866774
   },
   "2630": {
      "postcode": "PA35",
      "latitude": 56.4047653,
      "longitude": -5.2274523
   },
   "2631": {
      "postcode": "BT81",
      "latitude": 54.6958267,
      "longitude": -7.6113132
   },
   "2632": {
      "postcode": "DL8",
      "latitude": 54.2928606,
      "longitude": -1.7868123
   },
   "2633": {
      "postcode": "L37",
      "latitude": 53.5571245,
      "longitude": -3.0636989
   },
   "2634": {
      "postcode": "S26",
      "latitude": 53.3526108,
      "longitude": -1.2915543
   },
   "2635": {
      "postcode": "LL13",
      "latitude": 53.0344913,
      "longitude": -2.9590322
   },
   "2636": {
      "postcode": "SY20",
      "latitude": 52.6147887,
      "longitude": -3.81884
   },
   "2637": {
      "postcode": "BR6",
      "latitude": 51.3652346,
      "longitude": 0.0912592
   },
   "2638": {
      "postcode": "E18",
      "latitude": 51.5927827,
      "longitude": 0.0249672
   },
   "2639": {
      "postcode": "LA20",
      "latitude": 54.2942675,
      "longitude": -3.2062137
   },
   "2640": {
      "postcode": "EX9",
      "latitude": 50.6394596,
      "longitude": -3.3240203
   },
   "2641": {
      "postcode": "EN1",
      "latitude": 51.6542098,
      "longitude": -0.0680823
   },
   "2642": {
      "postcode": "BN41",
      "latitude": 50.8414939,
      "longitude": -0.2174858
   },
   "2643": {
      "postcode": "B26",
      "latitude": 52.4615675,
      "longitude": -1.7887486
   },
   "2644": {
      "postcode": "GU29",
      "latitude": 50.9846389,
      "longitude": -0.7477247
   },
   "2645": {
      "postcode": "SO50",
      "latitude": 50.9693035,
      "longitude": -1.3404267
   },
   "2646": {
      "postcode": "NE24",
      "latitude": 55.1218343,
      "longitude": -1.5228902
   },
   "2647": {
      "postcode": "MK7",
      "latitude": 52.0190228,
      "longitude": -0.6913147
   },
   "2648": {
      "postcode": "CH66",
      "latitude": 53.2774095,
      "longitude": -2.9364965
   },
   "2649": {
      "postcode": "NW26",
      "latitude": 51.5340605,
      "longitude": -0.2481317
   },
   "2650": {
      "postcode": "GL56",
      "latitude": 51.9895485,
      "longitude": -1.7034227
   },
   "2651": {
      "postcode": "NG21",
      "latitude": 53.1424089,
      "longitude": -1.1039866
   },
   "2652": {
      "postcode": "TQ13",
      "latitude": 50.5945854,
      "longitude": -3.7176059
   },
   "2653": {
      "postcode": "BL5",
      "latitude": 53.5481623,
      "longitude": -2.5154623
   },
   "2654": {
      "postcode": "PA34",
      "latitude": 56.3937657,
      "longitude": -5.4870915
   },
   "2655": {
      "postcode": "IV53",
      "latitude": 57.3443757,
      "longitude": -5.554202
   },
   "2656": {
      "postcode": "LS7",
      "latitude": 53.8205711,
      "longitude": -1.5396576
   },
   "2657": {
      "postcode": "SN5",
      "latitude": 51.5668285,
      "longitude": -1.8397596
   },
   "2658": {
      "postcode": "SK17",
      "latitude": 53.2445366,
      "longitude": -1.8815141
   },
   "2659": {
      "postcode": "NR31",
      "latitude": 52.5749904,
      "longitude": 1.708835
   },
   "2660": {
      "postcode": "AL6",
      "latitude": 51.832147,
      "longitude": -0.1998286
   },
   "2661": {
      "postcode": "TN40",
      "latitude": 50.8450642,
      "longitude": 0.4824058
   },
   "2662": {
      "postcode": "BA16",
      "latitude": 51.124174,
      "longitude": -2.7457829
   },
   "2663": {
      "postcode": "ST1",
      "latitude": 53.0273418,
      "longitude": -2.1730317
   },
   "2664": {
      "postcode": "SS7",
      "latitude": 51.5622938,
      "longitude": 0.5777041
   },
   "2665": {
      "postcode": "TN33",
      "latitude": 50.9114028,
      "longitude": 0.4750454
   },
   "2666": {
      "postcode": "SS13",
      "latitude": 51.5750029,
      "longitude": 0.5109302
   },
   "2667": {
      "postcode": "NE44",
      "latitude": 54.9428778,
      "longitude": -1.9779213
   },
   "2668": {
      "postcode": "WF7",
      "latitude": 53.66632,
      "longitude": -1.3528117
   },
   "2669": {
      "postcode": "NW4",
      "latitude": 51.5873411,
      "longitude": -0.2243033
   },
   "2670": {
      "postcode": "SY3",
      "latitude": 52.6989988,
      "longitude": -2.7732128
   },
   "2671": {
      "postcode": "LE13",
      "latitude": 52.7660063,
      "longitude": -0.8870665
   },
   "2672": {
      "postcode": "EH38",
      "latitude": 55.7773566,
      "longitude": -2.9528897
   },
   "2673": {
      "postcode": "CO11",
      "latitude": 51.942012,
      "longitude": 1.0767083
   },
   "2674": {
      "postcode": "G22",
      "latitude": 55.8907103,
      "longitude": -4.2520148
   },
   "2675": {
      "postcode": "ML4",
      "latitude": 55.8183531,
      "longitude": -4.0213658
   },
   "2676": {
      "postcode": "BN52",
      "latitude": 50.8344048,
      "longitude": -0.1680463
   },
   "2677": {
      "postcode": "PE31",
      "latitude": 52.8818331,
      "longitude": 0.5723975
   },
   "2678": {
      "postcode": "PR2",
      "latitude": 53.7782025,
      "longitude": -2.7072842
   },
   "2679": {
      "postcode": "TN19",
      "latitude": 51.0027867,
      "longitude": 0.4058702
   },
   "2680": {
      "postcode": "M7",
      "latitude": 53.5054293,
      "longitude": -2.2625151
   },
   "2681": {
      "postcode": "LA9",
      "latitude": 54.3254145,
      "longitude": -2.743368
   },
   "2682": {
      "postcode": "L35",
      "latitude": 53.4151247,
      "longitude": -2.7828814
   },
   "2683": {
      "postcode": "MK40",
      "latitude": 52.1378368,
      "longitude": -0.4764099
   },
   "2684": {
      "postcode": "PA2",
      "latitude": 55.8287846,
      "longitude": -4.4346865
   },
   "2685": {
      "postcode": "HG2",
      "latitude": 53.9855934,
      "longitude": -1.5286679
   },
   "2686": {
      "postcode": "N6",
      "latitude": 51.5731718,
      "longitude": -0.1460635
   },
   "2687": {
      "postcode": "WN4",
      "latitude": 53.4936763,
      "longitude": -2.6443803
   },
   "2688": {
      "postcode": "TA24",
      "latitude": 51.1819504,
      "longitude": -3.5105467
   },
   "2689": {
      "postcode": "WD4",
      "latitude": 51.7059771,
      "longitude": -0.4564485
   },
   "2690": {
      "postcode": "NG15",
      "latitude": 53.0446485,
      "longitude": -1.2037243
   },
   "2691": {
      "postcode": "PO21",
      "latitude": 50.7850953,
      "longitude": -0.6986558
   },
   "2692": {
      "postcode": "TA12",
      "latitude": 50.974841,
      "longitude": -2.7730116
   },
   "2693": {
      "postcode": "TW4",
      "latitude": 51.4654671,
      "longitude": -0.3879716
   },
   "2694": {
      "postcode": "CA19",
      "latitude": 54.3869014,
      "longitude": -3.3839245
   },
   "2695": {
      "postcode": "NE71",
      "latitude": 55.5554219,
      "longitude": -2.044318
   },
   "2696": {
      "postcode": "BB2",
      "latitude": 53.7416815,
      "longitude": -2.5018572
   },
   "2697": {
      "postcode": "LS5",
      "latitude": 53.8209598,
      "longitude": -1.6072846
   },
   "2698": {
      "postcode": "GL11",
      "latitude": 51.6901084,
      "longitude": -2.357213
   },
   "2699": {
      "postcode": "EH41",
      "latitude": 55.9483721,
      "longitude": -2.7767292
   },
   "2700": {
      "postcode": "IV42",
      "latitude": 57.2390335,
      "longitude": -5.8330149
   },
   "2701": {
      "postcode": "BS39",
      "latitude": 51.3282866,
      "longitude": -2.5335653
   },
   "2702": {
      "postcode": "BT24",
      "latitude": 54.4173126,
      "longitude": -5.8716837
   },
   "2703": {
      "postcode": "LS15",
      "latitude": 53.8055008,
      "longitude": -1.4450938
   },
   "2704": {
      "postcode": "M29",
      "latitude": 53.5084109,
      "longitude": -2.4581696
   },
   "2705": {
      "postcode": "CF63",
      "latitude": 51.4122519,
      "longitude": -3.2572808
   },
   "2706": {
      "postcode": "S20",
      "latitude": 53.3345997,
      "longitude": -1.3520598
   },
   "2707": {
      "postcode": "PA62",
      "latitude": 56.3592566,
      "longitude": -5.8515195
   },
   "2708": {
      "postcode": "SE12",
      "latitude": 51.4446759,
      "longitude": 0.0200181
   },
   "2709": {
      "postcode": "KA19",
      "latitude": 55.3460742,
      "longitude": -4.6679946
   },
   "2710": {
      "postcode": "CA24",
      "latitude": 54.5154439,
      "longitude": -3.5435607
   },
   "2711": {
      "postcode": "CF11",
      "latitude": 51.4724155,
      "longitude": -3.1922157
   },
   "2712": {
      "postcode": "EH9",
      "latitude": 55.9330122,
      "longitude": -3.1853241
   },
   "2713": {
      "postcode": "NE49",
      "latitude": 54.9672806,
      "longitude": -2.4607532
   },
   "2714": {
      "postcode": "NE15",
      "latitude": 54.9846077,
      "longitude": -1.7244563
   },
   "2715": {
      "postcode": "B96",
      "latitude": 52.2517197,
      "longitude": -1.9602473
   },
   "2716": {
      "postcode": "PE27",
      "latitude": 52.3315399,
      "longitude": -0.0713853
   },
   "2717": {
      "postcode": "BT92",
      "latitude": 54.2245245,
      "longitude": -7.4675641
   },
   "2718": {
      "postcode": "LL25",
      "latitude": 53.0537805,
      "longitude": -3.8808964
   },
   "2719": {
      "postcode": "TQ2",
      "latitude": 50.4764111,
      "longitude": -3.546236
   },
   "2720": {
      "postcode": "LD7",
      "latitude": 52.351601,
      "longitude": -3.0907216
   },
   "2721": {
      "postcode": "PE6",
      "latitude": 52.6575152,
      "longitude": -0.2526423
   },
   "2722": {
      "postcode": "SE25",
      "latitude": 51.3977747,
      "longitude": -0.0767868
   },
   "2723": {
      "postcode": "EX8",
      "latitude": 50.6297299,
      "longitude": -3.4017306
   },
   "2724": {
      "postcode": "LL31",
      "latitude": 53.2903448,
      "longitude": -3.8104002
   },
   "2725": {
      "postcode": "GL15",
      "latitude": 51.7369523,
      "longitude": -2.551235
   },
   "2726": {
      "postcode": "PH25",
      "latitude": 57.2615339,
      "longitude": -3.6477254
   },
   "2727": {
      "postcode": "RM12",
      "latitude": 51.5529171,
      "longitude": 0.207438
   },
   "2728": {
      "postcode": "DY12",
      "latitude": 52.3864341,
      "longitude": -2.3329518
   },
   "2729": {
      "postcode": "DN6",
      "latitude": 53.597914,
      "longitude": -1.1785488
   },
   "2730": {
      "postcode": "TR21",
      "latitude": 49.9189845,
      "longitude": -6.2986255
   },
   "2731": {
      "postcode": "S81",
      "latitude": 53.3386575,
      "longitude": -1.1239571
   },
   "2732": {
      "postcode": "BA1",
      "latitude": 51.3927912,
      "longitude": -2.3611374
   },
   "2733": {
      "postcode": "NG9",
      "latitude": 52.9258889,
      "longitude": -1.2382797
   },
   "2734": {
      "postcode": "CO13",
      "latitude": 51.8389206,
      "longitude": 1.2367597
   },
   "2735": {
      "postcode": "TS12",
      "latitude": 54.5628683,
      "longitude": -0.9670708
   },
   "2736": {
      "postcode": "BR3",
      "latitude": 51.4045675,
      "longitude": -0.0305611
   },
   "2737": {
      "postcode": "LA17",
      "latitude": 54.2395573,
      "longitude": -3.1758678
   },
   "2738": {
      "postcode": "CV11",
      "latitude": 52.5198747,
      "longitude": -1.453464
   },
   "2739": {
      "postcode": "RG1",
      "latitude": 51.4512045,
      "longitude": -0.9696684
   },
   "2740": {
      "postcode": "HR5",
      "latitude": 52.196357,
      "longitude": -3.0367417
   },
   "2741": {
      "postcode": "LE10",
      "latitude": 52.5368832,
      "longitude": -1.3698567
   },
   "2742": {
      "postcode": "BS25",
      "latitude": 51.3199339,
      "longitude": -2.820467
   },
   "2743": {
      "postcode": "PH21",
      "latitude": 57.0898405,
      "longitude": -4.0197579
   },
   "2744": {
      "postcode": "GL51",
      "latitude": 51.8990355,
      "longitude": -2.110465
   },
   "2745": {
      "postcode": "TN6",
      "latitude": 51.0522368,
      "longitude": 0.1754135
   },
   "2746": {
      "postcode": "CH6",
      "latitude": 53.2492592,
      "longitude": -3.1443958
   },
   "2747": {
      "postcode": "SG19",
      "latitude": 52.1394738,
      "longitude": -0.2395501
   },
   "2748": {
      "postcode": "S98",
      "latitude": 53.4041516,
      "longitude": -1.4311097
   },
   "2749": {
      "postcode": "CA1",
      "latitude": 54.8858561,
      "longitude": -2.9124405
   },
   "2750": {
      "postcode": "B14",
      "latitude": 52.4173564,
      "longitude": -1.8898132
   },
   "2751": {
      "postcode": "CM23",
      "latitude": 51.872518,
      "longitude": 0.1583719
   },
   "2752": {
      "postcode": "NE30",
      "latitude": 55.0213845,
      "longitude": -1.4386877
   },
   "2753": {
      "postcode": "CT2",
      "latitude": 51.2936699,
      "longitude": 1.0799396
   },
   "2754": {
      "postcode": "HU1",
      "latitude": 53.7428033,
      "longitude": -0.3379367
   },
   "2755": {
      "postcode": "CT3",
      "latitude": 51.2768265,
      "longitude": 1.2113391
   },
   "2756": {
      "postcode": "BT54",
      "latitude": 55.2043862,
      "longitude": -6.2565641
   },
   "2757": {
      "postcode": "SN2",
      "latitude": 51.5777424,
      "longitude": -1.7829919
   },
   "2758": {
      "postcode": "DA1",
      "latitude": 51.4480982,
      "longitude": 0.209464
   },
   "2759": {
      "postcode": "SA32",
      "latitude": 51.8878923,
      "longitude": -4.1696166
   },
   "2760": {
      "postcode": "AB42",
      "latitude": 57.5010193,
      "longitude": -1.8922218
   },
   "2761": {
      "postcode": "NR20",
      "latitude": 52.7232899,
      "longitude": 0.9810289
   },
   "2762": {
      "postcode": "EX32",
      "latitude": 51.0718819,
      "longitude": -4.020197
   },
   "2763": {
      "postcode": "LD5",
      "latitude": 52.1264542,
      "longitude": -3.6225562
   },
   "2764": {
      "postcode": "ML1",
      "latitude": 55.7990265,
      "longitude": -3.9750481
   },
   "2765": {
      "postcode": "N7",
      "latitude": 51.5534256,
      "longitude": -0.118356
   },
   "2766": {
      "postcode": "EH53",
      "latitude": 55.8947721,
      "longitude": -3.4727519
   },
   "2767": {
      "postcode": "PH8",
      "latitude": 56.5623822,
      "longitude": -3.599212
   },
   "2768": {
      "postcode": "HS6",
      "latitude": 57.601656,
      "longitude": -7.3011311
   },
   "2769": {
      "postcode": "NR1",
      "latitude": 52.6266317,
      "longitude": 1.3068176
   },
   "2770": {
      "postcode": "LL19",
      "latitude": 53.3311383,
      "longitude": -3.4106208
   },
   "2771": {
      "postcode": "IG4",
      "latitude": 51.5800576,
      "longitude": 0.0512052
   },
   "2772": {
      "postcode": "EN8",
      "latitude": 51.6992728,
      "longitude": -0.0338619
   },
   "2773": {
      "postcode": "IV11",
      "latitude": 57.677224,
      "longitude": -4.0390588
   },
   "2774": {
      "postcode": "BT15",
      "latitude": 54.6234399,
      "longitude": -5.9320317
   },
   "2775": {
      "postcode": "LL34",
      "latitude": 53.2705627,
      "longitude": -3.9145251
   },
   "2776": {
      "postcode": "CF61",
      "latitude": 51.4083951,
      "longitude": -3.4812082
   },
   "2777": {
      "postcode": "L75",
      "latitude": 53.4377607,
      "longitude": -2.9862275
   },
   "2778": {
      "postcode": "BT2",
      "latitude": 54.5937744,
      "longitude": -5.9306374
   },
   "2779": {
      "postcode": "AB15",
      "latitude": 57.1375445,
      "longitude": -2.16861
   },
   "2780": {
      "postcode": "YO10",
      "latitude": 53.9504564,
      "longitude": -1.0575048
   },
   "2781": {
      "postcode": "OL3",
      "latitude": 53.5535469,
      "longitude": -2.0115057
   },
   "2782": {
      "postcode": "IV4",
      "latitude": 57.4508097,
      "longitude": -4.5241263
   },
   "2783": {
      "postcode": "BD4",
      "latitude": 53.7763907,
      "longitude": -1.7186609
   },
   "2784": {
      "postcode": "TN5",
      "latitude": 51.0590304,
      "longitude": 0.3650914
   },
   "2785": {
      "postcode": "DE73",
      "latitude": 52.8472038,
      "longitude": -1.438215
   },
   "2786": {
      "postcode": "SA17",
      "latitude": 51.7568602,
      "longitude": -4.2854106
   },
   "2787": {
      "postcode": "BS23",
      "latitude": 51.3430959,
      "longitude": -2.9718955
   },
   "2788": {
      "postcode": "S75",
      "latitude": 53.5627102,
      "longitude": -1.5215009
   },
   "2789": {
      "postcode": "OX25",
      "latitude": 51.9002711,
      "longitude": -1.2130366
   },
   "2790": {
      "postcode": "SO20",
      "latitude": 51.1166333,
      "longitude": -1.5167063
   },
   "2791": {
      "postcode": "SL3",
      "latitude": 51.4987413,
      "longitude": -0.5516413
   },
   "2792": {
      "postcode": "BH24",
      "latitude": 50.8432801,
      "longitude": -1.7884673
   },
   "2793": {
      "postcode": "OX4",
      "latitude": 51.7312035,
      "longitude": -1.2173945
   },
   "2794": {
      "postcode": "UB10",
      "latitude": 51.5493776,
      "longitude": -0.4519988
   },
   "2795": {
      "postcode": "TN28",
      "latitude": 50.9828035,
      "longitude": 0.950948
   },
   "2796": {
      "postcode": "GU18",
      "latitude": 51.3483009,
      "longitude": -0.6692481
   },
   "2797": {
      "postcode": "WN3",
      "latitude": 53.5288084,
      "longitude": -2.6459714
   },
   "2798": {
      "postcode": "AB55",
      "latitude": 57.5245238,
      "longitude": -2.9896438
   },
   "2799": {
      "postcode": "PA49",
      "latitude": 55.7822695,
      "longitude": -6.3948363
   },
   "2800": {
      "postcode": "EH8",
      "latitude": 55.9487133,
      "longitude": -3.1641837
   },
   "2801": {
      "postcode": "BT57",
      "latitude": 55.2034959,
      "longitude": -6.5177372
   },
   "2802": {
      "postcode": "IV23",
      "latitude": 57.7675158,
      "longitude": -5.0094949
   },
   "2803": {
      "postcode": "BL78",
      "latitude": 53.5641145,
      "longitude": -2.410661
   },
   "2804": {
      "postcode": "FK21",
      "latitude": 56.4659591,
      "longitude": -4.3209044
   },
   "2805": {
      "postcode": "ME11",
      "latitude": 51.4129865,
      "longitude": 0.7466942
   },
   "2806": {
      "postcode": "RH17",
      "latitude": 51.0223327,
      "longitude": -0.1194834
   },
   "2807": {
      "postcode": "B65",
      "latitude": 52.4836373,
      "longitude": -2.0437814
   },
   "2808": {
      "postcode": "EH91",
      "latitude": 55.9249779,
      "longitude": -3.2986006
   },
   "2809": {
      "postcode": "CA11",
      "latitude": 54.6644988,
      "longitude": -2.7842759
   },
   "2810": {
      "postcode": "CO4",
      "latitude": 51.9091409,
      "longitude": 0.9196829
   },
   "2811": {
      "postcode": "W1W",
      "latitude": 51.5192066,
      "longitude": -0.1409008
   },
   "2812": {
      "postcode": "BT8",
      "latitude": 54.540416,
      "longitude": -5.9063825
   },
   "2813": {
      "postcode": "DN12",
      "latitude": 53.4826131,
      "longitude": -1.2241725
   },
   "2814": {
      "postcode": "TQ6",
      "latitude": 50.3471274,
      "longitude": -3.5905841
   },
   "2815": {
      "postcode": "DG5",
      "latitude": 54.9212114,
      "longitude": -3.8110519
   },
   "2816": {
      "postcode": "SO40",
      "latitude": 50.9129875,
      "longitude": -1.5038949
   },
   "2817": {
      "postcode": "IP12",
      "latitude": 52.0933236,
      "longitude": 1.3698157
   },
   "2818": {
      "postcode": "M12",
      "latitude": 53.4643203,
      "longitude": -2.202117
   },
   "2819": {
      "postcode": "EH46",
      "latitude": 55.7404828,
      "longitude": -3.3566775
   },
   "2820": {
      "postcode": "BD18",
      "latitude": 53.8304494,
      "longitude": -1.7768469
   },
   "2821": {
      "postcode": "SO32",
      "latitude": 50.9493624,
      "longitude": -1.2031646
   },
   "2822": {
      "postcode": "LS14",
      "latitude": 53.8275342,
      "longitude": -1.4585135
   },
   "2823": {
      "postcode": "LL26",
      "latitude": 53.1395034,
      "longitude": -3.7857607
   },
   "2824": {
      "postcode": "DD9",
      "latitude": 56.7482711,
      "longitude": -2.6683631
   },
   "2825": {
      "postcode": "LA16",
      "latitude": 54.187593,
      "longitude": -3.2030115
   },
   "2826": {
      "postcode": "DL9",
      "latitude": 54.3754022,
      "longitude": -1.7075078
   },
   "2827": {
      "postcode": "B76",
      "latitude": 52.5434894,
      "longitude": -1.7825543
   },
   "2828": {
      "postcode": "IP25",
      "latitude": 52.5865973,
      "longitude": 0.8391576
   },
   "2829": {
      "postcode": "PR0",
      "latitude": 53.7588071,
      "longitude": -2.6839072
   },
   "2830": {
      "postcode": "BD11",
      "latitude": 53.752252,
      "longitude": -1.6757083
   },
   "2831": {
      "postcode": "IP18",
      "latitude": 52.3304822,
      "longitude": 1.6707696
   },
   "2832": {
      "postcode": "B23",
      "latitude": 52.5285384,
      "longitude": -1.8553035
   },
   "2833": {
      "postcode": "BT68",
      "latitude": 54.3649415,
      "longitude": -6.84812
   },
   "2834": {
      "postcode": "IP6",
      "latitude": 52.1326541,
      "longitude": 1.110843
   },
   "2835": {
      "postcode": "BB8",
      "latitude": 53.8580089,
      "longitude": -2.1635237
   },
   "2836": {
      "postcode": "LA2",
      "latitude": 54.0661829,
      "longitude": -2.6713879
   },
   "2837": {
      "postcode": "DA15",
      "latitude": 51.4414641,
      "longitude": 0.0981804
   },
   "2838": {
      "postcode": "BN15",
      "latitude": 50.8303272,
      "longitude": -0.3257841
   },
   "2839": {
      "postcode": "NE62",
      "latitude": 55.1614961,
      "longitude": -1.593519
   },
   "2840": {
      "postcode": "M17",
      "latitude": 53.4680132,
      "longitude": -2.3205539
   },
   "2841": {
      "postcode": "BT38",
      "latitude": 54.7289788,
      "longitude": -5.8008313
   },
   "2842": {
      "postcode": "HU13",
      "latitude": 53.725529,
      "longitude": -0.4386443
   },
   "2843": {
      "postcode": "HD2",
      "latitude": 53.668833,
      "longitude": -1.7767268
   },
   "2844": {
      "postcode": "TD2",
      "latitude": 55.7309958,
      "longitude": -2.7543989
   },
   "2845": {
      "postcode": "TS22",
      "latitude": 54.6250233,
      "longitude": -1.320442
   },
   "2846": {
      "postcode": "G15",
      "latitude": 55.9092917,
      "longitude": -4.3662176
   },
   "2847": {
      "postcode": "SA34",
      "latitude": 51.8521658,
      "longitude": -4.6189874
   },
   "2848": {
      "postcode": "KA24",
      "latitude": 55.7094358,
      "longitude": -4.7157711
   },
   "2849": {
      "postcode": "CH48",
      "latitude": 53.3701791,
      "longitude": -3.1693842
   },
   "2850": {
      "postcode": "BN11",
      "latitude": 50.8135706,
      "longitude": -0.3771568
   },
   "2851": {
      "postcode": "TN21",
      "latitude": 50.9581826,
      "longitude": 0.2628954
   },
   "2852": {
      "postcode": "CV13",
      "latitude": 52.6173527,
      "longitude": -1.413049
   },
   "2853": {
      "postcode": "WR2",
      "latitude": 52.1883104,
      "longitude": -2.2484883
   },
   "2854": {
      "postcode": "RH4",
      "latitude": 51.2299509,
      "longitude": -0.3347519
   },
   "2855": {
      "postcode": "SW18",
      "latitude": 51.4512533,
      "longitude": -0.191462
   },
   "2856": {
      "postcode": "WR15",
      "latitude": 52.3054003,
      "longitude": -2.5688982
   },
   "2857": {
      "postcode": "G12",
      "latitude": 55.8805484,
      "longitude": -4.3006568
   },
   "2858": {
      "postcode": "M43",
      "latitude": 53.4836761,
      "longitude": -2.1491575
   },
   "2859": {
      "postcode": "EH7",
      "latitude": 55.9602104,
      "longitude": -3.1643887
   },
   "2860": {
      "postcode": "TF12",
      "latitude": 52.6120064,
      "longitude": -2.4817746
   },
   "2861": {
      "postcode": "WD3",
      "latitude": 51.6466313,
      "longitude": -0.4824803
   },
   "2862": {
      "postcode": "B92",
      "latitude": 52.4372881,
      "longitude": -1.7739201
   },
   "2863": {
      "postcode": "FK19",
      "latitude": 56.3715398,
      "longitude": -4.3126836
   },
   "2864": {
      "postcode": "NR14",
      "latitude": 52.5626096,
      "longitude": 1.3761424
   },
   "2865": {
      "postcode": "FK15",
      "latitude": 56.2030762,
      "longitude": -3.950473
   },
   "2866": {
      "postcode": "WV8",
      "latitude": 52.6259036,
      "longitude": -2.1876739
   },
   "2867": {
      "postcode": "SA18",
      "latitude": 51.7977271,
      "longitude": -3.9609347
   },
   "2868": {
      "postcode": "GL54",
      "latitude": 51.8965086,
      "longitude": -1.8457414
   },
   "2869": {
      "postcode": "DN8",
      "latitude": 53.6152815,
      "longitude": -0.9552368
   },
   "2870": {
      "postcode": "WR13",
      "latitude": 52.0930845,
      "longitude": -2.3428588
   },
   "2871": {
      "postcode": "EH25",
      "latitude": 55.8616321,
      "longitude": -3.1749932
   },
   "2872": {
      "postcode": "SY1",
      "latitude": 52.7226132,
      "longitude": -2.7405434
   },
   "2873": {
      "postcode": "DY10",
      "latitude": 52.386159,
      "longitude": -2.2238755
   },
   "2874": {
      "postcode": "TS28",
      "latitude": 54.7257395,
      "longitude": -1.3749668
   },
   "2875": {
      "postcode": "LL43",
      "latitude": 52.774527,
      "longitude": -4.0923764
   },
   "2876": {
      "postcode": "BN22",
      "latitude": 50.7896229,
      "longitude": 0.2838081
   },
   "2877": {
      "postcode": "GU8",
      "latitude": 51.1486935,
      "longitude": -0.6446799
   },
   "2878": {
      "postcode": "L40",
      "latitude": 53.6031134,
      "longitude": -2.8417029
   },
   "2879": {
      "postcode": "S5",
      "latitude": 53.4222438,
      "longitude": -1.4632305
   },
   "2880": {
      "postcode": "SA40",
      "latitude": 52.0842938,
      "longitude": -4.1755517
   },
   "2881": {
      "postcode": "SN99",
      "latitude": 51.5519943,
      "longitude": -1.7225477
   },
   "2882": {
      "postcode": "NE29",
      "latitude": 55.01176,
      "longitude": -1.4654419
   },
   "2883": {
      "postcode": "DH5",
      "latitude": 54.8232696,
      "longitude": -1.4551478
   },
   "2884": {
      "postcode": "G31",
      "latitude": 55.8566242,
      "longitude": -4.2081326
   },
   "2885": {
      "postcode": "L8",
      "latitude": 53.3898761,
      "longitude": -2.9636387
   },
   "2886": {
      "postcode": "SL60",
      "latitude": 51.518549,
      "longitude": -0.7147822
   },
   "2887": {
      "postcode": "WC1V",
      "latitude": 51.5180929,
      "longitude": -0.1165884
   },
   "2888": {
      "postcode": "TD14",
      "latitude": 55.8673888,
      "longitude": -2.1245054
   },
   "2889": {
      "postcode": "IV43",
      "latitude": 57.1555527,
      "longitude": -5.8106214
   },
   "2890": {
      "postcode": "SW95",
      "latitude": 51.4803984,
      "longitude": -0.1362742
   },
   "2891": {
      "postcode": "DE11",
      "latitude": 52.7727609,
      "longitude": -1.556556
   },
   "2892": {
      "postcode": "EH6",
      "latitude": 55.9725098,
      "longitude": -3.1753754
   },
   "2893": {
      "postcode": "NN5",
      "latitude": 52.2467249,
      "longitude": -0.9358726
   },
   "2894": {
      "postcode": "EC3V",
      "latitude": 51.5129745,
      "longitude": -0.0858623
   },
   "2895": {
      "postcode": "YO60",
      "latitude": 54.0861015,
      "longitude": -0.9389498
   },
   "2896": {
      "postcode": "TA10",
      "latitude": 51.0334527,
      "longitude": -2.8257148
   },
   "2897": {
      "postcode": "ME14",
      "latitude": 51.2787626,
      "longitude": 0.5435955
   },
   "2898": {
      "postcode": "YO24",
      "latitude": 53.945938,
      "longitude": -1.1169804
   },
   "2899": {
      "postcode": "SA67",
      "latitude": 51.783184,
      "longitude": -4.7328423
   },
   "2900": {
      "postcode": "LL39",
      "latitude": 52.7102009,
      "longitude": -4.0123647
   },
   "2901": {
      "postcode": "LU6",
      "latitude": 51.8780425,
      "longitude": -0.5377989
   },
   "2902": {
      "postcode": "DH7",
      "latitude": 54.7897219,
      "longitude": -1.6660103
   },
   "2903": {
      "postcode": "EH24",
      "latitude": 55.8496545,
      "longitude": -3.1370136
   },
   "2904": {
      "postcode": "SE1P",
      "latitude": 51.4927767,
      "longitude": -0.0801528
   },
   "2905": {
      "postcode": "TN34",
      "latitude": 50.8650015,
      "longitude": 0.5821191
   },
   "2906": {
      "postcode": "SS22",
      "latitude": 51.556979,
      "longitude": 0.7068231
   },
   "2907": {
      "postcode": "SA42",
      "latitude": 52.0154537,
      "longitude": -4.8524793
   },
   "2908": {
      "postcode": "PA20",
      "latitude": 55.8341544,
      "longitude": -5.0572403
   },
   "2909": {
      "postcode": "EH39",
      "latitude": 56.0470676,
      "longitude": -2.734215
   },
   "2910": {
      "postcode": "MK1",
      "latitude": 52.0055233,
      "longitude": -0.7243816
   },
   "2911": {
      "postcode": "FK18",
      "latitude": 56.3246007,
      "longitude": -4.3291315
   },
   "2912": {
      "postcode": "PE13",
      "latitude": 52.6700673,
      "longitude": 0.1371284
   },
   "2913": {
      "postcode": "TW1",
      "latitude": 51.4510989,
      "longitude": -0.3257026
   },
   "2914": {
      "postcode": "LE8",
      "latitude": 52.5550348,
      "longitude": -1.094569
   },
   "2915": {
      "postcode": "WF3",
      "latitude": 53.7239736,
      "longitude": -1.5253183
   },
   "2916": {
      "postcode": "NP26",
      "latitude": 51.5909077,
      "longitude": -2.7788809
   },
   "2917": {
      "postcode": "S99",
      "latitude": 53.404241,
      "longitude": -1.4310272
   },
   "2918": {
      "postcode": "B98",
      "latitude": 52.3022428,
      "longitude": -1.9130643
   },
   "2919": {
      "postcode": "PH4",
      "latitude": 56.2613859,
      "longitude": -3.7853249
   },
   "2920": {
      "postcode": "NE85",
      "latitude": 54.9319342,
      "longitude": -1.5848013
   },
   "2921": {
      "postcode": "PA47",
      "latitude": 55.6820071,
      "longitude": -6.5040794
   },
   "2922": {
      "postcode": "PA22",
      "latitude": 55.9714333,
      "longitude": -5.1344071
   },
   "2923": {
      "postcode": "L17",
      "latitude": 53.3775853,
      "longitude": -2.9406564
   },
   "2924": {
      "postcode": "TF2",
      "latitude": 52.7002332,
      "longitude": -2.4399297
   },
   "2925": {
      "postcode": "CR8",
      "latitude": 51.3319133,
      "longitude": -0.1138248
   },
   "2926": {
      "postcode": "EC3P",
      "latitude": 51.523986,
      "longitude": -0.1104578
   },
   "2927": {
      "postcode": "E9",
      "latitude": 51.5440387,
      "longitude": -0.0430441
   },
   "2928": {
      "postcode": "BH3",
      "latitude": 50.7365886,
      "longitude": -1.8833558
   },
   "2929": {
      "postcode": "YO62",
      "latitude": 54.2461752,
      "longitude": -0.9943394
   },
   "2930": {
      "postcode": "KW6",
      "latitude": 58.250139,
      "longitude": -3.4446253
   },
   "2931": {
      "postcode": "ST7",
      "latitude": 53.0885898,
      "longitude": -2.2685631
   },
   "2932": {
      "postcode": "WC1R",
      "latitude": 51.5196199,
      "longitude": -0.1158498
   },
   "2933": {
      "postcode": "SG5",
      "latitude": 51.9713173,
      "longitude": -0.2810918
   },
   "2934": {
      "postcode": "SY22",
      "latitude": 52.7568466,
      "longitude": -3.186804
   },
   "2935": {
      "postcode": "S72",
      "latitude": 53.5786497,
      "longitude": -1.3911586
   },
   "2936": {
      "postcode": "RM10",
      "latitude": 51.5448684,
      "longitude": 0.1578473
   },
   "2937": {
      "postcode": "CF38",
      "latitude": 51.5605507,
      "longitude": -3.3327717
   },
   "2938": {
      "postcode": "B67",
      "latitude": 52.485705,
      "longitude": -1.9787293
   },
   "2939": {
      "postcode": "HX1",
      "latitude": 53.7210243,
      "longitude": -1.8716182
   },
   "2940": {
      "postcode": "CB9",
      "latitude": 52.0833705,
      "longitude": 0.439697
   },
   "2941": {
      "postcode": "YO26",
      "latitude": 53.9757464,
      "longitude": -1.1783526
   },
   "2942": {
      "postcode": "HA3",
      "latitude": 51.5937695,
      "longitude": -0.3209409
   },
   "2943": {
      "postcode": "AB12",
      "latitude": 57.1020973,
      "longitude": -2.1129498
   },
   "2944": {
      "postcode": "BD97",
      "latitude": 53.8266825,
      "longitude": -1.7967244
   },
   "2945": {
      "postcode": "B9",
      "latitude": 52.4781837,
      "longitude": -1.8508904
   },
   "2946": {
      "postcode": "NR34",
      "latitude": 52.4387601,
      "longitude": 1.5835599
   },
   "2947": {
      "postcode": "WV5",
      "latitude": 52.5341081,
      "longitude": -2.2103369
   },
   "2948": {
      "postcode": "PL23",
      "latitude": 50.3374532,
      "longitude": -4.6368031
   },
   "2949": {
      "postcode": "TR12",
      "latitude": 50.042234,
      "longitude": -5.1794424
   },
   "2950": {
      "postcode": "S96",
      "latitude": 53.4023591,
      "longitude": -1.4250619
   },
   "2951": {
      "postcode": "TW12",
      "latitude": 51.4228861,
      "longitude": -0.3697391
   }
}