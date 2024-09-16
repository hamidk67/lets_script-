from flask import Flask, request, jsonify

app = Flask(__name__)

def dec_to_bin(dec):
    return bin(dec)[2:]

def dec_to_hex(dec):
    return hex(dec)[2:]

def bin_to_dec(bin_str):
    return int(bin_str, 2)

def hex_to_dec(hex_str):
    return int(hex_str, 16)

@app.route('/convert', methods=['GET'])
def convert():
    number = request.args.get('number')
    from_base = request.args.get('from')
    to_base = request.args.get('to')

    if not number or not from_base or not to_base:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        if from_base == 'dec':
            dec = int(number)
        elif from_base == 'bin':
            dec = bin_to_dec(number)
        elif from_base == 'hex':
            dec = hex_to_dec(number)
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

    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
