# -*- coding: utf-8 -*-
"""BaseCode.ipynb



- From Kaggle - Optiver


This data set contains stock market data relevant to the practical execution of trades in the financial markets.

In particular, it includes order book snapshots and executed trades.

With one second resolution, it provides a uniquely fine grained look at the micro-structure of modern financial markets.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

"""- Order Book File

From Kaggle the order book file: Provides order book data on the most competitive buy and sell orders entered into the market.The top two levels of the book are shared. The first level of the book will be more competitive in price terms, it will then receive execution priority over the second level.

In the following we use stock_id==0 as example, we can see that

 - bid-price from Buyer: the "maximun" dollar that "buyer" can accept
$$ bid price1 > bid price2 $$

 - ask-price from Seller: the "minimum" dollar that "seller" can accept
$$ ask price1 < ask price2 $$

bid/ask_size the number of volumne correspond to the price.

"""

example_book_df = pd.read_parquet(r'./book_train.parquet/stock_id=0/c439ef22282f412ba39e9137a3fdabac.parquet')
example_book_df

example_book_df[:10].to_excel(r'trade_book_sample_data.xlsx')

"""- Trade book File

The DataFrame `example_trade_book_df` that we've loaded presents data from the trade book for `stock_id=1`. It captures trade data at a high frequency, detailing transactions that occurred at specific seconds within the trading session denoted by `time_id`. Here's what each column represents:

1. **time_id**: This identifies the specific time interval or session during which these trades occurred. All the entries you showed are from `time_id = 5`, suggesting they all belong to the same trading segment or day.

2. **seconds_in_bucket**: Indicates the specific second within the `time_id` when these trades were executed. For example, the first entry shows that at 28 seconds into the trading session identified by `time_id = 5`, certain trades were executed.

3. **price**: This column shows the price at which trades were executed. These prices are normalized and weighted by the number of shares involved in each transaction. The weighting by the number of shares ensures that larger trades have a more significant impact on the average price calculation, giving a more accurate reflection of market prices.

4. **size**: Represents the total number of shares or units traded in that specific second. For instance, at 28 seconds (`seconds_in_bucket`), 553 shares were traded.

5. **order_count**: Indicates the number of unique orders that were executed to reach the total trade size reported in the `size` column for that second. The first entry with `order_count = 11` suggests that it took 11 separate orders to accumulate the 553 shares traded at that time.
"""

example_trade_book_df = pd.read_parquet(r'trade_train.parquet/stock_id=1/170b39f1f7144bb3b4554aabc336106e.parquet')
example_trade_book_df

"""### 1. Bid/Ask Spread
The bid/ask spread is a measure of the difference between the highest price that buyers are willing to pay (bid price) and the lowest price that sellers are willing to accept (ask price). It's calculated as follows:

$$ \text{Bid/Ask Spread} = \left(\frac{\text{Bid Price}_1}{\text{Ask Price}_1}\right) - 1 $$

#### Importance:
- **Market Liquidity**: A narrower bid/ask spread typically indicates greater liquidity, making it easier to execute trades near the market price without causing price movement. if bid/ask spread is higher, that means the liquidity for the single asset is not great. The lower the bid/ask spread the better the marekt liquidity for the specific asset.

- **Transaction Costs**: For traders, a lower spread means lower transaction costs, as they can buy and sell closer to the mid-price.
- **Market Sentiment**: Large spreads can also indicate higher uncertainty or lower confidence among traders regarding the asset's value.

### 2. Weighted Average Price (WAP)
The Weighted Average Price (WAP) is calculated by taking the volume-weighted average of orders at the top of the book (usually the first level). It gives a snapshot of where trades are likely to occur given current order book volumes. The formula is:

$$ WAP = \frac{(\text{Bid Price}_1 \times \text{Ask Size}_1) + (\text{Ask Price}_1 \times \text{Bid Size}_1)}{\text{Bid Size}_1 + \text{Ask Size}_1} $$

#### Importance:
- **Stock Valuation**: WAP helps assess the fair market price of a stock at which transactions could realistically occur given the current market conditions.
- **Market Depth and Balance**: Reflects the balance or imbalance between supply and demand. A book with more bids might push the WAP higher, indicating stronger demand. Conversely, more asks might lower the WAP, indicating greater supply.

