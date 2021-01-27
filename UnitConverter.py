import numpy as np
# ============================================================
# Defining my own functions here
# ============================================================

def dist_conv(amt,inp_unit,out_unit):
    meter=1.0
    feet=3.28084
    inches=39.3701
    miles=0.000621371
    if inp_unit=="feet":
        amt=amt/feet
    if inp_unit=="inch":
        amt=amt/inches
    if inp_unit=="mile":
        amt=amt/miles
    if out_unit=="feet":
        amt=amt*feet
    if out_unit=="inch":
        amt=amt*inches
    if out_unit=="mile":
        amt=amt*miles
    
    
def weight_conv(amt,inp_unit,out_unit):
    kilogram=1.0
    ounces=35.274
    pounds=2.20462
    if inp_unit=="ounce":
        amt=amt/ounces
    if inp_unit=="pound":
        amt=amt/pounds
    if out_unit=="ounce":
        amt=amt*ounces
    if out_unit=="pound":
        amt=amt*pounds

def temp_conv(amt,inp_unit,out_unit):
    celcius=(9/5)*amt+32
    fahrenheit=(amt-32)/1.8
    if out_unit=="fahrenheit":
        return fahrenheit
    if out_unit=="celcius":
        return celcius
    
def find_units(request):
    unit1=""
    unit2=""
    flag=0
    distance=[["eter"," m "],["eet","ft","oot"],["nch","in"],["mi","ile"]]
    dist=["meter","feet","inch","mile"]
    weight=[["ilogram","Kg","kg"],["unce","oz"],["lb","pound"]]
    wght=["kilogram","ounce","pound"]
    temperature=[["elcius"," C "],["ahrenheit"," F "]]
    temp=["celcius","fahrenheit"]
    for b in range(len(distance)-1):
        u=distance[b]
        for x in u:
            if request.find(x)!=-1 & flag==0:
                unit1=dist[b]
                flag=1
            if request.find(x)!=-1 & flag==1:
                unit2=dist[b]
                flag=2
    
    if flag!=2:
        for b in range(len(distance)-1):
        u=distance[b]
        for x in u:
            if request.find(x)!=-1 & flag==0:
                unit1=dist[b]
                flag=1
            if request.find(x)!=-1 & flag==1:
                unit2=dist[b]
                flag=2


# ============================================================
# Defining your own testing here
# ============================================================


