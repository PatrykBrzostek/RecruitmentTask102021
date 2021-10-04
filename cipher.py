
class Cipher():
    def __init__(self):
        pass

    @staticmethod
    def encode(text, e, n):
        '''
        :param text: text to be encoded
        :param e: public key
        :param n: public key
        :return: encoded text
        '''
        encoded_text=''
        for character in text:
            encoded_text+=Cipher.encode_character(character, int(e), int(n)).zfill(5)
        return encoded_text

    @staticmethod
    def decode(text, d, n):
        '''
        :param text: text to be decoded
        :param d: private key
        :param n: public key
        :return: decoded text
        '''
        encoded_characters=[text[i:i+5] for i in range(0, len(text), 5)]
        decoded_text=''
        for character in encoded_characters:
            decoded_text+=str(Cipher.decode_character(character,int(d),int(n)))
        return decoded_text

    @staticmethod
    def encode_character(character, e, n):
        return str(pow(ord(character), e ,n))

    @staticmethod
    def decode_character(character, d, n):
        return str(chr(pow(int(character), d, n)))

