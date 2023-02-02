def reverse(end,arr):
 
  
    #By incrementing count value swapping of first and last elements is done.

    

    i = 0

    main_rr = []

    while i < end:
        
        ss =  len(arr) - 1 
        last_element = arr[-1]
        second_elemnt = arr[0:ss]
        # print(second_elemnt)

        # arr[-1] = first_element
        arr[0]  = last_element
        arr[1:len(arr)] = second_elemnt
        # print(last_element)
        i = i + 1

        main_rr = arr

    
    print(main_rr)

        
    



print(reverse(120,[1,2,3,4,5,6,7]))