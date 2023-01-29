from isOdd import isOdd
import emoji


print(isOdd(1))
print(isOdd(4))

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.demojize('Python is 👍'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
print(emoji.is_emoji("👍"))
print(emoji.emojize('Python es :pulgar_hacia_arriba:', language='es'))