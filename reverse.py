######################################################################
#   Date Modified: 02/03/2020   By: kc8son
#   Fixed the reverse() function.  Adding the index [::-1] will start 
#   at the end of the string and run through it backwards.
import sys

def reverse(in_string):
  return in_string[::-1]
  
  
print("This is " + sys.argv[0])
print(" Your Input was " + sys.argv[1])
user_input = sys.argv[1]
print("reversed:  " + reverse(user_input)
