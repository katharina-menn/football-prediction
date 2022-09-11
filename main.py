"""
main file to execute in football-prediction
"""
## python imports

## external imports

## local imports
# modules
import modules.webscraper
import modules.data_explorer
# tests
import testing.webscraper

## variable inits
TESTING = True

## code
if TESTING:
    # testing.webscraper.example_matchday()
    e = modules.data_explorer.Explorer()
    print(e.get_unique_teams())
else:
    pass
