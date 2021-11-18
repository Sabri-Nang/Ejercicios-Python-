#hipoteca
# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo=61
pago_extra_mes_fin=108
pago_extra=1000

while saldo > 0:
    mes=mes+1
    if mes>=pago_extra_mes_comienzo and mes<=pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual-pago_extra
        total_pagado = total_pagado + pago_mensual+pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    if saldo * (1+tasa/12) < pago_mensual:
        pago_mensual=saldo*(1+tasa/12)  
    print(f'{mes:5d} {total_pagado:10.2f} {saldo:10.2f}')

print(f'Total pagado: {total_pagado:0.2f}')
print(f'Meses:{mes}')