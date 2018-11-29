from flask import Flask, Response, render_template
import jinja2
import pdfkit

service = Flask(__name__)

# Open route for PDF service
@service.route("/pdf", methods=['POST'])
def downloader():
    result = simple_template()
    return Response(result, mimetype='application/pdf')


def simple_template():
    opt = {
        'margin-top': '2.0cm',
        'margin-right': '2.0cm',
        'margin-bottom': '2.0cm',
        'margin-left': '2.0cm',
        'encoding': "UTF-8"
    }
    example_user = "This guy"
    pdf = pdfkit.from_string(render_template('template.html', user=example_user), output_path=False, options=opt)
    return pdf

# Open route to check whether server is up and running
@service.route('/')
def app():
    return 'Hello PDF!'


if __name__ == '__main__':
    service.run(debug=True,host='0.0.0.0')
