import dns.resolver
import time

aws_nv_txgw_vpn_01 = 0
aws_nv_txgw_vpn_02 = 0
aws_nv_txgw_vpn_03 = 0

aws_oh_txgw_vpn_02 = 0
aws_oh_txgw_vpn_03 = 0
aws_oh_txgw_vpn_04 = 0
total_count = 0

while True:
    use1_result = dns.resolver.resolve('aws-use1-w1.freedomremote.com', 'A')
    use2_result = dns.resolver.resolve('aws-use2-w1.freedomremote.com', 'A')

    for use1 in use1_result:
        if '54.89.54.112' in use1.address:
            aws_nv_txgw_vpn_01 += 1
        if '54.84.34.57' in use1.address:
            aws_nv_txgw_vpn_02 += 1
        if '54.146.0.105' in use1.address:
            aws_nv_txgw_vpn_03 += 1

        if '18.217.31.164' in use1.address:
            aws_oh_txgw_vpn_02 += 1
        if '3.128.67.134' in use1.address:
            aws_oh_txgw_vpn_03 += 1
        if '3.128.126.133' in use1.address:
            aws_oh_txgw_vpn_04 += 1

    for use2 in use2_result:
        if '54.89.54.112' in use2.address:
            aws_nv_txgw_vpn_01 += 1
        if '54.84.34.57' in use2.address:
            aws_nv_txgw_vpn_02 += 1
        if '54.146.0.105' in use2.address:
            aws_nv_txgw_vpn_03 += 1

        if '18.217.31.164' in use2.address:
            aws_oh_txgw_vpn_02 += 1
        if '3.128.67.134' in use2.address:
            aws_oh_txgw_vpn_03 += 1
        if '3.128.126.133' in use2.address:
            aws_oh_txgw_vpn_04 += 1

        total_count += 1
        print('US East1: ', use1)
        print(f'aws_nv_txgw_vpn_01: {aws_nv_txgw_vpn_01}')
        print(f'aws_nv_txgw_vpn_02: {aws_nv_txgw_vpn_02}')
        print(f'aws_nv_txgw_vpn_03: {aws_nv_txgw_vpn_03}')
        print(' ')
        print('US East2: ', use2)
        print(f'aws_oh_txgw_vpn_02: {aws_oh_txgw_vpn_02}')
        print(f'aws_oh_txgw_vpn_03: {aws_oh_txgw_vpn_03}')
        print(f'aws_oh_txgw_vpn_04: {aws_oh_txgw_vpn_04}')
        print(f'Total: {total_count}')
        print(' ')
        time.sleep(10)






