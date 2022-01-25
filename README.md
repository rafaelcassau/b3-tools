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
************************                                                                                                                          
|FII: IRDM11 | Tipo: CRI|                                                                                                                         
************************                                                                                                                          
Next Payment: 5.72                                                                                                                                
Quotas amount: 4                                                                                                                                  
change: 84.99                                                                                                                                     
equity_value: 98.06                                                                                                                               
market_value: 109.63                                                                                                                              
                                                                                                                                                  
************************                                                                                                                          
|FII: VRTA11 | Tipo: CRI|                                                                                                                         
************************                                                                                                                          
Next Payment: 4.76                                                                                                                                
Quotas amount: 4                                                                                                                                  
change: 101.91                                                                                                                                    
equity_value: 97.03                                                                                                                               
market_value: 105.40                                                                                                                              
                                                                                                                                                  
************************                                                                                                                          
|FII: MXRF11 | Tipo: CRI|                                                                                                                         
************************                                                                                                                          
Next Payment: 4.68
Quotas amount: 52
change: 0.39
equity_value: 10.27
market_value: 10.06

************************                                                                                                                  [52/387]
|FII: XPPR11 | Tipo: Laje comercial|                                                                                                              
************************                                                                                                                          
Next Payment: 4.40                                                                                                                                
Quotas amount: 8                                                                                                                                  
change: 5.43                                                                                                                                      
equity_value: 82.38                                                                                                                               
market_value: 64.76                                                                                                                               
                                                                                                                                                  
************************                                                                                                                          
|FII: XPML11 | Tipo: Shopping|                                                                                                                    
************************                                                                                                                          
Next Payment: 4.25                                                                                                                                
Quotas amount: 5                                                                                                                                  
change: 62.61                                                                                                                                     
equity_value: 101.72                                                                                                                              
market_value: 92.18                                                                                                                               
                                                                                                                                                  
************************                                                                                                                          
|FII: KNCR11 | Tipo: CRI|                                                                                                                         
************************                                                                                                                          
Next Payment: 4.10
Quotas amount: 5
change: 13.26
equity_value: 100.92
market_value: 102.05

************************
|FII: VISC11 | Tipo: Shopping|
************************
Next Payment: 4.05
Quotas amount: 5
change: 18.91
equity_value: 115.91
market_value: 100.92

************************                                                                                                                  [16/387]
|FII: BCFF11 | Tipo: FOF|
************************
Next Payment: 3.78
Quotas amount: 7
change: 5.58
equity_value: 79.04
market_value: 73.99

************************
|FII: XPLG11 | Tipo: Logistica|
************************
Next Payment: 3.20
Quotas amount: 5
change: 18.71
equity_value: 109.67
market_value: 100.96

************************
|FII: ALZR11 | Tipo: Laje/Logistica| 
************************
Next Payment: 3.00
Quotas amount: 4
change: 63.03
equity_value: 108.52
market_value: 115.12

************************
|FII: VILG11 | Tipo: Logistica|
************************
Next Payment: 2.80
Quotas amount: 4
change: 97.71
equity_value: 114.17
market_value: 106.45

************************
|FII: PVBI11 | Tipo: Laje comercial| 
************************
Next Payment: 2.80
Quotas amount: 5
change: 84.61
equity_value: 99.33
market_value: 87.78

************************
|FII: KNRI11 | Tipo: Laje/Logistica| 
************************
Next Payment: 2.64
Quotas amount: 3
change: 118.48
equity_value: 157.80
market_value: 135.01
```
