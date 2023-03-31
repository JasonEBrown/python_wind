# Meteorological saffir-simpson wind scale to classify hurricanes. A Python program that will prompt the user 
# for wind speed, then display hurricane's intensity based upon saffir-simpson scale.

wind_speed = int(input("Enter the sustained mph wind speed, ex: '135': " ))

if wind_speed <= 73:
    print ("Sorry, that does not qualify as a hurricane.")

elif wind_speed <= 95:
    print ("This is classified as a Cat 1 hurricane.")

elif wind_speed <= 110:
    print ("This is classified as a Cat 2 hurricane.")

elif wind_speed <= 130:
    print ("This is classified as a Cat 3 hurricane.")

elif wind_speed <= 155:
    print ("This is classified as a Cat 4 hurricane.")

elif wind_speed <= float('inf'):
    print ("This is classified as a Cat 5 hurricane.")
