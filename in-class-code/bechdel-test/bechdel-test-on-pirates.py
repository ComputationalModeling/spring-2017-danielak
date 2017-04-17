## Boring setup stuff
import pandas as pd
import requests


def load_pirates_movie_script():
    """
    Returns a DataFrame where each row is a line from the script
    """
    return pd.DataFrame(
        data=requests.get(
            "https://gist.githubusercontent.com/briandk/61d60180accecff51807ffddf0c5f18e/raw/00cfc60c64e75dbd730635850dc393d6c0196243/pirates.txt").text.splitlines(),
        # or in nltk: webtext.raw('pirates.txt').splitlines(),
        columns=["line_of_script"])


pirates_of_the_caribbean = load_pirates_movie_script()
pirates_of_the_caribbean.head()
