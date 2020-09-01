import pandas as pd
import numpy as np
from sklearn import linear_model
import requests
from nba_api.stats import endpoints
from matplotlib import pyplot as plt

# Here we access the leagueleaders module through endpoints & assign the class to "data"
data = endpoints.leagueleaders.LeagueLeaders()

# Our "data" variable now has built in functions such as creating a dataframe for our data
df = data.league_leaders.get_data_frame()

# take a sneak peak at the first 5 rows
df.head()
playerList = list(df.PLAYER)


def printModel(name):
    # First we need to get per game stats.
    # We divide each variable by games played (GP) to get per game average
    x, y = df.FGA / df.GP, df.PTS / df.GP

    # we have to reshape our array from 1d to 2d.
    # The proper shaped array is an input requirement for the linear model
    # reshaping is usually an issue when using 1 x variable
    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)

    # create an object that contains the linear model class
    # Fit our modeling using FGA (x) and PPG (y)
    model = linear_model.LinearRegression()
    model.fit(x, y)

    # Get our r2 value and round it to 2 decimals. How much variance is explained?
    # Get our predicted y values for x
    r2 = round(model.score(x, y), 2)
    predicted_y = model.predict(x)

    # Now, lets make a plot with matplot lib using a iterative approach (which is easy to read)

    plt.clf()
    plt.scatter(x, y, s=100, alpha=.5)  # Scatterplot:  Specfiy size(s) and transparency(alpha) of dots
    plt.plot(x, predicted_y, color='black')  # line: Add line for regression line w/ predicted values
    plt.title('NBA - Relationship Between FGA and PPG')  # Give it a title
    plt.xlabel('FGA per Game')  # Label x-axis
    plt.ylabel('Points Per Game')  # Label y-axis
    plt.text(0, 33, f'R2={r2}')  # 10, 25 are the coordinates for our text. Adjust accordingly

    if name in playerList:
        indexNumber = playerList.index(name)
        plt.annotate(name,  # This the name of the top scoring player. Refer to the .head() from earlier
                     (x[indexNumber], y[indexNumber]),  # This is the point we want to annotate.
                     (x[indexNumber] - 7, y[indexNumber]),  # These are coords for the text
                     arrowprops=dict(arrowstyle='-'))  # Here we use a flat line for the arrow '-'
        plt.scatter(x[indexNumber], y[indexNumber], s = 100, color = 'red')
    else:
        plt.annotate("Player not there",
                     (x[0] - 15, y[0]))

    # Finally, let's save an image called 'graph.png'.
    # We'll set the dpi (dots per inch) to 300, so we have a nice looking picture.
    plt.savefig('graph.png', dpi=300)
    plt.show()
