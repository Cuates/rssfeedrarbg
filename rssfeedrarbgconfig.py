##
#        File: rssfeedrarbgconfig.py
#     Created: 03/17/2019
#     Updated: 03/30/2019
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
    _pathParent = None
    _pathLevelOne = None
    _pathLevelTwo = None
    _filenameMedia = None

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
            self._mainURL = ''
            self._rssURL = ''
            self._categoryURL = ''
            self._torrentSearchURL = ''
            self._searchEntryURL = ''

    # Get configuration variable
    def _getConfigVars(self):
        return {'mainURL': self._mainURL, 'rssURL': self._rssURL, 'categoryURL': self._categoryURL, 'torrentSearchURL': self._torrentSearchURL, 'searchEntryURL': self._searchEntryURL}

    # Set filename variable
    def _setFilenameVars(self, mediaType, mediaAction):
        # Check if media action type is ignore
        if regEx.search(r'\bIgnore\b', mediaAction, flags=regEx.IGNORECASE):
            # Set variables
            self._pathParent = './resource'
            self._pathLevelOne = '/list'
            self._pathLevelTwo = '/mediaignore'
            # Check if media action is movie
            if regEx.search(r'\bMovie\b', mediaType, flags=regEx.IGNORECASE):
                self._filenameMedia = '/movieignorelist.txt'
            # Check if media action is television
            elif regEx.search(r'\bTelevision\b', mediaType, flags=regEx.IGNORECASE):
                self._filenameMedia = '/tvignorelist.txt'
        # Check if media action type is delete
        elif regEx.search(r'\bDelete\b', mediaAction, flags=regEx.IGNORECASE):
            # Set variables
            self._pathParent = './resource'
            self._pathLevelOne = '/list'
            self._pathLevelTwo = '/mediadelete'
            # Check if media action is movie
            if regEx.search(r'\bMovie\b', mediaType, flags=regEx.IGNORECASE):
                self._filenameMedia = '/moviedeletelist.txt'
            # Check if media action is television
            elif regEx.search(r'\bTelevision\b', mediaType, flags=regEx.IGNORECASE):
                self._filenameMedia = '/tvdeletelist.txt'
        # Check if media action type is view
        elif regEx.search(r'\bView\b', mediaAction, flags=regEx.IGNORECASE):
            # Set variables
            self._pathParent = './resource'
            self._pathLevelOne = '/list'
            self._pathLevelTwo = '/mediafeed'
            self._filenameMedia = '/mediafeed.txt'
        # Check if media action type is log
        elif regEx.search(r'\bLog\b', mediaAction, flags=regEx.IGNORECASE):
            self._pathParent = './resource'
            self._pathLevelOne = '/log'
            self._pathLevelTwo = ''
            self._filenameMedia = '/rssrarbgpy.log'
        else:
            self._pathParent = ''
            self._pathLevelOne = ''
            self._pathLevelTwo = ''
            self._filenameMedia = ''

    # Get filename variable
    def _getFilenameVars(self):
        return {'pathParent': self._pathParent, 'pathLevelOne': self._pathLevelOne, 'pathLevelTwo': self._pathLevelTwo, 'filenameMedia': self._filenameMedia}