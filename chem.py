######
#
# Script to look-up CAS numbers for generating chemical inventory.
#
######
import sys
import cirpy
import csv

PI_LastName  = "Hore"
PI_FirstName = "Michael"
PI_Bldg      = "KHS"
PI_Lab       = sys.argv[1]

# Open CSV file for append/write.
file = open('chem.csv', 'a', newline='')
writer = csv.writer(file)

# Fields that will change: 4 (chemical name), 7 (storage location), 8 (storage device), 9 (num. containers), 10 (amt), 11 (unit), 12 (CAS #)
default_row = ['', PI_LastName, PI_FirstName, 'Liquid', 'default', PI_Bldg, PI_Lab, 'default', 'default', 'default', 'default', 'default', 'default']

# Loop until end of universe.
while 1:
	chemical = input('Chemical: ')
	if chemical == 'quit':
		print("Quit!")
		file.close()
		quit()
	my_cas = cirpy.resolve(chemical, 'cas')
	i = 0
	for cas in my_cas:
		print(str(i) + ": " + cas + " - " + cirpy.resolve(cas, 'iupac_name'))
		i = i + 1

	cas_id = input('Choose CAS: ')
	cas = my_cas[int(cas_id)]

	stor_loc = input('Storage location: ')
	if stor_loc == '':
		stor_loc = default_row[7]

	stor_dev = input('Storage device: ')
	if stor_dev == '':
		stor_dev = default_row[8]

	num_con  = input('Num. containers: ')
	if num_con == '':
		num_con = '1'

	quant    = input('Amount: ')
	if quant == '':
		quant = default_row[10]

	unit     = input('Unit (mL, g, etc.): ')
	if unit == '':
		unit = default_row[11]

	# Update values in row.
	default_row[4]  = chemical
	default_row[7]  = stor_loc
	default_row[8]  = stor_dev
	default_row[9]  = num_con
	default_row[10] = quant
	default_row[11] = unit
	default_row[12] = cas

	# Write line.
	writer.writerow(default_row)
 
	print(' ')
