import pairwise.all_pairs2

all_pairs = pairwise.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""

# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [["x", "y"]
               , ["Win 7", "Win 8", "Win 10", "Linux"]
              , ["Network", "Modem", "Wifi"]
              , ["Salario", "Hora", "Part-Time"]
              , [6, 10, 15, 30, 60]]
             # , ['MASCULINO', 'FEMININO', 'BINARIO']]

pairwise = all_pairs(parameters)

print("PAIRWISE:")
for i, v in enumerate(pairwise):
    print("%i:\t%s" % (i, str(v)))