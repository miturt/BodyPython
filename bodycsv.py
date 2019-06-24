
# coding: utf-8


import numpy as np
def readcsv(path):
    f = open(path, 'r')
    line=f.readline()
    head = line[4:21]
    commt = line[23:-1]
    line =f.readline()
    names = line[:-1].split(',')

    print("head:",head,":")
    print("commt:",commt,":")
    #print(names)
    jj = len(names)

    data = np.loadtxt(path,skiprows=2,delimiter=',',dtype='float')
    ii=len(data)
    #print(ii)
    dat = np.reshape(data,(ii,jj))
    #print(dat)
    da = dat.transpose()
    # time
#     aaa = names[0]
#     ns = locals()
#     ns[aaa] = da[0,]

    return (head, commt, names, da )


def startend(da,start,end,ku):

    d = (end-start)/ku
    kd = np.arange(start,end,d)
#     print("kd ",kd," d=",d)

    nst = []
    nen = []
    nnn = 0
    kd = []
    i = 0
    if da[0,0] > start:
        if da[0,-1] < start :
            print("start error")
            exit()
        while start+ d*i <  da[0,0] :
            i += 1
        ds = start + d * (i-1)

    else:
        ds = start
    n=0
    while da[0,n] < ds:
        n += 1
    nst.append(n)
#     print('ds=',ds) 
#     print(nst)
    if end > da[0,-1]:
        de = da[0,-1]
    else:
        de = end
    nen =[]
    if da[0,0]>end:
        print("end error")
        exit()
    n=0
    ks=0
    while ds+d < de:
    #     ks = kd[n]
        while da[0,ks]<ds+d:
            ks += 1
        nst.append(ks)
        nen.append(ks-1)
        ds += d
#     print('ks=',ks,' de=',de)
    while da[0,ks]< de:
        ks += 1
    nen.append(ks-1)

    return(nst,nen)


import tkinter
import tkinter.filedialog
def selectfile():
    tk = tkinter.Tk()
    tk.withdraw()
    
    fTyp = [("csv files","*.csv")]

    filename = tkinter.filedialog.askopenfilename(initialdir  = '/Users/miy/Downloads/', filetypes = fTyp)
    tk.destroy()
    return (filename)

