A = [1,2,3,4,5,6,7,8,9]

def main(num=3):
	minx, maxx, found = 0,0,0
	mid = int(len(A)/2)
	while (num != int(A[mid])):
		if num < A[mid]:
			maxx = mid
			mid = (maxx-minx)/2
		elif num > A[mid]:
			print(num)
			minx = mid
			mid = (maxx-minx)/2
	print("It is in array {0}, corresponding number is {1} ".format(mid, A[mid]))

if __name__ == '__main__':
	main(6)