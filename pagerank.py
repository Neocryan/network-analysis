__author__ = 'Xiaoyu'

import pyspark
from operator import add
from pyspark.sql import SparkSession

try:
    sc.stop()
except:
    pass
sc = pyspark.SparkContext()


def parseNeighbors(urls):
    """Parses a link pair string into urls pair."""
    parts = urls.split('\t')
    return parts[0], parts[1]
def computeContribs(link, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_links = len(link)
    for i in link:
        yield (i, rank / num_links)

spark = SparkSession\
        .builder\
        .appName("PythonPageRank")\
        .getOrCreate()


lines = sc.textFile('/home/neoc/edgelist.txt')


links = lines.map(lambda x: parseNeighbors(x)).distinct().groupByKey().cache()


ranks = links.map(lambda x: (x[0], 1.0))

    # Calculates and updates ranks continuously using PageRank algorithm.
for iteration in range(100):
        # Calculates URL contributions to the rank of other URLs.
    contribs = links.join(ranks).flatMap(
            lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))

        # Re-calculates ranks based on neighbor contributions.
ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

ranks.sortBy(ascending=False,keyfunc=lambda x: x[-1]).saveAsTextFile('../Q5_2/out_100_times')

