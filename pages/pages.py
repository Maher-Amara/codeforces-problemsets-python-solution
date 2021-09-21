def printer(n, p, k):
    ch_left = ""
    ch_right = ""
    t1 = True
    t2 = True
 
    for i in (range(p - 1, p - k - 1, -1)):
        if i == 0:
            t1 = False
            break
 
        ch_left = str(i) + " " + ch_left
 
        if i == 1:
            t1 = False
            break
 
    ch_left = "<< " * t1 + ch_left
 
    for i in (range(p + 1, p + k + 1)):
        if i == n+1:
            t2 = False
            break
        ch_right += str(i) + " "
        if i == n:
            t2 = False
            break
    ch_right += ">>" * t2
    print(ch_left + "(" + str(p) + ")", ch_right)
 
 
def main():
    n, p, k = input().split()
    printer(int(n), int(p), int(k))
 
 
# main
if __name__ == "__main__":
    main()