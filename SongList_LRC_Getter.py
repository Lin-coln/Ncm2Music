#!/bin/env python
from bs4 import BeautifulSoup
import time,os,re,json,requests
def Getlrc(neteaseID):
	lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(neteaseID) + '&lv=1&kv=1&tv=-1'
	lyric = requests.get(lrc_url,timeout = 15)
	json_obj = lyric.text
	j = json.loads(json_obj)
	return j
def download(songlistID):
    url = 'http://music.163.com/m/playlist?id='+str(songlistID)
 
    header = {
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
 
    res = requests.get(url, headers=header,timeout = 15).text
    songlist = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res)
    n = 0
    for muu in songlist:
    	n = n+ 1
    	if n == 5:
    		time.sleep(1)
    		n = 0
        music_name = muu[1]
        music_id = muu[0]
        print (music_name + '   ' +music_id)
        song_url = "http://music.163.com/song/media/outer/url?id=%s" % music_id
        arhhc = Getlrc(music_id)
    	#print (type(arhhc['lrc']['lyric']))
    	if arhhc.has_key('lrc'):
        	try:
        	    if os.path.exists(music_name + '.lrc'):
        	        print ('Files exist!')			
        	        continue
    			f = open(music_name + '.lrc','w')
    			f.write(str(arhhc['lrc']['lyric'].encode('utf-8')))
    			f.close()
    		except:
        		print ('Error!')
                errorfile.write('LRC ERROR:' +music_name+ ':' + music_id +"\n")
        		#print (str(arhhc['lrc']['lyric'].encode('utf-8')))
    	if arhhc.has_key('tlyric'):
    		try:
    			l = open(music_name + '.tlyric','w')
    			l.write(str(arhhc['tlyric']['lyric'].encode('utf-8')))
    			l.close()
    		except:
        		print ('Error!')
                errorfile.write('TLYARC ERROR:' +music_name+ ':' + music_id +"\n")
        		#print (str(arhhc['tlyric']['lyric'].encode('utf-8')))
        
errorfile = open('error.list','a')
errorfile.write(str(time.asctime()).encode('utf-8') + "\n")
download(2117303846)
errorfile.close()
import glob,os

for i in glob.glob('*.mp3'):
	hg = i.split(' - ')
	if len(hg) == 2:
		sn = hg[1].split('.')[0] + '.lrc'
		snd = i.split('.')[0] + '.lrc'
		an = hg[1].split('.')[0] + '.tlyric'
		anr = snd = i.split('.')[0] + '.tlyric'
		if os.path.exists(sn):
			print ('[' + sn + ']>>>[' + snd + ']')
			os.rename(sn,snd)
		if os.path.exists(sn ):
			print ('[' + an + ']>>>[' + anr + ']')
			os.rename(an,anr)
for i in glob.glob('*.flac'):
	hg = i.split(' - ')
	if len(hg) == 2:
		sn = hg[1].split('.')[0] + '.lrc'
		snd = i.split('.')[0] + '.lrc'
		an = hg[1].split('.')[0] + '.tlyric'
		anr = snd = i.split('.')[0] + '.tlyric'
		if os.path.exists(sn):
			print ('[' + sn + ']>>>[' + snd + ']')
			os.rename(sn,snd)
		if os.path.exists(sn ):
			print ('[' + an + ']>>>[' + anr + ']')
			os.rename(an,anr)