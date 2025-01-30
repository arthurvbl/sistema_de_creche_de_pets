from bottle import run, Bottle, template, route, static_file

app = Bottle()

@app.route('/')
def index():
    return template('index')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)