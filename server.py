from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def temp_welcome():
    return render_template('index.html', welcome=True)

# Level 1
@app.route('/play')
def play_boxes():
    return render_template('index.html', level=1, num=3, color='lightskyblue')

# Level 2
@app.route('/play/<int:num>')
def play_boxes_num(num):
    return render_template('index.html', level=2, num=num, color='lightskyblue')

# Level 3
@app.route('/play/<int:num>/<string:color>')
def play_boxes_num_color(num, color):
    return render_template('index.html', level=3, num=num, color=color)

if __name__=='__main__':
    app.run(debug=True)