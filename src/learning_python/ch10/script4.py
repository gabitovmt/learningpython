while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdecimal():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')