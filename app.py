from flask import Flask, request, json,Response
import os
app = Flask(__name__)
cwd = os.getcwd()


@app.route("/")
def hello():
    return "Service health check OK!\n"

@app.route('/pemtoppk',methods=["POST"])
def pemtoppk():
    if request.method == 'POST':
        try:
            output_filename = request.form.get('output_filename')
            pem_key = request.form.get('pem_key')
            print("pem_key: ", pem_key)
            ppkKey = os.system("puttygen " + pem_key + " -O private -o "+ ppkFileName)
            print("ppkKey: ", ppkKey)
            resp = Response(ppkKey, status=200, mimetype='text/html')
            return resp
        except Exception as ex:
            print (ex)
            return Response(error = ex, status=400, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
