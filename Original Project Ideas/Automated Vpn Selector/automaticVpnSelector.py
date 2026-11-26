# This is a work in progress script that should automate selecting a vpn server from vpngate.net
from turtledemo.clock import display_date_time

# Part 1

# This script will parse data from either the public or private list hosted by this website

# Part 2

# It will select a server, filtered by country after prompting for user input (i.e. United States = US or USA, Japan = JPN or JP)

country_names = ["US", "USA", "JP", "JPN"]

print("What country do you want to connect to? (use 2 to 3 letter ISO compatible country codes)")

while True:
    country = input("__ ").strip().upper()

    # with the highest connection speed and lowest ping
    # It should aim to have a ping < 10 ms, and a Speed > 450 Mbps

    # If the selected server times out, It should select the next best server
    # (high speed, low ping)

# If the server connects
# verify that it passes region restrictions by testing connection to foreign website in selected region (i.e. if JPN, then biccamera.com)

# if region restriction passes, and the site can be accessed
# print('You're connected to x server with (ping, speed)')

# elif server connects, but fails to pass region restrictions

# try next_best_server until region restricted website can be reached without error

# When trying other servers, do not re-use the failed servers
# If run out of servers, try secondary vpn list
