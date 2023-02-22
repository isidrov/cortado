# https://collabapilab.ciscolive.com/lab/pod4/soap_apis/axl_python

from axltoolkit import AxlToolkit

from credentials import user, password

import csv
import os

dir_project = os.path.dirname(os.path.abspath(__file__))
DataFiles = os.path.join(dir_project, 'DataFiles')

# Be sure to update the credentials.py file with your AXL User and Platform User credentials

# Put the IP address of your UCM Publisher
ucm_ip = '10.101.10.45'
version = '14.0'

axl = AxlToolkit(username=user, password=password, server_ip=ucm_ip, tls_verify=False, version=version)



with open(os.path.join(DataFiles ,'reset_pins.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            userdata = {'userid': f'{row[0]}', 'pin':f'{row[1]}'}
            result = axl.update_user(userdata)
            print(result)
            line_count += 1
    print(f'Processed {line_count} lines.')
