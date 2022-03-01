import string


def main(target):
    alphabets=["ABCDE","FGHIK","LMNOP","QRSTU","VWXYZ"]
    ans = ""
    for i in range(len(target)//2):
        ans+=alphabets[int(target[i*2])-1][int(target[i*2+1])-1]
    return ans
        

if __name__=="__main__":
    print("please enter data")
    target = input()
    ans=main(target)
    print(ans)
