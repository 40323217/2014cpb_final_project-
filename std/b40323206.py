#@+leo-ver=5-thin
#@+node:lee.20141223114246.40: * @file example2.py
#@@language python
#@@tabwidth -4
import cherrypy
import random
from std.asciisymbol import asciiImage

#@+others
#@+node:lee.20141223114246.41: ** class Application
class Application(object):
    #@+others
    #@+node:lee.20141223114246.42: *3* def init
    def __init__(self):
    	#你的名子
        self.name = '黃婉菁'
        # 你的學號
        self.number = '40323206'
        # 你的班級
        self.classes = '四設一乙'
        # 你的 github repository url
        self.github_repo_url = 'https://github.com/michell1995huang/2014cp_project_40323206'
        # 你的 openshift app
        self.openshift_url = 'http://2014project-40323206.rhcloud.com/'
        # 你的自評
        self.evaluation = [('Project 7', 90), ('Project 8', 85), ('Project 9', 86)]
        # 你的照片 url
        self.photo_url = 'https://copy.com/2sizBmIPS8m9'
        # 這裡是心得
        self.my_remark = '''
       班級：四設一乙

姓名：黃婉菁

學號：40323206

1.個人 Github 倉儲連結與各版本推送內容說明

(1) git clone 倉儲的網址

(2) 連接成功後會在V槽發現你所連接的雲端資料夾

(3) cd 資料夾的名稱

(4) 把想要傳至遠端的檔案放入V槽的雲端資料夾

(5) git add 檔案的名稱

(6) git commit –m “註解”

(7) git push

◎連結：https://github.com/michell1995huang/2014cp_project_40323206

 2.與個人 Github 倉儲同步的個人 OpenShift 網站連結與內容說明

創立一個Openshift的Python介面，命名後在下方貼上Github的網址即可
https://copy.com/Mxk4c9KFDve9CYh1
https://copy.com/kr8wgTmEduvp0Stz
https://copy.com/9etwsGNQppwD9eXu
 

3.個人在班上協同倉儲中的推送連結與推送紀錄說明

協同倉儲的目的在於共享自己所學習以及了解的資料內容，由於我的能夠提供的資料已經有其他同學分享上傳，所以並沒有再次傳送相同的資料。

◎班級倉儲：https://github.com/Openandgit/2014cpb_final_project-

 

4.個人在班上協同網站上的連結與說明

※必須要先有公共鑰匙clone才會成功

◎ https://copy.com/ilBtpIl7tqIU3vGH
https://copy.com/ulBHIGBdLdlBoaXQ
(1) git clone ssh://5490ef895973caf9a70000d4@cpb-nfutaiwan.rhcloud.com/~/git/cpb.git/ 

(2) 連接成功後會在V槽發現你所連接的雲端資料夾cpb

(3) cd cpb 

(4) cd std

(5) 開啟example.py檔另存為自己的並進行內容修改 (拉到SciTE進行此步驟)

※如果拉其他同學的進行修改要點選的是另存!!!在執行時務必小心~如果發現錯誤不知道如何修改請停止此步驟重來，切勿push回遠端網站 

(6) git add 檔案的名稱

(7) git commit –m “註解”

(8) git push

◎班級網站：http://cpb-nfutaiwan.rhcloud.com/ 

備註：

基本很多同學已經知道如何在近端執行猜數字的遊戲了
https://copy.com/Xw0QKmcBOwzzfIhp
但是要如何在Leo進行修改並且可以推上遠端執行呢？ 

其實老師已經將修改過的檔案上傳到Github了！而且也分享了連結在2014 CP Project

◎https://github.com/chiamingyen/2014cp_project

此資料庫的內容推回自己的Github就可以完成上述所有的內容，不過重要的是內容到底是甚麼──以下：
https://copy.com/xco3ashHMASp2kGW
心得：

透過這次的課程我才明計算機程式並不是那麼的隨便，期中考時所學的內容只不過是程式學的冰山一角。

如果只會在近端寫程式卻無法分享到遠端是不夠的，講難聽一點即使你會多麼複雜的程式，它卻只能在你的電腦裡存活，那都比不上一個會寫猜數字遊戲並且分享到遠端和大家互動的人。可是要完成能夠透過遠端讓近端彼此互動又是件不容易的事。

所以我認為這是一堂非常有意義的課程，透過這堂課我明白到網際網路將人們串連在一起，背後的工程有多麼的龐大。每次在課堂上所學到的東西，產生的結果都讓我驚豔，在踏入這堂課程之前我從來沒有想過我可以不用開啟網頁就將資料上傳到自己的雲端資料夾，第一次開啟網頁時會想看網頁的原始碼，雖然我現在還是看不太懂一般網頁的原始碼內容，但我知道它們是有規則性的，且具有意義的，透過原始碼我看到這個世界在前進的速度遠遠超過台北車站每天每分每秒的流速，讓我感受到了時代在進步的感動及感嘆。
參考資料：

1. GitHub：https://github.com/

2.Openshift：https://www.openshift.com/

3.2014 CP Project：https://140.130.17.17:8443/?id=982

4.2014 CP final project：https://140.130.17.17:8443/?id=986
        '''

    #@+node:lee.20141223114246.43: *3* def use_template
    def use_template(self, content):
        above = """
        <!DOCTYPE html>
    <html lang="en">
    <head>

      <!-- Basic Page Needs
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <meta charset="utf-8">
      <title>title</title>
      <meta name="description" content="">
      <meta name="author" content="">

      <!-- Mobile Specific Metas
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- FONT
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <style>
    @font-face {
      font-family: 'Raleway';
      font-style: normal;
      font-weight: 300;
      src: local('Raleway Light'), local('Raleway-Light'), url(/static/font/Raleway300.woff) format('woff');
    }
    @font-face {
      font-family: 'Raleway';
      font-style: normal;
      font-weight: 400;
      src: local('Raleway'), url(/static/font/Raleway400.woff) format('woff');
    }
    @font-face {
      font-family: 'Raleway';
      font-style: normal;
      font-weight: 600;
      src: local('Raleway SemiBold'), local('Raleway-SemiBold'), url(/static/font/Raleway600.woff) format('woff');
    }
    </style>

      <!-- CSS
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <link rel="stylesheet" href="/static/css/normalize.css">
      <link rel="stylesheet" href="/static/css/skeleton.css">
      <link rel="stylesheet" href="/static/css/custom.css">
      <!-- Favicon
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
      <link rel="icon" type="image/png" href="/static/images/favicon.png" />

    </head>
    <body>

      <!-- Primary Page Layout
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <!-- .container is main centered wrapper -->
    <div class="container">
    """
        below = """
    </div>
    <footer class="center">
      2014 Computer Programming
    </footer>

    <!-- Note: columns can be nested, but it's not recommended since Skeleton's grid has %-based gutters, meaning a nested grid results in variable with gutters (which can end up being *really* small on certain browser/device sizes) -->

    <!-- End Document
      –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    </body>
    </html>
    """
        return above + self.generate_nav(self.link()) + content + below
    #@+node:lee.20141223114246.44: *3* def generate_nav
    def generate_nav(self, anchors):
        above_side = """
        <div class="row">
            <div class="nav twelve columns">
                <input type="checkbox" id="toggle" />
                <div>
                    <label for="toggle" class="toggle" data-open="Main Menu" data-close="Close Menu" onclick></label>
                    <ul class="menu">
        """

        content = ''
        for link, name in anchors:
            content += '<li><a href="' + link + '">' + name + '</a></li>'

        below_side = """
                    </ul>
                </div>
            </div>
        </div>
        """
        return above_side + content + below_side
    #@+node:lee.20141223114246.45: *3* def generate_form_page
    def generate_form_page(self, form='', output=''):
        content = """
            <div class="content">
            <div class="row">
              <div class="one-half column">
                %s
              </div>
              <div class="one-half column">
                <div class="output u-full-width">
                  <p>Output:</p>
                  <p>
                    %s
                  </p>
                </div>
              </div>
            </div>
          </div>
        """%(form, output)
        return self.use_template(content)
    #@+node:lee.20141223114246.55: *3* def generate_headline_page
    def generate_headline_page(self, headline, output):
        content = """
      <div class="content">
        <div class="row">
          <div class="headline center">%s</div>
          <div class="twelve columns">
            <p>%s</p>
          </div>
        </div>
      </div>
        """ % (headline, output)
        return self.use_template(content)
    #@+node:lee.20141223114246.46: *3* def generate_personal_page
    def generate_personal_page(self, data=None):
        if data is None:
            return ''

        # check data have all we need, if the key not exist, use empty string
        must_have_key = ('photo_url', 'name', 'ID', 'class', 'evaluation')
        for key in must_have_key:
            data[key] = data.get(key, '')


        if 'evaluation' in data:
            table_content = ''
            for projectName, score in data['evaluation']:
                table_content += """<tr><td>%s</td><td>%s</td>"""%(projectName, score)
            data['evaluation'] = table_content
        content = """
    <div class="content">
    <div class="row">
      <div class="one-half column">
        <div class="headline">
          About Me
        </div>
        <div class="photo">
          <img src="{photo_url:s}" alt="photo">
        </div>
        <div class="meta">
          <ul>
            <li>Name: {name:s}</li>
            <li>ID NO. : {ID:s}</li>
            <li>Class: {class:s}</li>
          </ul>
        </div>
      </div>
      <div class="one-half column">
        <div class="headline">
          Self Evaluation
        </div>
        <div>
          <table class="u-full-width">
            <thead>
              <tr>
                <th>Project Name</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
                {evaluation:s}
            </tbody>
          </table>

        </div>
      </div>
    </div>
    </div>
        """.format(**data)
        return self.use_template(content)
    #@+node:lee.20141223114246.47: *3* def link
    def link(self):
        aviable_link = [("index", "HOME"), ("remark", "心得"), (self.openshift_url, "openshift app"),(self.github_repo_url, "github repo"),]
        return aviable_link
    #@+node:lee.20141223114246.54: *3* def remark
    @cherrypy.expose
    def remark(self):
        # 這裡是心得
        # generate_headline_page(你的標題, 你的內容)
        return self.generate_headline_page("REMARK", self.my_remark)
    #@+node:lee.20141223114246.48: *3* def index
    @cherrypy.expose
    def index(self):
        # 這裡是首頁
        data = {
            'name':self.name,
            'ID':self.number,
            'class':self.classes,
            'evaluation': self.evaluation,
            'photo_url':self.photo_url,
        }
        return self.generate_personal_page(data)
    #@-others
#@-others
#@-leo

