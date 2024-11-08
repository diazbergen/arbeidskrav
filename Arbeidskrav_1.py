"""Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.

Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km."""

"""" forsikring elbil""" 
FE = 5000

"""forsikring bensinbil"""
FB = 7500

""""Trafikkforsikringsavgift bil"""
T = 8.38*365

"""Kjørte KM pr. år"""
KM = 12000

"""Drifstofforbruk elbil"""
DE = (0.2*KM)*2

"""Drivstofforbruk bensinbil"""
DB = 1*KM

"""Bomavgift elbil"""
BE = 0.1*KM

"""Bomavgift bensinbil"""
BB = 0.3*KM

Kostnader_elbil=FE+T+DE+BE

Kostnader_bensinbil=FB+T+DB+BB

print("Årlige totalkostnader for bensinbil=", Kostnader_bensinbil, 
      "Minus årlige kostnader for elbil=", Kostnader_elbil,
      "Årlig kostnadsdifferanse=", Kostnader_bensinbil-Kostnader_elbil)