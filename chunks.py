import difflib
import  re
import os
from tokenize import group

path = 'desktop/'
first_file = path+'file1.txt'
second_file = path+'file2.txt'

ff = open(first_file,'r').readlines()
sf = open(second_file,'r').readlines()

def chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
if len(ff) or len(sf)>1:
    ff_len = len(ff)
    sf_len = len(sf)

    if ff_len != sf_len:
        if ff_len > sf_len:
            for x in range(ff_len - sf_len):
                sf.append('\n')
        else:
            for x in range(sf_len - ff_len):
                ff.append('\n')
    ff_list =list(chunks(ff,1))
    sf_list = list(chunks(sf,1))

    dictionary = {'ff':ff_list,'sf':sf_list}

    for key,value in dictionary.items():
        n=0
        for elem in value:
            with open(path+'file_tmp_'+str(key)+'_{}.txt'.format(n),'w') as f:
                for line in elem:
                    f.write(line)
            print('file_tmp_'+str(key)+'_{}.txt is created...'.format(n))
            n+=1
    for i in range(len(ff_list)):
        first_chunk = path+'file_tmp_ff_{}.txt'.format(i)
        second_chunk = path+'file_tmp_sf_{}.txt'.format(i)
        if i == 0:
            #difference0 = difflib.HtmlDiff().make_file(ff_list[i],sf_list[i],first_chunk,second_chunk)
            out = list(difflib.Differ().compare(ff_list[i], sf_list[i]))
        else:
            difference = difflib.HtmlDiff().make_file(ff_list[i],sf_list[i], first_chunk, second_chunk)
    i+=1
    with open(path+'diff.html','w') as f:
        f.write(out)
#for f in os.listdir(path):
    #if re.search('file_tmp_[sf]f_(\d).txt',f):
        #os.remove(os.path.join(path,f))


