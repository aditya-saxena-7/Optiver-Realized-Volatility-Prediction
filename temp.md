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


### 📊 Evaluation: Understanding Trade Data
---
<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(800).png" width=80%>

#### Overview of Trade Data

While the primary focus of the Optiver Realized Volatility Prediction competition is on order book data, the trade data provided also plays a crucial role in modeling and forecasting market dynamics. This dataset captures the actual transactions that have occurred, providing a snapshot of executed trades.

**Key Aspects of Trade Data**:
- **Trade Execution**: Trade data records the finalized transactions where a buyer and a seller have agreed on a price and exchanged the security. Unlike the order book, which represents potential market actions, trade data reflects actual market activity.
- **Components**: Each entry in the trade dataset typically includes:
  - **Price**: The price at which the trade was executed.
  - **Size**: The number of shares or units traded.
  - **Order Count**: The number of individual orders that were aggregated to result in the total traded size at the listed price.

#### Example Data Structure

The provided image and description illustrate a typical structure of trade data:

- **time_id**: Identifies the time window the trade belongs to.
- **seconds_in_bucket**: Indicates the seconds past the start of the bucket (or window) when the trade occurred.
- **price**: The execution price of the trades.
- **size**: The number of shares involved in the trades.
- **order_count**: The count of separate trading orders that contributed to the aggregate volume reported.

This structured format allows participants to analyze the frequency, volume, and nature of trades within the specific time windows relevant to the competition's prediction tasks.

#### Relevance to Volatility Prediction

**Integration with Order Book Data**:
While order book data offers insights into potential price movements and market liquidity, trade data provides concrete evidence of how these possibilities materialize into real transactions. This helps in understanding the impact of market orders on price changes and liquidity consumption.

**From Trade Data to Volatility**:
- **Price Impact**: By examining the executed prices and sizes, analysts can infer the immediate impact of trades on market prices. Large trades at prices significantly different from recent WAPs (Weighted Average Prices) might indicate market moves that could affect volatility.
- **Market Activity**: Frequent trading or large aggregate trading volumes within short windows can be indicative of higher volatility. Conversely, sparse or small trades might suggest a less volatile market.

## Detailed Explanation of the Modeling Pipeline
---
<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(801).png" width=80%>

<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(802).png" width=80%>

### Stages in the Pipeline

1. **Feature Engineering**: This initial stage involves creating predictive variables from the raw data that are more effective or informative than the raw data alone. In the context of financial data like order book and trade data, feature engineering could involve calculating statistical summaries (mean, variance), indicators (moving averages), or transformations (logarithmic returns, weighted average prices) that capture underlying trends or patterns relevant for predicting volatility.

2. **Model Integration**: The feature-engineered data is then fed into three distinct models:
    - **Gradient Boosting**
    - **Neural Network (MLP - Multi-Layer Perceptron)**
    - **TabNet (Deep Learning model for tabular data)**
   
3. **Regression (Meta-Modeling)**: Outputs from each of the three models are combined using a regression model that learns to optimally weight the predictions from each primary model to produce a final prediction. This approach leverages the strengths of each model to improve overall prediction accuracy.

### Importance and Relevance

- **Feature Engineering**: Essential for reducing model complexity and enhancing model performance by providing refined inputs that are directly relevant to the target variable (volatility in this case).
- **Model Integration**: Using multiple models allows the capture of different aspects and patterns in the data, possibly reducing the risk of overfitting to the noise in a single modeling approach.
- **Regression (Meta-Model)**: Combines the different predictive signals from each model into a single, more accurate and robust prediction. This step is crucial as it harmonizes the diverse strengths of individual models, mitigating their respective weaknesses.

## Detailed Analysis of Each Model

### 1. Gradient Boosting

- **Pros**:
  - **Efficiency**: Gradient Boosting is generally very fast, especially with implementations like LightGBM.
  - **Performance**: Offers solid performance on structured/tabular data like financial datasets.
  - **Handling of Non-linearities**: Very effective at modeling complex patterns in data through ensemble learning.

