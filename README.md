# WhatsApp Media Decryptor 🔐

API leve e open-source para **descriptografar mídias do WhatsApp** (áudios e imagens) enviadas via WhatsApp.

> Desenvolvido por [Iuri Almeida](https://github.com/iurijalmeida) com apoio do ChatGPT — pronto para ser usado por desenvolvedores.

---

## O que esse projeto faz?

Permite descriptografar arquivos de mídia (como áudios `.ogg` e imagens `.jpeg`) protegidos com `media_key`, utilizando o padrão de criptografia usado pelo WhatsApp.

Você envia a `media_url`, a `media_key` e o tipo MIME (`mimetype`) e recebe a mídia decriptada em base64.

---

## Por que isso foi criado?

Esse projeto surgiu como solução à instabilidade recorrente da função `getBase64FromMediaMessage` da Evolution API, onde requisições para conversão de mídia em base64 resultavam em erros 400 e comportamentos intermitentes. A solução proposta aqui é independente da Evolution e pode ser usada por qualquer desenvolvedor, inclusive dentro do n8n ou em backends próprios.

---

## ✅ Exemplo de uso

### Requisição `POST /decode-media`

```json
{
  "media_url": "https://mmg.whatsapp.net/o1/v/t62.7118-24/...",
  "media_key": "base64-da-chave-decriptografada",
  "mimetype": "image/jpeg"
}
```

### ✅ Resposta esperada

```json
{
  "success": true,
  "base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

### Suporta:

* `audio/ogg` (áudios do WhatsApp)
* `image/jpeg` (fotos comuns)

---

## Instalação local

```bash
git clone https://github.com/seu-usuario/whatsapp-media-decryptor.git
cd whatsapp-media-decryptor
pip install -r requirements.txt
python main.py
```

A aplicação ficará disponível em: [http://localhost:8080/decode-media](http://localhost:8080/decode-media)

---

## Deploy (Heroku, Railway, EasyPanel)

Esse projeto já vem com um `Procfile`:

```
web: python -m flask run --host=0.0.0.0 --port=8080
```

Você pode subir facilmente usando:

* Railway
* Render
* Heroku
* Replit
* VPS (com ou sem Docker)

---

## Estrutura

* `main.py`: código principal da API
* `requirements.txt`: dependências
* `Procfile`: instrução de inicialização para ambientes como Railway/Heroku

---

## Licença

MIT — Use, adapte, contribua e compartilhe com a comunidade.

---

## Feedback

Se você usar essa API ou quiser melhorar algo, abra uma issue ou mande um pull request.

---
