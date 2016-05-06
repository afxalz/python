def binary_search(Array,search):
	
	beg=0;
	end=len(a)-1;
	flag=0;

	while(beg<end):
		mid=int((beg+end)/2)
		if(a[mid]==search):
			return 1
		elif(a[mid]>search):
			end=mid-1;
		elif(a[mid]<search):
			beg=mid+1;
		

	return 0

a=list();

print "Enter the  no. of elements of the list::"
length=raw_input();
for i in range(0,int(length)):
	a.append(raw_input());

a.sort()
print a

search=raw_input();
if(binary_search(a,search)):
	print "Element found!!"
