# WhatsApp Media Decryptor 🔐

API leve e open-source para **descriptografar mídias do WhatsApp** (áudios e imagens) enviadas via Whatsapp.

> Desenvolvido por [Iuri Almeida](https://github.com/iurijalmeida) com apoio do ChatGPT — pronto para ser usado por desenvolvedores.

---

## 🚀 O que esse projeto faz?

Permite descriptografar arquivos de mídia (áudios `.ogg` e imagens `.jpeg`) protegidos com `media_key`, utilizando o mesmo padrão de criptografia utilizado pelo WhatsApp.

Você envia a `media_key`, a `media_url` e o tipo de mídia (`mimetype`) e recebe a mídia em base64.

---

## ✅ Exemplo de uso

### Requisição `POST /decode-media`

```json
{
  "media_url": "https://mmg.whatsapp.net/o1/v/t62.7118-24/...",
  "media_key": "base64-da-chave-decriptografada",
  "mimetype": "image/jpeg"
}

🧠 Suporta:
audio/ogg (áudios do WhatsApp)

image/jpeg (fotos comuns)

🛠 Instalação local
bash
Copiar
Editar
git clone https://github.com/seu-usuario/whatsapp-media-decryptor.git
cd whatsapp-media-decryptor
pip install -r requirements.txt
python main.py
A aplicação ficará disponível em:
http://localhost:8080/decode-media

☁️ Deploy (Heroku, Railway, EasyPanel)
Esse projeto já vem com um Procfile:

less
Copiar
Editar
web: python -m flask run --host=0.0.0.0 --port=8080
Você pode subir com:

Railway.app

Render.com

Heroku

Replit

VPS (Docker opcional)

📁 Arquivos do projeto
main.py: código principal da API

requirements.txt: dependências

Procfile: comando de execução (para Heroku-like platforms)

📜 Licença
MIT. Use, adapte, contribua.

💬 Feedback
Se você usar isso em produção ou quiser melhorar, abra uma issue ou mande um PR!

