#!/usr/bin/env python3

# Program: .py

# Programmer: Aamir Alaud Din, PhD

# Date: ..2022

# Objective(s):
#	

import sys
import ib_ob_units as ibob
from colorama import Fore, Style

chain_size = int(input("Enter the number of repeat units (monomers) in the chain: "))

if chain_size == 1:
	print("Polymer must have at least two (2 x) repeat units, one (1 x) given.")
	print("The polymer generator can't work.")
	print("Exiting.")
	sys.exit()

print("Available charge methods are: ")
print("1. eem")
print("2. mmff94")
print("3. qtpie")
charge_method = input("Enter the charge method: ")

if charge_method == "eem":
	el_charge = [0.3381, -0.5686, -0.5368, 0.0887, 0.0887, 0.1966, 0.1966, 0.1967]
	er_charge = [0.4078, -0.6237, -0.6880, 0.0697, 0.1854, 0.1854, 0.1854, 0.2781]
	ib_ob_charge = [0.4487, -0.6090, -0.5454, 0.0819, 0.2079, 0.2079, 0.2080]
elif charge_method == "mmff94":	
	el_charge = [-4.8295, 0.9493, 1.6592, 0.7874, 0.7874, 0.2154, 0.2154, 0.2154]
	er_charge = [-2.2930, 1.0942, 1.6216, 0.1083, 0.1083, -0.2131, -0.2131, -0.2134]
	ib_ob_charge = [-2.8271, 1.3787, 1.2724, 0.1634, 0.1634, -0.0754, -0.0754]
elif charge_method == "qtpie":
	el_charge = [0.4078, -0.6237, -0.6880, 0.1286, 0.1286, 0.2156, 0.2156, 0.2156]
	er_charge = [0.4078, -0.6237, -0.6880, 0.1286, 0.1286, 0.2156, 0.2156, 0.2156]
	ib_ob_charge = [0.4487, -0.6090, -0.5454, 0.1501, 0.1501, 0.2027,0.2026,0.2027]

# x, y, and z-coordinates of extreme left unit
elx = [5.5376, 5.1022, 6.6642, 5.1638, 5.2617, 5.3465, 5.4812, 4.0000]
ely = [4.5543, 5.6022, 4.5543, 4.0795, 4.0000, 6.2225, 6.1312, 5.5750]
elz = [4.8506, 4.9355, 4.8506, 4.0326, 5.6520, 4.0545, 5.8289, 5.0160]

# x, y, and z-coordinates of extreme right unit
if chain_size % 2 == 0:
	erx = [5.5376, 5.1022, 6.6642, 5.2617, 5.3465, 5.4812, 4.0000, 7.0901]
	ery = [4.5543, 3.5064, 4.5543, 5.1086, 2.8861, 2.9774, 3.5336, 4.4656]
	erz = [4.8506, 4.7657, 4.8506, 4.0492, 5.6467, 3.8723, 4.6852, 5.7012]
elif chain_size % 2 == 1:
	erx = [5.5376, 5.1022, 6.6642, 5.2617, 5.3465, 5.4812, 4.0000, 7.0901]
	ery = [4.5543, 5.6022, 4.5543, 4.0000, 6.2225, 6.1312, 5.5750, 4.6430]
	erz = [4.8506, 4.9355, 4.8506, 5.6520, 4.0545, 5.8289, 5.0160, 4.0000]

# x, y, and z-coordinates of base monomer
obx = [5.5376, 5.1022, 6.6642, 5.2617, 5.3465, 5.4812, 4.0000]
oby = [4.5543, 5.6022, 4.5543, 4.0000, 6.2225, 6.1312, 5.5750]
obz = [4.8506, 4.9355, 4.8506, 5.6520, 4.0545, 5.8289, 5.0160]

# x, y, and z-coordinates of inverted base monomer
ibx = [5.5376, 5.1022, 6.6642, 5.2617, 5.3465, 5.4812, 4.0000]
iby = [4.5543, 3.5064, 4.5543, 5.1086, 2.8861, 2.9774, 3.5336]
ibz = [4.8506, 4.7657, 4.8506, 4.0492, 5.6467, 3.8723, 4.6852]

