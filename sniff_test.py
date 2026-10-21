from scapy.all import sniff

print("Listening for 10 packets...")
sniff(count=10, prn=lambda packet: print(packet.summary()))
print("Done!")