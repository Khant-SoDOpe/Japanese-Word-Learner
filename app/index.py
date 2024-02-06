from flask import Flask, render_template, request, redirect
import random

class QuizApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
        self.romaji = ["a","i","u","e","o","ka","ki","ku","ke","ko","sa","shi","su","se","so","ta","chi","tsu","te","to","na","ni","nu","ne","no","ha","hi","fu","he","ho","ma","mi","mu","me","mo","ya","yu","yo","ra","ri","ru","re","ro","wa","wo","n"]
        self.katakana = ["ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","サ","シ","ス","セ","ソ","タ","チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","マ","ミ","ム","メ","モ","ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン"]
        self.random_number = None
        self.hiraga = None
        self.choose = None

    def index(self):
        return render_template('index.html')

    def aboutus(self):
        return render_template('about_us.html')

    def select(self):
        return render_template("select.html")

    def hiragana_quiz(self):
        self.choose = "/hiragana"
        self.random_number = random.randint(0, 45)
        self.hiraga = self.hiragana[self.random_number]
        return render_template("quiz.html", hiraga=self.hiraga)

    def katakana_quiz(self):
        self.choose = "/katakana"
        self.random_number = random.randint(0, 45)
        self.hiraga = self.katakana[self.random_number]
        return render_template("quiz.html", hiraga=self.hiraga)

    def loading(self):
        answer = request.form.get("answer").lower()
        if self.romaji[self.random_number] == answer:
            return redirect(self.choose)
        else:
            status = " again"
            CorI = "Status = Incorrect"
            return render_template("quiz.html", hirag=status, hiraga=self.hiraga, CorI=CorI)

    def run(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/about_us', 'aboutus', self.aboutus)
        self.app.add_url_rule('/select', 'select', self.select)
        self.app.add_url_rule('/hiragana', 'hiragana', self.hiragana_quiz)
        self.app.add_url_rule('/katakana', 'katakana', self.katakana_quiz)
        self.app.add_url_rule('/loading', 'loading', self.loading, methods=['POST'])
        self.app.run()

if __name__ == "__main__":
    app = QuizApp()
    app.run()
