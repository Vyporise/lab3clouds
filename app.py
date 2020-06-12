from requests import  get,post,delete,put

fl = 55
while(int(fl)>0):
    print('Нажмите 1 чтобы запросить всю таблицу:')
    print('Нажмите 2 чтобы запросить запись по id:')
    print('Нажмите 3 чтобы создать запись:')
    print('Нажмите 4 чтобы удалить запись:')
    print('Нажмите 5 чтобы изменить запись по id:')
    print('Нажмите 0 чтобы выйти:')
    fl = input()

    if int(fl)==1:
        print(get('http://localhost:8088/myPhoneBook/').json())
        fl=1
        input('Нажмите ENTER чтобы продолжить:')
    else:
        if int(fl)==2:
            print('Введите id выводимой записи:')
            fl = input()
            print(get('http://localhost:8088/myPhoneBook/'+str(fl)).json())
            input('Нажмите ENTER чтобы продолжить:')
            fl=1
        else:
            if int(fl) == 3:
                a=input('Введите имя')
                b=input('Введите фамилию')
                c=int(input('Введите возраст'))
                d=input('Введите номер в формате +X(XXX)-XXX-XX-XX')
                e=input('Введите профессию')
                print(post('http://localhost:8088/myPhoneBook/', json={'tasks':[str(a),str(b),str(c),str(d),str(e)]}).json())
                input('Нажмите ENTER чтобы продолжить:')
            else:
                if int(fl) == 4:
                    fl = input('Введите id удаляемого элемента')
                    print(delete('http://localhost:8088/myPhoneBook/'+str(fl)).json())
                    input('Нажмите ENTER чтобы продолжить:')
                else:
                    if int(fl) == 5:
                        f = input('Введите id изменяемой записи:')
                        print('Изменяемая запись:')
                        print(get('http://localhost:8088/myPhoneBook/' + str(f)).json())
                        a = input('Введите имя')
                        b = input('Введите фамилию')
                        c = int(input('Введите возраст'))
                        d = input('Введите номер в формате +X(XXX)-XXX-XX-XX')
                        e = input('Введите профессию')
                        print(put('http://localhost:8088/myPhoneBook/', json={'tasks':[str(f),str(a),str(b),str(c),str(d),str(e)]}).json())
                        input('Нажмите ENTER чтобы продолжить:')


