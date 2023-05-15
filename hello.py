from flask import Flask
from flask import render_template
from flask import make_response
from flask import redirect, url_for, abort

ungdung = Flask(__name__, static_folder='C:\\Users\\higho\\Downloads\\shpCaMau\\templates\\static')

@ungdung.route("/")
def index():
  return redirect(url_for('login'))

@ungdung.route("/login")
def login():
  abort(401)
@ungdung.route('/monhoc/')
def learn():
    chuoi = "Đây là trang môn học!"
    return chuoi
@ungdung.route('/monhoc/<tenmon>')
def subject(tenmon):
    chuoi = "Đây là trang môn học"
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + monhoc
    return chuoi

@ungdung.route("/sinhvien/")
def students ():
    chuoi = "Đây là trang các khóa học"
    return chuoi
@ungdung.route("/sinhvien/<int:namhoc>")
def school_year(namhoc):
    chuoi = "Đây là năm học"
    nam = str(namhoc).upper()
    if nam == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + nam
    return chuoi

@ungdung.route("/hello")
@ungdung.route("/hello/<name>")
def xinchao(name = None):
    return render_template('hello.html', name = name)

@ungdung.route("/languages")
def languages(languages = None):
  languages = [ {'STT':1, 'ten': "Python"}, {'STT':2, 'ten': "Java"} , {'STT':3, 'ten': "C++"}]
  languages.append({'STT':4, 'ten': ".NET" })
  languages.append({'STT':5, 'ten': "Matlab" })
  return render_template('abc.html', ngon_ngu = languages)

if __name__ == "__main__":
  ungdung.run(port = 5050)

  



  
