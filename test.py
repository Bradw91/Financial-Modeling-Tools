from Finance import finance

myFinance = finance()

debt = 1000000
equity = 2000000
tax_rate = .34

A_coe = myFinance.cost_of_equity(.025,.10,1.2)
A_cod = myFinance.cod_simple(.0631,.34)
myFinance.WACC(A_coe,A_cod,debt,equity,tax_rate)
