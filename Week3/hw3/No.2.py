d= [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone':'555-1618','email':'helga@mail.net'},
    {'name': 'Princess', 'phone':'555-3141','email':''},
    {'name':'LJ', 'phone':'555-2718','email':'lj@mail.net'}]


#1. 전화번호가 8로 끝나는 사용자의 이름을 출력하라.
print("1번 : 전화번호가 8로 끝나는 사용자의 이름을 출력합니다.")
for x in d:
    if '8' in x['phone']:
        print(x['name'])

#2. 이메일이 없는 사용자 이름을 출력하라.
print("2번 : 이메일이 없는 사용자의 이름을 출력합니다.")
for x in d:
    if '@mail.net' not in x['email']:
        print(x['name'])

#3. 사용자의 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'를 출력하라.
print("3번 : 사용자의 이름을 입력하면 전화번호와 이메일을 출력합니다.")
user = input(">>") #이름을 입력받음

a= d[0]
b = d[1]
c = d[2]
e =d[3]
if user == a['name']:
    print(a['phone'],a['email'])
elif user == b['name']:
    print(b['phone'],b['email'])
elif user == c['name']:
    print(c['phone'],c['email'])
elif user == e['name']:
    print(e['phone'],e['email'])
else :
    print("이름이 없습니다")
