emoji = {
    'sad': '\U0001F612',
    'happy': '\U0001F607'
}
user = input('> ').lower()
user1 = user.split(' ')
out = ''
for i in user1:
    out = out + emoji.get(i,i) + ' '
print(out)