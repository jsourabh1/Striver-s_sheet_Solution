def isplaindrome(string):

	start=0
	end=len(string)-1

	while start<end:

		if string[start]!=string[end]:
			return False
		start+=1
		end-=1

	return True


def solve(string):


	count=0

	while True:

		if isplaindrome(string):
			return count


		string=string[:-1]
		count+=1


print(solve("AAAACECAAAA"))

