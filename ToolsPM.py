import time

'''
This function takes a string and an integer as parameters and
does not return aything.  It prints out the characters of the string
to the screen with a delay of delay sections between characters

pre-condition: str must be a string and delay must be a positive integer
post-condition: There are no post conditions
'''
def slowPrint(str, delay):

	for i in range(0,len(str),1):
		print(str[i])
		time.sleep(delay)


'''
This function takes a single integer value as a parameters and 
returns a list containing all the factors.

pre-condition: a > 0
post-condition: There are no post conditions
'''
def findFactorsA(a):

	factorList = [] #stores factors
	for i in range (1,a + 1,1): #loop 
		if a % i == 0:
			factorList.append(i)

	return factorList

def findFactorsB(a):

	factorList = []
	for i in range (1,int(a/2),1):
		if a % i == 0:
			factorList.append(i)
			factorList.append(a//i)

	return factorList


def count_hi(str):
   
  str1 = str.replace("hi","") 
  return (len(str) - len(str1))/2

  
    

