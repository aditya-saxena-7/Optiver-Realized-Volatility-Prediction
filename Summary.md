### Optiver Realized Volatility Prediction x Kaggle Challenge 📈

### **1. Project Requirements:**
---
The task is to develop predictive models that can accurately forecast short-term volatility of hundreds of stocks across various sectors. Volatility, in financial terms, refers to the degree of variation of a trading price series over time as measured by the standard deviation of logarithmic returns. In simpler terms, it measures how wildly prices swing up and down. This project requires handling and analyzing highly granular financial data—specifically, hundreds of millions of rows detailing stock movements over 10-minute periods.

### 2.🔍 **Why Predicting Volatility?**  
---

For trading firms like Optiver, predicting volatility is crucial for effectively trading options. Options are financial derivatives that provide the buyer the right, but not the obligation, to buy (call option) or sell (put option) an underlying asset at a predetermined price before a certain date. The price of options is largely influenced by the volatility of the asset it's based on—the more uncertain the asset's price, the higher the potential payoff for the option holder, and thus, the more valuable the option.

#### 2.1 Real-World Example

**High Realized Volatility**:

**Scenario**: A tech stock experiences high volatility due to market speculation and news about potential regulatory actions.

**Trader Actions**:
- **Reduce Position**: The trader sells a portion of their holdings to lock in profits and reduce exposure.
- **Hedging**: The trader buys put options to protect against a possible drop in stock price.
- **Day Trading**: The trader takes advantage of price swings by buying and selling within short periods to capture profits.

**Low Realized Volatility**:

**Scenario**: A utility company stock has low volatility due to its stable earnings and lack of market-moving news.

**Trader Actions**:
- **Increase Position**: The trader buys more shares, expecting stable returns.
- **Covered Calls**: The trader sells covered call options to generate additional income, leveraging the stock's stability.
- **Diversify**: The trader adds more of this stock to their portfolio to balance against more volatile tech stocks they hold.

#### 2.2 Portfolio Considerations

**High Volatility Portfolio**:
- **Scenario**: A portfolio with high-volatility stocks might see significant daily fluctuations in value.
- **Actions**: The trader might diversify into bonds, low-volatility stocks, or cash equivalents to stabilize returns and reduce risk.

**Low Volatility Portfolio**:
- **Scenario**: A portfolio with low-volatility stocks might provide steady but lower returns.
- **Actions**: The trader might introduce some higher-volatility stocks or sectors to enhance potential returns while maintaining an overall balanced risk profile.

### 3. 🔍 Methodology
---

<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(798).png" width=80%>

#### 3.1 Competition Format and Predictive Task

#### 3.2 **Realized Volatility (RV) Formula**:  

The simplified version ignores any mean of the returns and just sums the squared log returns. This is reasonable for high-frequency data where the mean return can be very close to zero. The formula is:

sigma = \sqrt{\sum_{t} r_{t-1,t}^2}

Here, (r_{t-1,t} represents the log returns of stock prices at consecutive time points, and the formula calculates the standard deviation of these log returns. 

Notably, the calculation assumes a zero mean return and omits any scaling factor, simplifying the volatility estimation to focus purely on the magnitude of price fluctuations without averaging.

#### 3.3 **Evaluation Metric**:

The accuracy of the predictions is assessed using the Root Mean Squared Percentage Error (RMSPE), defined as:

RMSPE = (1/n) \sum_{i=1}^n \left(\frac{(y_i - \hat{y}_i)}{y_i}\right)^2}

This metric evaluates the percentage errors relative to the actual values, emphasizing the proportional accuracy of the predictions across different stock price scales.

#### 3.4 **Data Scale and Utilization**:  

Participants are provided with a massive dataset consisting of approximately 150,000 data points across 112 stocks. Each data point represents a 10-minute window of trading activity, capturing intricate details of market movements. 

The predictive models utilize order book and transaction data from the preceding 10-minute window to forecast the upcoming volatility.

### 4. Key Challenges and Considerations
---

Participants must address several challenges inherent in this task:

- **Handling High-Frequency Data**: The models must efficiently process and extract useful patterns from vast amounts of granular data within limited time frames.
  
- **Accuracy under Market Volatility**: Ensuring prediction accuracy in diverse market conditions, including periods of high volatility and unpredictable market events.
  
- **Overfitting Prevention**: Developing a model that generalizes well to new data, avoiding overfitting to historical data used during the model development phase.

