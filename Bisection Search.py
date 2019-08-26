
def bisearch(L,e):
    def helper(L,e,low,high):
        if low==high:
            return L[low]==e
        mid = (low+high)//2
        if L[mid]==e:
            return True
        elif L[mid]>e:
            if low == mid:
                return False
            else:
                return helper(L,e,low,mid-1)
        elif L[mid]<e:
            return helper(L,e,mid+1,high)
    if len(L)==0:
        return False
    else:
        return helper(L,e,0,len(L)-1)
