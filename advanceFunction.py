def meter_to_km (meter,cm):
    km = meter / 1000 + meter / 10000
    return km

def mm_to_km (mm,cm=2345): #default value of this parameter should be changed with the passing value
    km = mm / 100000 + cm / 10000
    return km

print(meter_to_km(3490,32458))
print(mm_to_km(3490,32458))  #if there is no passing value then default value should be the parameter 
