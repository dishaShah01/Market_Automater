import pandas as pd
import snscrape.modules.twitter as sntwitter
import argparse
import itertools
from distutils.sysconfig import get_python_lib
import os
#search = '"electric scooter"'

# df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
#     'electric scooter near:"Mumbai" within:10km').get_items(), 50))[['date', 'content']]

# loc = '34.052235, -118.243683, 10km'
# os.system("snscrape --jsonl --max-results 100 --since 2021-08-01  twitter-search \"Maggi near:'Los Angeles' within:10km\" > tweets.json")


def tweet_data(search_query, radius = 10, location = None):
    if location is not None:
        df_coord = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
            search_query + ' near:"'+ location+'" within:'+str(radius)+'km').get_items(),1000)
                                )[['user', 'date','content']]
    else:
        df_coord = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
            search_query).get_items(),1000))[['user', 'date','content']]
    df_coord['user_location'] =  df_coord['user'].apply(lambda x: x['location'])
    df_coord.to_csv("Marketer/data/dataset/" + "twitter_results.csv", index= False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, help='query for which data has to be collected')
    parser.add_argument('--location', type=str, default=None, help='location for which data has to be collected')
    parser.add_argument('--radius', type=str, default=None, help='radius for location')
    args = parser.parse_args()
    print(args.query, args.radius, args.location)
    tweet_data(args.query, args.radius, args.location)

if __name__ == "__main__":
    main()

