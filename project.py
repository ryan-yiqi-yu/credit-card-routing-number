def is_valid_CC(ccnum):
  tot = tot2=0
  list = [str(ccnum)]
  tot =+ int(i) for i in list[::-2]
  for l in list[-1::-2]:
    list2 = []
    list2 = [int(d) for d  in str(2*int(l))]
    tot2 =+ sum(list2)
  return (tot2 + tot) % 10 == 0 
    
      
    
