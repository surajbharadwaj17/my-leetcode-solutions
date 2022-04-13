"""
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address 
or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 
and xi cannot contain leading zeros. 
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses,
while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

"""

def validateIP(address):

    acceptable_chars = [
                            'A','B','C','D','E','F',
                            'a','b','c','d','e','f'
                        ]

    acceptable_digits = ['0','1','2','3','4','5','6','7','8','9' ]

    print(f"Input: {address}")
    ip = address.split('.')

    if len(ip) > 1 :
        # Must start with a number
        try:
            p = int(ip[0]) + int(ip[-1])
        except:
            return 'Neither'

        print(f'IP array before removing empty elements: {ip}, length: {len(ip)}')
    
        while ("" in ip):
            ip.remove("")
        print(f'IP array after removing empty elements: {ip}, length: {len(ip)}')
        if len(ip) != 4:
            return 'Neither'

        # IPv4 case
        else:
            
        
            for ele in ip:
                # checking if all the chars are digits
                for char in ele:
                    print(char)

                    if not char:
                        return 'Neither'

                    if not char.isdigit():
                        return 'Neither'

                # checking the value constraint in IPv4
                if (int(ele) < 0) or (int(ele) > 255):
                    return 'Neither'
                
                # checking leading zeros constraint in IPv4
                if len(ele) > 1 and ele[0] == '0':
                    return 'Neither'

        return 'IPv4'

    else:
        # IPv6 case
        ip = address.split(':')

        if len(ip) != 8:
            return 'Neither'

        else:
            for ele in ip:
                if len(ele) > 4 or len(ele) < 1:
                    return 'Neither'
                else:
                    for char in ele:
                        if char not in acceptable_chars + acceptable_digits:
                            return 'Neither'
        return 'IPv6'




ip = "1..1.1.1"
print(validateIP(ip))
