from historical_robots.scraper import historical_scraper

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--url")

args = parser.parse_args()
domains = args.url.split(",")
for domain in domains:
    normalized_name = "_".join([x for x in reversed(domain.split("."))])
    historical_scraper(
        domain,
        f"output/{normalized_name}.csv",
        accept_allow=True,
        skip_sleep_interval=True,
        sleep_interval=0.0,
    )
