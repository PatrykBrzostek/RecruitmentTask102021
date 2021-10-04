from fastapi import FastAPI
from cipher import Cipher

app = FastAPI()

@app.get("/get_encoded_text/{e}/{n}/{text}")
def encode_text(text, e, n):
    return {"encoded_text": Cipher.encode(text, e, n)}

@app.get("/get_decoded_text/{d}/{n}/{text}")
def decode_text(text, d, n):
    return {"decoded_text": Cipher.decode(text, d, n)}

