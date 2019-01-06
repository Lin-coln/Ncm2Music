<h1>Netease Cloud Music Copyright Protection File Dump (Python version)</h1>

<h2>简介</h2>


<p>Python版本解密ncm文件，根据贴吧某位大神的源码再开发而来，加了很多使用功能，比如嵌入歌曲tags和封面图片<del>(flac嵌入图片有问题，但是保存为同名文件播放器是可以识别的,想要嵌入文件的童鞋可以自己琢磨一下mutagen库)</del>还有下载歌词啥的。</p>
<p6>flac文件内嵌图片功能已修复!</p6>

<h2>安装</h2>
<h3 style="background-color:green">依赖 pycrypto库</h3>

<code>pip(3) install pycrypto</code>
<p style="background-color:yellow">推荐使用下面的库！不安装上面的库</p>
<code>pip3 install -i https://pypi.douban.com/simple pycryptodome</code>
，嫌弃官方源太慢可以自行百度国内pypi源然后更换
使用<code>pip install pycryptodome mutagen requests urllib3</code>来安装依赖库

<h3>使用方法：</h3>
<p style="background-color:red">直接将Ncm2Music.py复制到有.ncm文件的文件夹里运行即可。</p>
您可以将NCM文件任意更名，就算更名也能输出正常的音乐文件歌手和歌曲名，因为这些数据被保存在ncm文件内了
<p style="background-color:red"><u>推荐在转换前将ncm文件全部更名为1.ncm,2.ncm,3.ncm.....这样可以防止因文件名内含有特殊字符导致的转换出错!这样改名并没有害处!</u></p>
<h5>高端操作</h5>
<p>开一个Ncm2Muaic只能占用1个CPU核心，将ncm文件分开几个文件夹储存，每个文件夹分别运行Ncm2Music，可以实现所谓的“手动多线程”，实测4核心开4个Ncm2Music刚好4核心全部100%占用，速度最快!!!</p>
<h3>文件列表:</h3>
<p>-----Ncm2Music.py 程序主体，推荐使用pyinstaller编译出来使用，直接运行于python2和3中</p>
<p>-----Ncm2Music_py2.py 此版本显示的歌曲信息更详细，没啥区别,但是这个版本我维护的不是很频繁，不推荐使用。</p>
<p>-----ncmdump.py 某贴吧大神的ncm文件转换器，此文件是源代码，上传供大家使用，代码来源可以在github上搜ncmdump这个项目</p>
<p>-----lrcget.py 根据网易云歌曲ID来获取歌词的源码，上传供大家使用，原理来自互联网。</p>
<p>-----SongList_LRC_Getter.py 获取一个歌单里所有歌曲的歌词，可以单独使用来获取歌词，普通歌词保存为lrc翻译歌词保存为tlyric,但是只能在Python2环境下运行</p>
<p>-----Song_LRC_Tlyric_copy.py 合并lyric和tlyric文件的脚本，若要合并lrc文件和tlyric文件，请将脚本中" #lrcTOlyric() " 去注释，具体在文件的"37"行</p>
<p>-----README.md 说明文件</p>

<em>copyright 2018-2020 KGDSAVE SOFTWARE STUDIO - CRMMC</em> 

<h2>更新日志</h2>
<dl>
  <dt><kbd>2018.10.12</kbd></dt>
    <dd>第一次更新---项目出生的日子，完成了程序主体和主要功能加入</dd>
  <dt><kbd>2018.10.20</kbd></dt>
    <dd>第二次更新---加入了下载中外文歌词，修复了flac文件无法内嵌歌曲图片的bug，添加了获取整个歌单的歌词的脚本,重新优化了界面，修复了无法在python3中运行的bug</dd>
  <dt><kbd>2018.12.1</kbd></dt>
    <dd>第三次更新---修复了在windows上由于编码不同导致的部分文件转换失败的bug，删除引用了部分无用库。加入错误文件日志功能,更方便找到错误文件。</dd>
  <dt><kbd>2019.1.2</kbd></dt>
    <dd>第四次更新---修复了在winxp上由于python2函数原因导致程序无法运行的bug，加入了将转换出错文件归类到文件夹方便再次转换的功能，进一步修复无法在winxp上使用python2转换文件的bug，再祝大家新年快乐/开心</dd>
  <dt><kbd>2019.1.6</kbd></dt>
    <dd>第五次更新---加入了合并歌词的功能，能将外语歌词和原版歌词合并到一个lrc文件</dd>
</dl>


<h2>例图</h2>
<p>使用Python2运行Ncm2Music</p>
<img src="html/s1.jpg" width=300 height=450></img>
<p>使用Python3运行Ncm2Music</p>
<img src="html/s3.jpg" width=300 height=420></img>
<p>转换输出后得到的文件</p>
<img src="html/s4.jpg"width=300 height=150></img>
<p>输出的原版歌词LRC文件</p>
<img src="html/s5.jpg"width=300 height=80></img>
<p>输出的翻译歌词Tlyric文件</p>
<img src="html/s6.jpg"width=300 height=80></img>
<p>合并原版歌词和翻译歌词</p>
<img src="html/s7.png" width=330 height=100></img>
<p>4核心开4个Ncm2Music图片</p>
<img src="html/s2.jpg" width=330 height=150></img>