### 5. Calculating Weighted Average Price (WAP)
---

To predict volatility from order book data, one needs to derive a price that best represents the market conditions at any given moment. The Weighted Average Price (WAP) is used for this purpose and is calculated as follows:

WAP = (BidPrice_i * AskSize_i) + (AskPrice_i * BidSize_i) / (BidSize_i + AskSize_i)

**Example**:

Using the formula, the WAP takes into account both the price and the size of bids and asks, providing a price point that reflects both the depth of the market and the existing trading volume.

### 6. From WAP to Volatility
---

#### 6.1 **Log Returns**:

Once the WAP is calculated, the next step involves computing the log returns. Log returns are a standard measure in finance for calculating the relative changes in price over time and are expressed as:

r_{t_1, t_2} = log(S_2/S_1)

where (S_1) and (S_2) are the WAPs at two consecutive time points.

#### 6.2 **Realized Volatility**:

Finally, realized volatility is calculated using the formula introduced earlier:

\sigma = \sqrt{\sum_{t} r_{t-1,t}^2}

- sigma: This represents the volatility.
- r_{t-1,t}: These are the log returns of the stock prices between consecutive time points.

This measure captures the standard deviation of log returns, providing a quantitative measure of the market's volatility over a specified period.

### 7. Understanding Volatility Calculation with Log Returns
---

**Volatility** measures how much the price of a financial asset fluctuates over a certain period. In simpler terms, it's a way to quantify the risk or uncertainty about the asset's price changes. 

#### 7.1 Step-by-Step Explanation:

1. **Log Returns**:
   
   - **Definition**: The log return (r_{t-1,t}) for a given time period from (t-1) to (t) is calculated as:
     
     r_{t-1,t} = log(P_t/P_t-1)
     
     where (P_t) and (P_{t-1}) are the stock prices at time (t) and (t-1) respectively.
   
- **Comparability**: Log returns can be summed over time to find the total return, unlike simple returns which need to be compounded.

- **Symmetry**: They treat positive and negative changes symmetrically, a property not seen in simple returns where a 50% loss cannot be recouped by a 50% gain.

- **Statistical Properties**: Log returns are more likely to be normally distributed, which simplifies various statistical analyses, such as hypothesis testing and interval estimation.

2. **Summing Squared Log Returns**:

   - **Square Each Log Return**: Squaring each log return magnifies the impact of larger fluctuations while ensuring all values are positive.
     
   - **Sum of Squared Log Returns**: Summing these squared values gives us a measure of the total variability in the stock price over the observed period.

3. **Square Root of the Sum**:
   
   - **Why Square Root**: Taking the square root of the sum of squared log returns converts our measure back to the original scale of the log returns, making it comparable to the standard deviation (a common measure of variability).

#### 7.2 Intuition Behind the Formula:

- **Log Returns Reflect Price Changes**: By using log returns, we capture the relative changes in stock prices over consecutive time periods.
  
- **Squaring and Summing Magnifies Variability**: Squaring the log returns emphasizes larger price changes (more volatility) and summing them aggregates the total variability.
  
- **Square Root Normalizes the Measure**: The square root brings the measure back to a scale comparable to the standard deviation, giving us a clear sense of the average volatility.

#### 7.3 Example:

Let's say we have the following stock prices over four time points: 
P_0 = 100
P_1 = 105
P_2 = 102
P_3 = 108

1. **Calculate Log Returns**:
   - r_{0,1} = log(105/100) = 0.04879 
   - r_{1,2} = log(102/105) = -0.02956 
   - r_{2,3} = log(108/102) = 0.05827 

2. **Square Each Log Return**:
   - r_{0,1}^2 = 0.00238 
   - r_{1,2}^2 = 0.00087 
   - r_{2,3}^2 = 0.00340 

3. **Sum of Squared Log Returns**:
   - Sum = 0.00238 + 0.00087 + 0.00340 = 0.00665 

4. **Square Root of the Sum**:
   - sigma = sqrt{0.00665} = 0.08154 

#### 7.4 Interpretation:

- The calculated volatility 0.08154 means that the stock's price fluctuations are relatively small over the observed period.
  
- This measure gives us a standardized way to compare volatility across different stocks or time periods.

### 8. **Based on our code files:**
---

1. [BaseCode](https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/codeBase/BaseCode.ipynb)
2. [Features_Construction_and_EDA](https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/codeBase/Features_Construction_and_EDA.ipynb)

