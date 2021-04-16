# CKAN Solr

Ckan solr is a specific component used by [CKAN](https://github.com/italia/ckan-it). Apache Solr is a highly reliable, scalable and fault tolerant software component, providing distributed indexing, replication and load-balanced querying, automated failover and recovery, centralized configuration and more. Solr powers the search and navigation features of many of the world's largest internet sites.

## Tools references

The tools referenced in this repository are

* [CKAN](https://ckan.org/)
* [Apache Solr](https://lucene.apache.org/solr/)

## Project components

* **Solr** version 6.2, packaged for CKAN and with some customizations. What's inside this repository.

## How to build this version of Solr and test it as part of CKAN

This specific version of Solr is distributed and consumed in a form of Docker container.

The container can be built using the `Dockerfile` in the root of this repository.

Docker-compose is used to build a fully-functional test environment (build the CKAN container and download pre-packaged dependencies, including Solr).

Instructions can be found in the [CKAN repository](https://github.com/italia/ckan-it).

## How to contribute

Contributions are welcome. Feel free to open issues and submit a pull request at any time!
