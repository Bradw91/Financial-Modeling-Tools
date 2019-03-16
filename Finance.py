import numpy as np
import pandas as pd
from datetime import date

class finance:

    def dcf(self, growth_rate, WACC, num_shares,debt,cash):
        cf_list = []
        for i in range(0,4):
            cf = CF0 * (1.05 ** i)
            discounted = cf / (WACC ** i)
            cf_list.append(discounted)

        TCF = (cf_list[-1] * WACC^5) / (WACC-growth_rate)
        cf_list.append(TCF)
        PV = sum(cf_list)
        Intrinsic_val = (PV + cash - debt / num_shares)
        return PV
        return Intrinsic_val

    def cost_of_equity(self,rf,ERm,beta):
        coe = rf + (beta*(ERm-rf))
        return coe

    def cod_simple(self,Int_rate,tax_rate):
        cost_of_debt = Int_rate * (1-tax_rate)
        return cost_of_debt

    def WACC(self,cost_of_equity,cost_of_debt,total_debt,total_equity,tax_rate):
        wacc = (cost_of_equity * total_equity/(total_debt+total_equity)) + (cost_of_debt * total_debt/(total_debt+total_equity)) * (1-tax_rate)
        return wacc
