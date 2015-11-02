import requests

server_url = '127.0.0.1'
server_port = '8888'
#server_port = '2222' # boatd
server      = 'http://' + server_url + ':' + server_port + '/'

def request(string):
    """ gets the data specified by the identifier """

    r = requests.get(server + string)
    if r.status_code == 404:
        print "ERROR 404 string not found"
    if r.status_code != 200:
        print "BAD STRING DYING"
        return -1
    assert r.status_code == 200
    return r
    