- **Cons**:
  - **Overfitting**: Without proper tuning, gradient boosting can overfit, especially with very noisy data.
  - **Interpretability**: Slightly less interpretable than simpler models due to the complexity of ensemble learning.

### 2. Neural Networks (MLP)

- **Pros**:
  - **Flexibility**: Can model complex non-linear relationships and interactions between features.
  - **Scalability**: Well-suited for large datasets and capable of leveraging high-performance computing resources.

- **Cons**:
  - **Tuning Difficulty**: Requires careful tuning of parameters and network architecture, which can be time-consuming and technically challenging.
  - **Data Requirement**: Typically requires large amounts of data to train effectively without overfitting.

### 3. TabNet

- **Pros**:
  - **State-of-the-art**: Incorporates techniques from the successful Transformer architecture to handle tabular data.
  - **Interpretability**: Offers some level of interpretability similar to decision trees by using attention across different features.

- **Cons**:
  - **Complexity**: More complex to set up and tune compared to more traditional models.
  - **Data Sensitivity**: May not always outperform simpler models unless carefully tuned and trained with sufficient data.

### Comparative Advantages and Choice of LightGBM

Choosing **LightGBM** among other gradient boosting options might be motivated by the following:

- **Speed**: LightGBM is designed to be faster and more efficient, particularly in handling large datasets, due to its histogram-based optimizations.
- **Resource Efficiency**: Uses less memory and handles large amounts of data more efficiently.
- **Handling Categorical Features**: Effective in managing categorical data directly without the need for extensive preprocessing.

## Explanation of Basic Features for Volatility Prediction
---

<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(803).png" width=80%>

The features described are crucial for creating a predictive model for financial volatility based on high-frequency order book and trade data. Each feature captures different aspects of market behavior and dynamics, which can significantly influence the model's accuracy and performance. Here’s a detailed breakdown of each feature and its importance:

### Features Based on the Order Book

1. **Weighted Average Price (WAP)**: 
   - **Definition**: A price metric that considers both the price and the quantity (size) of bids and asks. It is calculated as: \[ \text{WAP} = \frac{\text{BidPrice} \times \text{AskSize} + \text{AskPrice} \times \text{BidSize}}{\text{BidSize} + \text{AskSize}} \]
   - **Relevance**: Provides a balanced view of the market's buying and selling pressures at a specific time, reflecting the price at which most trading could occur.

2. **Log Return**:
   - **Definition**: The logarithmic difference between successive prices, commonly used to stabilize the variance of financial time series. \[ \text{Log Return} = \log\left(\frac{\text{Price}_{t}}{\text{Price}_{t-1}}\right) \]
   - **Relevance**: Helps in quantifying the price changes in a way that adjustments for compounding and asymmetries in positive and negative movements are considered.

3. **Volatility**:
   - **Definition**: A statistical measure of the dispersion of returns for a given security or market index. Typically, higher volatility means higher risk.
   - **Relevance**: Essential for risk management in trading and investment strategies, as it provides an estimate of the potential price range of an asset in a given time frame.

4. **Volume and Volume Imbalance**:
   - **Definition**: Volume indicates the number of shares traded in a particular period. Volume imbalance measures the difference between the volume of buy orders and sell orders.
   - **Relevance**: High trading volume can indicate a high interest in a stock, potentially leading to larger price changes. Volume imbalance can signal the direction of the market movement based on dominant trading interest (buying vs. selling).

5. **Bid-Ask Spread**:
   - **Definition**: The difference between the highest bid (buy price) and the lowest ask (sell price).
   - **Relevance**: A narrower spread often indicates a more liquid market, whereas a wider spread can signal higher transaction costs and lower liquidity.

### Smoothing Techniques

- **Moving Averages / Moving Standard Deviation**:
  - **Definition**: These are statistical operations applied to time series data to smooth out short-term fluctuations and highlight longer-term trends or cycles.
  - **Relevance**: They help in understanding underlying trends in the data by damping down the noise of random fluctuations. This is crucial for detecting trends in financial markets where recent changes might be more indicative of future movements.

### Change Detection in Time Series

