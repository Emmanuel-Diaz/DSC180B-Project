#!/usr/bin/env python
import sys
sys.path.append('./src')

import etl
import test_target

if __name__ =="__main__":

    targets = sys.argv[1:]
    #Begin WW2 Scraping process in etl.py
    #scraper = Scraper()
    if len(targets)>1:
        print("Please enter one target at a time")
    elif len(targets)==1 and targets[0] in ["test", "scrape", "test-project"]:
        if targets[0]=="test":
            #RUN TEST TARGET
            test_target.run_test()

