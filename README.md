# Shodan-Favicon-Hash-Search

This script allows you to search the Shodan database for servers with a specific favicon. It downloads the favicon from a specified URL, calculates its MurmurHash, and then uses the Shodan API to find hosts with the same favicon hash.

## Dependencies
This script requires the mmh3 and requests libraries. You can install them with pip:

`pip install mmh3 requests`

## Usage
First, replace 'your_shodan_api_key' with your actual Shodan API key in the script.

To run the script, use:

`python favicon_hash_search.py`

When prompted, enter the URL of the favicon you want to search for.

The script will then download the favicon, calculate its hash, and search for the hash in Shodan. The results will be printed on the screen. Each result will include the IP address, port, and hostnames of the matching host.

## Note
Please remember that this script does not handle errors that might occur if the Shodan API is not reachable. It also does not handle rate limiting, so if you're planning to use this script heavily, you might want to add some functionality to handle that.
