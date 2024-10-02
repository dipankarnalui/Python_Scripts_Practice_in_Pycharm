def binary_search(a,target):
    print("arr= ", a)
    print("target=", target)
    l,r=0,len(a)-1
    while(l<=r):
        print(f"left={l}, right={r}")
        mid=(l+r)//2
        print("mid=",mid)
        print("a[mid]=", a[mid])
        print(a[l:r])
        if a[mid]==target:
            print(f"target {target} found at location {mid}")
            break
        elif target>a[mid]:
            print("target is in right side")
            l=mid+1
        else:
            print("target is in left side")
            r=mid-1
        print("------------------------------")

a=[12,90,23,45,25,87,1,20,72,10,67,28,101]
target=67
binary_search(sorted(a),target)