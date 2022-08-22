
import ipaddress
ipn = ipaddress.ip_network("10.0.0.0/16")
print(ipn.with_prefixlen)
print(ipn.with_hostmask)
print(ipn.with_netmask)

