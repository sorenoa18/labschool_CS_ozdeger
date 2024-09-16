#code is deeiigned to extract a pice of information from string 

#using two string functrions today: split() and replace ()

sunocoPrice = "Suncoco gas price: $3.39"
mirabitoPrice = "Mirabito gas price: $3.79"

#extract and isolate the prices
priceOfSunoco = sunocoPrice.split(" ")
priceOfMirabito = mirabitoPrice.split(" ")
print(priceOfSunoco[3])
print(priceOfMirabito[3])

#what kind of type of data are these 
print(type(priceOfSunoco[3]))
print(type(priceOfMirabito[3]))

