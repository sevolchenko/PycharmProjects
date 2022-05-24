import os

from flask import Flask
from flask import request, render_template
from PIL import Image
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploaded_photos')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST', 'GET'])
def convert():
    if 'submit' in request.form and 'image_to_convert' in request.files:
        try:
            image_width = int(request.form['width'])
            image_monochrome = int(request.form['monochrome'])
            image_to_convert = Image.open(request.files['image_to_convert']).convert('L')
            new_image = image_to_convert.resize(([image_width, int(image_width * image_to_convert.size[1] / image_to_convert.size[0])]))
            for row in range(new_image.size[1]):
                for col in range(new_image.size[0]):
                    new_image.putpixel((col, row), 255 if new_image.getpixel((col, row)) > image_monochrome else 0)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], request.files['image_to_convert'].filename)
            new_image.save(full_filename)

            rows = []
            for row in range(new_image.size[1]):
                rows.append('')
                counter = 0
                for col in range(new_image.size[0]):
                    if new_image.getpixel((col, row)) == 0:
                        counter += 1
                    elif counter != 0:
                        rows[row] += (' ' + str(counter))
                        counter = 0
                if counter != 0:
                    rows[row] += (' ' + str(counter))

            cols = []
            for col in range(new_image.size[0]):
                cols.append('')
                counter = 0
                for row in range(new_image.size[1]):
                    if new_image.getpixel((col, row)) == 0:
                        counter += 1
                    elif counter != 0:
                        cols[col] += (' ' + str(counter))
                        counter = 0
                if counter != 0:
                    cols[col] += (' ' + str(counter))

            rows = pd.DataFrame(rows)
            rows.style.hide(axis='index', names=False).hide(axis='columns')
            cols = pd.DataFrame(cols).T
            cols.style.hide(axis='columns').hide(axis='index')
            rows = rows.to_html(header=False, index=False, classes=['dataframe__left'])
            cols = cols.to_html(header=False, index=False, classes=['dataframe__bottom'])

            return render_template('convert.html', image_path=full_filename, table_left=rows, table_bottom=cols, width=new_image.size[0], height=new_image.size[1])
        except Exception as e:
            print(e)
    return render_template('convert.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
