from flask import Flask, render_template, request
from pipeline import InterFacePipeline

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    pipeline = InterFacePipeline()
    result = None
    error = None
    if request.method == 'POST':
        try:
            fields = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
            values = []
            for f in fields:
                v = request.form.get(f)
                if v is None or v.strip == '':
                    raise ValueError(f'the {f} is required')
                values.append(float(v))
                
            pred = pipeline.run(values)
            category = ['This is Data for a Healthy Heart ❤️', 'This is Data for a Defective Heart 💔']
            result = category[int(pred[0])]
        except Exception as x:
            error = str(x)
    return render_template('prediction.html', result=result, error=error)
    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)