ibs, obs = ibob.ibs_obs(chain_size)



print("Calculating number of atoms in the polymer ... ", end="")
if chain_size == 2:
	n_atoms = 16
elif chain_size > 2:
	n_atoms = 16 + (chain_size - 2)*7
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Calculating number of bonds in the polymer ... ", end="")
if chain_size == 2:
	n_bonds = 14
elif chain_size > 2:
	n_bonds = 14 + (chain_size - 2)*6
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Allocating coordinates to atoms of monomers ... ", end="")
const_x_translate = 2.6266
monomer_translate = 0.0000
sysx = []
sysy = []
sysz = []
for i in range(ibs + obs):
	for j in range(len(ibx)):
		if i % 2 != 0:
			sysx.append(obx[j] + const_x_translate + monomer_translate)
			sysy.append(oby[j])
			sysz.append(obz[j])
		elif i % 2 == 0:
			sysx.append(ibx[j] + const_x_translate + monomer_translate)
			sysy.append(iby[j])
			sysz.append(ibz[j])
	monomer_translate += 2.6642

move_last_monomer = sysx[-5] - 4.0376

for i in range(len(elx)):
	sysx.append(elx[i])
	sysy.append(ely[i])
	sysz.append(elz[i])


for i in range(len(erx)):
	sysx.append(erx[i] + move_last_monomer)
	sysy.append(ery[i])
	sysz.append(erz[i])

print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Allocating bonds between bonded atoms ... ", end="")
bond_col_1 = []
bond_col_2 = []
col_1_atom_1 = 1
col_1_atom_2 = 2
for i in range(ibs + obs):
	bond_col_1.append(col_1_atom_1)
	bond_col_1.append(col_1_atom_1)
	bond_col_1.append(col_1_atom_1)
	bond_col_1.append(col_1_atom_2)
	bond_col_1.append(col_1_atom_2)
	bond_col_1.append(col_1_atom_2)
	bond_col_2.append(col_1_atom_2)
	bond_col_2.append(col_1_atom_2 + 1)
	bond_col_2.append(col_1_atom_2 + 2)
	bond_col_2.append(col_1_atom_2 + 3)
	bond_col_2.append(col_1_atom_2 + 4)
	bond_col_2.append(col_1_atom_2 + 5)
	col_1_atom_1 += 7
	col_1_atom_2 += 7

last_atom = bond_col_2[-1]

bond_col_1.append(last_atom + 1)
bond_col_1.append(last_atom + 1)
bond_col_1.append(last_atom + 1)
bond_col_1.append(last_atom + 1)
bond_col_1.append(last_atom + 2)
bond_col_1.append(last_atom + 2)
bond_col_1.append(last_atom + 2)
bond_col_1.append(last_atom + 9)
bond_col_1.append(last_atom + 9)
bond_col_1.append(last_atom + 9)
bond_col_1.append(last_atom + 10)
bond_col_1.append(last_atom + 10)
bond_col_1.append(last_atom + 10)
bond_col_1.append(last_atom + 11)

bond_col_2.append(last_atom + 2)
bond_col_2.append(last_atom + 3)
bond_col_2.append(last_atom + 4)
bond_col_2.append(last_atom + 5)
bond_col_2.append(last_atom + 6)
bond_col_2.append(last_atom + 7)
bond_col_2.append(last_atom + 8)
bond_col_2.append(last_atom + 10)
bond_col_2.append(last_atom + 11)
bond_col_2.append(last_atom + 12)
bond_col_2.append(last_atom + 13)
bond_col_2.append(last_atom + 14)
bond_col_2.append(last_atom + 15)
bond_col_2.append(last_atom + 16)
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Allocating bonds between monomers to generate polymer ... ", end="")
start_atom = 3
for i in range(chain_size - 1):
	bond_col_1.append(start_atom)
	start_atom += 7

