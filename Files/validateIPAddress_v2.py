"""
Logic involving exception handling and counting
"""
import collections

def validateIP(address):
    def isIPv4(s):
        try:
            return str(int(s)) == s and (0 <= int(s) <= 255)
        except:
            return False

    def isIPv6(s):
        try:
            return len(s) <= 4 and int(s,16) >= 0

        except:
            return False

    count = collections.Counter(address)

    if count['.'] == 3 and all(isIPv4(ele) for ele in address.split('.')):
        return 'IPv4'
    
    if count[':'] == 7 and all(isIPv6(ele) for ele in address.split(':')):
        return 'IPv6'

    return 'Neither'

