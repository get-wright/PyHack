#!/usr/bin/env python
import scapy.all as scapy
import argparse

#Input 
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="IP range (and subnet)")
    options = parser.parse_args()
    if not options.target:
        print('Input in the correct format: BASE_IP/SUBNET')
        options.target = input("Feed me IP and subnet: ")
    return options

#Scanning for hosts
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    ansed_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in ansed_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

#Print the discovered hosts with IP and the associated MAC
def prt_res(res_list):
    print("IP\t\t\tMAC Address\n-------------------------------------")
    for i in res_list:
        print(i["ip"] + "\t\t" + i["mac"])

print('\n')
print(" ██████   █████           █████              █████                             █████")
print("░░██████ ░░███           ░░███              ░░███                             ░░███")
print(" ░███░███ ░███   ██████  ███████             ░███████   █████ ████ ████████   ███████    ██████  ████████ ")
print(" ░███░░███░███  ███░░███░░░███░              ░███░░███ ░░███ ░███ ░░███░░███ ░░░███░    ███░░███░░███░░███")
print(" ░███ ░░██████ ░███████   ░███               ░███ ░███  ░███ ░███  ░███ ░███   ░███    ░███████  ░███ ░░░")
print(" ░███  ░░█████ ░███░░░    ░███ ███           ░███ ░███  ░███ ░███  ░███ ░███   ░███ ███░███░░░   ░███")
print(" █████  ░░█████░░██████   ░░█████  █████████ ████ █████ ░░████████ ████ █████  ░░█████ ░░██████  █████")
print("░░░░░    ░░░░░  ░░░░░░     ░░░░░  ░░░░░░░░░ ░░░░ ░░░░░   ░░░░░░░░ ░░░░ ░░░░░    ░░░░░   ░░░░░░  ░░░░░ ")
print('\n')

options = get_arguments()
scan_result = scan(options.target)
prt_res(scan_result)
