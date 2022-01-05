def beolvas(eleres):
    x = "C:/Users/" + eleres + "/Downloads/ots.csv"
    file = open(x)
    sorsolasok = []
    for l in file.readlines():
        teljes=[]
        if (l.split(';')[2]==''):
            st = l.split(';')[0] + '.' + l.split(';')[1] + '.'
            teljes.append(st)
        else:
            teljes.append(str(l.split(';')[2]))
        sorsolas = []
        sorsolas.append(int(l.split(';')[11]))
        sorsolas.append(int(l.split(';')[12]))
        sorsolas.append(int(l.split(';')[13]))
        sorsolas.append(int(l.split(';')[14]))
        sorsolas.append(int(l.split(';')[15]))
        teljes.append(sorted(sorsolas))
        teljes.append(sum(sorsolas))
        sorsolasok.append(teljes)
    return sorsolasok