::PC1::
Send, 150.59.5.10{Tab}
Send, 255.255.240.0{Tab}
Send, 150.59.0.1{Tab}
return
::PC2::
Send, 150.59.20.10{Tab}
Send, 255.255.240.0{Tab}
Send, 150.59.16.1{Tab}
return
::PC3::
Send, 150.59.10.10{Tab}
Send, 255.255.240.0{Tab}
Send, 150.59.0.1{Tab}
return
::PC4::
Send, 150.59.25.10{Tab}
Send, 255.255.240.0{Tab}
Send, 150.59.16.1{Tab}
return
::PC5::
Send, 150.59.15.10{Tab}
Send, 255.255.240.0{Tab}
Send, 150.59.0.1{Tab}
return
::PC6::
Send, 150.59.30.10{Tab}
Send, 255.255.240.0{Tab}
Send, 150.59.16.1{Tab}
return
::SW1::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 150.59.80.10 255.255.240.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 150.59.80.1{Enter}
Send, do wr{Enter}
return
::SW2::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 150.59.85.10 255.255.240.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 150.59.80.1{Enter}
Send, do wr{Enter}
return
::SW3::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 150.59.90.10 255.255.240.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 150.59.80.1{Enter}
Send, do wr{Enter}
return
::PC7::
Send, 70.59.40.10{Tab}
Send, 255.255.224.0{Tab}
Send, 70.59.32.1{Tab}
return
::PC8::
Send, 70.59.50.10{Tab}
Send, 255.255.224.0{Tab}
Send, 70.59.32.1{Tab}
return
::PC9::
Send, 70.59.60.10{Tab}
Send, 255.255.224.0{Tab}
Send, 70.59.32.1{Tab}
return
::PC10::
Send, 70.59.20.10{Tab}
Send, 255.255.224.0{Tab}
Send, 70.59.0.1{Tab}
return
::SW4::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 70.59.10.10 255.255.224.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 70.59.0.1{Enter}
Send, do wr{Enter}
return
::PC11::
Send, 60.59.250.10{Tab}
Send, 255.255.192.0{Tab}
Send, 60.59.192.1{Tab}
return
::PC12::
Send, 60.59.150.10{Tab}
Send, 255.255.192.0{Tab}
Send, 60.59.128.1{Tab}
return
::SW5::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 60.59.50.10 255.255.192.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 60.59.0.1{Enter}
Send, do wr{Enter}
return
::PC13::
Send, 160.59.230.10{Tab}
Send, 255.255.128.0{Tab}
Send, 160.59.128.1{Tab}
return
::PC14::
Send, 160.59.210.10{Tab}
Send, 255.255.128.0{Tab}
Send, 160.59.128.1{Tab}
return
::PC15::
Send, 160.59.190.10{Tab}
Send, 255.255.128.0{Tab}
Send, 160.59.128.1{Tab}
return
::PC16::
Send, 160.59.170.10{Tab}
Send, 255.255.128.0{Tab}
Send, 160.59.128.1{Tab}
return
::PC17::
Send, 160.59.150.10{Tab}
Send, 255.255.128.0{Tab}
Send, 160.59.128.1{Tab}
return
::PC18::
Send, 160.59.130.10{Tab}
Send, 255.255.128.0{Tab}
Send, 160.59.128.1{Tab}
return
::SW6::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 160.59.120.10 255.255.128.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 160.59.0.1{Enter}
Send, do wr{Enter}
return
::SW7::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 160.59.90.10 255.255.128.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 160.59.0.1{Enter}
Send, do wr{Enter}
return
::SW8::
Send, enable{Enter}
Send, configure terminal{Enter}
Send, interface vlan1{Enter}
Send, ip address 160.59.30.10 255.255.128.0{Enter}
Send, no shutdown{Enter}
Send, exit{Enter}
Send, ip default-gateway 160.59.0.1{Enter}
Send, do wr{Enter}
return
