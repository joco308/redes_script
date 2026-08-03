from ipaddress import IPv4Network, IPv4Interface
import ipaddress

dic = {}
switches = []
def ahksw(name,ip,msk):
    net = IPv4Network(f"{ip}{msk}", strict=False)
    with open("script.ahk","a") as ahk:
        ahk.write(f"::{name}::\n")
        ahk.write("Send, enable{Enter}\nSend, configure terminal{Enter}\nSend, interface vlan1{Enter}\n")
        ahk.write(f"Send, ip address {ip} {net.netmask}"+"{Enter}\nSend, no shutdown{Enter}\nSend, exit{Enter}\n")
        ahk.write(f"Send, ip default-gateway {next(net.hosts())}"+"{Enter}\nSend, do wr{Enter}\nreturn\n")

def ahkpc(name,ip,msk):
    net = IPv4Network(f"{ip}{msk}",strict=False)
    with open("script.ahk","a") as ahk:
        ahk.write(f"::{name}::\n")
        ahk.write(f"Send, {ip}"+"{Tab}\n")
        ahk.write(f"Send, {net.netmask}"+"{Tab}\n")
        ahk.write(f"Send, {next(net.hosts())}"+"{Tab}\nreturn\n")

def cmd_switches(name,ip,msk):
    net = IPv4Network(f"{ip}{msk}", strict=False)
    with open("CMD_SWITCH.txt", "a") as cmdS:
        cmdS.write(f"{name}\n")
        cmdS.write("enable\nconfigure terminal\ninterface vlan1\n")
        cmdS.write(f"ip address {ip} {net.netmask}\n")
        cmdS.write("no shutdown\nexit\n")
        cmdS.write(f"ip default-gateway {next(net.hosts())}\ndo wr\n\n")

def ordena(line, nline):
    try:
        name, ip,msk = line.split()
        net = IPv4Network(f"{ip}{msk}", strict=False)
        key = f"{net.network_address} {net.netmask}"
        if str(name).startswith("SW") or str(name).startswith("sw"):
            cmd_switches(name,ip,msk)
            ahksw(name,ip,msk)
        elif str(name).startswith("PC") or str(name).startswith("pc"):
            ahkpc(name,ip,msk)
            
        if not key in dic:
            dic[key] = []
        dic[key].append(f"{name} {ip} {net.netmask}")
    except Exception as e:
        print(f"Linea {nline} con formato erroneo...", e) 

def main():
    with open("ips.txt", "r") as ips:
        for nline, line in enumerate(ips, start= 1):
            ordena(line, nline )
    with open("segmentos2.txt", "w" ) as segm:
        for i in dic:
            ip, msk= i.split()
            prefix = ipaddress.IPv4Network(f"0.0.0.0/{msk}").prefixlen
            net = IPv4Network(f"{ip}/{prefix}")
            segm.write("DR: " + str(net.network_address)+"\n")
            segm.write("DB: " + str(net.broadcast_address)+"\n")
            segm.write("GW: " + str(next(net.hosts()))+"\n")
            segm.write("MASK: " + str(net.netmask)+"\n")
            for a in dic[i]:
                segm.write(a + "\n")
            segm.write("\n")
    with open("DRs.txt","w") as DRs:
        for i in dic.keys():
            DRs.write(f"ip route {i} s0/0\n")            
main()
