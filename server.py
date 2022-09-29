from flask import Flask  , render_template

    
    
app = Flask(__name__)    
    
# @app.route('/')          
# def home():
#     return render_template('play.html')
@app.route('/')
@app.route('/play')          
def play():
    num = 3 
    return render_template('play.html', num=num)

@app.route('/play/<int:num>')
def play1(num):
    return render_template('play.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def play2(num ,color):
    return render_template('play.html', num=num ,color=color)


if __name__=="__main__":    
    app.run(debug=True)    