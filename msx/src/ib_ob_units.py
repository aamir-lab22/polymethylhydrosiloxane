#!/usr/bin/env python3

# Program: .py

# Programmer: Aamir Alaud Din, PhD

# Date: ..2022

# Objective(s):
#	

def ibs_obs(num_units):
	if num_units % 2 == 0:
		ib_units = int((num_units - 2)/2)
		ob_units = int((num_units - 2)/2)
	elif num_units % 2 == 1:
		ib_units = int((num_units - 2)/2 + 0.5)
		ob_units = int((num_units - 2)/2 - 0.5)
	return ib_units, ob_units
