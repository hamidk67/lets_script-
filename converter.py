from flask import Flask

app = Flask(__name__)

def convert(value, input_format, output_format):
    try:

        if input_format == 'dec':
            num = int(value)
        elif input_format == 'bin':
            num = int(value, 2)
        elif input_format == 'hex':
            num = int(value, 16)
        else:
            return "Invalid output format....... Usage Guide:    Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.     Valid formats: dec (decimal), bin (binary), hex (hexadecimal)    Example: /convert/10/dec/bin will convert decimal 10 to binary."

        if output_format == 'dec':
            return str(num)
        elif output_format == 'bin':
            return bin(num)[2:]
        elif output_format == 'hex':
            return hex(num)[2:]
        else:
            return "Invalid output format........ Usage Guide:    Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.     Valid formats: dec (decimal), bin (binary), hex (hexadecimal)    Example: /convert/10/dec/bin will convert decimal 10 to binary."
    except ValueError: 
        return "Usage Guide:    Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.     Valid formats: dec (decimal), bin (binary), hex (hexadecimal)    Example: /convert/10/dec/bin will convert decimal 10 to binary."       
   
@app.route('/convert/<value>/<input_format>/<output_format>', methods=['GET'])
def convert_endpoint(value, input_format, output_format):
    result = convert(value, input_format, output_format)
    return result

@app.route('/', defaults={'path': '/convert/c/hex/dec'})
@app.route('/<path:path>')
def usage_guide(path):
    return '''Usage Guide:
    Access the endpoint /convert/<value>/<input-format>/<output-format> to convert values.
    Valid formats: dec (decimal), bin (binary), hex (hexadecimal)
    Example: /convert/10/dec/bin will convert decimal 10 to binary.'''

if __name__ == '__main__':
    app.run(port=8081)
