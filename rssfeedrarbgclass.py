##
#        File: rssfeedrarbgclass.py
#     Created: 03/17/2019
#     Updated: 03/27/2019
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
        except Exception as e:
            # Set exception error
            print('Issue setting tkinter window: ' + str(e))

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
            # Set exception error
            print('Issue with ' + mediaType + ' feed parser: ' + str(e))

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
            # Set exception error
            print('Issue with ' + mediaType + ' media search URL: ' + str(e))

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
            # Set exception error
            print('Issue displaying ' + mediaType + ' header(s): ' + str(e))

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
            # Set exception error
            print('Issue displaying ' + mediaType + ' content: ' + str(e))

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
            # Set exception error
            print('Issue opening ' + mediaType + ' link: ' + str(e))

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
            # Set exception error
            print('Issue ignoring ' + mediaType + ' entry: ' + str(e))

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
            # Set exception error
            print('Issue deleting ' + mediaType + ' entry: ' + str(e))

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
            filename = dictMediaType['pathParent'] + dictMediaType['pathLevelOne'] + dictMediaType['pathLevelTwo'] + dictMediaType['filenameMedia']

            # Set variable
            mediaFilename = pathlib.Path(filename)

            # Check if file does not exists or if file is not a file
            if not mediaFilename.exists() or not mediaFilename.is_file():
                # Open file in write mode
                fhMedia = open(filename, 'w+')

                # Close file
                fhMedia.close()
        except Exception as e:
            # Set exception error
            print('Issue writing to ' + mediaType + ' file: ' + str(e))

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

            # Set file name
            filename = dictMediaType['pathParent'] + dictMediaType['pathLevelOne'] + dictMediaType['pathLevelTwo'] + dictMediaType['filenameMedia']

            # Set variable
            mediaFilename = pathlib.Path(filename)

            # Check if file exists and if file is a file
            if mediaFilename.exists() and mediaFilename.is_file():
                # Open the file as read
                with open(filename, 'r') as meidaEntryRead:
                    # Loop through key, value in enumerate(meidaEntryRead)
                    mediaObj = [line.strip() for line in meidaEntryRead]
        except Exception as e:
            # Set exception error
            print('Issue reading from ' + mediaType + ' file: ' + str(e))

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

            # Set file name
            filename = dictMediaType['pathParent'] + dictMediaType['pathLevelOne'] + dictMediaType['pathLevelTwo'] + dictMediaType['filenameMedia']

            # Set variable
            mediaFilename = pathlib.Path(filename)

            # Check if file exists and if file is a file
            if mediaFilename.exists() and mediaFilename.is_file():
                # Open the file as write
                with open(filename, 'a+') as mediaEntryAppend:
                    # Append media entry into file with proper format
                    mediaEntryAppend.write(mediaEntryFixed + '\n')
        except Exception as e:
            # Set exception error
            print('Issue appending to ' + mediaType + ' file: ' + str(e))

    # Split media entries
    def _splitMediaEntries(self, mediaType, mediaEntry):
        # Initialize variable
        mediaEntryFixed = ''

        # Try to execute the command(s)
        try:
            # Check media for movie
            if mediaType == 'Movie':
                # Split movie string to retrieve the proper title
                mediaEntryFixed = regEx.split('.[0-9]{4}.', mediaEntry)
            elif mediaType == 'Television':
                # Split television string to retrieve the proper title
                mediaEntryFixed = regEx.split('.[0-9]{4}.', mediaEntry)
        except Exception as e:
            # Set exception error
            print('Issue spliting ' + mediaType + ' entries: ' + str(e))

        # Return string
        return mediaEntryFixed

    # Execute main loop
    def initMainLoop(self):
        # Try to execute the command(s)
        try:
            self.window.mainloop()
        except Exception as e:
            print('Issue executing tkinter main loop')