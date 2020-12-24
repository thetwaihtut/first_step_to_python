import telnetlib
import getpass
host=str(input('enter host:'))
name=input('enter name:')
x=str(input("enter password to enter enable mode"))
pwd=getpass.getpass()
tn=telnetlib.Telnet(host)
tn.write(name.encode('ascii')+b'\n')
if pwd:
    tn.read_until(b"Password:")
    tn.write(pwd.encode('ascii')+b'\n')

tn.write(b'en\n')
tn.write(x.encode('ascii')+b'\n')
tn.write(b'sh ip int br\n')
tn.write(b'exit\n')
print(tn.read_all().decode('ascii'))