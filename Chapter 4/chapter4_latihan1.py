import math
tarifawal = 200000
tariflanjutan = 10000
awalrental = 6.00
akhirrental = 23.50
durasirental = math.ceil(akhirrental-awalrental)
lamarentallanjutan = durasirental - 12
tarifrentallanjutan = lamarentallanjutan * tariflanjutan
totalharga = tarifawal + tarifrentallanjutan
print(totalharga)