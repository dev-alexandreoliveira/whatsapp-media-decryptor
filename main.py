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
    mimetype = data.get("mimetype")  # Ex: "image/jpeg", "audio/ogg"

    if not media_url or not media_key_b64 or not mimetype:
        return jsonify({"error": "Parâmetros 'media_url', 'media_key' e 'mimetype' são obrigatórios"}), 400

    try:
        # Download do arquivo criptografado
        response = requests.get(media_url)
        enc_data = response.content

        media_key = b64decode(media_key_b64)

        # Seleção do tipo de mídia
        if mimetype.startswith("image/"):
            # Verificação especial para stickers (normalmente webp)
            if mimetype == "image/webp":
                media_type = b'WhatsApp Sticker Keys'
            else:
                media_type = b'WhatsApp Image Keys'
        elif mimetype.startswith("audio/"):
            media_type = b'WhatsApp Audio Keys'
        elif mimetype.startswith("video/"):
            media_type = b'WhatsApp Video Keys'
        elif mimetype.startswith("application/"):
            media_type = b'WhatsApp Document Keys'
        else:
            return jsonify({"error": f"Tipo de mídia não suportado: {mimetype}"}), 400

        # Derivação das chaves
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

        # Remover MAC (últimos 10 bytes)
        encrypted_payload = enc_data[:-10]
        payload_length = len(encrypted_payload)

        # Verificação: payload precisa ser múltiplo de 16
        if payload_length % 16 != 0:
            return jsonify({
                "error": f"O payload criptografado deve ter tamanho múltiplo de 16 após remover o MAC, mas tem {payload_length} bytes."
            }), 400

        cipher = AES.new(cipher_key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted_payload)

        # Remover padding PKCS#7
        pad_len = decrypted[-1]
        if pad_len < 1 or pad_len > 16:
            return jsonify({"error": "Padding inválido na descriptografia"}), 400
        decrypted = decrypted[:-pad_len]

        # Retornar em base64
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
