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
    if inp_unit=="inches":
        amt=amt/inches
    if inp_unit=="miles":
        amt=amt/miles
    if out_unit=="feet":
        amt=amt*feet
    if out_unit=="inches":
        amt=amt*inches
    if out_unit=="miles":
        amt=amt*miles
    return amt


def weight_conv(amt,inp_unit,out_unit):
    kilogram=1.0
    ounces=35.274
    pounds=2.20462
    if inp_unit=="ounces":
        amt=amt/ounces
    if inp_unit=="pounds":
        amt=amt/pounds
    if out_unit=="ounces":
        amt=amt*ounces
    if out_unit=="pounds":
        amt=amt*pounds
    return amt

def temp_conv(amt,inp_unit,out_unit):
    fahrenheit=(9/5)*amt+32
    celcius=(amt-32)/1.8
    if out_unit=="fahrenheit":
        return fahrenheit
    if out_unit=="celcius":
        return celcius

def find_units(request):
    unit1=""
    unit2=""
    unit_type=""
    flag=0
    signal=0
    hold=9223372036854775807
    hold2=0
    distance=[["eter"," m "],["eet","ft","oot"],["nch","in"],["mi","ile"]]
    dist=["meters","feet","inches","miles"]
    weight=[["ilogram","Kg","kg"],["unce","oz"],["lb","pound"]]
    wght=["kilograms","ounces","pounds"]
    temperature=[["elcius"," C "],["ahrenheit"," F "]]
    temp=["celcius","fahrenheit"]
    unit_type=""
    for b in range(len(distance)):
        u=distance[b]

        for x in u:
            if -1<request.find(x)<hold:
                hold=request.find(x)
                unit1=dist[b]

        for y in u:
            if request.find(y)>hold2:
                hold2=request.find(y)
                unit_type="distance"
                unit2=dist[b]

    for b in range(len(weight)):
        u=weight[b]

        for x in u:
            for x in u:
                if -1<request.find(x)<hold:
                    hold=request.find(x)
                    unit1=wght[b]

            for y in u:
                if request.find(y)>hold2:
                    hold2=request.find(y)
                    unit_type="weight"
                    unit2=wght[b]

    for b in range(len(temperature)):
        u=temperature[b]

        for x in u:
            for x in u:
                if -1<request.find(x)<hold:
                    hold=request.find(x)
                    unit1=temp[b]

            for y in u:
                if request.find(y)>hold2:
                    hold2=request.find(y)
                    unit_type="temperature"
                    unit2=temp[b]

    return [unit1,unit2,unit_type]

def myParser(txt):

    units=find_units(txt)
    input_u=units[0]
    output_u=units[1]
    un_type=units[2]
    myflag=0
    num1=0
    num2=0
    for i in range(len(txt)):
        if txt[i].isdigit() and myflag==0:
            num1=i
            myflag=1
        if txt[i].isdigit() and myflag==1:
                num2=i
    final_num=float(txt[num1:num2+1])
    des_out=0
    if un_type == "distance":
        des_out=dist_conv(final_num,input_u,output_u)
    if un_type == "weight":
        des_out=weight_conv(final_num,input_u,output_u)
    if un_type == "temperature":
        des_out=temp_conv(final_num,input_u,output_u)
    if (input_u is output_u):
        return "ERROR: You have entered incorrect units"
    else:
        return (str(round(des_out,1))+" "+output_u)
