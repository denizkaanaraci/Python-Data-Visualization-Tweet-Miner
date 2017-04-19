def part3():
    # -*- coding: utf-8 -*-

    import json
    import string
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    from numpy import array
    from datetime import datetime
    from operator import itemgetter
    import time
    from collections import Counter
    import operator
    import os
    import csv
    import json
    import string
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    from datetime import datetime,timedelta
    from operator import itemgetter
    import time
    from collections import Counter
    import os
    import csv
    from collections import defaultdict
    from collections import OrderedDict


    t = time.time()
    data = [] #kelimeler
    wordfreq = [] #kac defa gectigi yaziyor
    punctuation = list(string.punctuation)
    stop = punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']
    listem=[]
    datalistesi=[]
    part3= open('term_cooccurrences.txt', 'w')
    with open('tweet_data.json', 'r') as f:

        for line in f:
            tweet = json.loads(line)
            str=tweet['text']#tweet
            str=str.lower()
            L=str.split(" ")
            datax=[]
            for x in L:
                if x not in stop:
                    data.append(x.encode("utf-8"))
                    datax.append(x.encode("utf-8"))

            datalistesi.append(datax)

        counted_list=Counter(data)
        final_list = counted_list.most_common(20)

        listforx=[]
        listfory=[]

        for zxc in range(20):
            listforx.append(final_list[zxc][0])
            listfory.append(final_list[zxc][1])


        list10x=listforx[:10] #10luk kelime listesi
        listfor3=[]
        for i in range(10):
            for j in range(10):
                cardo=(list10x[i],list10x[j])
                listfor3.append(cardo)



    for i in listfor3:
        yellow_and_violent = 0

        a = i[0].__str__()
        b = i[1].__str__()
        for j in range(len(datalistesi)):

            if (i[0] in datalistesi[j]) and (i[1] in datalistesi[j]):

                    yellow_and_violent += 1



        part3.write(''.join(a.__str__()) + "-" + ''.join(b.__str__()) + " " + ''.join(yellow_and_violent.__str__()) + '\n')


    x=np.linspace(0,10,30)
    y=x
    plt.plot(x,y)
    plt.savefig('term_cooccurrences.png')
    plt.title("bu grafigi yapamadim")
    plt.show()
def part2():
    # -*- coding: utf-8 -*-

    import json
    import string
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    from datetime import datetime,timedelta
    from operator import itemgetter
    import time
    from collections import Counter
    import os
    import csv
    from collections import defaultdict
    from collections import OrderedDict



    t = time.time()

    listforx=[]
    listfory=[]
    data = [] #kelimeler
    wordfreq = [] #kac defa gectigi yafyor
    punctuation = list(string.punctuation)
    stop = punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']
    time_time = []
    bulduk=defaultdict(list)
    bastirdict=defaultdict(list)
    part2= open('term_frequency_overtime.txt', 'w')

    with open('tweet_data.json', 'r') as f:
        for line in f:

            bulduk_data=[]
            tweet = json.loads(line)
            date=tweet["created_at"]#date-time in ISO format
            dt= datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y") #reading date in ISO format
            tmm=dt.strftime("%a %b %d %H:%M:00 +0000 %Y")
            tmmm=datetime.strptime(tmm,"%a %b %d %H:%M:%S +0000 %Y")
            str=tweet['text']#tweet
            str=str.lower()
            L=str.split(" ")

            for x in L:
                if x not in stop:
                    data.append(x.encode("utf-8"))
                    bulduk_data.append(x.encode("utf-8"))

            bulduk[tmmm].append(bulduk_data)



    counted_list=Counter(data)
    final_list = counted_list.most_common(10)
    for zxc in range(10):
        listforx.append(final_list[zxc][0])
        listfory.append(final_list[zxc][1])

    sonlist=listforx[:5]
    list_term=[]
    list_date=[]
    list_count=[]
    for k in sonlist:
        liste=[]
        for kk in bulduk.keys():
            bastirlist=[]
            liste1=[]
            ahmet=sum(bulduk[kk],[])
            saymali=Counter(ahmet)
            aa=[kk,saymali[kk]]
            bastirdict[k].append(aa)

            a=[kk,saymali[k]]
            liste.append(a)

        a=sorted(liste, key = itemgetter(0))
        for i in range(len(liste)):

            str_k=k.__str__()
            str_0=a[i][0].__str__()
            str_1=a[i][1].__str__()
            list_term.append(str_k)
            list_date.append(str_0)
            list_count.append(str_1)
            part2.write(''.join(str_k) + " " + ''.join(str_0) + " " + ''.join(str_1) + '\n')



    x=np.linspace(0,10,30)
    y=x
    plt.plot(x,y)
    plt.savefig('term_frequency_overtime.png')
    plt.title("bu grafigi yapamadim")
    plt.show()
    return part3()
def part1():
    # -*- coding: utf-8 -*-

    import json
    import string
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    import pylab as pl
    import matplotlib.font_manager as font_manager
    from datetime import datetime
    import matplotlib
    from operator import itemgetter
    import time
    from collections import Counter
    import os
    import csv



    data = [] #kelimeler
    wordfreq = [] #kac defa gectigi yaziyor
    punctuation = list(string.punctuation)
    stop = punctuation+[ 'a','an','the','rt', 'via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']
    part1= open('term_frequency.txt', 'w')
    with open('tweet_data.json', 'r') as f:

        for line in f:
            tweet = json.loads(line)
            str=tweet['text']#tweet
            str=str.lower()
            L=str.split(" ");

            for x in L:
                if x not in stop:
                    data.append(x.encode("utf-8"))


    counted_list=Counter(data)
    final_list = counted_list.most_common(20)

    listforx=[]
    listfory=[]
    for i in final_list:

        ii = i.__str__()
        part1.write(''.join(ii) + '\n')


    for zxc in range(20):
        listfory.append(final_list[zxc][1])
        listforx.append(final_list[zxc][0])


    fig=plt.figure()
    N = 20
    ind = np.arange(N)    # the x locations for the groups
    width = 0.7       # the width of the bars: can also be len(x) sequence
    p1 = plt.bar(ind, listfory, width, color='r')

    plt.ylabel('Term Frequencies')
    plt.title('Tweet Miner')
    plt.xticks(ind + width/2., listforx,fontsize=8)
    plt.yticks(np.arange(0, listfory[0],500),fontsize=8)
    label_size=2
    plt.savefig('term_frequency.png')
    plt.show()
    return part2()


part1()

#ilk part tam, 2. ve 3. partta grafik yazimlari disinda tamamen ayni