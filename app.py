from flask import Flask, redirect, request

app = Flask(__name__)

def extract_params(request):
    url = request.args.get('url') or request.form.get('url')
    status = request.args.get('status', 302) or request.form.get('status', 302)
    return url, status

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'CONNECT', 'TRACE'])
def handle_request():
    url, status = extract_params(request)

    if url:
        try:
            status = int(status)
            if status in [301, 302, 303, 307, 308]:

                return redirect(url, code=status)
            else:
                return "Invalid status code. Use 301, 302, 303, 307, or 308.", 400
        except ValueError:
            return "Invalid status code. Use 301, 302, 303, 307, or 308.", 400
    else:
        return "Missing 'url' parameter in your request.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
