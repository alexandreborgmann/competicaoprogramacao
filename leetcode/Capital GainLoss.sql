select stock_name, sum(price*decode(operation,'Buy',-1,1)) capital_gain_loss
from stocks s
group by stock_name