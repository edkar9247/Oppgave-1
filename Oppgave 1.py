# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 19:31:57 2025

@author: Edith
"""



#Oppgave 1#
#Sammenligning av årlige kostnadene ved elbil og bensinbil#


# Antall km/år
km_år = 10000  #kilometer per år

# Forsikringskostnader per år
elbil_forsikring = 5000
bensinbil_forsikring = 7500

# Trafikkforsikringsavgift er det samme for begge biler
trafikkavgift_dag = 8.38    #Trafikkforsikringsavgift per dag
trafikkavgift_år = trafikkavgift_dag * 365   #Trafikkforsikringsavgift per år

# Drivstoffbruk kostnader
# Elbil: 0,2 kWh/km * 2 kr/kWh
drivstoffkostnad_Elbil = km_år * 0.2 * 2.0
# Bensinbil: 1 kr/km
drivstoffkostnad_Bensinbil = km_år * 1.0

# Bomavgifter gjelder for hver bil
bomav_elbil = km_år * 0.1
bomav_bensinbil = km_år * 0.3

# Totale kostander årlig
Total_Elbil = elbil_forsikring + trafikkavgift_år + drivstoffkostnad_Elbil + bomav_elbil  #Årlige kostnader for elbil
Total_Bensinbil = bensinbil_forsikring + trafikkavgift_år + drivstoffkostnad_Bensinbil + bomav_bensinbil  #Årlige kostnader for bensinbil


#Årlige Kostnadsdifferanse mellom Bensinbil og Elbil
Differanse = Total_Bensinbil - Total_Elbil


