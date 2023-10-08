from flask import Flask, render_template, request

app = Flask(__name__)

# Embed the flag with ID 105 into the database
files = {
    '105': 'jctf{flag_here}'
}

# IDOR Challenge - Allow users to access files without proper authorization
@app.route('/files', methods=['GET'])
def view_file():
    file_id = request.args.get('file_id')
    
    if file_id == '98':
        return render_template('flag.html')
    elif file_id.isdigit() and 0 <= int(file_id) <= 97:
        return render_template('index.html', file_content=f'File content for ID {file_id}')
    else:
        return render_template('index.html')

# Home page with user login
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
