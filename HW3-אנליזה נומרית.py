#Moges Beyene - 319496816
#Almog Bar - 205630379

def Yakobi(matrix,arr):
    Xr,Yr,Zr=0,0,0
    for i in range(10):
        Xr1=(arr[0]-matrix[0][1]*Yr)/matrix[0][0]
        Yr1=(arr[1]-matrix[1][0]*Xr-matrix[1][2]*Zr)/matrix[1][1]
        Zr1=(arr[2]-matrix[2][1]*Yr)/matrix[2][2]
        print("Xr1=",Xr1,"Yr1=",Yr1,"Zr1=",Zr1)
        if(Xr+1-Xr<0.001 and Yr+1-Yr<0.001 and Zr+1<Zr):
            break;
        Xr,Yr,Zr=Xr1,Yr1,Zr1
def GausZaidel(matrix,arr):
    Xr,Yr,Zr=0,0,0
    for i in range(10):
        Xr1=(arr[0]-matrix[0][1]*Yr)/matrix[0][0]
        Yr1=(arr[1]-matrix[1][0]*Xr1-matrix[1][2]*Zr)/matrix[1][1]
        Zr1=(arr[2]-matrix[2][1]*Yr1)/matrix[2][2]
        print("Xr1=",Xr1,"Yr1=",Yr1,"Zr1=",Zr1)
        if(Xr+1-Xr<0.001 and Yr+1-Yr<0.001 and Zr+1<Zr):
            break;
        Xr,Yr,Zr=Xr1,Yr1,Zr1
        
def DominantMatrix(matrix):
    if(abs(matrix[0][0]>matrix[0][1] + matrix[0][2]) and abs(matrix[1][1]>matrix[1][0]+matrix[1][2]) and abs(matrix[2][2]>matrix[2][0]+matrix[2][1])):
        print("Matrix is dominant")
        return
    print("Matrix is not dominant")
    
arr=[2,6,5]
matrix=[[4,2,0],[2,10,4],[0,4,5]]
Yakobi(matrix,arr)
GausZaidel(matrix,arr)
DominantMatrix(matrix)
