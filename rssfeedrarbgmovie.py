##
#        File: rssfeedrarbgmovie.py
#     Created: 04/11/2019
#     Updated: 04/20/2019
#  Programmer: Cuates
#  Updated By: Cuates
#     Purpose: Retrieve RSS feed from Rarbg site
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
        import tkinter, feedparser, webbrowser, pathlib, re, requests, bs4, logging, json, datetime, sqlite3, pytz, tzlocal, sqlalchemy, sys, pythonjsonlogger

        # Extract RSS feed response
        rssFeedResponse = rfrbclass.extractRSSFeed('Movie')

        # Initialize variable
        dbType = 'SQLiteRarBG'
        tableName = 'rarbgmoviefeed'

        # Process all feed information one at a time
        for feedInformation in rssFeedResponse.entries:
            # Store title
            rssfeedtitle = feedInformation.title

            # Split string based on regular expression
            # r is to escape any back slashes within the regular expression string
            titlearray = re.split(r'.[0-9]{4}.', rssfeedtitle, flags=re.IGNORECASE)

            # Store title extracted
            rssfeedtitleshort = titlearray[0]

            # Store published date
            rssfeedpublish = feedInformation.published

            # Filter year
            yearStringValue = ""

            # Filter resolution
            resolution = "1080p|2160p"

            # Filter video encoding
            videoEncoding = "x264|x265|h264|h265"

            # Filter audio encoding
            audioEncoding = "dd5.1|ddp5.1|dts-hd.ma.5.1|dts-hd.ma.7.1|truehd.7.1.atmos"

            # Store current year
            yearString = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y'))

            # Store current month
            currentMonth = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%m'))

            # Check if current month is less than or equal to 3
            if (int(currentMonth) <= 3):
                # Set year string variable with previous year and pipe
                yearStringValue = str(int(yearString) - 1) + "|"

            # Final year string
            yearStringValue = yearStringValue + yearString

            # Filter only what is needed
            if (re.search(yearStringValue, rssfeedtitle, flags=re.IGNORECASE) and re.search(resolution, rssfeedtitle, flags=re.IGNORECASE) and re.search(videoEncoding, rssfeedtitle, flags=re.IGNORECASE) and re.search(audioEncoding, rssfeedtitle, flags=re.IGNORECASE)):
                # Set variable to local date time based on UTC current date time and format to date time for database storage
                currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

                # Set local time zone
                local_tz = tzlocal.get_localzone()

                # Insert record
                rfrbclass._mediaInsert(dbType, tableName, rssfeedtitle, rssfeedtitleshort, str(datetime.datetime.strptime(rssfeedpublish, '%a, %d %b %Y %H:%M:%S %z').astimezone(pytz.timezone(str(local_tz))).strftime('%Y-%m-%d %H:%M:%S')), 0, currentDateTime, currentDateTime)
    except Exception as e:
        # Log string
        rfrbclass._setLogger('Issue executing main rss feed rar bg movie ' + str(e))

# Run program
if __name__ == '__main__':
    main()
