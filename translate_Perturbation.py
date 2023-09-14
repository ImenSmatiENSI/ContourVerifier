import numpy as np
def any_number_range(a,b,s=1):
    result = []
    if (a == b):
        result.append(a)
        #print(type(result))
    else:
        mx = max(a,b)
        mn = min(a,b)
       
        # inclusive upper limit. If not needed, delete '+1' in the line below
        while(mn <= mx):
            # if step is positive we go from min to max
            if s > 0:
                result.append(mn)
                mn += s
            # if step is negative we go from max to min
            if s < 0:
                result.append(mx)
                mx += s
    #print(result)
    return result
def Upper_Lower_Translation(cont,x1,x2,y1,y2,batch_size):
    x=cont[0:120]
    y=cont[120:240]
    
    Lower_bound_final_x = np.zeros(120,)
    Upper_bound_final_x = np.zeros(120,)
    Lower_bound_final_y = np.zeros(120,)
    Upper_bound_final_y = np.zeros(120,) 
    Upper_bound = np.zeros(240,)
    Lower_bound = np.zeros(240,)
    up_x1 = np.zeros(120,)
    lw_x1 = np.zeros(120,)
    
    lw_y1 = np.zeros(120,)
    up_y1 = np.zeros(120,)
    
    pas_x=abs(x2-x1)/batch_size
    pas_y=abs(y2-y1)/batch_size
    
    for k in any_number_range(0,batch_size):
        
        delta_x = x1 + k*pas_x
        delta1_x = x1 + (k+1)*pas_x
        
        delta_y = y1 + k*pas_y
        delta1_y = y1 + (k+1)*pas_y
        
        #print (delta_x)
        #print(delta1_x)
        #print('delta_translation',delta_x,delta_y)

        for i in range(len(x)): 
            up_x1[i] = x[i] + delta1_x
            lw_x1[i] = x[i] + delta_x
            
            up_y1[i] = y[i] + delta1_y
            lw_y1[i] = y[i] - delta_y
            
            
            if  k == 0:
            
                lower_bound_final_x = lw_x1
                lower_bound_final_y = lw_y1
                upper_bound_final_x = up_x1
                upper_bound_final_y = up_y1
                
   
            else:
                for j in range(len(x)):       
                    lower_bound_final_x[j]=min(x[j]+x1,up_x1[j],lw_x1[j])
                    lower_bound_final_y[j]=min(y[j]+y1,up_y1[j],lw_y1[j])
                    upper_bound_final_x[j]=max(up_x1[j],lw_x1[j])
                    upper_bound_final_y[j]=max(up_y1[j],lw_y1[j])

        
    
    Lower_bound_final=np.concatenate([lower_bound_final_x,lower_bound_final_y]) 
    Upper_bound_final=np.concatenate([upper_bound_final_x,upper_bound_final_y])
                                   

    
    return(Lower_bound_final,Upper_bound_final)                           
    
