

from operator import contains
import telnetlib

HOST = "xxxx"

tn = telnetlib.Telnet(HOST, 2337)

# tn.read_until("What's the random number?")
output = tn.read_until(b"?")
print(output)
tn.write(b"1 "+ b"\n")
output = (tn.read_until(b"?"))
print(output)


for i in range(1,1001):
    if "No." in str(output):
        counter = str(i)
        tn.write(counter.encode("ascii") + b"\n")
        print(counter + " is the current number")
        output = (tn.read_until(b"?"))
        print(output)
    else:
        print("FOUND THE NUMBER!!! "+ counter)


        #286


