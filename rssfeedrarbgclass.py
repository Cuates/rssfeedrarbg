##
#        File: rssfeedrarbgclass.py
#     Created: 03/17/2019
#     Updated: 04/20/2019
#  Programmer: Daniel Ojeda
#  Updated By: Daniel Ojeda
#     Purpose: RSS feed Rarbg Class
##

# Import modules
import rssfeedrarbgconfig # rss feed rarbg config
import tkinter # tkinter
import feedparser # feed parser
import webbrowser # web browser
import pathlib # path
import re as regEx # regular expression
import requests # requests
import bs4 # beautiful soup
import logging # logging
import logging.config # logging configuration
import json # json
import sys # system
import datetime # datetime
import pytz # pytz
import tzlocal # tz local
import sqlalchemy # sqlalchemy
from sqlalchemy import event # sqlalchemy event
import pythonjsonlogger # python json logger
import sqlite3 # sqlite3

# Class
class RssFeedRarBgClass:
    # Constructor
    def __init__(self):
        pass

    # Set tkinter window
    #def _setTkinter(self, windowTitle, windowGeometry, windowBackground):
    def _setTkinter(self, windowTitle, windowGeometryWidth, windowGeometryHeight, windowBackground):
        # Try to execute the command(s)
        try:
            # Set tkinter object
            self.window = tkinter.Tk()

            # Set window title
            self.window.title(windowTitle)

            # Set window geometry width
            w = int(windowGeometryWidth)

            # Set window geometry height
            h = int(windowGeometryHeight)

            # Set window screen width
            ws = self.window.winfo_screenwidth()

            # Set window screen height
            hs = self.window.winfo_screenheight()

            # Set x position from the difference of window screen and geometry width
            x = int((ws/2) - (w//2))

            # Set y position from the difference of window screen and geometry height
            y = int((hs/2) - (h/2))

            # Set window geometry
            self.window.geometry('{}x{}+{}+{}'.format(w, h, x, y))

            # Set window background
            self.window.configure(bg=windowBackground)

            # Create menu object from window
            menu = tkinter.Menu(self.window)

            # Create menu object of menu
            new_item = tkinter.Menu(menu)

            # Add item to menu
            new_item.add_command(label='Movie', command=self._executeMovie)

            # Add item to menu
            new_item.add_command(label='Television', command=self._executeTelevision)

            # Add item menu separator
            new_item.add_separator()

            # Add close item menu
            new_item.add_command(label='Close', command=self.window.destroy)

            # Add item menu title
            menu.add_cascade(label='File', menu=new_item)

            # Configure menu
            self.window.configure(menu=menu)
        except Exception as e:
            # Log string
            self._setLogger('Issue setting tkinter window: ' + str(e))

    # Execute Movie
    def _executeMovie(self):
        # Loop through all grids in the window
        for grids in self.window.grid_slaves():
            # Forget all grids
            grids.grid_forget()

        # Initialize variables
        mediaType = 'Movie'
        databaseName = 'SQLiteRarBG'
        tableName = 'rarbgmoviefeed'

        # Set dictionary of column header values
        dictHeaderRow = {0: {'text': mediaType, 'relief': 'ridge', 'width': '100', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '0'},
        1: {'text': 'Date', 'relief': 'ridge', 'width': '30', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '1'},
        2: {'text': 'View', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '2'},
        3: {'text': 'Ignore', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '3'},
        4: {'text': 'Delete', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '4'}}

        # Display header row(s)
        self.rssFeedHeaderDisplay(mediaType, dictHeaderRow)

        ## Call set feed parser
        #rssFeedResponse = self._responseFeedParser('Movie')

        ## Display content row(s)
        #rssFeedResponse = self.rssFeedContentDisplay('Movie', rssFeedResponse, dictHeaderRow)

        # Extract record(s) from database
        databaseResponse = self._extractRecord(databaseName, tableName)

        # Display content row(s)
        self.databaseContentDisplay(mediaType, databaseName, tableName, databaseResponse, dictHeaderRow)

    # Execute Television
    def _executeTelevision(self):
        # Loop through all grids in the window
        for grids in self.window.grid_slaves():
            # Forget all grids
            grids.grid_forget()

        # Initialize variables
        mediaType = 'Television'
        databaseName = 'SQLiteRarBG'
        tableName = 'rarbgtvfeed'

        # Set dictionary of column header values
        dictHeaderRow = {0: {'text': mediaType, 'relief': 'ridge', 'width': '100', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '0'},
        1: {'text': 'Date', 'relief': 'ridge', 'width': '30', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '1'},
        2: {'text': 'View', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '2'},
        3: {'text': 'Ignore', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '3'},
        4: {'text': 'Delete', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '4'}}

        # Display header row(s)
        self.rssFeedHeaderDisplay(mediaType, dictHeaderRow)

        ## Call set feed parser
        #rssFeedResponse = self._responseFeedParser('Television')

        ## Display content row(s)
        #rssFeedResponse = self.rssFeedContentDisplay('Television', rssFeedResponse, dictHeaderRow)

        # Extract record(s) from database
        databaseResponse = self._extractRecord(databaseName, tableName)

        # Display content row(s)
        self.databaseContentDisplay(mediaType, databaseName, tableName, databaseResponse, dictHeaderRow)

    # RSS feed response from given URL
    def _responseFeedParser(self, mediaType):
        # Initialize variable
        rssFeedResponse = ''

        # Try to execute the command(s)
        try:
            # Create object of rss feed parser rarbg config
            rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set variables based on type
            rfrbgconfig._setConfigVars(mediaType)

            # Get dictionary of values
            dictMediaType = rfrbgconfig._getConfigVars()

            # Set variable
            urlFeed = dictMediaType['mainURL'] + dictMediaType['rssURL'] + dictMediaType['categoryURL']

            # Prepare feed parser
            rssFeedResponse = feedparser.parse(urlFeed)
        except Exception as e:
            # Log string
            self._setLogger('Issue with ' + mediaType + ' feed parser: ' + str(e))

        # Return feed response
        return rssFeedResponse

    # Build media serach URL
    def _mediaSearchURL(self, mediaType, urlType):
        # Initialize variable
        searchURL = ''

        # Try to execute the command(s)
        try:
            # Create object of rss feed parser rarbg config
            rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set variables based on type
            rfrbgconfig._setConfigVars(mediaType)

            # Get dictionary of values
            dictMediaType = rfrbgconfig._getConfigVars()

            # Check if url type is pseudo or genuine
            if urlType == 'pseudo':
                # Set variable
                searchURL = dictMediaType['mainURL'] + dictMediaType['torrentSearchURL'] + dictMediaType['categoryURL'] + dictMediaType['searchEntryURL']
            elif urlType == 'genuine':
                # Set variable
                searchURL = dictMediaType['mainURL']
        except Exception as e:
            # Log string
            self._setLogger('Issue with ' + mediaType + ' media search URL: ' + str(e))

        # Return search URL
        return searchURL

    # RSS Feed Header Display
    def rssFeedHeaderDisplay(self, mediaType, dictHeaderRow):
        # Try to execute the command(s)
        try:
            # Loop through dictionary values to create header row
            for keyOne, valueOne in dictHeaderRow.items():
                # Set variables from dictionary
                textVal = dictHeaderRow[keyOne]['text']
                reliefVal = dictHeaderRow[keyOne]['relief']
                widthVal = dictHeaderRow[keyOne]['width']
                fontVal = dictHeaderRow[keyOne]['font']
                fontWeightVal = dictHeaderRow[keyOne]['fontWeight']
                bgVal = dictHeaderRow[keyOne]['bg']
                fgVal = dictHeaderRow[keyOne]['fg']
                rowVal = dictHeaderRow[keyOne]['row']
                columnVal = dictHeaderRow[keyOne]['col']

                # Set header row label
                tkinter.Label(text=textVal, relief=reliefVal, width=widthVal, font=(fontVal, fontWeightVal), bg=bgVal, fg=fgVal).grid(row=rowVal,column=columnVal)
        except Exception as e:
            # Log string
            self._setLogger('Issue displaying ' + mediaType + ' header(s): ' + str(e))

    # Database Content Display
    def databaseContentDisplay(self, mediaType, databaseName, tableName, databaseResponse, dictHeaderRow):
        # Initialize variables
        posVal = 1

        ## Initialize media array
        #mediaEntries = []

        # Try to execute the command(s)
        try:
            # Set variables from dictionary
            reliefTitleVal = dictHeaderRow[0]['relief']
            reliefPublishedVal = dictHeaderRow[1]['relief']
            widthZeroVal = dictHeaderRow[0]['width']
            widthOneVal = dictHeaderRow[1]['width']
            widthTwoVal = dictHeaderRow[2]['width']
            widthThreeVal = dictHeaderRow[3]['width']
            widthFourVal = dictHeaderRow[4]['width']
            fontZeroVal = dictHeaderRow[0]['font']
            fontOneVal = dictHeaderRow[1]['font']
            fontTwoVal = dictHeaderRow[2]['font']
            fontThreeVal = dictHeaderRow[3]['font']
            fontFourVal = dictHeaderRow[4]['font']
            fontWeightZeroVal = dictHeaderRow[0]['fontWeight']
            fontWeightOneVal = dictHeaderRow[1]['fontWeight']
            fontWeightTwoVal = dictHeaderRow[2]['fontWeight']
            fontWeightThreeVal = dictHeaderRow[3]['fontWeight']
            fontWeightFourVal = dictHeaderRow[4]['fontWeight']
            bgZeroVal = dictHeaderRow[0]['bg']
            bgOneVal = dictHeaderRow[1]['bg']
            fgZeroVal = dictHeaderRow[0]['fg']
            fgOneVal = dictHeaderRow[1]['fg']
            columnZeroVal = dictHeaderRow[0]['col']
            columnOneVal = dictHeaderRow[1]['col']
            columnTwoVal = dictHeaderRow[2]['col']
            columnThreeVal = dictHeaderRow[3]['col']
            columnFourVal = dictHeaderRow[4]['col']
            
            # Loop through dictionary values to create header row
            for content in databaseResponse:
                # Set variables from dictionary
                textTitleVal = content[0]
                textTitleShortVal = content[1]
                textPublishedVal = content[2]

                # Set label to display the title
                tkinter.Label(text=textTitleVal, relief=reliefTitleVal, width=widthZeroVal, font=(fontZeroVal, fontWeightZeroVal), bg=bgZeroVal, fg=fgZeroVal).grid(row=posVal, column=columnZeroVal)
                tkinter.Label(text=textPublishedVal, relief=reliefPublishedVal, width=widthOneVal, font=(fontOneVal, fontWeightOneVal), bg=bgOneVal, fg=fgOneVal).grid(row=posVal, column=columnOneVal)
                tkinter.Button(text='View', width=widthTwoVal, font=(fontTwoVal, fontWeightTwoVal), command=lambda row=posVal: self._viewMediaRecord(mediaType, databaseResponse, row, columnTwoVal)).grid(row=posVal,column=columnTwoVal)
                tkinter.Button(text='Ignore', width=widthThreeVal, font=(fontThreeVal, fontWeightThreeVal), command=lambda row=posVal: self._mediaIgnoreUpdate(mediaType, databaseName, tableName, databaseResponse, row, columnTwoVal)).grid(row=posVal,column=columnThreeVal)
                tkinter.Button(text='Delete', width=widthFourVal, font=(fontFourVal, fontWeightFourVal), command=lambda row=posVal: self._mediaDeleteUpdate(mediaType, databaseName, tableName, databaseResponse, row, columnTwoVal)).grid(row=posVal,column=columnFourVal)

                # Increment position
                posVal = posVal + 1
        except Exception as e:
            # Log string
            self._setLogger('Issue displaying database ' + mediaType + ' content: ' + str(e))

    # RSS Feed Content Display
    def rssFeedContentDisplay(self, mediaType, rssFeedResponse, dictHeaderRow):
        # Initialize variables
        posVal = 1

        # Initialize media array
        mediaEntries = []

        # Try to execute the command(s)
        try:
            # Set variables from dictionary
            reliefTitleVal = dictHeaderRow[0]['relief']
            reliefPublishedVal = dictHeaderRow[1]['relief']
            widthZeroVal = dictHeaderRow[0]['width']
            widthOneVal = dictHeaderRow[1]['width']
            widthTwoVal = dictHeaderRow[2]['width']
            widthThreeVal = dictHeaderRow[3]['width']
            widthFourVal = dictHeaderRow[4]['width']
            fontZeroVal = dictHeaderRow[0]['font']
            fontOneVal = dictHeaderRow[1]['font']
            fontTwoVal = dictHeaderRow[2]['font']
            fontThreeVal = dictHeaderRow[3]['font']
            fontFourVal = dictHeaderRow[4]['font']
            fontWeightZeroVal = dictHeaderRow[0]['fontWeight']
            fontWeightOneVal = dictHeaderRow[1]['fontWeight']
            fontWeightTwoVal = dictHeaderRow[2]['fontWeight']
            fontWeightThreeVal = dictHeaderRow[3]['fontWeight']
            fontWeightFourVal = dictHeaderRow[4]['fontWeight']
            bgZeroVal = dictHeaderRow[0]['bg']
            bgOneVal = dictHeaderRow[1]['bg']
            fgZeroVal = dictHeaderRow[0]['fg']
            fgOneVal = dictHeaderRow[1]['fg']
            columnZeroVal = dictHeaderRow[0]['col']
            columnOneVal = dictHeaderRow[1]['col']
            columnTwoVal = dictHeaderRow[2]['col']
            columnThreeVal = dictHeaderRow[3]['col']
            columnFourVal = dictHeaderRow[4]['col']

            # Loop through dictionary values to create header row
            for content in rssFeedResponse.entries:
                # Set variables from dictionary
                textTitleVal = content['title']
                textPublishedVal = content['published']

                # Append title to movie list
                mediaEntries.append(textTitleVal)

                # Set label to display the title
                tkinter.Label(text=textTitleVal, relief=reliefTitleVal, width=widthZeroVal, font=(fontZeroVal, fontWeightZeroVal), bg=bgZeroVal, fg=fgZeroVal).grid(row=posVal, column=columnZeroVal)
                tkinter.Label(text=textPublishedVal, relief=reliefPublishedVal, width=widthOneVal, font=(fontOneVal, fontWeightOneVal), bg=bgOneVal, fg=fgOneVal).grid(row=posVal, column=columnOneVal)
                tkinter.Button(text='View', width=widthTwoVal, font=(fontTwoVal, fontWeightTwoVal), command=lambda row=posVal: self._viewMedia(mediaType, mediaEntries, row, columnTwoVal)).grid(row=posVal,column=columnTwoVal)
                tkinter.Button(text='Ignore', width=widthThreeVal, font=(fontThreeVal, fontWeightThreeVal), command=lambda row=posVal: self._ignoreMedia(mediaType, mediaEntries, row, columnThreeVal)).grid(row=posVal,column=columnThreeVal)
                tkinter.Button(text='Delete', width=widthFourVal, font=(fontFourVal, fontWeightFourVal), command=lambda row=posVal: self._deleteMedia(mediaType, mediaEntries, row, columnFourVal)).grid(row=posVal,column=columnFourVal)

                # Increment position
                posVal = posVal + 1
        except Exception as e:
            # Log string
            self._setLogger('Issue displaying ' + mediaType + ' content: ' + str(e))

    # View media action
    def _viewMedia(self, mediaType, mediaEntries, row, column):
        # Try to execute the command(s)
        try:
            # Intialize variable
            hrefURL = ''

            # Set pseudo variable
            pseudoURL = self._mediaSearchURL(mediaType, 'pseudo') + mediaEntries[row - 1]

            # Open search url
            webbrowser.open(pseudoURL)

            ## Requests html
            #responseHTML = requests.get(pseudoURL)

            ## Create object of beautiful soup
            #beautifulsoup = bs4.BeautifulSoup(responseHTML, 'html.parser')

            ## Find tag title with string
            #urlTitle = beautiful.find(title=mediaEntries[row])

            ## Check if name title is None
            #if urlTitle != None:
            #    # Set genuine url
            #    genuineURL = self._mediaSearchURL(mediaType, 'genuine') + urlTitle.get('href')[1:]

            #    # Open search url
            #    webbrowser.open(genuineURL)
            #else:
            #    print('There was an issue retrieving genuine href')
        except Exception as e:
            # Log string
            self._setLogger('Issue opening ' + mediaType + ' link: ' + str(e))

    # Ignore media action
    def _ignoreMedia(self, mediaType, mediaEntries, row, column):
        # Set variable
        mediaAction = 'Ignore'

        # Set list
        mediaEntryFixed = []

        # Try to execute the command(s)
        try:
            # Create to file
            self._createMediaFile(mediaType, mediaAction)

            # Store value from list
            mediaEntryFixed = self._splitMediaEntries(mediaType, mediaEntries[row - 1])

            # Read from file
            mediaObject = self._readFromMediaFile(mediaType, mediaAction)

            # Check if string does not exist in list
            if mediaEntryFixed[0] not in mediaObject:
                # Append to file
                self._appendToMediaFile(mediaType, mediaAction, mediaEntryFixed[0])
        except Exception as e:
            # Log string
            self._setLogger('Issue ignoring ' + mediaType + ' entry: ' + str(e))

    # Delete media action
    def _deleteMedia(self, mediaType, mediaEntries, row, column):
        # Set variable
        mediaAction = 'Delete'

        # Try to execute the command(s)
        try:
            # Create to file
            self._createMediaFile(mediaType, mediaAction)

            # Read from file
            mediaObject = self._readFromMediaFile(mediaType, mediaAction)

            # Check if string does not exist in list
            if mediaEntries[row] not in mediaObject:
                # Append to file
                self._appendToMediaFile(mediaType, mediaAction, mediaEntries[row - 1])
        except Exception as e:
            # Log string
            self._setLogger('Issue deleting ' + mediaType + ' entry: ' + str(e))

    # Create to media file
    def _createMediaFile(self, mediaType, mediaAction):
        # Try to execute the command(s)
        try:
            # Create object of rss feed parser rarbg config
            rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set variables based on type
            rfrbgconfig._setFilenameVars(mediaType, mediaAction)

            # Get dictionary of values
            dictMediaType = rfrbgconfig._getFilenameVars()

            # Set path
            pathDirectory = dictMediaType['pathParent'] + dictMediaType['pathLevelOne'] + dictMediaType['pathLevelTwo']

            # Set variable
            pathResourceFolder = pathlib.Path(pathDirectory)

            if not pathResourceFolder.exists():
                # Recursively creates the directory and does not raise an exception if the directory already exist
                # Parent can be skipped as an argument if not needed or want to create parent directory
                pathlib.Path(pathResourceFolder).mkdir(parents=True, exist_ok=True)

            # Set file name
            filename = pathDirectory + dictMediaType['filenameMedia']

            # Set variable
            mediaFilename = pathlib.Path(filename)

            # Check if file does not exists or if file is not a file
            if not mediaFilename.exists() or not mediaFilename.is_file():
                # Open file for reading and writing which will empty file or create if not exist
                fhMedia = open(filename, 'w+')

                # Close file
                fhMedia.close()
        except Exception as e:
            # Log string
            self._setLogger('Issue writing to ' + mediaType + ' file: ' + str(e))

    # Read from media file
    def _readFromMediaFile(self, mediaType, mediaAction):
        # Initialize obj
        mediaObj = []

        # Try to execute the command(s)
        try:
            # Create object of rss feed parser rarbg config
            rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set variables based on type
            rfrbgconfig._setFilenameVars(mediaType, mediaAction)

            # Get dictionary of values
            dictMediaType = rfrbgconfig._getFilenameVars()

            # Set path
            pathDirectory = dictMediaType['pathParent'] + dictMediaType['pathLevelOne'] + dictMediaType['pathLevelTwo']

            # Set variable
            pathResourceFolder = pathlib.Path(pathDirectory)

            if not pathResourceFolder.exists():
                # Recursively creates the directory and does not raise an exception if the directory already exist
                # Parent can be skipped as an argument if not needed or want to create parent directory
                pathlib.Path(pathResourceFolder).mkdir(parents=True, exist_ok=True)

            # Set file name
            filename = pathDirectory + dictMediaType['filenameMedia']

            # Set variable
            mediaFilename = pathlib.Path(filename)

            # Check if file exists and if file is a file
            if mediaFilename.exists() and mediaFilename.is_file():
                # Open file file to read
                with open(filename, 'r') as meidaEntryRead:
                    # Loop through key, value in enumerate(meidaEntryRead)
                    # strip applied to remove end of line characters
                    mediaObj = [line.strip() for line in meidaEntryRead]

                # Close file
                meidaEntryRead.close()
        except Exception as e:
            # Log string
            self._setLogger('Issue reading from ' + mediaType + ' file: ' + str(e))

        # Return media object
        return mediaObj

    # Append to media file
    def _appendToMediaFile(self, mediaType, mediaAction, mediaEntryFixed):
        # Try to execute the command(s)
        try:
            # Create object of rss feed parser rarbg config
            rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set variables based on type
            rfrbgconfig._setFilenameVars(mediaType, mediaAction)

            # Get dictionary of values
            dictMediaType = rfrbgconfig._getFilenameVars()

            # Set path
            pathDirectory = dictMediaType['pathParent'] + dictMediaType['pathLevelOne'] + dictMediaType['pathLevelTwo']

            # Set variable
            pathResourceFolder = pathlib.Path(pathDirectory)

            if not pathResourceFolder.exists():
                # Recursively creates the directory and does not raise an exception if the directory already exist
                # Parent can be skipped as an argument if not needed or want to create parent directory
                pathlib.Path(pathResourceFolder).mkdir(parents=True, exist_ok=True)

            # Set file name
            filename = pathDirectory + dictMediaType['filenameMedia']

            # Set variable
            mediaFilename = pathlib.Path(filename)

            # Check if file exists and if file is a file
            if mediaFilename.exists() and mediaFilename.is_file():
                # Open file for read and write and to append to end of the file
                with open(filename, 'a+') as mediaEntryAppend:
                    # Append media entry into file with proper format
                    mediaEntryAppend.write(mediaEntryFixed + '\n')

                # Close file
                mediaEntryAppend.close()
        except Exception as e:
            # Log string
            self._setLogger('Issue appending to ' + mediaType + ' file: ' + str(e))

    # Split media entries
    def _splitMediaEntries(self, mediaType, mediaEntry):
        # Initialize variable
        mediaEntryFixed = ''

        # Try to execute the command(s)
        try:
            # Check media for movie
            if mediaType == 'Movie':
                # Split movie string to retrieve the proper title
                mediaEntryFixed = regEx.split(r'.[0-9]{4}.', mediaEntry)
            elif mediaType == 'Television':
                # Split television string to retrieve the proper title
                mediaEntryFixed = regEx.split(r'.s[0-9]{2,3}.|.[0-9]{4}.[0-9]{2}.[0-9]{2}.|.[0-9]{4}.', mediaEntry)
        except Exception as e:
            # Log string
            self._setLogger('Issue spliting ' + mediaType + ' entries: ' + str(e))

        # Return string
        return mediaEntryFixed

    # Set Logger
    def _setLogger(self, logString):
        # Initialize dictionary
        config_dict = {}

        # Create object of rss feed parser rarbg config
        rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

        # Set variables based on type
        rfrbgconfig._setFilenameVars('None', 'Log')

        # Get dictionary of values
        dictMediaType = rfrbgconfig._getFilenameVars()

        # Set path
        pathDirectory = dictMediaType['pathParent'] + dictMediaType['pathLevelOne'] + dictMediaType['pathLevelTwo']

        # Set variable
        pathResourceFolder = pathlib.Path(pathDirectory)

        if not pathResourceFolder.exists():
            # Recursively creates the directory and does not raise an exception if the directory already exist
            # Parent can be skipped as an argument if not needed or want to create parent directory
            pathlib.Path(pathResourceFolder).mkdir(parents=True, exist_ok=True)

        # Set file name
        logFilename = pathDirectory + dictMediaType['filenameMedia']

        # Set variable for JSON configuration
        logConfigFilename = pathlib.Path('./logging_dictConfig.json')

        # Check if file exists and if file is a file
        if logConfigFilename.exists() and logConfigFilename.is_file():
            # Open the file as read
            with open('./logging_dictConfig.json', 'r') as jsonConfigRead:
                # Read and set configuration
                config_dict = json.load(jsonConfigRead)

            # Close file
            jsonConfigRead.close()

            ## Set configuration based on JSON schema
            logging.config.dictConfig(config_dict)
        else:
            # Configure basic logging
            #logging.basicConfig(filename=logFilename,level=logging.INFO, format='{"": %(asctime)s, "": %(levelname)s, "": %(levelno)s, "": %(module)s, "": %(pathname)s, "": %(filename)s, "": %(lineno)d, "": %(funcName)s, "": %(message)s}')
            logging.basicConfig(filename=logFilename,level=logging.DEBUG, format='%(asctime)s - %(levelname)s:%(levelno)s [%(module)s] [%(pathname)s:%(filename)s:%(lineno)d:%(funcName)s] %(message)s')

        # Set root logger
        #logger = logging.getLogger('rssfeedrarbginfo')
        logger = logging.getLogger(__name__)

        # Log string for debugging and provide traceback with exc_info=true
        logger.debug(logString, exc_info=True)

    # Decorator style event listens for any connection
    # Need the at symbol in front of the event parameter as this is the only way it will work for listens_for function
    @event.listens_for(sqlalchemy.engine.Engine, 'connect')

    # Set a protect function to handle the connection with two parameters
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        # Check if the connection is a sqlite connection instance
        if isinstance(dbapi_connection, sqlite3.Connection):
            # Set the cursor to the connection
            cursor = dbapi_connection.cursor()

            # Set foreign key to on
            cursor.execute("PRAGMA foreign_keys=ON;")

            # Close the connection
            cursor.close()

    # Open connection based on type
    def __dbOpenConnection(self, type = 'notype'):
        # Create empty dictionary
        returnDict = {}

        # Try to execute the command(s)
        try:
            # Create object of configuration script
            hrfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set variables based on type
            hrfrbgconfig._setDatabaseVars(type)

            # Create empty dictionary
            conVars = {}

            # Get dictionary of values
            conVars = hrfrbgconfig._getDatabaseVars()

            # Set credentials from dictionary
            self.Driver = conVars['Driver']
            self.Server = conVars['Servername']
            self.Port = conVars['Port']
            self.PathParent = conVars['PathParent']
            self.PathLevelOne = conVars['PathLevelOne']
            self.PathLevelTwo = conVars['PathLevelTwo']
            self.PathDB = conVars['PathDB']
            self.Database = conVars['Database']
            self.User = conVars['Username']
            self.Pass = conVars['Password']

            # Check if string is MS SQL
            if regEx.match(r'SQLite[a-zA-Z]{1,}', type, flags=regEx.IGNORECASE):
                # Set engine
                self.engine = sqlalchemy.create_engine(self.Database)
                #self.engine = sqlalchemy.create_engine(self.Database, echo=True) # for debugging purposes only

                # Connect to engine
                self.connection = self.engine.connect()
            else:
                # Set server error
                returnDict['SError'] = 'Cannot connect to the database'

        # Set error message
        except Exception as e:
            # Set execption error
            returnDict['SError'] = 'Caught - cannot connect to the database - ' + str(e)

            # Log string
            self._setLogger('SError~Caught - cannot connect to the database - ' + str(e))

        return returnDict

    # Create database tables
    def _create_db_tables(self):
        try:
            # Create object of rss feed parser rarbg config
            rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set database variables based on type
            rfrbgconfig._setDatabaseVars('SQLiteRarBG')

            # Get dictionary of values
            dictMediaType = rfrbgconfig._getDatabaseVars()

            # Set path
            pathDirectory = dictMediaType['PathParent'] + dictMediaType['PathLevelOne'] + dictMediaType['PathLevelTwo']
            
            # Set variable
            pathResourceFolder = pathlib.Path(pathDirectory)

            if not pathResourceFolder.exists():
                # Recursively creates the directory and does not raise an exception if the directory already exist
                # Parent can be skipped as an argument if not needed or want to create parent directory
                pathlib.Path(pathResourceFolder).mkdir(parents=True, exist_ok=True)

            # Open database connection
            self.__dbOpenConnection('SQLiteRarBG')

            # Set meta data based on engine
            metadata = sqlalchemy.MetaData(self.engine)

            # Establish table schema
            actionstatustable = sqlalchemy.Table(
                'actionstatus', metadata,
                sqlalchemy.Column('asid', sqlalchemy.Integer, nullable = False, primary_key = True, autoincrement = True, unique = True),
                sqlalchemy.Column('actionnumber', sqlalchemy.Integer, nullable = False, unique = True),
                sqlalchemy.Column('actiondescription', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('createddate', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('modifieddate', sqlalchemy.Text, nullable = False)
            )

            # Establish table schema
            rarbgmoviefeedtable = sqlalchemy.Table(
                'rarbgmoviefeed', metadata,
                sqlalchemy.Column('rbmfid', sqlalchemy.Integer, nullable = False, primary_key = True, autoincrement = True, unique = True),
                sqlalchemy.Column('titlelong', sqlalchemy.Text, nullable = False, unique = True),
                sqlalchemy.Column('titleshort', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('publishdate', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('actionstatus', sqlalchemy.Integer, sqlalchemy.ForeignKey('actionstatus.actionnumber'), nullable = False, default = 0, server_default = '0'),
                sqlalchemy.Column('createddate', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('modifieddate', sqlalchemy.Text, nullable = False)
            )

            # Establish table schema
            rarbgtvfeedtable = sqlalchemy.Table(
                'rarbgtvfeed', metadata,
                sqlalchemy.Column('rbtvfid', sqlalchemy.Integer, nullable = False, primary_key = True, autoincrement = True, unique = True),
                sqlalchemy.Column('titlelong', sqlalchemy.Text, nullable = False, unique = True),
                sqlalchemy.Column('titleshort', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('publishdate', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('actionstatus', sqlalchemy.Integer, sqlalchemy.ForeignKey('actionstatus.actionnumber'), nullable = False, default = 0, server_default = '0'),
                sqlalchemy.Column('createddate', sqlalchemy.Text, nullable = False),
                sqlalchemy.Column('modifieddate', sqlalchemy.Text, nullable = False)
            )

            # Create all tables
            metadata.create_all()
        except Exception as e:
            # Log string
            self._setLogger('Issue creating database: ' + str(e))

    # Initialize action status
    def _actionStatusReg(self, databaseName, tableName, actionNumberVal, actionDescriptionVal, createdDateVal, modifiedDateVal):
        try:
            # Open database connection
            self.__dbOpenConnection(databaseName)

            # Set meta data based on engine
            metadata = sqlalchemy.MetaData(self.engine)

            # Set variable with table schema
            actionStatusTable = sqlalchemy.Table(tableName, metadata, autoload = True, autoload_with = self.engine)

            # Set variable query
            query = sqlalchemy.select([actionStatusTable.c.actionnumber, actionStatusTable.c.actiondescription, actionStatusTable.c.createddate, actionStatusTable.c.modifieddate]).where(actionStatusTable.c.actionnumber == actionNumberVal).order_by(sqlalchemy.desc(actionStatusTable.c.actionnumber)).limit(1)

            ## Print query with values
            #print(query.compile(compile_kwargs={"literal_binds": True}))

            # Execute query
            result = self.connection.execute(query)

            # Fetch record
            fetchRecord = result.fetchone()

            # Check if record exist
            if fetchRecord is None:
                # Set query insert
                queryInsert = actionStatusTable.insert(None).values(actionnumber = actionNumberVal, actiondescription = actionDescriptionVal, createddate = createdDateVal, modifieddate = modifiedDateVal)

                ## Print query with values
                #print(queryInsert.compile(compile_kwargs={"literal_binds": True}))

                # Insert record
                self.connection.execute(queryInsert)

            # Close database connection
            self.connection.close()
        except Exception as e:
            # Log string
            self._setLogger('Issue inserting action status: ' + str(e))

    # Insert media
    def _mediaInsert(self, databaseName, tableName, titleLongVal, titleShortVal, publishDateVal, actionStatusVal, createdDateVal, modifiedDateVal):
        try:
            # Open database connection
            self.__dbOpenConnection(databaseName)

            # Set meta data based on engine
            metadata = sqlalchemy.MetaData(self.engine)

            # Set variable with table schema
            mediaTable = sqlalchemy.Table(tableName, metadata, autoload = True, autoload_with = self.engine)

            # Set variable query based on short name and action status
            querySNAS = sqlalchemy.select([mediaTable.c.titlelong, mediaTable.c.titleshort, mediaTable.c.publishdate, mediaTable.c.actionstatus]).where(sqlalchemy.and_(mediaTable.c.titleshort == titleShortVal, mediaTable.c.actionstatus == 1))

            ## Print query with values
            #print(querySNAS.compile(compile_kwargs={"literal_binds": True}))

            # Execute query
            resultSNAS = self.connection.execute(querySNAS)

            # Fetch record
            fetchRecordSNAS = resultSNAS.fetchone()

            # Check if record exist
            if fetchRecordSNAS is None:
                # Select based on long name
                queryLN = sqlalchemy.select([mediaTable.c.titlelong, mediaTable.c.titleshort, mediaTable.c.publishdate, mediaTable.c.actionstatus]).where(mediaTable.c.titlelong == titleLongVal)

                ## Print query with values
                #print(queryLN.compile(compile_kwargs={"literal_binds": True}))

                # Execute query
                resultLN = self.connection.execute(queryLN)

                # Fetch record
                fetchRecordLN = resultLN.fetchone()

                # Check if record exist
                if fetchRecordLN is None:
                    # Set query insert
                    queryInsert = mediaTable.insert(None).values(titlelong = titleLongVal, titleshort = titleShortVal, publishdate = publishDateVal, actionstatus = actionStatusVal, createddate = createdDateVal, modifieddate = modifiedDateVal)

                    ## Print query with values
                    #print(queryInsert.compile(compile_kwargs={"literal_binds": True}))

                    # Insert record
                    self.connection.execute(queryInsert)

            # Close database connection
            self.connection.close()
        except Exception as e:
            # Log string
            self._setLogger('Issue inserting media : ' + str(e))

    # View media action
    def _viewMediaRecord(self, mediaType, databaseResponse, row, column):
        # Try to execute the command(s)
        try:
            # Intialize variable
            hrefURL = ''

            # Set pseudo variable
            pseudoURL = self._mediaSearchURL(mediaType, 'pseudo') + databaseResponse[row - 1][0]

            # Open search url
            webbrowser.open(pseudoURL)

            ## Requests html
            #responseHTML = requests.get(pseudoURL)

            ## Create object of beautiful soup
            #beautifulsoup = bs4.BeautifulSoup(responseHTML, 'html.parser')

            ## Find tag title with string
            #urlTitle = beautiful.find(title=mediaEntries[row])

            ## Check if name title is None
            #if urlTitle != None:
            #    # Set genuine url
            #    genuineURL = self._mediaSearchURL(mediaType, 'genuine') + urlTitle.get('href')[1:]

            #    # Open search url
            #    webbrowser.open(genuineURL)
            #else:
            #    print('There was an issue retrieving genuine href')
        except Exception as e:
            # Log string
            self._setLogger('Issue opening ' + mediaType + ' link: ' + str(e))
            ## Set exception error
            #print('Issue opening ' + mediaType + ' link: ' + str(e))

    # Select records
    def _extractRecord(self, dbType, tableName):
        # Open database connection
        self.__dbOpenConnection(dbType)

        # Set meta data based on engine
        metadata = sqlalchemy.MetaData(self.engine)

        # Set variable with table schema
        mediaTable = sqlalchemy.Table(tableName, metadata, autoload = True, autoload_with = self.engine)

        # Set variable query based on short name and action status
        querySNAS = sqlalchemy.select([mediaTable.c.titlelong, mediaTable.c.titleshort, mediaTable.c.publishdate]).where(mediaTable.c.actionstatus == 0)

        ## Print query with values
        #print(querySNAS.compile(compile_kwargs={"literal_binds": True}))

        # Execute query
        resultSNAS = self.connection.execute(querySNAS)

        # Fetch record
        fetchRecordSNAS = resultSNAS.fetchall()

        # Return records
        return fetchRecordSNAS

    # Ignore Update media
    def _mediaIgnoreUpdate(self, mediaType, databaseName, tableName, databaseResponse, row, column):
        try:
            # Extract elements
            titleShortVal = databaseResponse[row - 1][1]

            # Open database connection
            self.__dbOpenConnection(databaseName)

            # Set meta data based on engine
            metadata = sqlalchemy.MetaData(self.engine)

            # Set variable with table schema
            mediaTable = sqlalchemy.Table(tableName, metadata, autoload = True, autoload_with = self.engine)

            # Set variable query based on short name
            querySN = sqlalchemy.select([mediaTable.c.titlelong, mediaTable.c.titleshort, mediaTable.c.actionstatus]).where(mediaTable.c.titleshort == titleShortVal).limit(1)

            ## Print query with values
            #print(querySN.compile(compile_kwargs={"literal_binds": True}))

            # Execute query
            resultSN = self.connection.execute(querySN)

            # Fetch record
            fetchRecordSN = resultSN.fetchone()

            # Check if record exist
            if fetchRecordSN is not None:
                # Set variable current date
                modifiedDateVal = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

                # Set query update
                queryUpdate = sqlalchemy.update(mediaTable).values(actionstatus = 1, modifieddate = modifiedDateVal).where(sqlalchemy.and_(mediaTable.c.titleshort == titleShortVal, mediaTable.c.actionstatus != 1))

                ## Print query with values
                #print(queryUpdate.compile(compile_kwargs={"literal_binds": True}))

                # Insert record
                self.connection.execute(queryUpdate)

            # Close database connection
            self.connection.close()

            # Check media type
            if mediaType == 'Movie':
                # Re execute media feed
                self._executeMovie()
            # Check media type
            elif mediaType == 'Television':
                # Re execute media feed
                self._executeTelevision()
        except Exception as e:
            # Log string
            self._setLogger('Issue ignore update media : ' + str(e))

    # Delete Update media
    def _mediaDeleteUpdate(self, mediaType, databaseName, tableName, databaseResponse, row, column):
        try:
            # Extract elements
            titleLongVal = databaseResponse[row - 1][0]

            # Open database connection
            self.__dbOpenConnection(databaseName)

            # Set meta data based on engine
            metadata = sqlalchemy.MetaData(self.engine)

            # Set variable with table schema
            mediaTable = sqlalchemy.Table(tableName, metadata, autoload = True, autoload_with = self.engine)

            # Set variable query based on short name
            querySN = sqlalchemy.select([mediaTable.c.titlelong, mediaTable.c.titleshort, mediaTable.c.actionstatus]).where(mediaTable.c.titlelong == titleLongVal).limit(1)

            ## Print query with values
            #print(querySN.compile(compile_kwargs={"literal_binds": True}))

            # Execute query
            resultSN = self.connection.execute(querySN)

            # Fetch record
            fetchRecordSN = resultSN.fetchone()

            # Check if record exist
            if fetchRecordSN is not None:
                # Set variable current date
                modifiedDateVal = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

                # Set query update
                queryUpdate = sqlalchemy.update(mediaTable).values(actionstatus = 2, modifieddate = modifiedDateVal).where(mediaTable.c.titlelong == titleLongVal)

                ## Print query with values
                #print(queryUpdate.compile(compile_kwargs={"literal_binds": True}))

                # Insert record
                self.connection.execute(queryUpdate)

            # Close database connection
            self.connection.close()

            # Check media type
            if mediaType == 'Movie':
                # Re execute media feed
                self._executeMovie()
            # Check media type
            elif mediaType == 'Television':
                # Re execute media feed
                self._executeTelevision()
        except Exception as e:
            # Log string
            self._setLogger('Issue delete update media : ' + str(e))

    # Extract URL
    def extractRSSFeed(self, mediaType):
        # Initialize variable
        feedList = []

        # Try to execute the command(s)
        try:
            # Create object of rss feed parser rarbg config
            rfrbgconfig = rssfeedrarbgconfig.RssFeedRarBgConfig()

            # Set variables based on type
            rfrbgconfig._setConfigVars(mediaType)

            # Get dictionary of values
            dictMediaType = rfrbgconfig._getConfigVars()

            # Set file name
            urlString = dictMediaType['mainURL'] + dictMediaType['rssURL'] + dictMediaType['categoryURL']

            # Pull RSS feed from given URL
            feedList = feedparser.parse(urlString)
        except Exception as e:
            # Log string
            self._setLogger('Issue extract RSS feed ' + mediaType + ' ' + str(e))

        # Return built URL string
        return feedList

    # Execute main loop
    def initMainLoop(self):
        # Try to execute the command(s)
        try:
            self.window.mainloop()
        except Exception as e:
            # Log string
            self._setLogger('Issue executing tkinter main loop: ' + str(e))