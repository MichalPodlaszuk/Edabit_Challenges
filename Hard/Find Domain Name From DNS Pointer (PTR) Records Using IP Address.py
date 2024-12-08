import socket


def get_domain_name(ip_address):
    hostname = socket.gethostbyaddr(ip_address)[0]
    return hostname


domain_name = get_domain_name('8.8.8.8')
print(domain_name)