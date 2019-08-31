import pickle

ip = input('Type Server IP address: ')
port = input('Type server port number: ')
secret = input('Type api key: ')

ipport = 'http://'+ip+':'+port

pickle.dump([ipport,secret], open('config.p','wb'))

try:
	ip,secret, moose = pickle.load(open('config.p','rb'))
except ValueError: 
	time = input('another one')
	pickle.dump([time], open('config.p', 'wb'))
	time = pickle.load((open('config.p', 'rb')))
print(ip)




