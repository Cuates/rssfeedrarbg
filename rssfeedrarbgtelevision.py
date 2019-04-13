##
#        File: rssfeedrarbgtelevision.py
#     Created: 04/11/2019
#     Updated: 04/12/2019
#  Programmer: Guadalupe Ojeda
#  Updated By: Daniel Ojeda
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
        rssFeedResponse = rfrbclass.extractRSSFeed('Television')

        # Initialize variable
        dbType = 'SQLiteRarBG'
        tableName = 'rarbgtvfeed'

        # Process all feed information one at a time
        for feedInformation in rssFeedResponse.entries:
            rssfeedtitle = feedInformation.title
            titlearray = re.split(r'.s[0-9]{2,3}.', rssfeedtitle, flags=re.IGNORECASE)
            rssfeedtitleshort = titlearray[0]
            rssfeedpublish = feedInformation.published

            # Filter resolution
            resolution = "1080p|2160p"

            # Filter video encoding
            videoEncoding = "x264|x265|h264|h265"

            # Filter audio encoding
            audioEncoding = "dd5.1|ddp5.1|dts-hd.ma.5.1|dts-hd.ma.7.1|truehd.7.1.atmos"

            # Filter misc
            miscTag = "amzn|nf"

            # Filter only what is needed
            if ((re.search(resolution, rssfeedtitle, flags=re.IGNORECASE) and re.search(videoEncoding, rssfeedtitle, flags=re.IGNORECASE) and re.search(audioEncoding, rssfeedtitle, flags=re.IGNORECASE) and re.search(miscTag, rssfeedtitle, flags=re.IGNORECASE)) or (re.search(resolution, rssfeedtitle, flags=re.IGNORECASE) and re.search(videoEncoding, rssfeedtitle, flags=re.IGNORECASE) and re.search(audioEncoding, rssfeedtitle, flags=re.IGNORECASE))):
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