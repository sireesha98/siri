i=raw_input("")
p=['a','e','i','o','u','A','E','I','O','U']
if (i>='a' and i<='z'  or i>='A' and  i<='Z'):
       if (i in p):
	print("vowel")
       else:
        	print("consonant")
else:
	print("invalid")
	
