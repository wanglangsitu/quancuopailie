import math
def C(x,y):
    result=math.factorial(x)/(math.factorial(y)*math.factorial(x-y))
    return result

n=eval(input('请输入项数：'))

A=[1]   #为了和Python的下标统一，令项数为0时的全错排序为1种，实际无意义

A.append(0)   #项数为1时，全错排序为0种
if n<=0:
    print('请重新输入项数')
elif n==1:
    print('%d项的全错排列有%d种'%(n,A[n]))
else:
    print('1项的全错排列有0种')
    for i in range(2,n+1):     #从项数为2的情况开始计算
        result=math.factorial(i)
        for j in range(0,i):   #总排列数中依次减去错0个、错1个、错2个…错(i-1)个
            result=result-C(i,j)*A[j]
        A.append(result)
        print('%d项的全错排列有%d种'%(i,A[i]))
