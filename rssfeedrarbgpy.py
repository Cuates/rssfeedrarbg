##
#        File: rssfeedrarbg.py
#     Created: 03/16/2019
#     Updated: 03/24/2019
#  Programmer: Guadalupe Ojeda
#  Updated By: Daniel Ojeda
#     Purpose: Retrieve RSS feed from RarBg site
#     Version: 0.0.1 Python3
##

# Try to execute the command(s)
try:
    # Import modules
    import rssfeedrarbgclass # rss feed rarbg class

    # Set object
    rfrbclass = rssfeedrarbgclass.RssFeedRarBgClass()

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
    
    # Display content row(s)
    rssFeedResponse = rfrbclass.rssFeedContentDisplay('Movie', rssFeedResponse, dictHeaderRow)

    # Execute tkinter main loop
    rfrbclass.initMainLoop()
except Exception as e:
    print('Issue executing main PY file' + str(e))