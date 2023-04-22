# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Microsoft Windows (64-bit) (June 24, 2021)
# Date: Wed 19 Oct 2022 16:38:21


from object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1,
                    perturbative_expansion = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)

VLF = CouplingOrder(name = 'VLF',
                    expansion_order = 99,
                    hierarchy = 3)

