from flask import Flask, request, Response, render_template
import jinja2
import pdfkit

service = Flask(__name__)

# Open route to check whether server is up and running
@service.route('/')
def app():
    return 'Hello backend!'


@service.route("/pdf-1", methods=['GET'])
def downloader_1():
    example_data = "Hello, Python Pizza Berlin!"
    result = generate_pdf_with(example_data, 'template_1.html')
    return result


@service.route("/pdf-2", methods=['GET'])
def downloader_2():
    input = request.args
    result = generate_pdf_with(input, 'template_2.html')
    return result


@service.route("/pdf-3", methods=['POST'])
def downloader_3():
    input = request.get_json()
    result = generate_pdf_with(input, 'template_3.html')
    return result


def generate_pdf_with(data_input, template):
    opt = {
        'margin-top': '2.0cm',
        'margin-right': '2.0cm',
        'margin-bottom': '2.0cm',
        'margin-left': '2.0cm',
        'encoding': "UTF-8"
    }
    pdf = pdfkit.from_string(render_template(template, data=data_input), output_path=False, options=opt)
    return Response(pdf, mimetype='application/pdf')


# Run our application
if __name__ == '__main__':
    service.run(debug=True,host='0.0.0.0')
