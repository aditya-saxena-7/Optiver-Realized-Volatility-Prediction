# Trading Volatility Using Historical VolatilityCones
---

Volatility cones are a tool used by traders to assess whether the current implied volatility of options is high or low compared to historical volatilities over similar time frames. Here's how they work and why they're important in options trading: 📉📈

### Understanding Volatility Cones

1. **Concept of Volatility**: Volatility measures how much the price of an asset varies over time. In options trading, two types of volatility are considered:
   - **Historical Volatility**: This looks at how much the asset's price has fluctuated in the past over a given period.
   - **Implied Volatility**: This is derived from the current market price of options and reflects the market's expectation of future volatility.

2. **Building the Cone**: The volatility cone is essentially a graphical representation that shows the range of historical volatilities for different time periods (like 1 month, 3 months, etc.). These ranges are plotted to see how they compare to the current implied volatility of an option.

   - **Mean Reversion**: This principle suggests that volatility tends to return to its average over time. By plotting historical volatilities, traders can see a pattern or trend indicating mean reversion.

3. **Comparison with Implied Volatility**: Traders use the volatility cone to determine if the current implied volatility is unusually high or low compared to historical norms. This comparison helps in deciding:
   - **Overpriced Options**: If the implied volatility is higher than the historical range, the options might be overpriced.
   - **Underpriced Options**: Conversely, if it's lower, the options might be underpriced.

Volatility cones are crucial tools in the toolkit of volatility traders, helping them navigate the often unpredictable markets. 🌐 Let’s break down the excerpt from your paper and sprinkle in some emojis for added clarity and engagement! 🎉

### What are Volatility Cones? 📐

Volatility cones are used to gauge if options are priced reasonably based on the historical volatility data. They compare current implied volatility against historical volatility to decide if options are underpriced or overpriced. Here's a deeper look:

1. **Challenge in Volatility Trading**: When you trade based on volatility, you're essentially betting against the market’s consensus on how much the price of an underlying asset will swing. The key challenge here is determining whether the options are cheap or expensive, which isn't straightforward. 🤔

2. **Limits of Black-Scholes Model**: This model, a cornerstone in option pricing, assumes that the volatility of an option is constant and known beforehand. However, this isn’t practical because volatility changes over time. Therefore, traders turn to historical and implied volatilities to make their assessments. 📉📈

3. **Shortcomings of Traditional Methods**: Often, traders face issues due to the mismatch in the time horizons of historical and implied volatilities. Implied volatility represents a forecast for the future, while historical volatility is based on past data, making direct comparisons tricky due to different time frames. ⏳➡️⌛

4. **How Volatility Cones Help**: Introduced by Burghardt and Lane, volatility cones help reconcile these differences by comparing like with like:
   - **Mean Reversion**: Supported by empirical evidence, mean reversion suggests that price volatility tends to return to a mean over time. Using this principle, volatility cones forecast future movements and provide a benchmark for comparison. 🔄
   - **Time Horizon Matching**: This is a critical aspect of using volatility cones effectively. For example, if you’re looking at an option with 1 month until expiry, you should compare its implied volatility with the 1-month historical volatility, not with a longer or shorter period. This ensures a more accurate and fair comparison. ⏱️

### Practical Example: 🎓

Imagine you are analyzing an option on a stock with a current implied volatility suggesting significant fluctuations. By using a volatility cone, you can quickly check if this implied volatility is higher or lower compared to historical norms for the same time frame. If it’s higher, the options might be overpriced, and if it’s lower, they could be underpriced. This insight allows traders to make more informed decisions, potentially leading to profitable trading opportunities. 💸📊

In essence, volatility cones offer a systematic way to evaluate the price fairness of options by aligning historical data with current market expectations, helping traders navigate the complex dynamics of options markets with greater confidence. 👍💡

### Trader Reactions to High and Low Implied Volatility

When traders use volatility cones to compare current implied volatility with historical volatility, they can gauge whether options are overpriced or underpriced. Here’s a detailed look at how traders might react in real-world scenarios:

### Scenario 1: High Implied Volatility

**Situation**: The current implied volatility is higher than the historical range for a given time frame, suggesting that the options might be overpriced.

**Possible Trader Actions**:

1. **Sell Options (Short Volatility)**
   - **Action**: A trader might sell call or put options.
   - **Reason**: If options are overpriced, selling them can allow the trader to collect higher premiums. The expectation is that volatility will decrease, and the option prices will drop, allowing the trader to buy them back at a lower price or let them expire worthless.

   **Example**:
   - **Stock**: XYZ Corp
   - **Current Implied Volatility**: 40%
   - **Historical Volatility Range**: 20-30%
   - **Action**: Sell call options on XYZ Corp to collect high premiums, anticipating that implied volatility will revert to the historical range.

