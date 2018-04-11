# network analysis

## Requirements
- NetworkX 1.2.1 (2.0+ may have also troube importing pickle file)
- gtfspy (linux or osx)
- gmplot
- gmap

## Data Cleaning + Centrality Calculation ##
Please refer to `Data Cleaning + Centrality.ipynb` file.
### `save_n_load.py`
save or load the networkx graph with `.gpickle` file.
gpickle files:
* `net0` 
* `net100`
* `0.gpickle`
* `1.gpickle`
* `2.gpickle`
* `3.gpickle`
* `combined.gpickle`
### `gtfs_recursive.py`
This script group the stations within 100 meters into one node, and reconnect the edges.
### `Pagerank.py`
Using spark to pagerank the network.
### `est_price.py`
Explore the relationship between centrality and real estate price.
### `network_att.ipynb`
Attack the network and discover the resilience of the graph.

