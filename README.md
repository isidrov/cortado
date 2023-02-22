# cortado

Based on AxlToolkit project from Paul Giralt

An easy way to automate Communications Manager (CUCM)

userdata = {'userid':'johnS', 'pin':'1234'}
result = axl.update_user(userdata)

axl = AxlToolkit(username=user, password=password, server_ip=ucm_ip, tls_verify=False, version=version)

Useful resources

https://collabapilab.ciscolive.com/lab/pod4/soap_apis/axl_python