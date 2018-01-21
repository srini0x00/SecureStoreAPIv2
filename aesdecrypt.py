import Crypto
import Crypto.Random
from Crypto.Cipher import AES
import base64
import sys

def pad_data(data):
    if len(data) % 16 == 0:
        return data
    databytes = bytearray(data)
    padding_required = 15 - (len(databytes) % 16)
    databytes.extend(b'\x80')
    databytes.extend(b'\x00' * padding_required)
    return bytes(databytes)

def unpad_data(data):
    if not data:
        return data

    data = data.rstrip(b'\x00')
    if data[-1] == 128: # b'\x80'[0]:
        return data[:-1]
    else:
        return data

def generate_aes_key():
    rnd = '35e685a1411a605852ec1045ef7f16f10e68dc18bdc1f13fa240a6996edb306c'
    rnd = rnd.decode('hex')
    return rnd

def encrypt(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = pad_data(data)
    return aes.encrypt(data)

def decrypt(key, iv, data):
    data = data.decode('base64')
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = aes.decrypt(data)
    return unpad_data(data)

def test_crypto (input):
    key = generate_aes_key()
    iv = '00000000000000000000000000000000'
    iv = iv.decode('hex')
    #iv = generate_aes_key() # get some random value for IV
    #msg = '{"actionType":"AUTHENTICATION4CITI","deviceToken":"","appID":"com.aiahk.ipos","deviceID":"F9F983D3-D71F-46B0-A32E-77EDBFC2A00B","loginId":"ERGRTG","deviceName":"iPad5,3","lang":"en-SG","passWord":"dfgfgeth","random":"448834000"}'
    #code = encrypt(key, iv, input)
    #print code.encode('hex')
    #iv = generate_aes_key() # change the IV to something random
    #code = 'E704AAD5C880685B84D3A78EBF9DBF338613076F64E225DC170547C3A0113F7B621A96D55DA64FC1BD33A237C0FBF3C7BF0E777F8A8CCEFD8B2A27423AA2A2A058A2DDE2783A2C909F94A3AF205CC980FE46FEF9D1935A2BCF58E84ED2F4C36A38CE769496E63A8518B6C6E8BEAEB4F5CDDF8F81968A4FBC3A7883FB03C83799590D248A330965654CB8979C60D8976CF893DC2B99C8B20F82E33E74210948042EC51429FC103F59F4DF8865EB3B979E9040C87DF68F2EBC6AC07A95D3AC0A9BF6B39ECBB06643AB07B494404A3392E3270A3435CBE56D0C4769683010B8A64D612861B8C04C9B6811B81C79F615FEDD'
    #print "\n"
    #print code
    #print "\n"
    #code = code.decode('hex')
    decoded = decrypt(key, iv, input)
    return decoded
    #print(decoded)

if __name__ == '__main__':
    decrypted = test_crypto(sys.argv[1])
    print decrypted;

