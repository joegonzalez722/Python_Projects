#This is a work in progress script that should automate selecting a vpn server from vpngate.net

#It should parse data from either the public or private list hosted by this website


#And should select a server, filtered by country, with the highest connection speed and lowest ping

#It should aim to have a ping < 10 ms, and Speed > 450 Mbps

#If the selected server times out, It should select the next best server, prioritizing a low ping (ms) and high connection speed (Mbps)

#If the server connected