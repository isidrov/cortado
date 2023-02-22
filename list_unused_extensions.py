# https://collabapilab.ciscolive.com/lab/pod4/soap_apis/axl_python

from axltoolkit import AxlToolkit

from credentials import ucm_ip, ucm_version, user, password

import csv
import os

import pprint

# Be sure to update the credentials.py file with your AXL User and Platform User credentials

# Obtain directory paths

dir_project = os.path.dirname(os.path.abspath(__file__))
DataFiles = os.path.join(dir_project, 'inputDataFiles')

# Create AxlToolkit object

axl = AxlToolkit(username=user, password=password, server_ip=ucm_ip, tls_verify=False, version=ucm_version)

# Query for unassigned DNs

query = """
SELECT n.dnorpattern, rp.name , n.description
FROM numplan n
LEFT OUTER JOIN devicenumplanmap m ON m.fkdevice = n.pkid
LEFT OUTER JOIN routepartition rp ON rp.pkid = n.fkroutepartition
WHERE m.fkdevice IS NULL
AND n.tkpatternusage = '2'
AND n.iscallable = 't'"""

# run query

result = axl.run_sql_query(query)

# Print results

pretty_print_1 = pprint.pprint(result['rows'])