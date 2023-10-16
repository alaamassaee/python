from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form template
form_template = """
<!doctype html>
<html>
  <body>
    <form method="post" action="/">
      <label for="input_text">Enter Text:</label>
      <input type="text" id="input_text" name="input_text" required>
      <input type="submit" value="Submit">
    </form>
    <p>Output: {{ output }}</p>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def hello():
    output = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Process input_text here as needed
        # For example, you can perform some operations on input_text and store the result in the 'output' variable
        # For now, let's just echo the input_text back
        output = input_text
    return render_template_string(form_template, output=output)

if __name__ == '__main__':
    # Run the Flask app on port 80
    app.run(host='0.0.0.0', port=80)

