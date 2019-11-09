# Download_from_book118


作用：爬取https://max.book118.com 网站的pdf并生成pdf文件（其他格式文档，本程序暂不支持爬取）

使用方法：

一、第一次运行run.py

运行run.py,在交互界面把你要下载的文件当前网址复制下来，粘贴上去，按enter。运行一段时间后程序会报错终止，报错原因是是img.py的18行x[21:-4]中21数字不适用当前文件。

二、运行beforeRun.py

运行beforeRun.py，根据运行的报错结果更改x[21:-4]中21处的数值，数值适当时运行结果是输出一系列文件名（且文件名按照升序排列）；用得到适当数字代替img.py的18行x[21:-4]中的21。

三、正式运行运行run.py

此时再次运行run.py——输入网址——程序运行——运行结束（“文件库”下既有生成的pdf文件）




使用注意：在run.py同级目录下建立两个文件夹：分别命名：图片、文件库；“图片”文件夹用于储存爬取的图片，“文件库”文件夹用于储存生成的pdf文件




本仓库的程序是在https://github.com/GallenQiu/-book118- 的基础上稍加改动

在2019.11.5时https://github.com/GallenQiu/-book118- 的程序不能正常运行，本仓库的程序可以正常运行

测试时运行的环境为python3.8
beautifulsoup4             4.8.1
PyMuPDF                    1.16.6
reportlab                  3.5.32
requests                   2.22.0
urllib3                    1.25.6
