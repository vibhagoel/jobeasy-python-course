# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

# type your code here
temperature_fahrenheit = input("enter temperature in Farenheit- ")
temp_far = float(temperature_fahrenheit)
temp_cel = (temp_far - 32)*5 / 9

result_temperature = int(temp_cel)

