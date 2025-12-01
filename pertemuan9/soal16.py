# 1. buatlah sebuah fungsi bersama celcius_ke_ferenheit yang menerima satu argumen : suhu dalam celcius. fungsi ini harus mengembalikan suhu yang di konversi ke farenheit
    #print(celcius_ke_fahrenheit (0))      # output: 32.0
    #print(celcius_ke_fahrenheit(100))      # output: 212.0
def celcius_ke_fahrenheit(celcius):
    fahrenheitn = (celcius *1.8) + 32
    return fahrenheitn

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))