### 9. Terminologies
---

- **time_id:** This identifies the specific time interval or session during which these trades occurred. All the entries you showed are from time_id = 5, suggesting they all belong to the same trading segment or day.

- **seconds_in_bucket:** Indicates the specific second within the time_id when these trades were executed. For example, the first entry shows that at 28 seconds into the trading session identified by time_id = 5, certain trades were executed.

- **price:** This column shows the price at which trades were executed. These prices are normalized and weighted by the number of shares involved in each transaction. The weighting by the number of shares ensures that larger trades have a more significant impact on the average price calculation, giving a more accurate reflection of market prices.

- **size:** Represents the total number of shares or units traded in that specific second. For instance, at 28 seconds (seconds_in_bucket), 553 shares were traded.

- **order_count:** Indicates the number of unique orders that were executed to reach the total trade size reported in the size column for that second. The first entry with order_count = 11 suggests that it took 11 separate orders to accumulate the 553 shares traded at that time.

- **bid_size1 and bid_size2:** Indicate the number of shares buyers are willing to purchase at the corresponding bid prices (bid_price1 and bid_price2). These sizes can be used to gauge market depth and buying interest at different price levels.

- **ask_size1 and ask_size2:** Reflect the number of shares sellers are ready to sell at the corresponding ask prices (ask_price1 and ask_price2). Similar to bid sizes, these provide insights into the market depth on the selling side.

- **ask_spread:** Calculated as ask_size1 - ask_size2, this represents the difference in volume between the closest and next-closest ask levels. It can indicate the liquidity or tightness of the ask side of the order book.

- **bid_spread:** Calculated as bid_size1 - bid_size2, this indicates the volume difference between the top two bid levels. It helps assess the liquidity or tightness on the bid side of the order book.

- **volume_imbalance:** The absolute difference between total bid volumes and total ask volumes (abs(ask_size1 + ask_size2 - bid_size1 - bid_size2)). It's a measure of the current supply-demand balance in the order book.

- **Bid/Ask Spread**
  
The bid/ask spread is a measure of the difference between the highest price that buyers are willing to pay (bid price) and the lowest price that sellers are willing to accept (ask price). It's calculated as follows:

Bid/Ask Spread = (Bid Price/Ask Price) - 1

-- **Market Liquidity**: A narrower bid/ask spread typically indicates greater liquidity, making it easier to execute trades near the market price without causing price movement. if bid/ask spread is higher, that means the liquidity for the single asset is not great. The lower the bid/ask spread the better the marekt liquidity for the specific asset.

-- **Transaction Costs**: For traders, a lower spread means lower transaction costs, as they can buy and sell closer to the mid-price.

-- **Market Sentiment**: Large spreads can also indicate higher uncertainty or lower confidence among traders regarding the asset's value.

### 10. EDA
---

#### 10.1 First Plot: Weighted Average Price (WAP) and Best Bid/Ask Prices

**Conclusions from the WAP Plot:**

- **Price Movements:** The WAP, bid, and ask prices move in sync, as expected, since WAP is derived from these prices. Fluctuations in WAP reflect real-time changes in market conditions.

- **Bid-Ask Convergence and Divergence:** There are periods where the bid and ask prices converge (indicating a tighter spread) and periods where they diverge (wider spread), which could imply changing market liquidity.

- **Price Volatility:** The extent of fluctuation in the WAP line could be indicative of the volatility during this time period. Sharp movements in bid or ask prices that are mirrored in the WAP suggest rapid changes in market sentiment.

#### 10.2 Second Plot: Log Return and Cumulative Log Return

**Conclusions from the Log Return Plot:**

- **Return Fluctuations:** The log returns fluctuate around zero, with no discernible trend, suggesting a market that doesn't have a strong directional movement in this time frame.

- **Cumulative Returns:** The cumulative log return line gives an overall picture of how returns are accumulating or compounding over time. If this line is trending upwards or downwards, it would suggest a longer-term price movement within this bucket.
  
- **Intraday Volatility:** The plot of log returns shows the price volatility at each second. Sharp spikes or dips indicate moments of high volatility.
Combined Insights

By examining both the WAP/bid/ask prices and the log returns together, one can correlate price levels with return patterns. For example, a large gap between the bid and ask prices could lead to more significant log returns due to larger price movements required to match buyers and sellers.

