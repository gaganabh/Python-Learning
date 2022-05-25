for(i = 0; i < N-1;i=i+1)
  for(j=N-1;j!=i;j=j-1)
	  if(a[j]<a[j-1])
	    swap(a[j],[j-1])