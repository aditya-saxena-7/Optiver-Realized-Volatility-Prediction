### Optiver Realized Volatility Prediction x Kaggle Challenge 📈

#### **1. Project Requirements:**
---
The task is to develop predictive models that can accurately forecast short-term volatility of hundreds of stocks across various sectors. Volatility, in financial terms, refers to the degree of variation of a trading price series over time as measured by the standard deviation of logarithmic returns. In simpler terms, it measures how wildly prices swing up and down. This project requires handling and analyzing highly granular financial data—specifically, hundreds of millions of rows detailing stock movements over 10-minute periods.

🔍 **Why Predicting Volatility?**  
---
For trading firms like Optiver, predicting volatility is crucial for effectively trading options. Options are financial derivatives that provide the buyer the right, but not the obligation, to buy (call option) or sell (put option) an underlying asset at a predetermined price before a certain date. The price of options is largely influenced by the volatility of the asset it's based on—the more uncertain the asset's price, the higher the potential payoff for the option holder, and thus, the more valuable the option.

### Real-World Example
---
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

### Portfolio Considerations

**High Volatility Portfolio**:
- **Scenario**: A portfolio with high-volatility stocks might see significant daily fluctuations in value.
- **Actions**: The trader might diversify into bonds, low-volatility stocks, or cash equivalents to stabilize returns and reduce risk.

**Low Volatility Portfolio**:
- **Scenario**: A portfolio with low-volatility stocks might provide steady but lower returns.
- **Actions**: The trader might introduce some higher-volatility stocks or sectors to enhance potential returns while maintaining an overall balanced risk profile.

### 🔍 Methodology
---

<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(798).png" width=80%>

#### Competition Format and Predictive Task

**Realized Volatility (RV) Formula**:  
The key metric of interest, Realized Volatility, is computed as:

sigma = \sqrt{\sum_{t} r_{t-1,t}^2}

Here, (r_{t-1,t} represents the log returns of stock prices at consecutive time points, and the formula calculates the standard deviation of these log returns. 

Notably, the calculation assumes a zero mean return and omits any scaling factor, simplifying the volatility estimation to focus purely on the magnitude of price fluctuations without averaging.

**Evaluation Metric**:
The accuracy of the predictions is assessed using the Root Mean Squared Percentage Error (RMSPE), defined as:

\text{RMSPE} = \sqrt{\frac{1}{n} \sum_{i=1}^n \left(\frac{(y_i - \hat{y}_i)}{y_i}\right)^2}

This metric evaluates the percentage errors relative to the actual values, emphasizing the proportional accuracy of the predictions across different stock price scales.

**Data Scale and Utilization**:  

Participants are provided with a massive dataset consisting of approximately 150,000 data points across 112 stocks. Each data point represents a 10-minute window of trading activity, capturing intricate details of market movements. 

The predictive models utilize order book and transaction data from the preceding 10-minute window to forecast the upcoming volatility.

### Key Challenges and Considerations

Participants must address several challenges inherent in this task:

- **Handling High-Frequency Data**: The models must efficiently process and extract useful patterns from vast amounts of granular data within limited time frames.
  
- **Accuracy under Market Volatility**: Ensuring prediction accuracy in diverse market conditions, including periods of high volatility and unpredictable market events.
  
- **Overfitting Prevention**: Developing a model that generalizes well to new data, avoiding overfitting to historical data used during the model development phase.

#### Calculating Weighted Average Price (WAP)

To predict volatility from order book data, one needs to derive a price that best represents the market conditions at any given moment. The Weighted Average Price (WAP) is used for this purpose and is calculated as follows:

WAP = (BidPrice_i * AskSize_i) + (AskPrice_i * BidSize_i) / (BidSize_i + AskSize_i)

**Example**:

Using the formula, the WAP takes into account both the price and the size of bids and asks, providing a price point that reflects both the depth of the market and the existing trading volume.

#### From WAP to Volatility

**Log Returns**:

Once the WAP is calculated, the next step involves computing the log returns. Log returns are a standard measure in finance for calculating the relative changes in price over time and are expressed as:

r_{t_1, t_2} = log(S_2/S_1)

where (S_1) and (S_2) are the WAPs at two consecutive time points.

**Realized Volatility**:

Finally, realized volatility is calculated using the formula introduced earlier:

\sigma = \sqrt{\sum_{t} r_{t-1,t}^2}

- **\( \sigma \)**: This represents the volatility.
- **\( r_{t-1,t} \)**: These are the log returns of the stock prices between consecutive time points.

This measure captures the standard deviation of log returns, providing a quantitative measure of the market's volatility over a specified period.

### Understanding Volatility Calculation with Log Returns

**Volatility** measures how much the price of a financial asset fluctuates over a certain period. In simpler terms, it's a way to quantify the risk or uncertainty about the asset's price changes. 

#### Step-by-Step Explanation:

1. **Log Returns**:
   - **Definition**: The log return \( r_{t-1,t} \) for a given time period from \( t-1 \) to \( t \) is calculated as:
     
     \[ r_{t-1,t} = \log \left( \frac{P_t}{P_{t-1}} \right) \]
     where \( P_t \) and \( P_{t-1} \) are the stock prices at time \( t \) and \( t-1 \) respectively.
   
   - **Purpose**: Log returns are used because they make the data more stable and easier to handle mathematically, especially when dealing with compounding returns over time.

2. **Summing Squared Log Returns**:

   - **Square Each Log Return**: Squaring each log return magnifies the impact of larger fluctuations while ensuring all values are positive.
     
   - **Sum of Squared Log Returns**: Summing these squared values gives us a measure of the total variability in the stock price over the observed period.

3. **Square Root of the Sum**:
   
   - **Why Square Root**: Taking the square root of the sum of squared log returns converts our measure back to the original scale of the log returns, making it comparable to the standard deviation (a common measure of variability).

#### Intuition Behind the Formula:

- **Log Returns Reflect Price Changes**: By using log returns, we capture the relative changes in stock prices over consecutive time periods.
  
- **Squaring and Summing Magnifies Variability**: Squaring the log returns emphasizes larger price changes (more volatility) and summing them aggregates the total variability.
  
- **Square Root Normalizes the Measure**: The square root brings the measure back to a scale comparable to the standard deviation, giving us a clear sense of the average volatility.

#### Example:

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

#### Interpretation:

- The calculated volatility 0.08154 means that the stock's price fluctuations are relatively small over the observed period.
  
- This measure gives us a standardized way to compare volatility across different stocks or time periods.





































