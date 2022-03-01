import string


def main(target):
    alphabets1=["ABCDE","FGHIK","LMNOP","QRSTU","VWXYZ"]
    alphabets2=["abcde","fghik","lmnop","qrstu","vwxyz"]
    ans = ""
    for i in target:
        if(i=='j' and i=="J"):
            ans+="24"
        else:
            for j in range(len(alphabets1)):
                for k in range(len(alphabets1[j])):
                    if i==alphabets1[j][k]:
                        ans+=str(j+1)+str(k+1)
                for k in range(len(alphabets2[j])):
                    if i==alphabets2[j][k]:
                        ans+=str(j+1)+str(k+1)
    return ans
        

if __name__=="__main__":
    print("please enter data")
    target = input()
    ans=main(target)
    print(ans)
