from flask import Flask,render_template,request,redirect
import random

hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']

romaji = ["a","i","u","e","o","ka","ki","ku","ke","ko","sa","shi","su","se","so","ta","chi","tsu","te","to","na","ni","nu","ne","no","ha","hi","fu","he","ho","ma","mi","mu","me","mo","ya","yu","yo","ra","ri","ru","re","ro","wa","wo","n"]

katakana =["ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","サ","シ","ス","セ","ソ","タ","チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","マ","ミ","ム","メ","モ","ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about_us")
def aboutus():
    return render_template('about_us.html')

@app.route("/select")
def select():
    return render_template("select.html")

@app.route("/hiragana")
def hiragan():
    global random_number,hiraga,choose
    choose = "/hiragana"
    random_number = random.randint(0, 45)
    hiraga = hiragana[random_number]
    return render_template("quiz.html",hiraga=hiraga)

@app.route("/katakana")
def kataka():
    global random_number,hiraga,choose
    choose = "/katakana"
    random_number = random.randint(0, 45)
    hiraga = katakana[random_number]
    return render_template("quiz.html",hiraga=hiraga)

@app.route("/loading",methods=["POST"])
def loading():
    answer = request.form.get("answer").lower()
    print(answer,romaji[random_number],random_number,hiragana[random_number])
    if romaji[random_number] == answer:
        return redirect(choose)
    else:
        status = " again"
        CorI = "Status = Incorrect"
        return render_template("quiz.html",hirag=status,hiraga=hiraga,CorI=CorI)

if __name__ == "__main__":
    app.run()