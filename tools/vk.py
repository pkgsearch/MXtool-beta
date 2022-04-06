import vk_api

token_raw = input("Ввeди токен: ")
token = vk_api.VkApi(token=tok)
vk = token.get_api()
vk.wall.post(
    message="Аккаунт  взломан! Ответственность взял анонимный хакер\n\nvto.pe\nvto.pe\nvto.pe"
)
print("[log] Сообщение отправленно. Ожидайте бана!")
