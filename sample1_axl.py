# https://collabapilab.ciscolive.com/lab/pod4/soap_apis/axl_python

from axltoolkit import AxlToolkit

from credentials import user, password, ucm_ip, ucm_version, platform_user, platform_password

# Be sure to update the credentials.py file with your AXL User and Platform User credentials


axl = AxlToolkit(username=user, password=password, server_ip=ucm_ip, tls_verify=False, version=ucm_version)


# Example of using Thick AXL to retrieve User Info
# Replace this with a valid User ID from your UCM cluster:
userid = '1002'

result = axl.get_user(userid)

print(result)

userdata = result['return']['user']

print("Your name is " + userdata['firstName'])

userdata = {'userid':'1002', 'pin':'5555'}

result = axl.update_user(userdata)

print(result)


# Example of using thin AXL to retrieve User Info:

query = "select * from enduser where userid = '1002'"
result = axl.run_sql_query(query)

# print(result)


result = axl.list_phone(name='CSF%')
# print(result)

