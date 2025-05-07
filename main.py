from flask import Flask, request, jsonify
import requests
import base64
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256

app = Flask(__name__)

@app.route("/decode-media", methods=["POST"])
def decode_media():
    data = request.get_json()

    media_url = data.get("media_url")
    media_key_b64 = data.get("media_key")
    mimetype = data.get("mimetype")  # ← Ex: "image/jpeg", "audio/ogg"

    if not media_url or not media_key_b64 or not mimetype:
        return jsonify({"error": "Parâmetros 'media_url', 'media_key' e 'mimetype' são obrigatórios"}), 400

    try:
        response = requests.get(media_url)
        enc_data = response.content

        media_key = b64decode(media_key_b64)

        # Escolher media_type correto
        if mimetype.startswith("image/"):
            media_type = b'WhatsApp Image Keys'
        elif mimetype.startswith("audio/"):
            media_type = b'WhatsApp Audio Keys'
        else:
            return jsonify({"error": f"Tipo de mídia não suportado: {mimetype}"}), 400

        # Derivar chaves
        expanded_key = HKDF(
            master=media_key,
            key_len=112,
            salt=None,
            hashmod=SHA256,
            num_keys=1,
            context=media_type
        )

        iv = expanded_key[0:16]
        cipher_key = expanded_key[16:48]
        cipher = AES.new(cipher_key, AES.MODE_CBC, iv)

        decrypted = cipher.decrypt(enc_data[:-10])  # Remove MAC

        pad_len = decrypted[-1]
        decrypted = decrypted[:-pad_len]

        base64_media = base64.b64encode(decrypted).decode("utf-8")

        return jsonify({
            "success": True,
            "base64": base64_media
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
