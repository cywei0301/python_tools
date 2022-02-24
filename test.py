
msg='中文'
msg.encode('unicode_escape').decode('utf-8')
print(msg)
msg2 = msg.encode('utf-8').decode('unicode_escape')
with open('test.txt','w', encoding='utf-8') as fp:
    print(fp, msg2)