- **Change Metrics**:
  - **Definition**: Statistical calculations designed to identify significant changes or breaks in a time series, such as differences in volume or price over specified intervals.
  - **Relevance**: Critical for capturing shifts in market conditions, which could be indicative of events or changes in trader behavior, affecting volatility.

### Levels of Information

- **Stock x Time Level, Stock Level, Time Level**:
  - **Definition**: Different granularities of data aggregation — from individual stocks at specific times to broader averages across stocks or time periods.
  - **Relevance**: These features allow models to capture both micro-level fluctuations specific to particular stocks and macro-level trends affecting the entire market or segments of the market over time. 

## Finding New Ideas for Feature Extraction

In competitive modeling environments like the Optiver Realized Volatility Prediction challenge, the standard features—such as volume, volatility, and bid-ask spreads—are often used by many competitors. To gain an edge, it becomes essential to think outside the box or to implement innovative methods that other competitors might not be considering. This often involves exploring new ways to extract meaningful features from the data that capture the underlying patterns or trends not immediately obvious through conventional methods.

## Introduction to Autoencoders
---

<img src="https://github.com/aditya-saxena-7/Optiver-Realized-Volatility-Prediction/blob/main/assets/Screenshot%20(804).png" width=80%>

### What Are Autoencoders?

Autoencoders are a type of neural network used to learn efficient codings of unlabeled data, typically for the purpose of dimensionality reduction. An autoencoder learns to compress (encode) the input into a lower-dimensional code and then reconstruct (decode) the output back to the original input.

### How Autoencoders Work

The typical architecture of an autoencoder includes three main parts:
1. **Encoder**: This part of the network compresses the input into a smaller representation.
2. **Code**: This is the lower-dimensional representation of the input data.
3. **Decoder**: This part attempts to reconstruct the input data from the code, ideally as close to the original input as possible.

The aim is to minimize the difference between the input and the output, which encourages the code to retain as much meaningful information about the input data as possible.

## LSTM Autoencoders for Time Series Data

### What is LSTM?

Long Short-Term Memory (LSTM) units are a building block for layers of a recurrent neural network (RNN). An LSTM is designed to overcome the limitations of traditional RNNs, which are prone to forget earlier information in the input data, making them ineffective for long sequences. LSTMs are capable of learning long-term dependencies in data, which makes them particularly useful for time series analysis where such dependencies are common.

### Why Choose LSTM for Autoencoders in Time Series?

1. **Pattern and Shape Recognition**: LSTMs are well-suited for learning from sequences where the order of data points is important. They can recognize patterns or changes in patterns over time, making them ideal for time series data where the goal is to capture inherent trends that are predictive of future movements.

2. **Handling Time Series Data**: In financial markets, data points are often not independent but are instead a sequence where the past is indicative of the future to some extent. LSTMs can process such data effectively and can be used in autoencoders to both compress and reconstruct the time series data accurately.

### Implementation and Its Relevance

In the model depicted, the LSTM autoencoder is configured to:
- Initially compress a multi-feature time series into a lower-dimensional representation.
- Then expand it back out to reconstruct the original input.

This process helps in extracting the most crucial features from the sequence, encapsulating the information in fewer dimensions while maintaining the sequence's dynamics.

### Pros of Using LSTM Autoencoders

- **Efficient Information Capture**: Can compress information without losing critical temporal dynamics.
- **Pattern Learning**: Especially good at capturing and learning from the patterns in time series data.

### Cons of Using LSTM Autoencoders

- **Complexity in Training**: They are generally more complex and computationally expensive to train compared to simpler models.
- **Need for Down-Sampling**: To manage computational resources effectively, it might be necessary to down-sample the input data, which could potentially lead to loss of some finer details in the data.

### Conclusion

Using LSTM Autoencoders allows for a deep and nuanced understanding of time series data, making them a powerful tool in financial predictions where the dataset is large and complex. However, the trade-off includes increased computational demand and complexity in model tuning and training. Such sophisticated methods are often necessary in competitive environments to achieve superior performance by capturing subtle patterns missed by conventional models.

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









