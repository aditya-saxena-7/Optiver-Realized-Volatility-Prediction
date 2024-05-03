### Optiver x Kaggle Challenge
---
📈 **Predicting Short-Term Realized Volatility in the Financial Markets: A Quantitative Analysis Using High-Frequency Trading Data**
---
### Table of Contents
1. 📝 [Abstract](#abstract)
2. 🎯 [Introduction](#introduction)
3. 📚 [Literature Review](#literature-review)
4. 🔍 [Methodology](#methodology)
5. 🧠 [Model Development](#model-development)
6. 📊 [Evaluation](#evaluation)
7. 🗃️ [Data Citation](#data-citation)
8. 📈 [Results and Discussion](#results-and-discussion)
9. 🏁 [Conclusion](#conclusion)

### 🔍 Abstract

---

Volatility is one of the most prominent terms you’ll hear on any trading floor – and for good reason. In financial markets, volatility captures the amount of fluctuation in prices. High volatility is associated to periods of market turbulence and to large price swings, while low volatility describes more calm and quiet markets. For trading firms like Optiver, accurately predicting volatility is essential for the trading of options, whose price is directly related to the volatility of the underlying product.

As a leading global electronic market maker, Optiver is dedicated to continuously improving financial markets, creating better access and prices for options, ETFs, cash equities, bonds and foreign currencies on numerous exchanges around the world. Optiver’s teams have spent countless hours building sophisticated models that predict volatility and continuously generate fairer options prices for end investors. However, an industry-leading pricing algorithm can never stop evolving, and there is no better place than Kaggle to help Optiver take its model to the next level.

In the first three months of this competition, you’ll build models that predict short-term volatility for hundreds of stocks across different sectors. You will have hundreds of millions of rows of highly granular financial data at your fingertips, with which you'll design your model forecasting volatility over 10-minute periods. Your models will be evaluated against real market data collected in the three-month evaluation period after training.

Through this competition, you'll gain invaluable insight into volatility and financial market structure. You'll also get a better understanding of the sort of data science problems Optiver has faced for decades. We look forward to seeing the creative approaches the Kaggle community will apply to this ever complex but exciting trading challenge. 📈

### 🌍 Introduction

---

The inherently dynamic nature of financial markets necessitates a profound understanding and precise prediction of short-term price fluctuations, pivotal for effective financial risk management and trading strategies. Specifically, the prediction of realized volatility within concise intervals, such as 10 minutes, is essential for the strategic structuring and accurate pricing of financial derivatives. This project leverages the comprehensive dataset from the Optiver Realized Volatility Prediction, on Kaggle, which provides intricate insights into the microstructure of the financial markets captured through one-second snapshots of order book data and executed trades.

🚀 Focusing on these high-frequency data points, our research endeavors to forge robust predictive models and simultaneously enrich the broader field of financial analytics by refining the accuracy of short-term volatility forecasts. Such forecasts are crucial, underpinning a wide array of financial decisions that range from day trading strategies to the hedging of intricate financial portfolios, thereby enhancing the decision-making processes within dynamic market environments. 📈

### 📚 Literature Review

---

The concept of realized volatility has been thoroughly explored within the realm of financial literature, with seminal contributions emphasizing its pivotal role in risk management and the pricing of derivatives. Notably, the groundbreaking studies by [Andersen and Bollerslev (1998)](https://www.jstor.org/stable/10.1086/209620) pioneered the utilization of high-frequency trading data to estimate volatility with greater precision than traditional models. This innovative approach has laid the foundation for subsequent research, which has increasingly integrated sophisticated machine learning techniques to further refine prediction accuracy.

🌐 Building upon these academic pillars, more recent inquiries have implemented advanced computational methods such as [Random Forests](https://link.springer.com/chapter/10.1007/978-1-4614-6849-3_12), [Neural Networks](https://ieeexplore.ieee.org/document/7849326), and [Support Vector Machines](https://www.sciencedirect.com/science/article/pii/S0957417407006719) to predict stock price movements based on historical volatility patterns, as explored by Brooks in 2014. These contemporary studies underscore the dynamic evolution of financial analytics and highlight an increasing dependency on fine-grained, high-frequency trading data to capture the subtle nuances of market dynamics, thereby advancing our understanding and capabilities in financial analysis. 📊

### 🔍 Methodology
---

<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(798).png" width=80%>

#### Competition Format and Predictive Task

The Optiver Realized Volatility Prediction competition poses a unique challenge centered on predicting the short-term realized volatility of stocks over a 10-minute window using high-frequency trading data. Let's break down the core elements of this task:

**Realized Volatility (RV) Formula**:  
The key metric of interest, Realized Volatility, is computed as:
\[ \sigma = \sqrt{\sum_{t} r_{t-1,t}^2} \]
Here, \( r_{t-1,t} \) represents the log returns of stock prices at consecutive time points, and the formula calculates the standard deviation of these log returns. Notably, the calculation assumes a zero mean return and omits any scaling factor, simplifying the volatility estimation to focus purely on the magnitude of price fluctuations without averaging.

**Evaluation Metric**:
The accuracy of the predictions is assessed using the Root Mean Squared Percentage Error (RMSPE), defined as:
\[ \text{RMSPE} = \sqrt{\frac{1}{n} \sum_{i=1}^n \left(\frac{(y_i - \hat{y}_i)}{y_i}\right)^2} \]
This metric evaluates the percentage errors relative to the actual values, emphasizing the proportional accuracy of the predictions across different stock price scales.

**Data Scale and Utilization**:  
Participants are provided with a massive dataset consisting of approximately 150,000 data points across 112 stocks. Each data point represents a 10-minute window of trading activity, capturing intricate details of market movements. The predictive models utilize order book and transaction data from the preceding 10-minute window to forecast the upcoming volatility.

#### Model Training and Evaluation Process

The competition format is structured to simulate real-world trading scenarios, where timely and accurate predictions are crucial:

1. **Model Development**: During the initial phase, participants can experiment with various modeling techniques, refine their strategies, and submit predictions as frequently as desired. This phase allows for iterative learning and model optimization based on immediate feedback from the competition platform.

2. **Live Validation**: Post the development phase, a fixed model is used to predict unseen market data over a subsequent three-month period. This live test phase prohibits model adjustments, thus mimicking a real trading environment where algorithms must perform robustly against future data without the possibility for real-time tuning.

3. **Competition Outcome**: The final performance of each participant's model is determined after the live validation period, ensuring that all models are tested impartially and rigorously against actual market developments.

### Key Challenges and Considerations

Participants must address several challenges inherent in this task:

- **Handling High-Frequency Data**: The models must efficiently process and extract useful patterns from vast amounts of granular data within limited time frames.
- **Accuracy under Market Volatility**: Ensuring prediction accuracy in diverse market conditions, including periods of high volatility and unpredictable market events.
- **Overfitting Prevention**: Developing a model that generalizes well to new data, avoiding overfitting to historical data used during the model development phase.

This competition format not only tests participants' ability to develop advanced predictive models but also their skill in creating strategies that are adaptable and resilient in the dynamic landscape of financial markets.

---

### Understanding Order Book Data

<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(799).png" width=80%>

#### Overview of Order Book Data

In the Optiver Realized Volatility Prediction competition, the primary dataset provided is the **Order Book** data. This dataset is critical for understanding market dynamics and is essential for predicting short-term volatility. Here’s a detailed look at what order book data encompasses and how it's utilized in this context:

**Definition**:  
An order book is an electronic list of buy and sell orders for a specific security or financial instrument, organized by price level. It provides a real-time snapshot of market liquidity and is used to gauge potential future movements in the market.

**Components of an Order Book**:
- **Bid**: The bid prices represent the maximum price that buyers are willing to pay for the security. Each bid price is associated with a specific quantity of shares, referred to as the bid size.
- **Ask**: Conversely, the ask prices are the minimum prices at which sellers are willing to sell the security, each accompanied by an ask size.

The data snapshot in the image illustrates how bid and ask information is presented at various price levels, capturing the depth and range of market sentiment.

#### Data Structure and Key Variables

**Columns in Order Book Data**:
- **Price Levels (BidPrice1, AskPrice1, BidPrice2, AskPrice2, etc.)**: These columns represent various price points at which market participants are willing to buy (bid) or sell (ask). The '1' denotes the most competitive (closest to the current market price) bid and ask prices, while '2' represents the next best available prices.
- **Size Levels (BidSize1, AskSize1, BidSize2, AskSize2, etc.)**: These columns correspond to the number of shares available at each of the price points mentioned above.

This structured data format allows traders and algorithms to quickly assess the market's supply and demand dynamics at multiple price levels, providing a granular view of market liquidity.

#### Calculating Weighted Average Price (WAP)

To predict volatility from order book data, one needs to derive a price that best represents the market conditions at any given moment. The Weighted Average Price (WAP) is used for this purpose and is calculated as follows:
\[ \text{WAP} = \frac{\text{BidPrice}_i \times \text{AskSize}_i + \text{AskPrice}_i \times \text{BidSize}_i}{\text{BidSize}_i + \text{AskSize}_i} \]

**Example**:
Using the formula, the WAP takes into account both the price and the size of bids and asks, providing a price point that reflects both the depth of the market and the existing trading volume.

#### From WAP to Volatility

**Log Returns**:
Once the WAP is calculated, the next step involves computing the log returns. Log returns are a standard measure in finance for calculating the relative changes in price over time and are expressed as:
\[ r_{t_1, t_2} = \log \left( \frac{S_2}{S_1} \right) \]
where \( S_1 \) and \( S_2 \) are the WAPs at two consecutive time points.

**Realized Volatility**:
Finally, realized volatility is calculated using the formula introduced earlier:
\[ \sigma = \sqrt{\sum_{t} r_{t-1,t}^2} \]
This measure captures the standard deviation of log returns, providing a quantitative measure of the market's volatility over a specified period.

---

### 🧠 Model Development

---

[Need to Add]

Each model's performance is rigorously evaluated using a validation set, and ensemble techniques are employed to combine the strengths of individual models, thereby enhancing the overall predictive accuracy. The final model selection is guided by the RMSPE, ensuring that the chosen model not only fits the training data well but also generalizes effectively to unseen data.

### 📊 Evaluation

---

To accurately assess the performance of our volatility prediction models, we employ the Root Mean Square Percentage Error (RMSPE), which offers a robust measure of prediction accuracy relative to the true observed values. This metric is particularly useful for comparing the effectiveness of our diverse set of models across different stock segments and time periods. We further refine our evaluation process by conducting cross-validation within the training set, ensuring our model's stability and robustness against overfitting. Through iterative testing and model refinement, we optimize parameters to enhance predictive performance, striving to achieve the lowest possible RMSPE.

### 🗃️ Data Citation

---

The data used in this project is sourced from the "Optiver Realized Volatility Prediction," available on Kaggle. This dataset is critical for our analysis as it provides high-resolution insights into the micro-structure of the financial markets, including order book snapshots and executed trades data, which are pivotal for our predictive modeling.

Tom Forbes, John Macgillivray, Matteo Pietrobon, Sohier Dane, Maggie Demkin. (2023). [Optiver - Realized Volatility Prediction](https://www.kaggle.com/c/optiver-realized-volatility-prediction/overview).

### 📈 Results and Discussion

---

[Need to Add]


### 🏁 Conclusion

---

[Need to Add]

---

Feel free to reach out at [adityasaxena@g.harvard.edu](mailto:adityasaxena@g.harvard.edu) for more insights or potential collaboration! 🤝 Happy trading and analyzing! 📊🚀









