# b3-tools

Tools I'm building in order to help my investments decisions.

Based in the REITs I've in my personal portifolio I ran a script that scrapy the last quotas price.
Based in the prices list and the last yield in BRL and in the amount of money I'll invest it calculate which of the REITs will pay more money.

## TODOs

 - The best way to do this calculation is not based only in the last month but based at least in the average of the last 12 months.

## installation steps:

```
git clone git@github.com:rafaelcassau/b3-tools.git
cd b3-tools
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the script:

```
python choice_better_DY.py
```

## input:

```
informe o valor do aporte em R$: 5200
```

## output

```
{'fii': 'IRDM11', 'next_payment_yield_BRL': Decimal('75.79')}                                                                                     
{'fii': 'VRTA11', 'next_payment_yield_BRL': Decimal('63.07')}                                                                                     
{'fii': 'MXRF11', 'next_payment_yield_BRL': Decimal('45.54')}                                                                                     
{'fii': 'XPML11', 'next_payment_yield_BRL': Decimal('43.35')}                                                                                     
{'fii': 'KNCR11', 'next_payment_yield_BRL': Decimal('41.82')}                                                                                     
{'fii': 'VISC11', 'next_payment_yield_BRL': Decimal('35.64')}                                                                                     
{'fii': 'ALZR11', 'next_payment_yield_BRL': Decimal('35.25')}                                                                                     
{'fii': 'BCFF11', 'next_payment_yield_BRL': Decimal('35.10')}                                                                                     
{'fii': 'XPPR11', 'next_payment_yield_BRL': Decimal('34.65')}                                                                                     
{'fii': 'VILG11', 'next_payment_yield_BRL': Decimal('31.50')}                                                                                     
{'fii': 'XPLG11', 'next_payment_yield_BRL': Decimal('30.08')}                                                                                     
{'fii': 'PVBI11', 'next_payment_yield_BRL': Decimal('29.12')}                                                                                     
{'fii': 'KNRI11', 'next_payment_yield_BRL': Decimal('28.16')}
```
