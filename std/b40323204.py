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
        self.name = '張筱萱'
        # 你的學號
        self.number = '40323204'
        # 你的班級
        self.classes = '四設計一乙'
        # 你的 github repository url
        self.github_repo_url = 'https://github.com/hsungchang/-2014cp_project_40323204'
        # 你的 openshift app
        self.openshift_url = 'http://2014cp-40323204.rhcloud.com/'
        # 你的自評
        self.evaluation = [('Project 7', 90), ('Project 8', 85), ('Project 9', 90)]
        # 你的照片 url
        self.photo_url = 'https://copy.com/a10O9YyCzAgz'
        # 這裡是心得
        self.my_remark = """
      <p><span style="font-size: 18px; background-color: #ffff00;">期末報告</span></p>
<p><span style="font-size: 18px;">班級:四設計一乙</span></p>
<p><span style="font-size: 18px;">學號:40323204</span></p>
<p><span style="font-size: 18px;">姓名:張筱萱</span></p>
<hr>
<p><span style="font-size: 18px;"><span>這個 Github 程式專案將從無到有, 串連 2014 Fall 計算機程式的課程內容, 利用 Github, Bitbucket 與 OpenShift 同步管理程式碼</span></span></p>
<p><span style="font-size: 18px; background-color: #ffff00;">第一步-在近端執行猜數字遊戲</span></p>
<p><span style="font-size: 18px;"><span><span> 代碼可從課文中(<span> </span><a href="http://cpgroup.kmol.info/inventwithpythontw/">http://cpgroup.kmol.info/inventwithpythontw/</a>)的第四章下載(<span><a href="http://inventwithpython.com/hello.py">http://inventwithpython.com/hello.py</a>)</span></span></span></span></p>
<p><span style="font-size: 18px;"><span><span><span> <span style="text-decoration: underline;">程式內容</span></span></span></span></span></p>
<pre class="brush: python; fontsize: 100; first-line: 1; toolbar: false; "># This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken &lt; 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess &lt; number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess &gt; number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)</pre>
<p><span style="text-decoration: underline;"><span style="font-size: 18px;"> 執行協果</span></span></p>
<pre class="brush: python; fontsize: 100; first-line: 1; toolbar: false; ">&gt;V:\IDE\Python33\pythonw -u "22"
Hello! What is your name?sandy

Well, sandy, I am thinking of a number between 1 and 20.
Take a guess.
5
Your guess is too high.
Take a guess.
2
Your guess is too low.
Take a guess.
8
Your guess is too low.
Take a guess.
10
Your guess is too low.
Take a guess.
3
Your guess is too low.
Take a guess.
9
Your guess is too high.
Nope. The number I was thinking of was 19
&gt;Exit code: 0</pre>
<p><span style="font-size: 18px;"><span style="background-color: #ffff00;">第二步</span><span style="background-color: #ffff00;">-更改LEO內容使得遊戲可在遠端執行</span><br></span></p>
<p><span style="font-size: 18px;">下載老師所提供的程式再根據程式進行修改</span></p>
<p><span style="font-size: 18px;">根據老師影片的作法更改<a href="http://vimeo.com/114514650">http://vimeo.com/114514650</a></span></p>
<p><span style="font-size: 18px;">補充:print須改為return才能在遠端中執行</span></p>
<p><span style="font-size: 18px;"><span style="background-color: #ffff00;">第三步</span><span style="background-color: #ffff00;">-在 Github 建立起始倉儲</span></span></p>
<p><span style="font-size: 18px;">(1)在 Github 建立倉儲, 名稱為 -2014cp_project_40323204</span></p>
<p><span style="font-size: 18px;">-<a href="https://github.com/hsungchang/-2014cp_project_40323204">https://github.com/hsungchang/-2014cp_project_40323204</a></span></p>
<p><span style="font-size: 18px;">其中內建 README, 並且選擇使用授權為 GNU gpl 3.0.</span></p>
<p><span style="font-size: 18px;">(2)clone 倉儲資料到近端</span></p>
<p><span style="font-size: 18px;">指令為:git clone <a href="https://github.com/hsungchang/-2014cp_project_40323204.git">https://github.com/hsungchang/-2014cp_project_40323204.git</a>(由github所提供的網址)</span></p>
<p><span style="font-size: 18px;"><span>執行完成後, 在 V:\ 就會有一個 -2014cp_project_40323204 目錄, 內容即為倉儲資料</span></span></p>
<p><span style="font-size: 18px;"><img src="https://copy.com/7cXaU1wiOysnlhMW" alt="" width="631" height="358"></span></p>
<p><span style="font-size: 18px;"> (黃色部分為網址)</span></p>
<p><span style="font-size: 18px;"> 老師所提供<span>完成後的程式版本: </span><a href="https://github.com/chiamingyen/2014cp_project/releases/tag/v1.0">https://github.com/chiamingyen/2014cp_project/releases/tag/v1.0</a></span></p>
<p><span style="font-size: 18px;">套用 CherryPy 程式框架格式</span></p>
<p><span style="font-size: 18px;">利用 <a href="https://github.com/chiamingyen/2014cp_project/blob/master/setup.py">setup.py</a> 安裝 cherrypy 模組</span></p>
<p><span style="font-size: 18px;">將程式存為 <a href="https://github.com/chiamingyen/2014cp_project/blob/master/wsgi.py">wsgi.py</a></span></p>
<p><span style="font-size: 18px;">套用 cherrypy 框架程式格式</span></p>
<p><span style="font-size: 18px;"><span style="background-color: #ffff00;">第四步</span><span style="background-color: #ffff00;">-將遊戲需在遠端執行所需的所有東西推回github(<span style="color: #ff0000;">在推回前一定要把名字和email改為自己的</span>)</span></span></p>
<p><span style="font-size: 18px;">指令為:(1)cd <span>-2014cp_project_40323204(此指令是指進入資料夾)</span></span></p>
<p><span style="font-size: 18px;">           (2)git add .</span></p>
<p><span style="font-size: 18px;">           (3)git commit -m "add 40323204"</span></p>
<p><span style="font-size: 18px;">           (4)git push</span></p>
<p><span style="font-size: 18px;">推回成功後即所有東西都傳回了github</span></p>
<p><span style="font-size: 18px;">所需的東西可參考老師的:<a href="https://github.com/chiamingyen/2014cp_project">https://github.com/chiamingyen/2014cp_project</a></span></p>
<p><span style="font-size: 18px; background-color: #ffff00;">第五步<span style="background-color: #ffffff;"><span style="background-color: #ffff00;">-</span><span><span style="background-color: #ffff00;">建立 OpenShift Python 3.3 應用程式</span><span style="background-color: #ffff00;"> (同時處理近端 V:\home\.ssh\id_rsa 與 OpenShift setting 上私鑰與公鑰的權限認證)</span></span></span></span></p>
<p><span style="font-size: 18px;">(1)OpenShift 上的 1b 共同鑰匙</span><span style="font-size: 18px;">近端: </span><a style="font-size: 18px;" href="http://cpgroup.kmol.info/public/cp/2014fall/1b/">http://cpgroup.kmol.info/public/cp/2014fall/1b/</a></p>
<p><span style="font-size: 18px;">(2)<span>利用 Github 倉儲作為程式碼, 完成後 OpenShift 上的程式碼與此階段的 Github 程式碼為同一版本</span></span></p>
<p><span style="font-size: 18px;">詳細步驟:</span></p>
<p><span style="font-size: 18px;"> <img src="https://copy.com/CPJ10Fz7PhidZGtW" alt="" width="615" height="329"></span></p>
<p><span style="font-size: 18px;"><img src="https://copy.com/tGpllTWylsGsMt6l" alt="" width="617" height="338"></span></p>
<p> <img src="https://copy.com/DKVX1kC892TDLMpy" alt="" width="615" height="409"></p>
<p><span style="font-size: 18px;"> <img src="https://copy.com/riYBryGyBUqTHkt7" alt="" width="609" height="379"></span></p>
<p><img src="https://copy.com/Qwoc64DRgM2QWAnF" alt="" width="615" height="180"></p>
<p><img src="https://copy.com/Pk6E67MZ3Ll02Qvi" alt="" width="615" height="294"></p>
<hr>
<p><span style="font-size: 18px; background-color: #ffff00;"> 補充內容:</span></p>
<p><span style="font-size: 18px;">(1)個人在班上協同倉儲中的推送連結與推送紀錄說明</span></p>
<p><span style="font-size: 18px;"> <span>Github 協同倉儲</span><span>乙班命名為 </span><a href="https://github.com/Openandgit/2014cpb_final_project-">2014cpb_final_project</a></span></p>
<p><span style="font-size: 18px;">先輸入指令git clone <a href="https://github.com/Openandgit/2014cpb_final_project-.git">https://github.com/Openandgit/2014cpb_final_project-.git</a></span></p>
<p><span style="font-size: 18px;">資料夾內會多出2014cpb_final_project</span></p>
<p><span style="font-size: 18px;">將自己github所有的資料丟進2014cpb_final_project</span></p>
<p><span style="font-size: 18px;">接著輸入指令git add .</span></p>
<p><span style="font-size: 18px;">git commit -m "add 檔案名稱"</span></p>
<p><span style="font-size: 18px;">git push即完成</span></p>
<p><span style="font-size: 18px; color: #ff0000;">(假如push後失敗可能是因為自己在推回去時有人先推了東西上去所以自己的資料夾少了東西，這時候只要輸入指令git pull讓自己的資料夾跟遠端同步一次在push就可以成功)</span></p>
<p><span style="font-size: 18px;">(2)個人在班上協同網站上的連結與說明</span></p>
<p><span style="font-size: 18px;"> </span><span style="font-size: 18px;">OpenShift 上的 1b 共同網站倉儲</span><a style="font-size: 18px;" href="ssh://5490ef895973caf9a70000d4@cpb-nfutaiwan.rhcloud.com/~/git/cpb.git/">ssh://5490ef895973caf9a70000d4@cpb-nfutaiwan.rhcloud.com/~/git/cpb.git/</a></p>
<p><span style="font-size: 18px;"> 首先git clone <a href="ssh://5490ef895973caf9a70000d4@cpb-nfutaiwan.rhcloud.com/~/git/cpb.git/">ssh://5490ef895973caf9a70000d4@cpb-nfutaiwan.rhcloud.com/~/git/cpb.git/</a></span></p>
<p><span style="font-size: 18px;">v槽內會增加一個cpb的資料夾</span></p>
<p><span style="font-size: 18px;"> <img src="https://copy.com/4vsK7p7SKdgltv9B" alt="" width="253" height="371"></span></p>
<p><span style="font-size: 18px;"> 在資料夾中有一個叫std的資料夾</span></p>
<p> <img src="https://copy.com/kv9iMh3KxiVQdDDy" alt=""></p>
<p><span style="font-size: 18px;">點進std後會看到example.py</span></p>
<p><img src="https://copy.com/DYwnEEaXrWGdvSNp" alt=""></p>
<p><span style="font-size: 18px;">將它拉近scite內更改(也可拉同學得但切記要另存新檔)</span></p>
<p><img src="https://copy.com/GDsHaFacYtVIZLTq" alt=""></p>
<p><span style="font-size: 18px;"> 更改完後git add .</span></p>
<p><span style="font-size: 18px;">             git commit -m "add 40323204"</span></p>
<p><span style="font-size: 18px;">             git push即完成</span></p>
<p><span style="font-size: 18px;">自己的學號變成粉紅色即為成功</span></p>
<p><span style="font-size: 18px;"> <img src="https://copy.com/EZxURbTQ8QG0SJBa" alt="" width="687" height="255"></span></p>
<p><span style="font-size: 18px;">我的執行結果:<a href="http://cpb-nfutaiwan.rhcloud.com/40323204/">http://cpb-nfutaiwan.rhcloud.com/40323204/</a></span></p>
<hr>
<p><span style="font-size: 18px; background-color: #ffff00;">心得:</span></p>
<p><span style="font-size: 18px;">這一學期我對於python近端及遠端懂了很多，從一開始什麼都不懂到現在懂了不少，我不敢說自己都會了，但我覺得自己學到的比別人還多，剛開始聽到作業是做出一個猜數字遊戲的時候覺得根本不可能，在中間的幾次課堂老師教了很多也有許多通學陸陸續續的開始交期末報告的一小部分，雖然都只有第一步但我還是很緊張，因為自己完全不懂該怎麼做，還停在什麼都沒有的狀態下，我很意外我是第一個讓遊戲在openshift上執行的人，這讓我從原本的緊張變為放鬆，因為我不僅沒有比別人弱甚至我還可以去教別人，看到同學用佩服得眼神看著我和稱讚我，老實說我是非常的驕傲和高興的，我覺得我花在上面的時間沒有浪費，未來如果還有機會我會想要學得更深學得更多，非常感謝老師在這一學期的教導，也很謝謝班上同學的幫忙更要感謝犧牲時間教導我們的助教，計算機程式讓我學到了:電腦是如何運作的，並與之溝通。</span></p>
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

