#Weighted Average Cost of Capital

A = float(input("Assets?"))         #Assets (market value)
D = float(input("Debt?"))           #debt (market value)
Rd = input("Cost of Debt?")         #cost of debt
Re = input("Cost of Equity?")       #cost of equity
t =  input("Corporate tax rate?")   #corporate tax rate
E = A - D                           #EQUITY
V = D + E                           #total market value of firms financing


WACC = (E/V)*Re + (D/V)*Rd * (1-t)

print WACC * 100
