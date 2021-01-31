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
    return amt


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
    return amt

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
    sec_u=0
    distance=[["eter"," m "],["eet","ft","oot"],["nch","in"],["mi","ile"]]
    dist=["meter","feet","inch","mile"]
    weight=[["ilogram","Kg","kg"],["unce","oz"],["lb","pound"]]
    wght=["kilogram","ounce","pound"]
    temperature=[["elcius"," C "],["ahrenheit"," F "]]
    temp=["celcius","fahrenheit"]
    unit_type=""
    for b in range(len(distance)-1):
        u=distance[b]
        unit_type="distance"
        for x in u:

            if flag==1:
                sec_u=1
            if request.find(x)>-1 & flag==0:

                unit1=dist[b]
                flag=1
            if request.find(x)>-1 & sec_u==1:

                unit2=dist[b]
                sec_u=2
                flag=2

    if flag!=2:
        for b in range(len(weight)-1):
            u=weight[b]
            unit_type="weight"
            for x in u:

                if flag==1:
                    sec_u=1
                if request.find(x)>-1 & flag==0:

                    unit1=wght[b]
                    flag=1
                if request.find(x)>-1 & sec_u==1:

                    unit2=wght[b]
                    sec_u=2
                    flag=2

    if flag!=2:
        for b in range(len(temperature)-1):
            u=temperature[b]
            unit_type="temperature"
            for x in u:

                if flag==1:
                    sec_u=1
                if request.find(x)>-1 & flag==0:

                    unit1=temp[b]
                    flag=1
                if request.find(x)>-1 & sec_u==1:

                    unit2=temp[b]
                    sec_u=2
                    flag=2

    return [unit1,unit2,unit_type]

def myParser(txt):

    units=find_units(txt)
    input_u=units[0]
    output_u=units[1]
    un_type=units[2]
    myflag=0
    num1=0
    num2=0
    for i in range(len(txt)-1):
        if txt[i].isdigit() and myflag==0:

            num1=i
            myflag=1
        else:
            if txt[i].isdigit() and myflag==1:

                num2=i
    final_num=float(txt[num1:num2])
    des_out=0
    if un_type == "distance":
        des_out=dist_conv(final_num,input_u,output_u)
    if un_type == "weight":
        des_out=weight_conv(final_num,input_u,output_u)
    if un_type == "temperature":
        des_out=temp_conv(final_num,input_u,output_u)
    print(des_out,output_u)

# ============================================================
# Defining your own testing here
# ============================================================

user_txt="12 inches to mile"
myParser(user_txt)
