import os

print("#" * 60)

ip_ou_host = input('Digite o Ip ou Host a ser verificado: ')

print("_" * 60)

os.system('ping -n 6 {}'.format(ip_ou_host))

print("_" * 60)