### Examples:
**Example 1: Buyer Dominance**
- Bid Price = $1, Ask Price = $2
- Bid Size = 1, Ask Size = 2

  The calculation:
  $$ WAP_1 = \frac{(1 \times 2) + (2 \times 1)}{1 + 2} = \frac{4}{3} \approx 1.33 $$

**Example 2: Seller Dominance**
- Bid Price = $1, Ask Price = $2
- Bid Size = 2, Ask Size = 1

  The calculation:
  $$ WAP_2 = \frac{(1 \times 1) + (2 \times 2)}{2 + 1} = \frac{5}{3} \approx 1.67 $$

### 3. Log Return
Log return is used to measure the relative change in price over time, making it time additive. This is particularly useful in financial mathematics for analyzing returns over multiple periods. The formula is:

$$ r_{t1, t2} = \log\left(\frac{S_{t2}}{S_{t1}}\right) $$

where \( S_{t1} \) and \( S_{t2} \) are the stock prices at times \( t1 \) and \( t2 \), respectively.

#### Importance:
- **Comparability**: Log returns can be summed over time to find the total return, unlike simple returns which need to be compounded.
- **Symmetry**: They treat positive and negative changes symmetrically, a property not seen in simple returns where a 50% loss cannot be recouped by a 50% gain.
- **Statistical Properties**: Log returns are more likely to be normally distributed, which simplifies various statistical analyses, such as hypothesis testing and interval estimation.

These financial metrics provide crucial insights into market conditions, helping traders make informed decisions and analysts to evaluate market dynamics comprehensively.

The plot we've generated visualizes the logarithmic function, which is commonly used to calculate log returns in finance. The natural logarithm is indeed unbounded as it approaches zero from the right, meaning it can extend to negative infinity, which is what the plot shows as the curve drops sharply as it nears zero.

The x-axis in our plot likely represents the ratio of prices (S_t2 / S_t1) used in the log return formula:

$$ r_{t1, t2} = \log\left(\frac{S_{t2}}{S_{t1}}\right) $$

As the price ratio decreases towards zero (implying S_t2 is much less than S_t1), the log return decreases without bound. This reflects the concept that there is no limit to how much money an investment can lose, in percentage terms. If an asset's price fell to zero, the log return would be negative infinity, effectively representing a total loss.

On the other hand, as the price ratio increases (implying S_t2 is greater than S_t1), the log return increases as well, but it is bounded above by the growth of the asset. There is no upper limit to the asset's price increase in theory, and hence no upper limit to the log return.

It's also important to note that log returns cannot actually be calculated for a zero or negative price ratio, as the logarithm of zero or a negative number is undefined. This is an important consideration when working with log returns in practice; they are only meaningful for positive price ratios.

The horizontal and vertical dashed red lines represent the axes, with the horizontal line marking the zero point for the return and the vertical line marking the zero point for the price ratio. The log function is not defined for a price ratio of zero (since log(0) is undefined), which is why the plot does not extend to or past the vertical red line at the zero point on the x-axis.
"""

x = np.linspace(0,10,100)
fig,ax = plt.subplots(figsize=(8,6))
ax.set_title('Log Retrurn is not bounded and can go below -100%')
ax.axhline(0,color='red',linestyle='--')
ax.axvline(0,color='red',linestyle='--')
ax.plot(x,np.log(x),color='blue')
plt.show()

"""In the context of financial time series, **realized volatility** is a measure of the variation in log returns over a specific time period. It is often used as an estimate of the future volatility of an asset's price and is a crucial input for various risk management and option pricing models. Here's a bit more detail on the definitions you provided:

### Simplified Realized Volatility
The simplified version ignores any mean of the returns and just sums the squared log returns. This is reasonable for high-frequency data where the mean return can be very close to zero. The formula is:

$$ \sigma = \sqrt{ \sum_{t}r^{2}_{t-1,t}} $$

Here, \( \sigma \) represents the realized volatility, and \( r_{t-1,t} \) is the log return from time \( t-1 \) to time \( t \).

