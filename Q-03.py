# Problem: Planetary Weight Calculator  

# Milestone #1: Mars Weight

# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars. 

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14. 

# x = 3.1415926
# rounded_x = round(x, 2) # rounds x to 2 decimal places 
# print(rounded_x) 

# # This would print out out 3.14


# Milestone #2: Adding in All Planets

# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# - Mercury: 37.6%

# - Venus: 88.9%

# - Mars: 37.8%

# - Jupiter: 236.0%

# - Saturn: 108.1%

# - Uranus: 81.5%

# - Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets. 

# Sample Run

# $ python planetaryweight.py

# Enter a weight on Earth: 120

# Enter a planet: Mars

# The equivalent weight on Mars: 45.36

# Sample Run

# $ python planetaryweight.py

# Enter a weight on Earth: 150

# Enter a planet: Jupiter

# The equivalent weight on Jupiter: 354.0


# Useful Syntax

# Python has an if statement, just like in Karel! This if statement passes if the value of x is the same as the value of y. x and y can be literal numbers, strings, variables, or constants.

# x = 42
# y = 42

# if x == y:
# print("x and y are equal!")


#? MILESTONE 01 PROBLEM :  MARS WEIGHT

# TAKE AN INPUT FROM THE USER TO ENTER WEIGHT.
# CONVERT THE WEIGHT ON EARTH INTO WEIGHT ON MARS.
# THE WEIGHT OF MARS IS 37.8% OF WEIGHT ON EARTH
# ROUND THE RESULT INTO 2 DECIMAL PLACES.

#* PSUEDO CODE :

# USER INPUT = FLOAT('ENTER A WEIGHT ON EARTH') 20
# WEIGHT ON MARS = 37.8%
# CALCULATION : 37.8 / 100 = 0.378
# CALCULATED VALUE = ROUND(USER WEIGHT * 0.378 , 2 )
# PRINT('THE EQUIVALENT WEIGHT ON MARS:' + CALCULATED VALUE)

#* CODE :

print('Milestone : 01')

Mars_weight = 0.378
# WE USED FLOAT FOR CONVERTING THE DEFAULT STRING VALUE INTO FLOAT VALUE.
weight_on_Earth = float(input('Enter a weight on Earth '))
weight_on_Mars = round(weight_on_Earth * Mars_weight , 2)
# F ALLOW US TO USE EXPRESSIONS INSIDE THE STRING.
print(f'The equivalent weight on Mars: {weight_on_Mars}')

print('\n')



#? MILESTONE 02 PROBLEM :

# CALCULATE THE WEIGHT ON DIIFERENT PLANETS IN OUR SOLAR SYSTEM.
# TO CALCULATE THAT, WE HAVE CONSTANT VALUES FOR EACH PLANET.
# STORE ALL THE CONSTANT VALUES FOR EACH VARIABLE.
# THE RESULT SHOULD BE ACCORDING TO THE USER PLANET CHOICE



#* PSEUDO CODE :

# - Mercury: 37.6%

# - Venus: 88.9%

# - Mars: 37.8%

# - Jupiter: 236.0%

# - Saturn: 108.1%

# - Uranus: 81.5%

# - Neptune: 114.0%

# PLANETS = THIER CONSTANT VALUES
# ENTER WEIGHT ON EARTH
# ENTER A PLANET
# IF PLANET == SPECIFIC PLANET:
    #  ROUND (EARTH WEIGHT VALUE * SPECIFIC PLANET VALUE , 2 )

#* CODE :

print('Milestone : 02')

# STORED VALUES IN EACH CONSTANT
Mercury , Venus , Mars , Jupiter , Saturn , Uranus , Neptune = 0.376 , 0.889 , 0.378 , 2.36 , 1.081 , 0.815 , 1.14

weight_on_Earth = float(input('Enter weight on Earth: '))

planet = input('Enter a Planet: ')

if planet == 'Mercury':
    weight_on_Mercury = round(weight_on_Earth * Mercury , 2 )
    print(f'The equivalent weight on Mercury: {weight_on_Mercury} ')

elif planet == 'Venus':
    weight_on_Venus = round(weight_on_Earth * Venus , 2 )
    print(f'The equivalent weight on Venus: {weight_on_Venus} ')

elif planet == 'Mars':
    weight_on_Mars = round(weight_on_Earth * Mars , 2 )
    print(f'The equivalent weight on Mars: {weight_on_Mars} ')


elif planet == 'Jupiter':
    weight_on_Jupiter = round(weight_on_Earth * Jupiter , 2 )
    print(f'The equivalent weight on Jupiter: {weight_on_Jupiter} ')


elif planet == 'Saturn':
    weight_on_Saturn = round(weight_on_Earth * Saturn , 2 )
    print(f'The equivalent weight on Saturn: {weight_on_Saturn} ')


elif planet == 'Uranus':
    weight_on_Uranus = round(weight_on_Earth * Uranus , 2 )
    print(f'The equivalent weight on Uranus: {weight_on_Uranus} ')


elif planet == 'Neptune':
    weight_on_Neptune = round(weight_on_Earth * Neptune , 2 )
    print(f'The equivalent weight on Neptune: {weight_on_Neptune} ')
else:
    print('Invalid Input')