The second plot's cumulative log return can help identify periods of sustained upward or downward price pressure. It's a visual tool that can signal trends within the intraday data that might not be evident from the raw log returns alone.

### 11. Implementing the Bucket Time Inverval Feature Construction
---

#### 11.1 **Splitting the Data**

Based on observation and the plotted data, the idea is to divide the seconds in bucket into segments that likely represent different market conditions:

- **Early Trading Period (0 to 150 seconds):** Captures the opening minutes when trading volumes are typically high due to overnight news, early reactions, and other factors.

- **Mid-Session (150 to 300 seconds and 300 to 450 seconds):** Might capture more of the steady-state trading conditions during the middle part of the trading window.

- **Late Trading Period (450+ seconds):** Likely to encapsulate the closing rush, where traders adjust positions, and liquidity can surge again

#### 11.2 Resulting DataFrame and Its Implications

The final DataFrame df_book_feature contains a rich set of features for each time_id, with each set corresponding to a specific interval of seconds within the bucket. These features include:

- **Realized Volatility:** Measures the volatility for each interval, providing insight into how turbulent the market was during that period.
  
- **WAP Balance Mean:** Indicates the average balance of weighted average prices, useful for understanding market direction.
  
- **Price Spread Mean:** Offers an average of the price differences, which can suggest liquidity or market tightness.
  
- **Volume Imbalance Mean:** Shows the average difference between buying and selling volumes, which can indicate market pressure.

The image displays a heatmap of correlation coefficients between realized volatilities of log returns calculated at different intervals within the trading session (0 seconds, 150 seconds, 300 seconds, and 450 seconds). From the plot, we can observe the following:

- **Strong Positive Correlations:** All the correlation coefficients are positive and relatively high (ranging approximately from 0.73 to 0.85), indicating that there is a strong positive linear relationship between the realized volatilities at different time intervals. This suggests that if volatility is high during one interval, it is likely to be high in the others as well.

- **Consistency Across Time Intervals:** The relatively uniform correlation coefficients across different intervals (no extremely low or negative values) imply that the market exhibits somewhat consistent behavior in terms of volatility throughout these intervals. This consistency can be important for trading strategies that assume stable volatility patterns.

- **No Perfect Correlation:** While the correlations are strong, they are not perfect (not equal to 1), suggesting that there are differences in volatility patterns across different segments of the trading day. These differences can be exploited for timing trades or for risk management.

- **Similarity in Adjacent Intervals:** The higher correlations between adjacent intervals (e.g., 0-150 seconds with 150-300 seconds) compared to non-adjacent intervals (e.g., 0-150 seconds with 300-450 seconds) suggest that volatility does not change abruptly in short succession but might evolve throughout the trading session.

- **Potential for Volatility Clustering:** High correlations in financial time series often indicate volatility clustering, a phenomenon where high-volatility events are followed by high-volatility events, and low-volatility events are followed by low-volatility events. This could inform risk management strategies, as periods of high volatility could be expected to persist.

In conclusion, the heatmap analysis supports the notion that volatility exhibits time-dependent patterns which are relatively stable within the observed intervals but still exhibit some variation. 

The plot reinforces the idea that market volatility does not drastically differ across the specified time intervals on average, which could be an indication of a market that has a consistent behavior in volatility terms through the trading day, at least across the intervals observed here.

### 12. Third Plot: Trade Order vs time_id

This scatter plot visualizes the distribution of trades across different time_ids over the seconds_in_bucket. Here's what we can interpret from the image:

- **Uniform Distribution of Trades:** The plot shows a dense and uniform red area, indicating that trades are evenly distributed throughout the time for each time_id. This could suggest that trading is constant and occurs regularly throughout the trading session.

- **Trade Activity Throughout the Day:** Since there are data points spread across the entire range of seconds_in_bucket, it indicates that trades are happening at all times from the beginning to the end of each trading session.

- **Gaps and Pauses in Trading:** The lighter vertical lines, where the red is less intense, may indicate moments with fewer trades, suggesting brief periods of inactivity or lower trading volume.

- **Alpha Transparency:** The use of alpha=0.1 makes individual points nearly transparent. Areas that appear darker are where many points overlap, suggesting a higher density of trades.

- **No Clear Patterns Over Time:** The distribution appears random without any clear patterns or trends over different time_ids. This randomness implies that the trade frequency is not significantly changing over time across the different time intervals.

- **High-Frequency Data:** The granularity and high frequency of data points are evident, typical of high-frequency trading datasets. This level of detail is necessary for microstructure analysis and algorithmic trading strategies

