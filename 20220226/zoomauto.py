import time
from datetime import datetime
import os

def main():
    #dataファイルを開く
    try:
        f=open("data.txt","r")
    except:
        with open("data.txt","w"):
            exit()

    print("OBSのディレクトリパスとその他設定を入力すれば自動でmeetingを録画します。録画しますか？('y' or other key)")
    use_obs = input()
    if(use_obs=='y'):
        print("OBSのディレクトリパスを入力してください")
        obspath = input()
        is_file = os.path.isfile(obspath+"/obs64.exe")
        print(obspath)
        print(is_file)
        if(not is_file):
            print("OBS not found")
            exit()
        print("OBSで利用するプロファイル名を入力してください")
        obs_profilename = input()
        print("OBSで利用するシーンコレクションを入力してください")
        obs_collection = input()
        print("OBSで利用するシーンを入力してください")
        obs_scene = input()
        print("以下のコマンドが実行されます")
        obs_cmd = 'cd '+ obspath +' & start "" obs64.exe --profile "'+ obs_profilename + '" --collection "'+ obs_collection +'" --scene "'+ obs_scene +'" –-studio-mode --startrecording'
        print(obs_cmd)

    lines=f.readlines()
    datalist=[]
    for index in range(len(lines)):
        if(index != 0):
            i=lines[index]
            print(i)
            a=i.split()
            t=datetime(int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]))
            datalist.append([t,a[5],a[6]])

    #1日間60秒置きに確認時間ならzoom参加
    for i in range(60*24):
        for j in datalist[1:]:
            if((j[0]-datetime.now()).seconds<=60):
                c = "start zoommtg:"+'"'+"//zoom.us/join?confno="+j[1]+"&pwd="+j[2]+'"'
                os.system(c)
                if(use_obs):
                    os.system(obs_cmd)
        time.sleep(59)
    f.close()

if __name__=="__main__":
    main()