### Standard Volatility Calculation
The standard calculation for volatility, used in statistics and often applied in finance for longer time frames (like annual volatility), would take the mean of the returns into account:

$$ \sigma = \sqrt{ \sum_{t}(r_{t-1,t}-\bar{r})^{2}} $$

In this formula, \( \bar{r} \) represents the average return over the time period, and \( r_{t-1,t} \) is the log return as before.

### Importance in Finance
Volatility is a fundamental concept in finance because it represents the risk associated with the price changes of a security. Higher volatility implies higher risk and potentially higher returns or losses. Traders and investors use volatility to assess the risk of their portfolios and to price derivatives such as options.

Options and futures are derivative instruments used by traders and investors to hedge risk, speculate, or gain leverage.

### Options

**Options** give the holder the right, but not the obligation, to buy or sell an underlying asset at a predetermined price on or before a certain date.

**Example 1: Hedging with Options**
An investor holding shares of Company XYZ might be worried about potential short-term downside risk. To hedge this risk, the investor can buy put options on XYZ. If XYZ’s price falls, the investor can exercise the put options and sell the shares at the strike price, thus limiting their losses.

**Example 2: Speculation with Options**
A trader believes that the price of ABC stock will rise due to an upcoming product launch. To capitalize on this move with limited risk, the trader buys call options on ABC. If the price goes up, the trader can exercise the calls to buy shares at a lower strike price and benefit from the increase. If the price doesn’t go up, the trader's loss is limited to the premium paid for the options.

**Example 3: Income Generation with Options**
An investor owns shares of company MNO and doesn’t expect much price movement in the near term. The investor can write (sell) call options against their MNO shares, receiving the option premium as income. If the stock price remains below the strike price of the calls, the options expire worthless, and the investor keeps the premium.

### Futures

**Futures** are standardized contracts to buy or sell a specific quantity of an asset at a predetermined price at a specified time in the future.

**Example 1: Hedging with Futures**
A farmer expects to harvest 10,000 bushels of wheat in three months and is concerned about the risk of a price drop. To lock in a sale price, the farmer sells wheat futures contracts. When the harvest comes in, the farmer will deliver the wheat at the agreed-upon price, regardless of the market price.

**Example 2: Speculation with Futures**
A speculator anticipates that oil prices will rise due to geopolitical tensions. They buy oil futures contracts hoping to sell them later at a higher price. If the price of oil increases as expected, the speculator can sell the futures contracts at a profit before the delivery date.

**Example 3: Portfolio Diversification with Futures**
An investment fund wants exposure to gold without physically holding it. The fund can buy gold futures, allowing it to profit from price movements of gold. This adds diversification to the portfolio since gold often has a negative correlation with other financial assets.

Both options and futures trading require a good understanding of the instruments and the market, as they can amplify both gains and losses. Therefore, they are typically used by more experienced traders and investors.

**For the Kaggle context and similar financial modeling tasks, sticking with the simplified realized volatility formula is often preferable due to its simplicity and the short time frame typically involved. Annualizing the volatility or adjusting for the mean return is more relevant for longer-term investment horizons where those factors become significant.**

1. **Log Return Function**:
   - The `log_return` function calculates the natural logarithm of the ratio of consecutive prices. The `.diff()` method is used to find the difference between each price and its preceding price, which, when passed to the `np.log` function, gives the log return.

2. **Bid/Ask Spread**:
   - This new column is calculated by dividing the `ask_price1` by `bid_price1` and subtracting 1. It represents the relative difference between the lowest price sellers are willing to accept and the highest price buyers are willing to pay.
   - A smaller bid/ask spread typically indicates a more liquid market where trades can be executed more easily without a significant price impact.

3. **Total bid/ask1 Size**:
   - The sum of `ask_size1` and `bid_size1` gives the total number of shares available at the best ask and bid prices. This can be an indicator of market depth and liquidity at the best prices.

4. **Weighted Average Price (WAP)**:
   - The WAP is calculated using the provided formula which multiplies each price by the opposite side's size (bid price by ask size and vice versa) and divides by the total size at the best bid and ask. It's a measure that gives a fair price estimate where the next trade could occur given the current order book.

In the DataFrame `example_book_df`, you can see these new calculations as additional columns:

