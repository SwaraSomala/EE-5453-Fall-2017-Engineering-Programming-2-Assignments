#1 foot= 0.305 meter
#1 meter =3.281 foot
def get_valid_unit(input1,input2): #function definition for checking valid units
    if input1=='m'or 'ft' and input2=='m' or 'ft':
        print('Convert from unit:',input1) 
        print('Convert to unit:',input2)
    else:
        print('Enter a valid unit (m for meters and ft for feet)')
def get_validnumber(num): #function definition for checking valid integer number
 if (type(num)==int):
  print('ok')
 else:
  print("Enter a valid integer number")
def convert(number,from_unit,to_unit):
 if(from_unit=='m' and to_unit=='ft'):
   print("The value of ",number,"m in ft is",number*3.281,'ft')
 elif(from_unit=='ft' and to_unit=='m'):
   print("The value of ",number,"ft in m is",number*0.305,'m')
 else:
   print('Please check the units or the value of the number')

unit1=input('Convert from units (enter m for meter and ft for feet)') #user defined from unit input
unit2=input('Convert to units(enter m for meter and ft for feet)') #user defined to unit input
get_valid_unit(unit1,unit2)     #checks if the units are valid
number=int(input('Enter a valid integer number')) #user defined number input
get_validnumber(number)
convert(number,unit1,unit2) #function call to conver from meters to feet and vice-versa