2. **Credit Spreads**
   - **Action**: The trader might enter into a credit spread by selling a higher strike option and buying a lower strike option of the same type (both calls or both puts).
   - **Reason**: This strategy profits from the collected premiums and limited risk due to the protective bought option.

   **Example**:
   - **Stock**: ABC Inc
   - **Current Implied Volatility**: 50%
   - **Historical Volatility Range**: 30-40%
   - **Action**: Enter a bear call spread by selling a call at $50 strike and buying a call at $55 strike.

3. **Volatility Contraction Strategies**
   - **Action**: The trader might use strategies like straddles or strangles when expecting a decrease in volatility.
   - **Reason**: As the implied volatility decreases, the price of these strategies would decrease, allowing the trader to close them at a profit.

   **Example**:
   - **Stock**: DEF Ltd
   - **Current Implied Volatility**: 60%
   - **Historical Volatility Range**: 35-45%
   - **Action**: Enter an iron condor by selling an out-of-the-money call and put and buying further out-of-the-money call and put, profiting from reduced volatility.

### Scenario 2: Low Implied Volatility

**Situation**: The current implied volatility is lower than the historical range for a given time frame, suggesting that the options might be underpriced.

**Possible Trader Actions**:

1. **Buy Options (Long Volatility)**
   - **Action**: A trader might buy call or put options.
   - **Reason**: If options are underpriced, buying them can be profitable if the implied volatility increases or if there is a significant move in the underlying asset’s price.

   **Example**:
   - **Stock**: GHI Co
   - **Current Implied Volatility**: 15%
   - **Historical Volatility Range**: 25-35%
   - **Action**: Buy call options on GHI Co, anticipating an increase in implied volatility or a significant upward price move.

2. **Debit Spreads**
   - **Action**: The trader might enter into a debit spread by buying a lower strike option and selling a higher strike option of the same type.
   - **Reason**: This strategy takes advantage of the expected increase in implied volatility and potential movement in the stock price.

   **Example**:
   - **Stock**: JKL Ltd
   - **Current Implied Volatility**: 10%
   - **Historical Volatility Range**: 20-30%
   - **Action**: Enter a bull call spread by buying a call at $30 strike and selling a call at $35 strike.

3. **Long Straddles and Strangles**
   - **Action**: The trader might buy straddles or strangles to benefit from significant price movements in either direction.
   - **Reason**: These strategies are profitable if the underlying asset experiences large movements, and the low implied volatility means cheaper options.

   **Example**:
   - **Stock**: MNO Corp
   - **Current Implied Volatility**: 12%
   - **Historical Volatility Range**: 22-32%
   - **Action**: Buy a straddle by purchasing both a call and a put option at the same strike price, expecting significant movement in the stock.

### Summary

**High Implied Volatility**:
- **Sell Options**: Take advantage of high premiums.
- **Credit Spreads**: Collect premiums with limited risk.
- **Volatility Contraction Strategies**: Profit from expected decrease in volatility.

**Low Implied Volatility**:
- **Buy Options**: Benefit from potential increase in volatility or significant price movements.
- **Debit Spreads**: Use expected movement and volatility increase to profit.
- **Long Straddles and Strangles**: Capture large price movements in either direction with cheap options.

By using volatility cones, traders can align their strategies with historical volatility trends, enhancing their decision-making process and potentially improving their trading outcomes.

Let’s dive into the fascinating world of volatility cones and historical data using your research paper on Nortel Networks stock! 🌍📊

### Estimating Historical Volatility 🧮