start_atom = 1
last_atom = chain_size - 1
for i in range(chain_size - 1):
	if (i < last_atom - 1):
		start_atom += 7
	elif (i == last_atom - 1):
		start_atom += 8
	bond_col_2.append(start_atom)
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Defining Sybyl mol2 atom names and types and moltemplate atom types ... ", end="")
end_atom_symbols = ['SI', 'C ', 'O ', 'H ', 'H ', 'H ', 'H ', 'H ']
end_atom_types = ['Si ', 'C.3', 'O.3', 'H  ', 'H  ', 'H  ', 'H  ', 'H  ']
mid_atom_symbols = ['SI', 'C ', 'O ', 'H ', 'H ', 'H ', 'H ']
mid_atom_types = ['Si ', 'C.3', 'O.3', 'H  ', 'H  ', 'H  ', 'H  ']
lt_mid_atom_types = ['@atom:869', '@atom:871', '@atom:41', '@atom:870', '@atom:85', '@atom:85', '@atom:85']
lt_lend_atom_types = ['@atom:869', '@atom:871', '@atom:41', '@atom:870', '@atom:870', '@atom:85', '@atom:85',  '@atom:85']
lt_rend_atom_types = ['@atom:869', '@atom:871', '@atom:96', '@atom:870', '@atom:85', '@atom:85', '@atom:85', '@atom:97']
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Assigning atom names and types for Sybyl mol2 format ... ", end="")
atom_symbols = []
for i in range(ibs + obs):
	for j in mid_atom_symbols:
		atom_symbols.append(j)
for i in range(2):
	for j in end_atom_symbols:
		atom_symbols.append(j)

atom_types = []
for i in range(ibs + obs):
	for j in mid_atom_types:
		atom_types.append(j)
for i in range(2):
	for j in end_atom_types:
		atom_types.append(j)
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Assigning atom types for moltemplate format ... ", end="")
lt_atom_types = []
for i in range(ibs + obs):
	for j in lt_mid_atom_types:
		lt_atom_types.append(j)
for i in lt_lend_atom_types:
	lt_atom_types.append(i)
for i in lt_rend_atom_types:
	lt_atom_types.append(i)
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Assigning charges to atoms ... ", end="")
charges = []
for i in range(ibs + obs):
	for j in ib_ob_charge:
		charges.append(j)
for j in el_charge:
	charges.append(j)
for j in er_charge:
	charges.append(j)
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Writing polymer.mol2 ... ", end="")
f = open("polymer.mol2", "w")
f.writelines("@<TRIPOS>MOLECULE\n")
f.writelines("*****\n")
f.writelines(" {0} {1} 0 0 0\n".format(len(sysx), len(bond_col_2)))
f.writelines("SMALL\n")
f.writelines("GASTEIGER\n\n")
f.writelines("@<TRIPOS>ATOM\n")
for i in range(len(atom_types)):
	f.writelines("    {0:<4d} {1}    {2:<8.4f}    {3:<8.4f}    {4:<8.4f}    {5}    1    UNIL1    {6:<7.4f}\n".format(i + 1, atom_symbols[i], sysx[i], sysy[i], sysz[i], atom_types[i], charges[i]))
f.writelines("@<TRIPOS>BOND\n")
for i in range(len(bond_col_1)):
	f.writelines("    {0:4d}    {1:4d}    {2:4d}    1\n".format(i + 1, bond_col_1[i], bond_col_2[i]))
f.close()
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")

print("Writing polymer.lt ... ", end="")
f = open("polymer.lt", "w")
f.writelines("import \"oplsaa.lt\"")
f.writelines("\n\n")
f.writelines("silicone inherits OPLSAA {\n")
f.writelines("write(\"Data Atoms\") {\n")
for i in range(len(lt_atom_types)):
	f.writelines("    $atom:atom{0:<6d}    $mol:silicone    {1:<9s}    {2:<7.4f}  {3:10.4f}  {4:10.4f}  {5:10.4f}\n".format(i + 1, lt_atom_types[i], charges[i], sysx[i], sysy[i], sysz[i]))
f.writelines("\t}\n")
f.writelines("write(\"Data Bond List\") {\n")
for i in range(len(bond_col_1)):
	f.writelines("    $bond:bond{0:<6d}    $atom:atom{1:<6d}    $atom:atom{2:<6d}\n".format(i + 1, bond_col_1[i], bond_col_2[i]))
f.writelines("\t}\n")

f.writelines("} # end of silicone")
f.close()
print("[ " + Fore.GREEN + "DONE" + Style.RESET_ALL + " ]")
