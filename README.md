# Python Tasks Set
The [recruitment_tasks.py](recruitment_tasks.py) file contains my solutions of tasks from 'Python Tasks Set.pdf'. There are some simple unit tests in the [recruitment_tasks_tests.py](recruitment_tasks_tests.py) file.

# Python Dev Task - cipher
## Comments
* It's possible to encode every sign, which has a ASCII code.
* The [cipher.py](cipher.py) file contains my implementation of a cipher algorithm. I chosen the RSA algorithm. Firstly I convert each sign to its ASCII code, then I encode it using a public key and finally join all encoded signs to one string. I decided to encode each sign separately, because my implementation fails, when I try to encode a really big integers. The decoding proceeds in reverse order using a private key.
* The [tests.py](tests.py) file contains a few tests. You have to run a local server before you run these tests.
* I couldn't manage to implement BasicAuth authorization.

## Requirements
* fastapi
* uvicorn
* requests

## Usage
Run a local server by command:
```bash
uvicorn api:app --reload
```

The API provides two methods, which allows to encode and decode a text. You can call them using the following requests:
```bash
http://127.0.0.1:8000/get_encoded_text/{e}/{n}/{text}
http://127.0.0.1:8000/get_decoded_text/{d}/{n}/{text}
```
The parameters **e** and **n** are your public key, and **d** is your private key. You can test the api with the following keys: **e=5**, **n=2021**, **d=2705** or make your own keys with the help of [this article](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/). 
The both methods return json with the struture shown below.
```bash
{"encoded_text":"some_encoded_text"}
{"decoded_text":"some_decoded_text"}
```