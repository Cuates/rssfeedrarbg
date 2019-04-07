##
#        File: rssfeedrarbg.py
#     Created: 03/16/2019
#     Updated: 04/07/2019
#  Programmer: Guadalupe Ojeda
#  Updated By: Daniel Ojeda
#     Purpose: Retrieve RSS feed from RarBg site
#     Version: 0.0.1 Python3
##

# Import modules
import rssfeedrarbgclass # rss feed rarbg class

# Set object
rfrbclass = rssfeedrarbgclass.RssFeedRarBgClass()

# Program entry point
def main():
    # Try to execute the command(s)
    try:
        # Check if modules are installed
        import tkinter, feedparser, webbrowser, pathlib, re, requests, bs4, logging, json, datetime, sqlite3, pytz, tzlocal, sqlalchemy, sys

        # Create tables
        rfrbclass._create_db_tables()

        # Set variable to local date time based on UTC current date time and format to date time for database storage
        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        # Insert action status record
        rfrbclass._actionStatusReg('SQLiteRarBG', 'actionstatus', 0, 'Register', currentDateTime, currentDateTime)

        # Set variable to local date time based on UTC current date time and format to date time for database storage
        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        # Insert action status record
        rfrbclass._actionStatusReg('SQLiteRarBG', 'actionstatus', 1, 'Ignore', currentDateTime, currentDateTime)

        # Set variable to local date time based on UTC current date time and format to date time for database storage
        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        # Insert action status record
        rfrbclass._actionStatusReg('SQLiteRarBG', 'actionstatus', 2, 'Delete', currentDateTime, currentDateTime)

        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        local_tz = tzlocal.get_localzone()

        rfrbclass._mediaInsert('SQLiteRarBG', 'rarbgmoviefeed', 'The.Shameless.2015.KOREAN.1080p.BluRay.H264.AAC-VXT', 'The.Shameless', str(datetime.datetime.strptime('Fri, 29 Mar 2019 03:08:15 +0100', '%a, %d %b %Y %H:%M:%S %z').astimezone(pytz.timezone(str(local_tz))).strftime('%Y-%m-%d %H:%M:%S')), 0, currentDateTime, currentDateTime)

        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        rfrbclass._mediaIgnoreUpdate('SQLiteRarBG', 'rarbgmoviefeed', 'The.Shameless.2015.KOREAN.1080p.BluRay.H264.AAC-VXT', 'The.Shameless', str(datetime.datetime.strptime('Fri, 29 Mar 2019 03:08:15 +0100', '%a, %d %b %Y %H:%M:%S %z').astimezone(pytz.timezone(str(local_tz))).strftime('%Y-%m-%d %H:%M:%S')), 1, currentDateTime, currentDateTime)

        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        rfrbclass._mediaDeleteUpdate('SQLiteRarBG', 'rarbgmoviefeed', 'The.Shameless.2015.KOREAN.1080p.BluRay.H264.AAC-VXT', 'The.Shameless', str(datetime.datetime.strptime('Fri, 29 Mar 2019 03:08:15 +0100', '%a, %d %b %Y %H:%M:%S %z').astimezone(pytz.timezone(str(local_tz))).strftime('%Y-%m-%d %H:%M:%S')), 2, currentDateTime, currentDateTime)

        # Call set tkinter
        rfrbclass._setTkinter('RarBg RSS Feed', '1450', '855', '#000000')
        #rfrbclass._setTkinter('RarBg RSS Feed', '1720x820', '#000000')

        # Set dictionary of column header values
        dictHeaderRow = {0: {'text': 'Movie', 'relief': 'ridge', 'width': '80', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '0'},
        1: {'text': 'Date', 'relief': 'ridge', 'width': '30', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '1'},
        2: {'text': 'View', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '2'},
        3: {'text': 'Ignore', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '3'},
        4: {'text': 'Delete', 'relief': 'ridge', 'width': '10', 'font': 'Arial Bold', 'fontWeight': '12', 'bg': '#000000', 'fg': '#FFFFFF', 'row': '0', 'col': '4'}}

        # Display header row(s)
        rfrbclass.rssFeedHeaderDisplay('Movie', dictHeaderRow)

        # Call set feed parser
        rssFeedResponse = rfrbclass._responseFeedParser('Movie')

        # Extract record(s) from database
    
        # Display content row(s)
        rssFeedResponse = rfrbclass.rssFeedContentDisplay('Movie', rssFeedResponse, dictHeaderRow)

        # Execute tkinter main loop
        rfrbclass.initMainLoop()
    except Exception as e:
        # Log string
        rfrbclass._setLogger('Issue executing main PY file ' + str(e))
        ## Set Exception error
        #print('Issue executing main PY file' + str(e))
    #except ImportError as e:
    #    # Log string
    #    rfrbclass._setLogger('Import Error ' + str(e))

# Run program
if __name__ == '__main__':
    main()