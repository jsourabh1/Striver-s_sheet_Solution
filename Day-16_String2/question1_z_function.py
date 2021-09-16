def solve(string):

	# print(string)
	z=[0]*len(string)

	n=len(string)
	first=end=0

	for i in range(1,len(string)):
		flag=False
		if i<=end:
			z[i]=min(end-i+1,z[i-first])
		
		while i+z[i]<n and string[z[i]]==string[z[i]+i]:
			flag=True
			z[i]+=1

		if i+z[i]-1>end and flag:
			first=i
			end=i+z[i]-1
	# print(z)
	return z

def helper(text):


	string=text

	n=len(string)

	arr=solve(string)

	for i in range(n):

		 if (arr[i] + i == n and n % (n - arr[i]) == 0):return True

	return False 


text = "abcabcabcabc"

print(helper(text))
