"""
testing the webscraper modules
"""
import modules.webscraper

def example_matchday():
    """
    runs 'load_matchday' for the example matchday 5 in 22/23
    """
    modules.webscraper.load_matchday(2022, 5)
