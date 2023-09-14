import numpy as np
#def cart2pol(x, y):
   # theta = np.arctan2(y, x)
    #rho = np.hypot(x, y)
    #return theta, rho
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(phi,rho)

def pol2cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y

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

def rotate_lower_upper(cont,angle,angle2,batch_size):
    x=cont[0:120]
    y=cont[120:240]
    
    Lower_bound_x = np.zeros(120,)
    Upper_bound_x = np.zeros(120,)
    Lower_bound_y = np.zeros(120,)
    Upper_bound_y = np.zeros(120,) 
    Upper_bound = np.zeros(240,)
    Lower_bound = np.zeros(240,)
    
    thetas, rhos = cart2pol(x, y)
    thetas_deg = np.rad2deg(thetas)
    
    pas=abs(angle2-angle)/batch_size
    
    for k in any_number_range(0,batch_size):
        degre=angle+k*pas 
        degre1=angle+(k+1)*pas
        #print('degre', degre)
        #print('degre1', degre1)
        thetas1_upper = np.zeros(120,)
        thetas1_lower = np.zeros(120,)
        thetas1_upper=np.deg2rad(thetas_deg + degre1)
        thetas1_lower=np.deg2rad(thetas_deg + degre)
        
        up_x1, up_y1 = pol2cart(thetas1_upper, rhos)
        lw_x1, lw_y1 = pol2cart(thetas1_lower, rhos)
        
        #print(k)
        if (k == 0):
            
            lower_bound_final_x = lw_x1
            lower_bound_final_y = lw_y1
            upper_bound_final_x = up_x1
            upper_bound_final_y = up_y1
        else:    
            
            for j in range(len(x)):
          
                lower_bound_final_x[j]=min(lower_bound_final_x[j],upper_bound_final_x[j],up_x1[j],lw_x1[j])
                lower_bound_final_y[j]=min(lower_bound_final_y[j],upper_bound_final_y[j],up_y1[j],lw_y1[j])
                upper_bound_final_x[j]=max(upper_bound_final_x[j],lower_bound_final_x[j],up_x1[j],lw_x1[j])
                upper_bound_final_y[j]=max(upper_bound_final_y[j],lower_bound_final_y[j],up_y1[j],lw_y1[j])
            
        

            
    
    
    
    Lower_bound_final=np.concatenate([lower_bound_final_x,lower_bound_final_y]) 
    Upper_bound_final=np.concatenate([upper_bound_final_x,upper_bound_final_y])    
    
    
    
    

    
    


    return(Lower_bound_final,Upper_bound_final) 
            
            
            
            
    
    
    
