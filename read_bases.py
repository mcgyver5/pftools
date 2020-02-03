import sys
import binascii
if len(sys.argv) > 2:
    answer = ""
    cat = sys.argv[1]

    if cat == "b":
        for x in range(2,len(sys.argv)):
            s = sys.argv[x]
            i = int(s,2)
            answer = answer + binascii.unhexlify('%x' % i)

    if cat == "dec":
        for x in range(2, len(sys.argv)):
            s = sys.argv[x]
            for y in range(0, len(s),2):
                i = int(s[y:y+2])
                answer = answer + chr(i)
    if cat == "oct":

        for h in range(2,len(sys.argv)):
            s = sys.argv[h]
            for y2 in range(0, len(s),3):
                i = int(s[y2:y2+3],8)
                answer = answer + chr(i)
    if cat == "hex":
        for h in range(2,len(sys.argv)):
            s = sys.argv[h]
            for y2 in range(0, len(s),2):
                i = int(s[y2:y2+2],16)
                answer = answer + chr(i)
    print(answer)
else:
    print("Need at least two arguments.  First argument is type:  b= binary, dec=decimal, hex=hex.")
    print("example:  $ python read_binary.py b 01100110 ")
    sys.exit(1)
