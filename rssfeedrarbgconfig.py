##
#        File: rssfeedrarbgconfig.py
#     Created: 03/17/2019
#     Updated: 03/24/2019
#  Programmer: Daniel Ojeda
#  Updated By: Daniel Ojeda
#     Purpose: RSS feed Rarbg Configuration
##

# Import modules
import re as regEx # regular expression

# Class
class RssFeedRarBgConfig:
    # Declare protected variables
    _mainURL = None
    _categoryURL = None
    _rssURL = None
    _torrentSearchURL = None
    _searchEntryURL = None
    _filenameIgnore = None
    _filenameDelete = None

    # Constructor
    def __init__(self):
        pass

    # Set configuration variable
    def _setConfigVars(self, mediaType):
        # Check if movie
        if regEx.search(r'\bMovie\b', mediaType, flags=regEx.IGNORECASE):
            self._mainURL = 'https://rarbg.to/'
            self._rssURL = 'rssdd.php?'
            self._categoryURL = 'category=44;50;51;52'
            self._torrentSearchURL = 'torrents.php?'
            self._searchEntryURL = '&search='
        elif regEx.search(r'\bTelevision\b', mediaType, flags=regEx.IGNORECASE):
            self._mainURL = 'https://rarbg.to/'
            self._rssURL = 'rssdd.php?'
            self._categoryURL = 'rssdd.php?categories=41;49'
            self._torrentSearchURL = 'torrents.php?'
            self._searchEntryURL = '&search='
        else:
            self._mainURL = None
            self._rssURL = None
            self._categoryURL = None
            self._torrentSearchURL = None
            self._searchEntryURL = None

    # Get configuration variable
    def _getConfigVars(self):
        return {'mainURL': self._mainURL, 'rssURL': self._rssURL, 'categoryURL': self._categoryURL, 'torrentSearchURL': self._torrentSearchURL, 'searchEntryURL': self._searchEntryURL}

    # Set filename variable
    def _setFilenameVars(self, mediaType):
        # Check if movie
        if regEx.search(r'\bMovie\b', mediaType, flags=regEx.IGNORECASE):
            self._pathResource = './resource'
            self._pathLog = '/log'
            self._pathMediaFeed = '/mediafeed'
            self._pathMediaIgnore = '/mediaignore'
            self._pathMediaDelete = '/mediadelete'
            self._filenameFeed = '/moviefeedlist.txt'
            self._filenameIgnore = '/movieignorelist.txt'
            self._filenameDelete = '/moviedeletelist.txt'
        elif regEx.search(r'\bTelevision\b', mediaType, flags=regEx.IGNORECASE):
            self._pathResource = './resource'
            self._pathLog = '/log'
            self._pathMediaFeed = '/mediafeed'
            self._pathMediaIgnore = '/mediaignore'
            self._pathMediaDelete = '/mediadelete'
            self._filenameFeed = '/tvfeedlist.txt'
            self._filenameIgnore = '/tvignorelist.txt'
            self._filenameDelete = '/tvdeletelist.txt'
        else:
            self._pathResource = None
            self._pathLog = None
            self._pathMediaFeed = None
            self._pathMediaIgnore = None
            self._pathMediaDelete = None
            self._filenameFeed = None
            self._filenameIgnore = None
            self._filenameDelete = None

    # Get filename variable
    def _getFilenameVars(self):
        return {'pathResource': self._pathResource, 'pathLog': self._pathLog, 'pathMediaFeed': self._pathMediaFeed, 'pathMediaIgnore': self._pathMediaIgnore, 'pathMediaDelete': self._pathMediaDelete, 'filenameFeed': self._filenameFeed, 'filenameIgnore': self._filenameIgnore, 'filenameDelete': self._filenameDelete}