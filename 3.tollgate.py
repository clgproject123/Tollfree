# Tollgate system

motorTypes = {
    1:{ 
     'Bike':50   
    },
    2:{ 
     'Car':100
    },
    3:{ 
     'Lorry':150   
    },
    4:{ 
     'Others':200
    }
}

def amountProcessing(amount,userAmount,vehicleType):
    if(amount == userAmount):
        print('Your amount is successfully paid happy journey')
    elif(amount < userAmount):
        print('Your amount is', amount, "only")
        print("Get the amount", userAmount - amount)
    else:
        print('Your amount is', amount)
        print(vehicleType,'tollfree amount is ', amount, ' you paid only', userAmount, 'now i need', amount - userAmount )


def VehicleType(motorTpyes):
     print('your tollfree will be:', list(motorTpyes.values())[0])
     userAmount = int(input('Enter the amount:'))
     amount = list(motorTpyes.values())[0]
     vehicleType = list(motorTpyes.keys())[0]
     amountProcessing(amount, userAmount, vehicleType)

def tollGate():
    print('Choose the vehicle type')
    vehicleType = int(input(' 1.Bike \n 2.car \n 3.lorry \n 4.other \n:'))

    if(vehicleType == 1):
         VehicleType(motorTypes[1])
    elif(vehicleType == 2):
         VehicleType(motorTypes[2])
    elif(vehicleType == 3):
         VehicleType(motorTypes[3])
    elif(vehicleType == 4):
         VehicleType(motorTypes[4])
    else:
         print('Please choose the correct option')

tollGate()
