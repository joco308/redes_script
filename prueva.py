from ipaddress import IPv4Interface, IPv6Network


def analizar_ipv4(ip_cadena: str) -> dict:
    try:
        iface = IPv4Interface(ip_cadena)
        net = iface.network
        return {
            "ip": str(iface.ip),
            "mascara": str(iface.netmask),
            "prefijo": f"/{net.prefixlen}",
            "direccion_red": str(net.network_address),
            "segmento_cidr": str(net),
            "gateway": str(net.network_address + 1),
            "ultima_ip": str(net.broadcast_address - 1),
            "broadcast": str(net.broadcast_address),
            
        }
    except ValueError as e:
        raise ValueError(f"IP o formato de máscara inválido: '{ip_cadena}'") from e



# Prueba de uso:
datos = analizar_ipv4("10.0.4.123/12")
for clave, valor in datos.items():
    print(f"{clave:15}: {valor}")
print("-------------------------------------------------------------------------")

from ipaddress import IPv6Interface, IPv6Address

# Entrada en formato IPv6/Prefijo
ip_str = "2001:db8:abcd:0012::fe/64"

# 1. Crear el objeto interfaz
iface = IPv6Interface(ip_str)


# 2. Extraer el objeto de red (IPv6Network)
net = IPv6Network(ip_str,strict=False)

# 3. Cálculo eficiente de datos del segmento
direccion_red = net.network_address
prefijo = net.prefixlen

# Primera IP asignable (Gateway por convención)
gateway = direccion_red + 1

# Última IP del segmento (La última dirección global del bloque)
# Nota: net[-1] u obtener la última IP sumando el total de hosts - 1
ultima_ip = net.network_address + (net.num_addresses - 1)

print(f"IP ingresada:       {iface.ip}")
print(f"Prefijo:            /{prefijo}")
print(f"Dirección de Red:   {direccion_red}")
print(f"Segmento / CIDR:    {net}")
print(f"Puerta de Enlace:   {gateway}")
print(f"Última IP del bloc: {ultima_ip}")
print(f"Total direcciones:  {net.num_addresses}")