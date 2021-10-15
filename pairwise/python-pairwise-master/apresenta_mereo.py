import pairwise.all_pairs2

all_pairs = pairwise.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""

# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [["<=299.00", "300.00",  ">=300.01"]
            , ["Sem Cupom", "Inválido_Nro", "Inválido_expirado", "Inválido_15.01%", "válido_15,00%", "válido_14,99%"]
            , ["Meliuz_Sim", "Meliuz_Não"]
            , ["1ª_Compra_SIM", "1ª_Compra_NÃO"]
            , ["1_Unid_MP", "2_Unid_MP", "3_Unid_MP"]
            , ["Capital", "Interior"]
            , ["Boleto", "Débito", "Crédito"]
            , ["DT Pedido", "Dta Pedido+6d", "Dta pedido+7d", "Dta pedido+8d(Inválido)"]]


pairwise = all_pairs(parameters)

print("PAIRWISE:")
for i, v in enumerate(pairwise):
    print("%i:\t%s" % (i, str(v)))