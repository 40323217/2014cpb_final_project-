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
        self.name = '李伯皇'
        # 你的學號
        self.number = '40323217'
        # 你的班級
        self.classes = '四設計一乙'
        # 你的 github repository url
        self.github_repo_url = 'https://github.com/Openandgit/2014cp_project--40323217'
        # 你的 openshift app
        self.openshift_url = 'http://newsfile-40323217gm.rhcloud.com/'
        # 你的自評
        self.evaluation = [('Project 7', 80), ('Project 8', 85), ('Project 9', 85)]
        # 你的照片 url
        self.photo_url = 'https://copy.com/4vbQRPcklDdC'
        # 這裡是心得
        self.my_remark = """
        期末報告

班級:四設計一乙

姓名:李伯皇

學號:40323217

---

1.個人 Github 倉儲連結與各版本推送內容說明, 含與本資料緒中個人資料同步的 Wiki 資料內容.

1-1 先創一個github的倉儲



1-1.1git clone (github的網址) 

1-2 至V槽確認資料夾是否以clone下來 

1-3 把老師的github的程式碼貼過去( https://github.com/chiamingyen/2014cp_project )

1-4 V槽命令列

1-5 cd 資料夾名稱

1-6 git add .    --> git commit -m "註解"  --> git push 

完成後網址: https://github.com/Openandgit/2014cp_project--40323217

完成後圖片:



2.與個人 Github 倉儲同步的個人 OpenShift 網站連結與內容說明.

2.1 至Openshift創一個新的python 3.3

2.2 在 Source Code 上貼 github所創倉儲的網址( https://github.com/Openandgit/2014cp_project--40323217 )

第二點操作照片:



2-3 創好之後點網址(執行結果如下)

 

3.個人在班上協同倉儲中的推送連結與推送紀錄說明

班級共用倉儲網址: https://github.com/Openandgit/2014cpb_final_project-

 

4.個人在班上協同網站上的連結與說明.

4-1.先用puttygen.exe創班級共用鑰匙(沒有共用鑰使慧沒辦法clone) 

4-1.1 班級共用鑰匙網站 http://cpgroup.kmol.info/public/cp/2014fall/1b/ 

4-2 git clone ssh://5490ef895973caf9a70000d4@cpb-nfutaiwan.rhcloud.com/~/git/cpb.git/ 

4-3 確認V槽內有"班級"共用資料夾 cpb

4-4 開起 cpb  -> std 資料夾裡 ->拿exampe2.py修改 ->拉到SCIte裡修改自己個人資料

注意事項:

4.4-1 假如修改過程中有人先push了,那麼你在git push之前你要先git pull,因為你的clone不是最新他會要求你先git pull後你才能push

4.4-2 假如是拉其他同學的去更改請務必要另存,要不然你所拉的那位同學的自料會被你更改後蓋過去!!

4-5 修改好後-> git add . -> git commit -m '註解" -> git push

個人網站: http://cpb-nfutaiwan.rhcloud.com/40323217/

班級網站:http://cpb-nfutaiwan.rhcloud.com/

 

 

(2) 為個人的 OpenShift 網站, 內容為個人的 final project 內容執行結果.

(3) 為個人的 Github 倉儲, 內容為與個人 OpenShift 網站同步的倉儲紀錄資料, 其中包含將本資料緒中的個人資料同步一份到個人 Github 倉儲中的 Wiki 資料區.

(4) 為各班的協同網站連結, 各學員必須依照學號安排放入學期自評心得與自評分數.

(5) 為各班的 Github 協同倉儲, 紀錄與各班協同網站同步的內容資料.

 

期末心得：在快速的時代需要有一種工具可以快速的寫好程式(python),並且在近端遠端都有備份,以及在做專案的時候可以有協同者(collabortors)共同開發專案,還有能夠使用github、bitbucket、cherrypy這些都是在這學期的計算機程式當中很重要的一環,假如程式在遠端近端都有備份近端電腦如果發生問題,資料在遠端還會有備份github的功能),在來就是開發個人服務功能,客戶網站上輸入需要的工具或是商品,輸入他們需要的尺寸或者商品編號,能夠自動出現"客製化"的商品達到滿足客戶的要求,這也是本學期重要的一環.

而在全球化的競爭當中學好英文也是未來的趨勢,不僅要會寫程式也要會有流利的語言能力,這是一個機械工程師所需要具備的能力,還有就是口條能力,能夠在設計出程式之後可以簡潔有力地介紹出產品的特點及功能.

還有就是終生學習,學習程式碼是這學期的課程,但是這是入門,往後的路還很長所以必須達到終生學習的目標. 

 

應用資料(網址):

1.Openshift:https://www.openshift.com/

2.GitHub：https://github.com/

3.2014 CP Project：https://140.130.17.17:8443/?id=982

4.2014 CP final project：https://140.130.17.17:8443/?id=986
        """

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

