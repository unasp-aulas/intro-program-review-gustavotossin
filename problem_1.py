def fun_sal(esc, num):

    if (esc == 'jr'): 
      return num * 1.15
    
    elif (esc == 'pl'): 
      return num * 1.26
    
    elif (esc == 'sr'): 
      return num * 1.34
    else: 
      return -1
