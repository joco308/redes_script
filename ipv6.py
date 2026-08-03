from ipaddress import IPv6Interface, IPv6Address, IPv6Network, IPv4Network

vlans = {}

def ips_Segmento(dic: dict, i_ip: list):
    name, ip = i_ip
    # ojoooo
    if str(name).startswith("sw") or str(name).startswith("SW"):
        dic["sw"].append([name,"2001:db8:abcd:12::fe"])
        return
    # ojooooo
    print(f"{name}---{ip}")
    net = IPv6Network(ip, strict=False)
    if not net in dic:
        dic[net] = []
    dic[net].append([name, ip])

def bloque():
    bloks = {}
    cont_blocks = 1
    bloks[cont_blocks] = []
    with open("ips.txt", "r") as ips:
        for ip in ips:
            if ip != "\n":
                bloks[cont_blocks].append(ip.split())
            else:
                cont_blocks+=1
                bloks[cont_blocks] = []
    return bloks


def segmentos(block: list):
    vlans = {}
    vlans["sw"] = []
    for i in block:
        ips_Segmento(vlans,i)
    return vlans

def make_comands(dic: dict):# aca paso loas vlans de 1 bloque entero
    vlans = len(dic)
    comand = ""
    for k, v in dic.items():
        for name, ip in v:
            ipv6 = IPv6Interface(ip).ip
            if str(name).startswith("PC") or str(name).startswith("pc"):
                comand+=f"::{name}::\nSend, {ipv6}"+"{Tab}\n"+f"Send, {k.prefixlen}"+"{Tab}\n"+"Send, {Tab}\n"+f"Send, {k.network_address + 1}"+"{Tab}\nreturn\n"
            if str(name).startswith("SW") or str(name).startswith("sw"):
                comand+=f"::{name}::\nSend, enable"+"{Enter}\nSend, conf t{Enter}\n"
                for i in range(1,vlans):
                    comand+=f"Send, vlan {i}"+"{Enter}\n"
                comand+="return\n"
    with open("script_ipv6.ahk","a") as ahk:
        ahk.write(comand)

def make_secmentos(dic: dict):
    comand = ""
    for k, v in dic.items():
        if k == "sw":
            continue
        comand+=f"DR: {k.network_address}\nH1: {k.network_address + 1}\n"
        for name, ip in v:
            comand+=f"{name} {ip}\n"
        comand+="------------------\n\n"
    with open("segmentos_ipv6.txt", "w" ) as segm:
        segm.write(comand)
            





blocks = bloque()
vlans_g = {}
for k, v in blocks.items():
    print(f"{k} = {v}")
    print("######################################")
    vlans_g[k] = segmentos(v)

for k, v in vlans_g.items():
    print(f"{k}, {v}")
    print("-------------------")
    make_comands(v)
    make_secmentos(v)
