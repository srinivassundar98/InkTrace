Abstract
Our project analyzes features such as headlines, article content, and the emotions and sentiments expressed. We aim to identify unique writing styles and thematic preferences among journalists and media outlets. By developing a predictive model using deep learning techniques, we seek to ascertain the authorship of news articles. This approach will significantly enhance content personalization and provide deeper insights into media biases and reporting styles

Data Processing Pipeline
The data is processed as a pipeline for a ML project, beginning with raw data sources from Kaggle, All News, All News 2.0, and NY Times. The raw data undergoes cleaning, including feature selection, dropping null values, and down-sampling. This clean data is then enriched and transformed through sentiment and emotional recognition, and vectorization. The enriched data feeds into an ML model, which in turn predicts the author of the article.

Sentiment and Emotion Recognition
For Sentiment Analysis, RoBERTa– a pretrained LLM was used. For Emotion Recognition another pretrained LLM, distilBERT was used. A sentiment analysis of the news headlines reveal that 73.2% of the headlines were neutral, 19.7% of the headlines were negative and the remaining 7.12% were positive. The box plot displays the distribution of confidence scores for six different emotions. Each emotion shows a median value above 0.8. This sentiment analysis was important to get the insights of the data.

Classification of the Model
A LSTM model has been built and trained to perform author classification based on Article Title, Article Content, Title Sentiment and Title Emotion. We obtained a Validation Accuracy of 89% in attributing authorship to news articles for a set of 10 authors. This success paves the way for a more granular analysis of media narratives and author styles.