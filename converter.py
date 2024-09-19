from flask import Flask, Response
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)
logging.info('This is an info message')
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

message = """try to access this endpoint --> /convert/value/input-format/output-format \n
Valid parameter values: \n
value: Any alphanumeric value, but has to be in a format specified by input-format and output-format: \n
dec: Specifies a decimal (base-10) format \n
bin: Specifies a binary (base-2) format \n
hex: Specifies a hexadecimal (base-16) format\n
"""

def convert(value, input_format, output_format):
    try:

        if input_format == 'dec':
            num = int(value)
        elif input_format == 'bin':
            num = int(value, 2)
        elif input_format == 'hex':
            num = int(value, 16)
        else:
            #return "Invalid output format....... Usage Guide:    Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.     Valid formats: dec (decimal), bin (binary), hex (hexadecimal)    Example: /convert/10/dec/bin will convert decimal 10 to binary."
            return Response(message, mimetype='text/plain')

        if output_format == 'dec':
            return str(num)
        elif output_format == 'bin':
            return bin(num)[2:]
        elif output_format == 'hex':
            return hex(num)[2:]
        else:
            #return "Invalid output format........ Usage Guide:    Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.     Valid formats: dec (decimal), bin (binary), hex (hexadecimal)    Example: /convert/10/dec/bin will convert decimal 10 to binary."
            return Response(message, mimetype='text/plain')
    except ValueError: 
        #return "Usage Guide:    Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.     Valid formats: dec (decimal), bin (binary), hex (hexadecimal)    Example: /convert/10/dec/bin will convert decimal 10 to binary."       
        return Response(message, mimetype='text/plain')
   
@app.route('/convert/<value>/<input_format>/<output_format>', methods=['GET'])
def convert_endpoint(value, input_format, output_format):
    result = convert(value, input_format, output_format)
    return result

@app.route('/', defaults={'path': '/convert/c/hex/dec'})
@app.route('/<path:path>')
def usage_guide(path):
    #return '''Usage Guide:
    #Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.
    #Valid formats: dec (decimal), bin (binary), hex (hexadecimal)
    #Example: /convert/10/dec/bin will convert decimal 10 to binary.'''
    return Response(message, mimetype='text/plain')
@app.route('/health', methods=['GET'])
def health_check():
    return "OK"
if __name__ == '__main__':
 
    # Run the app with multiple workers
    app.run(debug=False, host='0.0.0.0', port=8080, threaded=True)
