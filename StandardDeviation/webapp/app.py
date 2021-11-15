from flask import Flask, request, render_template
import MyMath

app = Flask(__name__)

math_test = None


@app.route('/')
def index():
    global math_test
    math_test = MyMath()
    return render_template('index.html')


@app.route('/background_process/<num>')
def background_process(num):
    global math_test
    math_test.num_list.append(float(num))
    return render_template("nothing")


@app.route('/result')
def result():
    max = math_test.find_max_number()
    avg = math_test.calculate_average()
    stddev = math_test.calculate_standard_deviation();


if __name__ == '__main__':
    app.run(debug=True)
