#from ipaddress import IPv4Address, IPv4Network
IPv4Network =
classA = IPv4Network(("0.0.0.0", "127.255.255.255"))
classB = IPv4Network(("128.0.0.0", "191.255.255.255"))
classC = IPv4Network(("192.0.0.0", "223.255.255.255"))
classD = IPv4Network(("224.0.0.0", "239.255.255.255"))
classE = IPv4Network(("240.0.0.0", "255.255.255.255"))

ip = input()
ip = IPv4Address(ip)

if ip in classA:
  print("A")
elif ip in classB:
  print("B")
elif ip in classC:
  print("C")
elif ip in classD:
  print("D")
elif ip in classE:
  print("E")
else:
  print("False")
