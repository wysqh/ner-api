from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# rule with <converter: variable_name>
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/api/zhRelationExtract', methods=['POST', 'GET'])
def relation_extract():
    error = None
    if request.method == 'GET':
        entity1 = request.args.get('e1', '')
        entity2 = request.args.get('e2', '')
        sentence = request.args.get('s', '')
    else:
        entity1 = request.form['e1']
        entity2 = request.form['e2']
        sentence = request.form['s']

    if not check_para(entity1, entity2, sentence):
        error = "some parameters are not assigned!"
        return error

    return "entity1: %s, entity2: %s, sentence: %s" % (entity1, entity2, sentence)


def check_para(*args):
    check_f = True
    for i in range(len(args)):
        if len(args[i]) == 0:
            check_f = False
            break
    for i in range(len(args)):
        print("%d, %s" % (i, args[i]))

    return check_f


if __name__ == '__main__':
    app.run()
