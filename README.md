# Stock-Monitoring-Using-Python

Hey Everyone!

In this project I have build a Stock Monitoring system in which the program will keep a eye on a stock of your choice and when it goes 5% up or down it will alert you via a message on your mobile phone with a relevant news that caused that stock to go up/down.
I have used some API's over here to pull the data of a particular stock and also send a message on mobile phone.

API's used:
1. Alphavantage to pull stock data
2. Newsapi to get relevant news
3. Twilio to send SMS on your mobile phones

Step by Step guide:

1. Pull in the stock prices we are interested in (I have used Reliance)
2. Filtering out necessary data like eg: share price, closing price, opening. price etc.
3. Writing a program to calculate how much the loss/profit is in percentage.
4. By using Newsapi's API will fetch relevant news about the stock we are interested in.
5. Sending all the information to the user using Twilio API
