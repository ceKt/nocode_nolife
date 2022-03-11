import pikepdf
import sys
targetfile = "test.pdf"
ansfile = "ANS"+targetfile

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count=1861829800 #←開始位置
while(1):
    count+=1
    i = count
    password=""
    while(i!=0):
        password=chars[i%len(chars)]+password
        i = i//len(chars)
          
    try:
        pdf = pikepdf.open(targetfile, password=password)
        pdf_clear = pikepdf.new()
        pdf_clear.pages.extend(pdf.pages)
        pdf_clear.save(ansfile)
    except:
        print(password)
    else:
        print("passwarod is "+password)
        sys.exit()