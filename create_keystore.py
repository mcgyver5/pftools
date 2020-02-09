# This file uses python library pexpect to autocreate a java keystore
# first install pyt, then pexpect
# pip install pyt
# pip install expect
import sys
import pexpect
child = pexpect.spawn('keytool -genkeypair -alias popcorn5 -keystore popcorn5.jks')
child.logfile = sys.stdout

child.expect('Enter keystore password:')
child.sendline('changeit')
child.expect('Re-enter new password:')
child.sendline('changeit')
child.expect('What is your first and last name?')
child.sendline('tony malone')
child.expect('What is the name of your organizational unit?')
child.sendline('oo')
child.expect('What is the name of your organization?')
child.sendline('oo')
child.expect('What is the name of your City or Locality?')
child.sendline('oo')
child.expect('What is the name of your State or Province?')
child.sendline('MN')
child.expect('What is the two-letter country code for this unit?')
child.sendline('US')
child.expect('Is CN=two tone, OU=oo, O=oo, L=oo, ST=MN, C=US correct?')
child.sendline('yes')
child.expect(pexpect.EOF)
