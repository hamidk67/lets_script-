from flask import Flask, jsonify

app = Flask(__name__)

def dec_to_bin(dec):
    return bin(dec)

def dec_to_hex(dec):
    return hex(dec)

def bin_to_dec(bin_str):
    return int(bin_str, 2)

def hex_to_dec(hex_str):
    return int(hex_str, 16)

@app.route('/convert/<value>/<from_base>/<to_base>', methods=['GET'])
def convert(value, from_base, to_base):
    if from_base == 'dec':
        dec = int(value)
    elif from_base == 'bin':
        dec = bin_to_dec(value)
    elif from_base == 'hex':
        dec = hex_to_dec(value)
    else:
        return jsonify({'error': 'Invalid from_base'}), 400

    if to_base == 'dec':
        result = dec
    elif to_base == 'bin':
        result = dec_to_bin(dec)
    elif to_base == 'hex':
        result = dec_to_hex(dec)
    else:
        return jsonify({'error': 'Invalid to_base'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8085)