The key takeaway is that trading does not seem to concentrate at particular times within each session, and there are no immediately apparent anomalies or irregularities in trade timing. This plot provides a foundational understanding of trade distribution, which can be a starting point for more detailed time series analysis or to explore the impact of trades on price movements and volatility.

### 12. Naive AR(1) Model Prediction: Using Last Timestamp realized volatility as target
---

Now we know how to build our predict target, let's using realized volatility of t_i-1 to predict t_i as predeiction benchmark.

A commonly known fact about volatility is that it tends to be autocorrelated.

The concept we are referring to is a basic forecasting technique for time series data where past values are used to predict future values. This method is often called a "naive" forecast because it assumes that the conditions affecting the system won't change much in the short term.

In financial markets, the volatility of an asset is the degree to which its price fluctuates over time. An important characteristic of volatility is that it often shows autocorrelation.

Autocorrelation means that the volatility from one time period is correlated with the volatility from adjacent time periods. In simpler terms, if the volatility is high today, there is a tendency that it might be high tomorrow as well, and vice versa.

A naive model takes advantage of this property by using the realized volatility from the previous time period (say t_i-1) as the forecast for the next period (say t_i). For example, if we know the realized volatility for the first 10 minutes of trading, we might use this as our "prediction" for the realized volatility of the next 10 minutes.

This approach is naive because it does not take into account any other information that could affect price fluctuations, such as market news, economic events, or changes in trading volume. It assumes that the future will be like the immediate past.

Despite its simplicity, the naive model can sometimes be a tough benchmark to beat, especially in markets where conditions do not change drastically over short periods. It's a starting point in model development, providing a baseline against which more complex models can be compared. If a sophisticated model can't outperform the naive model, it may not be providing valuable predictive insight.

In practice, while a naive model may not be the best strategy for making actual trading decisions due to its simplicity, it serves as an important benchmark in the model development process.

#### 12.1 AR(1) Model Formula

The AR(1) model is expressed as:

RV_t = alpha + beta * RV_{t-1} + \epsilon_t

where:
- RV_t is the realized volatility at time t.
- alpha is the intercept term (a constant).
- beta is the autoregressive coefficient, representing the relationship between RV_t and RV_{t-1}.
- epsilon_t is the error term (white noise) at time t.

#### 12.2 Steps for Calculation and Prediction with Dummy Data

[Example](https://www.notion.so/821588e3e88e46a18e40a6b7b4706dde?v=72c1e390d65e4f899bd6694752c1a82e&p=de645508caad45699db1496e79d4b1a6&pm=s)

#### 12.3 Summary

- **Model Fitting:** We used OLS to fit the AR(1) model, obtaining the intercept (\(\alpha\)) and autoregressive coefficient (\(\beta\)).
- **Prediction:** Using the fitted model, we predicted the next period's realized volatility based on the previous period's volatility.

This step-by-step approach demonstrates how to build and interpret an AR(1) model, leveraging the autocorrelation in realized volatility data to make predictions.

### 13.Results & Interpretation:
---

We've defined a function to calculate the Root Mean Squared Percentage Error (RMSPE), which is a commonly used metric to evaluate the performance of regression models when the target variable is continuous and strictly positive. The RMSPE is particularly popular in finance and stock market predictions because it normalizes the error based on the size of the true value, making it a relative error metric.

The RMSPE function calculates the square root of the average squared percentage errors between the actual values (`y_true`) and the predicted values (`y_pred`).

We then calculate the R-squared (R2) score, which provides a measure of how well the variability of the target is explained by the model's predictions. An R2 score of 1 indicates perfect correlation, while a score of 0 indicates no correlation.

- **R2 score**: With a value of 0.628, the naive model explains about 62.8% of the variability in the target. This is a fairly decent score for a naive model and indicates some level of predictive power.

- **RMSPE**: A value of 0.341 means that, on average, the predictions of the naive model deviate from the actual realized volatilities by 34.1%. This value gives an idea of the error magnitude in relation to the actual volatility values.

The performance metrics suggest that while the naive model has a certain predictive capability, there is still room for improvement. The R2 score shows a positive correlation, but the RMSPE indicates that the predictions are not very close to the actual values in percentage terms, which could be critical when making trading decisions or managing risk. The goal in a predictive modeling task would be to develop a model that increases the R2 score and decreases the RMSPE.