- **bid/ask spread**: A measure of market spread and liquidity.
- **Total bid/ask1 Size**: The sum of the sizes of the best bid and ask, giving an immediate sense of market depth.
- **wap**: The Weighted Average Price, a useful statistic for gauging where the market is pricing the stock considering the order book's state.
"""

def log_return(list_stock_prices):
    return np.log(list_stock_prices).diff()


example_book_df.loc[:,('bid/ask spread')] = (example_book_df['ask_price1']/example_book_df['bid_price1'])-1 # Construct Bid/Ask Spread.
example_book_df.loc[:,('Total bid/ask1 Size')] = example_book_df['ask_size1'] + example_book_df['bid_size1']
example_book_df.loc[:,('wap')] = (example_book_df['bid_price1']*example_book_df['ask_size1'] + example_book_df['ask_price1']*example_book_df['bid_size1']) / (example_book_df['ask_size1'] + example_book_df['bid_size1'])
example_book_df

"""

1. **Calculate Log Returns**:
   - Group the data by `time_id` since log returns are typically calculated per trading session or day.
   - Apply the `log_return` function to the `wap` column for each group. This calculates the natural log of the ratio of consecutive WAPs.
   - The `.diff()` method, used inside the `log_return` function, calculates the difference between each WAP and its preceding value.

