"""
main file to execute in football-prediction
"""
## python imports

## external imports

## local imports
# modules
import modules.webscraper
import modules.database_sync
# tests
import testing.webscraper

## variable inits
TESTING = True

## code
if TESTING:
    # testing.webscraper.example_matchday()
    modules.database_sync.sync()
else:
    pass
