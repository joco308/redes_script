::SW1_::
Send, enable{Enter}
Send, conf t{Enter}
Send, vlan 1{Enter}
Send, vlan 2{Enter}
Send, vlan 3{Enter}
Send, vlan 4{Enter}
Send, vlan 5{Enter}
Send, vlan 6{Enter}
Send, vlan 7{Enter}
Send, vlan 8{Enter}
Send, int f0/1{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 1{Enter}
Send, exit{Enter}
Send, int f0/2{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 2{Enter}
Send, exit{Enter}
Send, int f0/3{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 3{Enter}
Send, exit{Enter}
Send, int f0/4{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 4{Enter}
Send, exit{Enter}
return
::SW2::
Send, enable{Enter}
Send, conf t{Enter}
Send, vlan 1{Enter}
Send, vlan 2{Enter}
Send, vlan 3{Enter}
Send, vlan 4{Enter}
Send, vlan 5{Enter}
Send, vlan 6{Enter}
Send, vlan 7{Enter}
Send, vlan 8{Enter}
Send, int f0/1{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 5{Enter}
Send, exit{Enter}
Send, int f0/2{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 5{Enter}
Send, exit{Enter}
Send, int f0/3{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 6{Enter}
Send, exit{Enter}
Send, int f0/4{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 6{Enter}
Send, exit{Enter}
return
::SW3::
Send, enable{Enter}
Send, conf t{Enter}
Send, vlan 1{Enter}
Send, vlan 2{Enter}
Send, vlan 3{Enter}
Send, vlan 4{Enter}
Send, vlan 5{Enter}
Send, vlan 6{Enter}
Send, vlan 7{Enter}
Send, vlan 8{Enter}
Send, int f0/1{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 4{Enter}
Send, exit{Enter}
Send, int f0/2{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 3{Enter}
Send, exit{Enter}
Send, int f0/3{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 2{Enter}
Send, exit{Enter}
Send, int f0/4{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 1{Enter}
Send, exit{Enter}
return
::SW4_::
Send, enable{Enter}
Send, conf t{Enter}
Send, vlan 1{Enter}
Send, vlan 2{Enter}
Send, vlan 3{Enter}
Send, vlan 4{Enter}
Send, vlan 5{Enter}
Send, vlan 6{Enter}
Send, vlan 7{Enter}
Send, vlan 8{Enter}
Send, int f0/1{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 7{Enter}
Send, exit{Enter}
Send, int f0/2{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 8{Enter}
Send, exit{Enter}
Send, int f0/3{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 7{Enter}
Send, exit{Enter}
Send, int f0/4{Enter}
Send, switchport mode access{Enter}
Send, switchport access vlan 8{Enter}
Send, exit{Enter}
return
::PC1::
Send, 2001:59:abcd:1234:1::10{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:1::1{Tab}
return
::PC12::
Send, 2001:59:abcd:1234:1::20{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:1::1{Tab}
return
::PC2::
Send, 2001:59:abcd:1234:2::10{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:2::1{Tab}
return
::PC11::
Send, 2001:59:abcd:1234:2::20{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:2::1{Tab}
return
::PC3::
Send, 2001:59:abcd:1234:3::10{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:3::1{Tab}
return
::PC10::
Send, 2001:59:abcd:1234:3::20{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:3::1{Tab}
return
::PC4::
Send, 2001:59:abcd:1234:4::10{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:4::1{Tab}
return
::PC9::
Send, 2001:59:abcd:1234:4::20{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:4::1{Tab}
return
::PC5::
Send, 2001:59:abcd:1234:5::10{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:5::1{Tab}
return
::PC6::
Send, 2001:59:abcd:1234:5::20{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:5::1{Tab}
return
::PC7::
Send, 2001:59:abcd:1234:6::10{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:6::1{Tab}
return
::PC8::
Send, 2001:59:abcd:1234:6::20{Tab}
Send, 80{Tab}
Send, {Tab}
Send, 2001:59:abcd:1234:6::1{Tab}
return
::PC13::
Send, 2002:59:59::10{Tab}
Send, 48{Tab}
Send, {Tab}
Send, 2002:59:59::1{Tab}
return
::PC15::
Send, 2002:59:59::20{Tab}
Send, 48{Tab}
Send, {Tab}
Send, 2002:59:59::1{Tab}
return
::PC14::
Send, 2003:59:59::10{Tab}
Send, 48{Tab}
Send, {Tab}
Send, 2003:59:59::1{Tab}
return
::PC16::
Send, 2003:59:59::20{Tab}
Send, 48{Tab}
Send, {Tab}
Send, 2003:59:59::1{Tab}
return
::R1::
Send, enable{Enter}
Send, conf t{Enter}
Send, hostname R1{Enter}
Send, ipv6 unicast-routing{Enter}
Send, interface GigabitEthernet0/0{Enter}
Send, no ip address{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/0.1{Enter}
Send, encapsulation dot1Q 1{Enter}
Send, ipv6 address 2001:59:abcd:1234:1::1/80{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/0.2{Enter}
Send, encapsulation dot1Q 2{Enter}
Send, ipv6 address 2001:59:abcd:1234:2::1/80{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/0.3{Enter}
Send, encapsulation dot1Q 3{Enter}
Send, ipv6 address 2001:59:abcd:1234:3::1/80{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/0.4{Enter}
Send, encapsulation dot1Q 4{Enter}
Send, ipv6 address 2001:59:abcd:1234:4::1/80{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/0.5{Enter}
Send, encapsulation dot1Q 5{Enter}
Send, ipv6 address 2001:59:abcd:1234:5::1/80{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/0.6{Enter}
Send, encapsulation dot1Q 6{Enter}
Send, ipv6 address 2001:59:abcd:1234:6::1/80{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/1{Enter}
Send, no ip address{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/1.7{Enter}
Send, encapsulation dot1Q 7{Enter}
Send, ipv6 address 2002:59:59::1/48{Enter}
Send, exit{Enter}
Send, interface GigabitEthernet0/1.8{Enter}
Send, encapsulation dot1Q 8{Enter}
Send, ipv6 address 2003:59:59::1/48{Enter}
Send, exit{Enter}
return
