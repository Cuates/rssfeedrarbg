##
#        File: rssfeedrarbgconfig.py
#     Created: 03/17/2019
#     Updated: 04/07/2019
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
    _driver = None
    _serverName = None
    _port = None
    _database = None
    _username = None
    _password = None
    _pathDB = None

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
            else:
                self._filenameMedia = ''
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
            else:
                self._filenameMedia = ''
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

    # Set database variable
    def _setDatabaseVars(self, type):
        # Define server information
        ServerInfo = 'DWC-DEV-INT-01'

        # Define list of dev words
        ServerType = ['dev']

        # Set production database information where server info does not consist of server type
        if not regEx.search(r'\b' + "|".join(ServerType) + r'\b', ServerInfo, flags=regEx.IGNORECASE):
            # Check if type is SQLite
            if type == 'SQLiteRarBG':
                # Set variables
                self._driver = 'sqlite:///'
                self._servername = ''
                self._port = ''
                self._pathParent = './resource'
                self._pathLevelOne = '/database'
                self._pathLevelTwo = ''
                self._pathDB = '/mediaRSSFeed.sqlite3'
                self._database = self._pathParent  + self._pathLevelOne + self._pathLevelTwo + self._pathDB
                self._username = ''
                self._password = ''
            # Else
            else:
                self._driver = ''
                self._servername = ''
                self._port = ''
                self._pathParent = ''
                self._pathLevelOne = ''
                self._pathLevelTwo = ''
                self._pathDB = ''
                self._database = ''
                self._username = ''
                self._password = ''
        else:
            # Else set development database information
            # Check if type is SQLite
            if type == 'SQLiteRarBG':
                # Set variables
                self._driver = 'sqlite:///'
                self._servername = ''
                self._port = ''
                self._pathParent = './resource'
                self._pathLevelOne = '/database'
                self._pathLevelTwo = ''
                self._pathDB = '/mediaRSSFeed.sqlite3'
                self._database = self._driver + self._pathParent  + self._pathLevelOne + self._pathLevelTwo + self._pathDB
                self._username = ''
                self._password = ''
            # Else
            else:
                self._driver = ''
                self._servername = ''
                self._port = ''
                self._pathParent = ''
                self._pathLevelOne = ''
                self._pathLevelTwo = ''
                self._pathDB = ''
                self._database = ''
                self._username = ''
                self._password = ''

    # Get database variable
    def _getDatabaseVars(self):
        return {'Driver': self._driver, 'Servername': self._servername, 'Port': self._port, 'PathParent': self._pathParent, 'PathLevelOne': self._pathLevelOne, 'PathLevelTwo': self._pathLevelTwo, 'PathDB': self._pathDB, 'Database': self._database, 'Username': self._username, 'Password': self._password}