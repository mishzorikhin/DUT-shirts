"""import pymorphy2
morph = pymorphy2.MorphAnalyzer()


otv = morph.parse('Миша')[0]


print('nomn'+ " : " +otv.inflect({'nomn'})[0])
print('gent'+ " : " +otv.inflect({'gent'})[0])
print('accs'+ " : " +otv.inflect({'accs'})[0])
print('ablt'+ " : " +otv.inflect({'ablt'})[0])
print('loct'+ " : " +otv.inflect({'loct'})[0])
print('voct'+ " : " +otv.inflect({'voct'})[0])


markers = ['где' ,'находится' ,'пройти' ,'дехать' ,'добраться', 'попасть', 'как']
markersNorm = []

for i in markers:
    print(morph.parse(i)[0].normal_form)
"""

import re

phones_str = str('9160000000')


def check_string(string):
    phone = re.sub(r'\b\D', '', string)
    clear_phone = re.sub(r'[\ \(]?', '', phone)
    if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$',string):
        return(bool(string))
    else: return(False)

print(check_string(phones_str))
