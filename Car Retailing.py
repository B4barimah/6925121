
"""
Created on Fri Feb 24 09:23:06 2023

@author: AGYEKUM KOFI BARIMAH
Index number:6925121
"""
#Available brands of cars and their prices in a car retail shop
cars={'Maserati':25000, 'Bugatti veyron':35000, 'Chevrolet camaro':20000, 
      'Mercedes Benz':50000, 'Peugeot':60000, 'Honda civic':15000,
      'Honda accord':15000, 'Range Rover':75000, 'Rolls Royce':95000,
      'Tesla':68000, 'Saturn':34000, 'Nissan altima':42000, 'Toyota vitz':15000,
      'Hyundai elantra':55000, 'Ford Mustang':45000, 'Volkswagen beetle':12000,
      'Land cruiser V16':80000, 'Highlander V16':78000, 'Mitsubishi':10000,
      'Lamborghini murcielago': 150000, 'Lamborghini aventidor':184000}
carName = input("Welcome to B4barimah car retails, enter your preferred choice of car:")
carPrice = cars[carName]
if carName in cars:
    print('This brand of car is available and its price is:{}'.format(carPrice))
   #https://github.com/users/B4barimah/emails/242519171/confirm_verification/24507290?via_launch_code_email=true 
    


