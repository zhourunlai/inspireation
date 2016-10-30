# coding:utf-8

from flask import Flask, render_template, request, Response, jsonify
from werkzeug import secure_filename
import inspiration_image_creater_for_development
import inspiration_image_creater_for_production

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/creation')
def creation():
    return render_template('creation.html')


@app.route('/inspiration')
def inspiration():
    return render_template('inspiration.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    content = request.args.get('content')
    # elements = [
    #     {
    #         'path': 'element/cao1.svg',
    #         'x': 80,
    #         'y': 60,
    #     },
    #     {
    #         'path': 'element/cao2.svg',
    #         'x': 100,
    #         'y': 60,
    #     },
    #     {
    #         'path': 'element/shu1.svg',
    #         'x': 160,
    #         'y': 120,
    #     },
    # ]
    elements = inspiration_image_creater_for_production.main(content)
    return render_template('result.html', elements=elements)


@app.route('/canvas')
def canvas():
    return render_template('canvas.html')


@app.route('/handle', methods=['GET', 'POST'])
def add():
    content = request.args.get('content')
    query, path = inspiration_image_creater_for_development.main(content)
    result = {
        "query": query,
        "path": path,
    }
    return jsonify(result=result)


@app.route('/element/<filename>')
def show(filename):
    image = file("element/" + filename)
    return Response(image, mimetype="image/svg+xml")


@app.route('/json', methods=['GET', 'POST'])
def json():
    result = {
        "element1": {
            'path': 'element/cao1.svg',
            'x': 80,
            'y': 60,
        },
        "element2": {
            'path': 'element/cao2.svg',
            'x': 100,
            'y': 60,
        },
        "element3": {
            'path': 'element/shu1.svg',
            'x': 160,
            'y': 120,
        }
    }
    return jsonify(result=result)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        path = '/var/www/uploads/' + secure_filename(f.filename)
        f.save(path)
        return path
    if request.method == 'GET':
        return 'file is ok'


@app.route('/fenci', methods=['GET', 'POST'])
def fenci():
    import jieba
    content = request.args.get('content')
    seg_list = jieba.cut(content, cut_all=True)
    seg = "/ ".join(seg_list)
    tags = jieba.analyse.extract_tags(content, topK=1)
    tag = tags[0]
    result = {
        'seg': seg,
        'tag': tag
    }
    return jsonify(result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
