import matplotlib.pyplot as plt
import numpy as np

team1_score = [25,47,34,38,27,48,42,18]
team2_score = [20,32,8,11,43,18,50,31]

score = [5,10,15,20,25,30,35,40]

plt.scatter(team1_score, score,color='red')
plt.scatter(team2_score, score,color='blue')

plt.xlabel('Team score')
plt.ylabel('Score range')

plt.title('Scatter Plot')
plt.show()