2. **Handle Null Values**:
   - After the log return is calculated, the first value of each `time_id` group is always `NaN` (since there's no previous WAP to compare to), so these rows are dropped using `example_book_df = example_book_df[~example_book_df['log_return'].isnull()]`.

3. **DataFrame Content**:
   - The resulting DataFrame contains the original order book data along with the `bid/ask spread`, the total size at the best bid and ask, the WAP, and now the `log_return` for each snapshot within a `time_id`.

### Practical Insights:

- **log_return**: This new column is critical for analyzing the price movement dynamics and volatility of the asset over very short periods (from second to second within a trading session). A zero log return implies no change in price, while positive and negative values indicate upward and downward price movements, respectively.

- **Use in Volatility Calculation**: The log returns are used to calculate the realized volatility over a trading session, providing a measure of how much the price has fluctuated in that period.

- **Time Series Analysis**: With log returns, you can perform time series analyses to identify patterns, trends, or to build predictive models for intraday price movements.

- **Financial Analysis**: The `log_return` and WAP can be used together to get insights into market behavior, such as the impact of liquidity (visible through the total size and spread) on price stability and movement."""

example_book_df.loc[:,('log_return')] = example_book_df.groupby('time_id')['wap'].apply(log_return)
example_book_df = example_book_df[~example_book_df['log_return'].isnull()] # drop the first null return value
example_book_df

"""The two plots we've generated provide a visual representation of the order book dynamics and the evolution of log returns for a particular stock (`stock_id=0`) during a specific time interval (`time_id=5`).

### First Plot: Weighted Average Price (WAP) and Best Bid/Ask Prices
This plot shows the WAP along with the best bid and ask prices over the seconds within the bucket for `time_id=5`.

**Conclusions from the WAP Plot**:
1. **Price Movements**: The WAP, bid, and ask prices move in sync, as expected, since WAP is derived from these prices. Fluctuations in WAP reflect real-time changes in market conditions.
2. **Bid-Ask Convergence and Divergence**: There are periods where the bid and ask prices converge (indicating a tighter spread) and periods where they diverge (wider spread), which could imply changing market liquidity.
3. **Price Volatility**: The extent of fluctuation in the WAP line could be indicative of the volatility during this time period. Sharp movements in bid or ask prices that are mirrored in the WAP suggest rapid changes in market sentiment.

### Second Plot: Log Return and Cumulative Log Return
This plot illustrates the log returns and the cumulative log returns, which is the sum of all log returns up to each point in time.

**Conclusions from the Log Return Plot**:
1. **Return Fluctuations**: The log returns fluctuate around zero, with no discernible trend, suggesting a market that doesn't have a strong directional movement in this time frame.
2. **Cumulative Returns**: The cumulative log return line gives an overall picture of how returns are accumulating or compounding over time. If this line is trending upwards or downwards, it would suggest a longer-term price movement within this bucket.
3. **Intraday Volatility**: The plot of log returns shows the price volatility at each second. Sharp spikes or dips indicate moments of high volatility.

### Combined Insights
- By examining both the WAP/bid/ask prices and the log returns together, one can correlate price levels with return patterns. For example, a large gap between the bid and ask prices could lead to more significant log returns due to larger price movements required to match buyers and sellers.
- The second plot's cumulative log return can help identify periods of sustained upward or downward price pressure. It's a visual tool that can signal trends within the intraday data that might not be evident from the raw log returns alone.

Overall, these plots are tools that can aid a trader or analyst in understanding the short-term behavior of a stock. They can help identify moments of high liquidity, increased volatility, and potential price trends, all of which are critical for making informed trading decisions.
"""

fig ,ax = plt.subplots(figsize=(12,6))
ax.set_title('WAP of stock_id_0, time_id_5')
ax.plot(example_book_df[example_book_df['time_id']==5].seconds_in_bucket,example_book_df[example_book_df['time_id']==5].wap,color="blue",label='wap')
ax.plot(example_book_df[example_book_df['time_id']==5].seconds_in_bucket,example_book_df[example_book_df['time_id']==5].ask_price1,color="green",label='ask_price1')
ax.plot(example_book_df[example_book_df['time_id']==5].seconds_in_bucket,example_book_df[example_book_df['time_id']==5].bid_price1,color="orange",label='bid_price1')
ax.set_xlabel('seconds_in_bucket')
ax.set_ylabel('wap')
ax.legend()

fig ,ax = plt.subplots(figsize=(12,6))
ax.set_title('Log return of stock_id_0, time_id_5')
ax.plot(example_book_df[example_book_df['time_id']==5].seconds_in_bucket,example_book_df[example_book_df['time_id']==5].log_return,color="blue")
ax.plot(example_book_df[example_book_df['time_id']==5].seconds_in_bucket,example_book_df[example_book_df['time_id']==5].log_return.cumsum(),color="red",label='cumulative return')
ax.set_xlabel('seconds_in_bucket')
ax.set_ylabel('log_return')
plt.show()

"""# Construct Kaggle Realized Volatility per Time_ID for stock_id == 0

The function `realized_volatility` that we've defined calculates the realized volatility for a series of log returns. Realized volatility is a measure of the variation of an asset’s price over time and is computed as the square root of the sum of squared log returns.


1. **Group by `time_id`**: This operation is used to segment the `example_book_df` DataFrame into groups, each containing data for a specific `time_id`. This is important because realized volatility is calculated for each time interval independently.

2. **Aggregate log returns**: The `.agg(realized_volatility)` method applies the `realized_volatility` function to the `log_return` column within each group. This calculates the realized volatility for each time interval (`time_id`).

3. **Reset Index with Name**: The `.reset_index(name='realized_volatility')` method transforms the aggregated data into a DataFrame and assigns the name 'realized_volatility' to the column containing the calculated volatilities.

The result is `df_realized_vol_per_stock`, a DataFrame with two columns: `time_id` and `realized_volatility`. This DataFrame shows the realized volatility of the stock's log returns for each `time_id`, which can be an entire trading day or a specific trading session depending on the data's context.

The realized volatility values give insight into the level of market activity and the risk associated with the stock's price movements within each time interval. A higher realized volatility indicates larger price fluctuations, suggesting greater risk or uncertainty about the stock's price. This information is crucial for traders and risk managers, as it helps in portfolio risk assessment, derivative pricing, and developing volatility trading strategies.

In a trading context, especially for high-frequency data, this measure can help identify periods of market stress or calm, both of which may present different trading opportunities. For example, a trader might use periods of low volatility to establish positions in anticipation of future price movements, or use periods of high volatility to trade more actively, capitalizing on larger price swings.
"""

def realized_volatility(series_log_return):
    return np.sqrt(np.sum(series_log_return**2))

df_realized_vol_per_stock =  example_book_df.groupby(['time_id'])['log_return'].agg(realized_volatility).reset_index(name='realized_volatility')
df_realized_vol_per_stock

"""From the plot showing the realized volatility of `stock_id_0`, we can draw several conclusions:

1. **Volatility Spikes**: There are noticeable spikes in volatility at certain `time_id` intervals. These spikes could be indicative of market events or news that significantly impacted the price of the stock, leading to increased trading activity and larger price movements during those periods.

2. **Volatility Fluctuations**: There's a fluctuation in volatility across different `time_id` values, suggesting variability in market conditions across different trading sessions or days.

3. **Periods of Calm**: In between the spikes, there are extended periods where volatility appears to be relatively lower and more stable. This could suggest a more settled market sentiment or lack of significant market-moving events during these times.

4. **Long-Term Trends**: If the `time_id` intervals correspond to a longer-term timeline (like trading days), one could analyze for long-term trends in volatility. For instance, a clustering of spikes might suggest a period of market stress.

5. **Trading Strategy Implications**: High-volatility periods might be targeted by certain traders for speculative trades, while low-volatility periods might be preferred for strategies that benefit from stable prices, such as "range trading."

6. **Risk Management**: The overall distribution and range of volatility can aid in risk management. Portfolios may need to be rebalanced to account for the observed volatility levels, particularly if the asset's volatility is higher than anticipated.

7. **Liquidity Considerations**: High volatility can sometimes coincide with low liquidity, meaning that trades could have a larger price impact. This should be considered when planning entry and exit strategies.

It is important to note that while this plot provides valuable insights into the volatility of the stock, it should be combined with other data and analyses to form a comprehensive view of the stock's behavior and to inform decision-making.
"""

fig ,ax = plt.subplots(figsize=(20,6))
ax.set_title('Realized Volatility of stock_id_0')
ax.plot(df_realized_vol_per_stock.time_id,df_realized_vol_per_stock.realized_volatility,color="blue")
ax.set_xlabel('time_id')
ax.set_ylabel('realized volatility')
plt.show()

"""# Naive Prediction: Using Last Timestamp realized volatility as target

Now we know hoe to build our predict target, let's using realized volatility of $t_{i-1}$ to predict $t_{i}$ as predeiction benchmark.

A commonly known fact about volatility is that it tends to be autocorrelated.

The concept we are referring to is a basic forecasting technique for time series data where past values are used to predict future values. This method is often called a "naive" forecast because it assumes that the conditions affecting the system won't change much in the short term.

In financial markets, the volatility of an asset is the degree to which its price fluctuates over time. An important characteristic of volatility is that it often shows autocorrelation.

Autocorrelation means that the volatility from one time period is correlated with the volatility from adjacent time periods. In simpler terms, if the volatility is high today, there is a tendency that it might be high tomorrow as well, and vice versa.

A naive model takes advantage of this property by using the realized volatility from the previous time period (say $t_{i-1}$) as the forecast for the next period (say $t_{i}$). For example, if we know the realized volatility for the first 10 minutes of trading, we might use this as our "prediction" for the realized volatility of the next 10 minutes.

This approach is naive because it does not take into account any other information that could affect price fluctuations, such as market news, economic events, or changes in trading volume. It assumes that the future will be like the immediate past.

Despite its simplicity, the naive model can sometimes be a tough benchmark to beat, especially in markets where conditions do not change drastically over short periods. It's a starting point in model development, providing a baseline against which more complex models can be compared. If a sophisticated model can't outperform the naive model, it may not be providing valuable predictive insight.

In practice, while a naive model may not be the best strategy for making actual trading decisions due to its simplicity, it serves as an important benchmark in the model development process.
"""

import glob
from tqdm import tqdm
from sklearn.metrics import r2_score


list_order_book_file_train = glob.glob(r'./book_train.parquet/*')

print(list_order_book_file_train)
print(len(list_order_book_file_train))

"""The function `realized_volatility_per_stock_and_time` we've written processes an order book for a given stock to calculate its realized volatility for each `time_id`. Here's how the function works, along with the additional context of how this relates to a predictive modeling task like a Kaggle competition:

1. **Read the Order Book Data**: The function starts by reading the parquet file for a specific `stock_id`. It uses `pd.read_parquet` to load the data into a DataFrame named `example_book_df`.

2. **Calculate Supplementary Metrics**:
   - **Bid/Ask Spread**: The relative difference between the ask and bid prices.
   - **Total bid/ask1 Size**: The sum of the best bid size and ask size.
   - **Weighted Average Price (WAP)**: A price level that is reflective of both the best bid and ask prices, weighted by their respective sizes.
   - **Log Returns**: The function computes log returns of the WAP.

3. **Calculate Realized Volatility**: The log returns are then grouped by `time_id`, and the realized volatility is calculated using the `realized_volatility` function previously discussed. This results in a new DataFrame, `df_realized_vol_per_stock`, which has `time_id` and the corresponding realized volatility.

4. **Create a Submission-Friendly DataFrame**: For each `time_id`, a `row_id` is constructed in the format `stock_id-time_id`, which is required for submission in many predictive modeling competitions, like those on Kaggle. The DataFrame is then filtered to only include the necessary columns for submission, which are `row_id` and `realized_volatility`.

Here's an extended description of this process in a predictive modeling context:

- The aim is to predict the realized volatility for a future time period based on historical data. The historical realized volatilities are calculated as the target variable for model training.
- In a Kaggle competition, participants are often required to submit predictions in a specific format, usually with an identifier (`row_id`) and the predicted value. This function prepares the dataset in such a way that it could be used to generate submissions after a model has been trained and predictions have been made.
- The naive prediction approach, mentioned previously, would involve shifting the realized volatility values to create predictions for the subsequent `time_id`. For example, the realized volatility for `time_id=5` could be used to predict the volatility for `time_id=6`.
- The predictive performance of a model could be evaluated using a metric such as the R-squared value, which measures the proportion of the variance for the dependent variable that's explained by the independent variables in a regression model. In this context, it would tell you how well the past volatilities explain the future volatilities.

To actually implement the naive prediction model and evaluate it with R-squared, we'd need to shift the realized volatilities in `df_realized_vol_per_stock` by one `time_id` and compare them with the true volatilities of the shifted `time_id`s using `r2_score` from the `sklearn.metrics` library. This would give you a benchmark for how well you can predict future volatility based on past volatility.
"""

path = r'./book_train.parquet/stock_id=0'

def realized_volatility_per_stock_and_time(path):

    stock_id = path.split("=")[1]
    example_book_df = pd.read_parquet(path)

    # construct item for realized volatility calculation
    example_book_df.loc[:,('bid/ask spread')] = (example_book_df['ask_price1']/example_book_df['bid_price1'])-1 # Constrcut Bid/Ask Spread.
    example_book_df.loc[:,('Total bid/ask1 Size')] = example_book_df['ask_size1'] + example_book_df['bid_size1']
    example_book_df.loc[:,('wap')] = (example_book_df['bid_price1']*example_book_df['ask_size1'] + example_book_df['ask_price1']*example_book_df['bid_size1']) / (example_book_df['ask_size1'] + example_book_df['bid_size1'])
    example_book_df.loc[:,('log_return')] = example_book_df.groupby('time_id')['wap'].apply(log_return)
    example_book_df = example_book_df[~example_book_df['log_return'].isnull()] # drop the first null return value

    # construct realized volatility
    df_realized_vol_per_stock = example_book_df.groupby(['time_id'])['log_return'].agg(realized_volatility).reset_index(name='realized_volatility')
    # for every stock, we have to built a row_id inable for us to submit the prediction result
    df_realized_vol_per_stock.loc[:,('row_id')] = df_realized_vol_per_stock['time_id'].apply(lambda x: f'{stock_id}-{x}')

    return df_realized_vol_per_stock[['row_id','realized_volatility']]

realized_volatility_per_stock_and_time(path)

"""The function `past_realized_volatility_per_stock` takes a list of file paths (`list_file`) corresponding to order book data files for different stocks and calculates the realized volatility for each `time_id` within each stock. The process is encapsulated within a `for` loop, iterating over each file, and is designed to concatenate the results into a single DataFrame.

Here's a detailed walkthrough:

1. **Initialize an Empty DataFrame**: `df_past_realized` is initialized to store the concatenated results.

2. **Iterate Over Files**:
   - The `tqdm` function is used to create a progress bar that provides feedback during the loop execution.
   - In each iteration, the function `realized_volatility_per_stock_and_time` is called with the current file path. This function calculates the realized volatility for the given stock.
   - The resulting DataFrame for each stock is concatenated to `df_past_realized` using `pd.concat`.

3. **Return Concatenated DataFrame**: After processing all files, the function returns a DataFrame containing the `row_id` and `realized_volatility` for all stocks and `time_id`s present in the list of files.

4. **Sorting the Results**: Once you have the final DataFrame, `df_past_realized_train`, it's sorted by `row_id`. The `row_id` is typically a combination of `stock_id` and `time_id` and is used to uniquely identify each prediction for submission in competitions like those on Kaggle.


"""

def past_realized_volatility_per_stock(list_file):
    df_past_realized = pd.DataFrame()
    for file in tqdm(list_file):
        df_past_realized = pd.concat([df_past_realized,realized_volatility_per_stock_and_time(file)],axis=0)
    return df_past_realized


df_past_realized_train = past_realized_volatility_per_stock(list_file=list_order_book_file_train)
df_past_realized_train.sort_values(by='row_id')

"""
1. **Load CSV**: You load the `train.csv` file into a pandas DataFrame.
   
2. **Create 'row_id'**: You create a new column `row_id` by concatenating `stock_id` and `time_id` after converting them to strings. This unique identifier matches the `row_id` format you've used in the earlier volatility calculations.

3. **Filter Columns**: You filter the DataFrame to include only the `row_id` and `target` columns.

The resulting `train` DataFrame is set up for use in training a machine learning model. The `target` column is what the model will try to predict, and the `row_id` serves as a key to match predictions with the corresponding stock and time period. In the context of a Kaggle competition or any predictive modeling task, this target is the ground truth we'll use to train your model and evaluate its predictions."""

train = pd.read_csv('./train.csv')
train['row_id'] = train['stock_id'].astype(str) + '-' + train['time_id'].astype(str)
train = train[['row_id','target']]
train

"""- Join the df_train and realized_volatility"""

df_joined = train.merge(df_past_realized_train, on = ['row_id'], how = 'left')
df_joined

"""We've defined a function to calculate the Root Mean Squared Percentage Error (RMSPE), which is a commonly used metric to evaluate the performance of regression models when the target variable is continuous and strictly positive. The RMSPE is particularly popular in finance and stock market predictions because it normalizes the error based on the size of the true value, making it a relative error metric.

The RMSPE function calculates the square root of the average squared percentage errors between the actual values (`y_true`) and the predicted values (`y_pred`).

We then calculate the R-squared (R2) score, which provides a measure of how well the variability of the target is explained by the model's predictions. An R2 score of 1 indicates perfect correlation, while a score of 0 indicates no correlation.

- **R2 score**: With a value of 0.628, the naive model explains about 62.8% of the variability in the target. This is a fairly decent score for a naive model and indicates some level of predictive power.

- **RMSPE**: A value of 0.341 means that, on average, the predictions of the naive model deviate from the actual realized volatilities by 34.1%. This value gives an idea of the error magnitude in relation to the actual volatility values.

The performance metrics suggest that while the naive model has a certain predictive capability, there is still room for improvement. The R2 score shows a positive correlation, but the RMSPE indicates that the predictions are not very close to the actual values in percentage terms, which could be critical when making trading decisions or managing risk. The goal in a predictive modeling task would be to develop a model that increases the R2 score and decreases the RMSPE.
"""

def rmspe(y_true, y_pred):
    return  (np.sqrt(np.mean(np.square((y_true - y_pred) / y_true))))

R2 = round(r2_score(y_true = df_joined['target'], y_pred = df_joined['realized_volatility']),3)
RMSPE = round(rmspe(y_true = df_joined['target'], y_pred = df_joined['realized_volatility']),3)

print(f'Performance of the naive prediction:\nR2 score: {R2}, \nRMSPE: {RMSPE}.')

"""# Kaggle Submision"""

list_order_book_file_test = glob.glob('./book_test.parquet/*')
list_order_book_file_test

df_naive_pred_test = past_realized_volatility_per_stock(list_file=list_order_book_file_test)
df_naive_pred_test

df_naive_pred_test.to_csv('submission.csv',index = False)
