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

def make_interfaces_whit_velans(pcs: list, vlans: list):
    comand = ""
    n_int = 1
    pcSwitch
    for name, ip in pcs:
        net = IPv6Network(ip, strict=False)
        vlan = vlans.index(net)
        comand+=f"Send, int f0/{n_int}"+"{Enter}\n"+"Send, switchport mode access{Enter}\n"+f"Send, switchport access vlan {vlan}"+"{Enter}\n"+"Send, exit{Enter}\n"
        n_int+=1
    return comand
        

def make_comands(dic: dict, pcSwitch: dict):# aca paso loas vlans de 1 bloque entero
    vlans = len(dic)
    n_vlans = list(dic.keys())
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
                pcs = pcSwitch[name]
                comand+=make_interfaces_whit_velans(pcs, n_vlans)
                comand+="Send, int f0/24{Enter}\nSend, switchport mode trunk{Enter}\nSend, exit{Enter}\nSend, int f0/23{Enter}\nSend, switchport mode trunk{Enter}\nSend, exit{Enter}\nSend, int g0/1{Enter}\nSend, switch mode trunk{Enter}\nSend, exit{Enter}\n"
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
            
def pc_switch(block: list, switches: dict):
    actual_switch = ""
    for name, ip in block:
        if str(name).startswith("sw") or str(name).startswith("SW"):
            switches[name] = []
            actual_switch = name
        else:
            switches[actual_switch].append([name, ip])
        
def contSubBlockInBlock(blocks: dict, g_vlans: dict):
    switch_act = ""
    blocks_with_subBlocks = {}
    for k, v in blocks.items():
        n_vlans = list(g_vlans[k].keys())
        blocks_with_subBlocks[k] = {}
        for name, ip in v:
            if name.endswith("_"):
                blocks_with_subBlocks[k][name] = {}
                switch_act = name
            #ojoooo
            if name.startswith("SW") or name.startswith("sw"):
                continue
            # ojooo
            net = IPv6Network(ip, strict=False)
            vlan = n_vlans.index(net)
            if not vlan in list(blocks_with_subBlocks[k][switch_act].keys()):
                blocks_with_subBlocks[k][switch_act][vlan] = f"{net.network_address + 1}/{net.prefixlen}"    
    return blocks_with_subBlocks


def make_comand_ruter(blocks_with_subBlocks: dict):
    comand = ""
    for k,v in blocks_with_subBlocks.items():
        comand+=f"::R{k}::\n"
        comand+="Send, enable{Enter}\nSend, conf t{Enter}\n"+f"Send, hostname R{k}"+"{Enter}\nSend, ipv6 unicast-routing{Enter}\n"
        cont = 0
        for key, value in v.items():
            comand+=f"Send, interface GigabitEthernet0/{cont}"+"{Enter}\nSend, no ip address{Enter}\nSend, no shutdown{Enter}\nSend, exit{Enter}\n"
            for kk, vv in value.items():
                comand+=f"Send, interface GigabitEthernet0/{cont}.{kk}"+"{Enter}\n"+f"Send, encapsulation dot1Q {kk}"+"{Enter}\n"+f"Send, ipv6 address {vv}"+"{Enter}\nSend, exit{Enter}\n"
            cont+=1
        comand+="return\n"
    with open("script_ipv6.ahk","a") as ahk:
        ahk.write(comand)



blocks = bloque()
pcSwitch = {}
vlans_g = {}
for k, v in blocks.items():
    print(f"{k} = {v}")
    print("######################################")
    vlans_g[k] = segmentos(v)
    pc_switch(v,pcSwitch)
    
for k, v in pcSwitch.items():
    print(f"{k} = {v}")
    print("||||||||||||||||||||||||||||||||||||")

for k, v in vlans_g.items():
    print(f"{k}, {v}")
    print("-------------------")
    make_comands(v,pcSwitch)
    make_secmentos(v)

print("+++++++++++++++++++++++++++")

subBlocks = contSubBlockInBlock(blocks, vlans_g)
for k, v in subBlocks.items():
    print(f"{k} : ",end="  ")
    for key,value in v.items():
        print(f"{key} : {value}")

make_comand_ruter(subBlocks)