1. **Data Collection**: The analysis starts with collecting 15 months of stock price data from [Yahoo! Finance](http://finance.yahoo.com/) for Nortel Networks (symbol "nt.to"). This comprehensive dataset allows for a detailed examination of stock volatility over various time periods.

2. **Calculating Volatility**:
   - **Formula Used**: Volatility is estimated using the formula:

   <img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/formula.png" width=80%>

   - **Annualization**: The factor "square toot of 252" is used to annualize the volatility, as there are typically 252 trading days in a year.

   - **S and N**: \(S\) represents the stock closing price, and \(N\) is the number of business days in the period under study (e.g., 20 days for 1 month, 60 days for 3 months, etc.).

3. **Data Segmentation**: The analysis segments the data into different periods: 1, 3, 6, 9, and 12 months. This segmentation helps understand how volatility changes over different time horizons.

### Constructing the Volatility Cone 📈

   <img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/charts.png" width=80%>

This chart, labeled "Figure I - Historical Volatility Cone of Nortel Networks as at January 2003: 30-day Historical Volatilities vs. Implied Volatility," provides a visual representation of the historical and implied volatilities of a specific Nortel Networks call option (March 04 call at 4.500) over time leading up to its expiry. Here's a breakdown of the elements in the chart:

### 1. **Axes**
   - **X-axis**: Represents the "Days to Option Expiry," ranging from 0 to 360 days. This timeline helps in analyzing how volatility changes as the option approaches its expiration date.
   - **Y-axis**: Represents the volatility levels, expressed as percentages, from 0% to 180%.

### 2. **Lines on the Chart**
   - **Dashed Line (Blue Dashes)**: Represents the 30-day historical volatility observed over different time periods. This line shows how the historical volatility of the stock has trended as the option nears its expiry.
   - **Solid Line (Red)**: Represents the implied volatility, which is the market's expectation of future volatility derived from the current price of options.

### 3. **Behavior of the Lines**
   - The **historical volatility** starts very high (near 180%) and shows significant fluctuations early on (within the first 60 days to expiry). It tends to decrease and stabilize as the option approaches its expiry, fluctuating around lower values.
   - The **implied volatility** line starts lower than the initial historical volatility and exhibits less volatility. It remains relatively stable over time, indicating that the market's expectations about future price movements are more consistent compared to past price movements.

### 4. **Volatility Cone**
   - The "cone" shape is formed by the outer bounds of the historical volatility, which taper as the days to expiry decrease. The cone's boundary lines are not explicitly drawn here but can be visualized as encompassing the highest and lowest points of the historical volatility, indicating the range in which the volatility typically resides.

### 5. **Key Observations**
   - Throughout most of the time period, the implied volatility closely tracks the lower range of historical volatility, suggesting that the market's expectations are leaning towards the less volatile end of historical observations.

This chart is essential for options traders focusing on volatility strategies, such as those looking to capitalize on discrepancies between implied and historical volatilities.

### Table Analysis 🖼️

   <img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/table.png" width=80%>

The table you've shown, labeled as "Table I - Nortel Networks Stock Historical Volatilities," presents historical volatility data for various time horizons: 1-month, 3-month, 6-month, 9-month, and 12-month. Here's a detailed explanation and the insights we can derive from it:

### Understanding the Table Structure
- **Rows**: Each row represents a different period ending, from January 2004 back to November 2002. This provides a timeline of volatility data for each specified time frame.
- **Columns**: Each column after the period ending indicates the calculated historical volatility for the respective time horizons (1-month through 12-month).

### Key Figures in the Table
- **Maximum, Mean, Minimum (Bottom Rows)**:
  - These rows summarize the highest, average, and lowest historical volatilities observed for each time frame over the specified period. This summary provides a quick reference for understanding the range of volatility experienced by Nortel Networks' stock.
  
### Insights from the Table
1. **Volatility Ranges**:
   - **1-Month Volatility**: Shows a dramatic range from a low of 27.11% to a high of 127.96%. This indicates high short-term volatility fluctuations, which can be critical for short-term trading strategies.
   - **Longer-Term Volatility**: As you look at longer durations (such as 9-months and 12-months), the volatility range narrows (e.g., 9-month volatility varies from 50.50% to 76.40%). This suggests that longer-term volatilities are more stable compared to short-term, reflecting lesser uncertainty or better predictability over longer periods.

2. **Volatility Trends**:
   - Typically, as shown in the table, shorter time horizons exhibit higher and more erratic volatility due to immediate market reactions and shorter-term uncertainties. In contrast, longer durations show moderated volatilities as they absorb and average out short-term fluctuations.
     
### 1. **Comparison of Implied and Historical Volatilities**
- **Common Practice**: Traders often compare current implied volatilities (the market's expectation of future volatility as reflected in options prices) with short-term historical volatilities (actual volatility experienced by the stock in the recent past) to gauge whether options are overpriced or underpriced.
- **Potential Misleading Outcomes**: This practice can be misleading. For example, the passage notes that from late October 2003 to early January 2004, implied volatilities were consistently higher than historical volatilities. This might suggest that options were overpriced. However, the implied volatilities were actually aligning with their long-term average, indicating that the options might not have been overpriced after all.

In the context of trading options, **implied volatility** is a measure derived from the current price of the options themselves and reflects the market's expectation of future volatility. When we talk about implied volatilities "aligning with their long-term average," it means that the current implied volatility is similar to the average volatility values observed over a longer historical period. This alignment suggests that the current market expectations for future volatility are consistent with what has been typically observed in the past.

### Breaking Down the Implication:

1. **Understanding Implied Volatility**: Implied volatility isn't an observed statistic like historical volatility; rather, it is inferred from market prices of options. It embodies expectations about how much the underlying asset will move in the future. Higher implied volatility generally leads to higher option prices, and vice versa.

2. **Long-term Average**: This refers to the average level of implied volatility calculated over a long period. This could encompass several months or years, depending on the analysis. The long-term average helps in gauging whether current levels are typical or anomalous compared to past norms.

3. **Market Pricing of Options**: If the current implied volatility is close to the long-term average, it suggests that the pricing of options (which is sensitive to changes in implied volatility) might be reasonable or justified based on historical patterns. Therefore, even if the implied volatility is higher than what recent historical volatility would suggest, it might still be in line with longer-term trends, indicating that options may not be overpriced.

### Practical Example:

- Suppose the long-term average implied volatility for a particular stock is around 30%, and due to recent market events, the implied volatility observed is 32%. While this might be higher compared to the last month's average of 25%, it's still close to the long-term average.
- In this scenario, despite the short-term spike, the options might not be overpriced because they align with the broader, more stable historical expectation of volatility, suggesting that the market conditions are normal rather than exceptional.

### 2. **Utilization of Volatility Cones**
- **Advantages**: Volatility cones provide a broader perspective by comparing current implied volatilities not just to a fixed period (like 20 or 30 days) but across a range of historical volatilities over varying time frames. This method gives a more nuanced view of how current volatility compares to past performance under similar conditions.
- **Practical Example**: For the period of late January to early February 2004, the volatility cone suggested that volatility levels were higher than normal, which could represent an opportunity for traders to take positions that benefit from a potential decrease in volatility (short volatility positions).

### 3. **Confidence in Decision Making**
- **Enhanced Decision Making**: By using volatility cones, traders can make more informed decisions based on a comprehensive analysis of how current volatilities compare to a historical range. This method reduces the risk of decisions based solely on recent volatility, which may not reflect longer-term trends or anomalies.

### Practical Uses for Options Traders
- **Volatility Cone Construction**: The data is used to construct a volatility cone, which helps traders understand where the current implied volatility stands in relation to historical norms. This is crucial for assessing whether options are priced fairly relative to historical volatility levels.
- **Decision Making**: Traders use this historical volatility data to inform their decisions on buying or selling options. For example:
  - If current implied volatility is above the historical maximum for a similar time to expiry, it might suggest that the option is overpriced (a potential sell signal).
  - Conversely, if it's below the historical minimum, the option might be underpriced (a potential buy signal).

## Conclusion
---

### Practical Application of Volatility Cones
We've successfully applied the concept of volatility cones using real-world data from Nortel Networks stock options. This technique is widely recognized for its ability to pinpoint potential trading opportunities that could be profitable.  Think of volatility cones as a tool that helps traders understand if the current price of stock options is high, low, or just right. It does this by comparing today’s option price (which anticipates future price swings) with how the stock has actually behaved in the past over similar periods.

### Importance of Time Horizon Matching
When comparing current option prices to historical data, it's essential to align the time frames precisely. The period used to calculate historical volatilities should match the remaining life of the option we are analyzing. This ensures that the comparison is accurate and meaningful.

**Why Match Time Horizons?**  
Imagine you’re trying to predict the weather for a two-week vacation based on past weather data. You wouldn’t look at weather patterns from just a few days to make your decision; you’d look at what the weather was typically like for the whole two weeks in previous years. Similarly, matching time horizons means using past stock data that covers the same time frame as the life left in the options you're studying.
   
### Volatility Mean Reversion
Our empirical analysis confirms that stock volatilities tend to revert to a mean or average level over time. We utilized this characteristic, along with historical data, to predict how volatilities might change as options approach their expiration. This can help traders anticipate and strategize according to likely future volatility shifts.

### Continuation
---
1. Historical_Volatility_Cone_vs_Implied_Volatility Demostration
- [Python Code](https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/volatilityCones/Historical_Volatility_Cone_vs_Implied_Volatility.ipynb)
- [Youtube Video](https://youtu.be/_2wa9ldwi5A?si=mAu7xXdpekfryt29)

2. Option Implied Volatility using Newton's Method in Python
- [Python Code](https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/volatilityCones/Option_Implied_Volatility_using_Newtons_Method_in_Python.ipynb)
- [Youtube Video](https://youtu.be/mPgVeazeq5U?si=OOv36rZBdBmP_dQ6)

### References
---
1. Galen Burghardt and Morton Lane, *How to tell if options are cheap*, Journal of Portfolio Management, Winter 1990, Vol. 16. Nov 2.
2. M. Desmond Fitzgerald, *The Handbook of Risk Management and Analysis, Chapter 12: Trading Volatilities*.
3. Anchal Jai, *Rolling down the volatility term structure*, ICICI Bank Limited. [Available here](http://www.icicicareers.com/pdf/VolatilityStructureRolldownl.pdf).

