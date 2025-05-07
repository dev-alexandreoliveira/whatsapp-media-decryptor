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
