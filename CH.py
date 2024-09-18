from flask import Flask, jsonify

app = Flask(__name__)

# Function to convert decimal to binary
def dec_to_bin(dec):
    return bin(dec)[2:]

# Function to convert decimal to hexadecimal
def dec_to_hex(dec):
    return hex(dec)[2:]

# Function to convert binary to decimal
def bin_to_dec(bin_str):
    return int(bin_str, 2)

# Function to convert hexadecimal to decimal
def hex_to_dec(hex_str):
    return int(hex_str, 16)

# Define a route for the conversion API
@app.route('/convert/<value>/<input_format>/<output_format>', methods=['GET'])
def convert(value, input_format, output_format):
    try:
        # Convert the input value to decimal based on the input_format
        if input_format == 'dec':
            dec = int(value)
        elif input_format == 'bin':
            dec = bin_to_dec(value)
        elif input_format == 'hex':
            dec = hex_to_dec(value)
        else:
            return jsonify({'error': 'Invalid input_format'}), 400

        # Convert the decimal value to the desired output format
        if output_format == 'dec':
            result = dec
        elif output_format == 'bin':
            result = dec_to_bin(dec)
        elif output_format == 'hex':
            result = dec_to_hex(dec)
        else:
            return jsonify({'error': 'Invalid output_format'}), 400

        # Return the conversion result as a JSON response
        return jsonify({'result': result})
    except ValueError:
        # Return an error if the input value is invalid
        return jsonify({'error': 'Invalid value format'}), 400

# Run the Flask application on host 0.0.0.0 and port 8080
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
