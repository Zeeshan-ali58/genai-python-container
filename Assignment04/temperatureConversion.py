def converTemperatureToFahrenheit(tempInCelcius):
    tempInFahrenheit = tempInCelcius * (9/5) + 32
    print(f"Temperature in Fahrenheit is {tempInFahrenheit}" )

def converTemperatureToCelcius(tempInFahrenheit):
    tempInCelciusReConvert = (tempInFahrenheit -32) * 5/9
    print(f"Temperature in Celcius is {tempInCelciusReConvert}" )

tempInCelciusIn = float(input("Enter temperature in Celcius: "))
converTemperatureToFahrenheit(tempInCelciusIn)

tempInFahrenheitIn = float(input("Enter temperature in Fahrenheit: "))
converTemperatureToCelcius(tempInFahrenheitIn)