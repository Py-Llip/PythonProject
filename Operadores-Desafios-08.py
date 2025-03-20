medida = float(input('Escolha uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida * 0.001
#micra = medida * 1 * 10**6
#nm = medida * 1 * 10**9
hm = medida / 100
dam = medida / 10
dm = medida * 10
print('A medida de {}m corresponte a {}km e {:.0f}cm e {:.0f}mm e {}hm e {}dam e {}dm'.format(medida, km, cm, mm, hm, dam, dm))
print('=' * 90)