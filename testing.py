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



