# Building a smart thermostat alert system
# if the device status is "active" add temperature > 35 warn " hight temp alert"
# else "temperature normal"
# if device is off "device is offline"





device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")    
else:
    print("Device is offline")