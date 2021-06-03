
from optionprice import Option




    
some_option = Option(european=False,
                    kind='call',
                    s0=x,
                    k=635,
                    t=4,
                    sigma=0.49,
                    r=0.05,
                    dv=0)


some_option2 = Option(european=False,
                    kind='call',
                    s0=x,
                    k=627.5,
                    t=4,
                    sigma=0.49,
                    r=0.01,
                    dv=0)

    ##Type:           European
    ##Kind:           call
    ##Price initial:  80
    ##Price strike:   120
    ##Volatility:     1.0%
    ##Risk free rate: 5.0%
    ##Start Date:     2020-03-24
    ##Expire Date:    2020-04-24
    ##Time span:      31.0 days



    ##print(some_option)

for x in range(10):
    print(x)
    price = some_option.getPrice()
    price2 = some_option2.getPrice()
    

##    print(x,"vertical spread:" ,(price2-price).round(2))

