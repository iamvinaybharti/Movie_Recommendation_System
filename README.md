Movie Recommendation System

Welcome to the Movie Recommendation System! This system is designed to provide personalized movie recommendations based on user preferences. Whether you're a film enthusiast or just looking for something new to watch, this system aims to enhance your movie-watching experience.

Introduction
The Movie Recommendation System employs collaborative filtering and machine learning algorithms to analyze user preferences and recommend movies that are likely to be enjoyed. It takes into account user ratings, viewing history, and similarity to other users to provide accurate and relevant recommendations.

How It Works
The system primarily operates in two phases:

Data Collection: User preferences, movie ratings, and viewing history are collected to build a comprehensive dataset.
Recommendation Generation: Based on the dataset, the system employs collaborative filtering to identify similar users and recommends movies that align with their preferences but are unseen by the target user.
Features


Users can rate movies to help the system understand their preferences better.
Get Recommendations:

Based on user interactions and ratings, the system generates movie recommendations.
Dependencies
Python 3.x
Django
Pandas
NumPy
SQLite

Happy movie watching! 🎬

Similarity Score :
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
![cosine](https://github.com/iamvinaybharti/Movie_Recommendation_System/assets/55456432/8c818629-ab57-4531-8443-f17ea2d83602)



How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
![cos dis](https://github.com/iamvinaybharti/Movie_Recommendation_System/assets/55456432/148bff7c-dce1-44e0-b57f-d05618e2067f)
