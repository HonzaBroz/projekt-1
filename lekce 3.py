skupina_1 = [
    'h.vybíralová@firma.cz', 'w.štrumlová@firma.cz', 'm.vybíralová@firma.cz',
    's.bechyňka@firma.cz', 'z.urbánková@firma.cz', 'l.riečan@firma.cz',
    'v.koudelová@firma.cz', 'f.vorlová@firma.cz', 'i.seleš@firma.cz'
]

skupina_2 = [
    'j.šmíd@firma.cz', 'j.procházková@firma.cz', 'l.riečan@firma.cz', 'd.hlavatá@firma.cz', 
    'm.železný@firma.cz', 'p.niklesová@firma.cz', 'b.skok@firma.cz',
    ]
s1 = set(skupina_1)
s2 = set(skupina_2)


if s1.intersection(s2):
    print("v obou skupinách jsou", s1.intersection(s2))
else:
    print("není tu nikdo stejný")
s2.difference_update(s1.intersection(s2))
print(s2)
s2.add("m.holinka@gmail.com")
s3 = frozenset(s1.union(s2))
print(s3)
print(s2 - s1.intersection(s2))
s2.discard

