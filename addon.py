import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import urllib2
import socket
import xbmcaddon
import datetime
import re
import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])


line1 = ''
line2 = "We can write anything we want here"
line3 = "Using Python"

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'folder', 'foldername': '1'})
    li = xbmcgui.ListItem('Category 1', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder', 'foldername': '2'})
    li = xbmcgui.ListItem('Category 2', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder', 'foldername': '3'})
    li = xbmcgui.ListItem('Category 3', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder', 'foldername': '4'})
    li = xbmcgui.ListItem('Category 4', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = "plugin://plugin.video.genesis"
    li = xbmcgui.ListItem('Genesis', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = "plugin://plugin.video.mediacorp"
    li = xbmcgui.ListItem('MediaCorp', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    url = "plugin://plugin.video.1channel"
    li = xbmcgui.ListItem('1Channel', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)


elif mode[0] == 'folder':
    foldername = args['foldername'][0]
    if foldername == '1':
    	url = "plugin://plugin.video.genesis"
        li = xbmcgui.ListItem('Genesis', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)    	
    	
    	url = "plugin://plugin.video.1channel"
        li = xbmcgui.ListItem('1Channel', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    #xbmcgui.Dialog().ok(addonname, line1, line2, line3)
    	xbmcplugin.endOfDirectory(addon_handle) 
    elif foldername == '2':
    	url = 'http://localhost/some_video.mkv'
    	li = xbmcgui.ListItem("item 2.1", iconImage='DefaultVideo.png')
    	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    	li = xbmcgui.ListItem("item 2.2", iconImage='DefaultVideo.png')
    	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    	xbmcplugin.endOfDirectory(addon_handle) 
    elif foldername == '3':
    	url = 'http://localhost/some_video.mkv'
    	li = xbmcgui.ListItem("item 3.1", iconImage='DefaultVideo.png')
    	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    	li = xbmcgui.ListItem("item 3.2", iconImage='DefaultVideo.png')
    	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    	xbmcplugin.endOfDirectory(addon_handle) 
    elif foldername == '4':
    	url = 'http://localhost/some_video.mkv'
    	li = xbmcgui.ListItem("item 4.1", iconImage='DefaultVideo.png')
    	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    	li = xbmcgui.ListItem("item 4.2", iconImage='DefaultVideo.png')
    	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    	xbmcplugin.endOfDirectory(addon_handle)
else:
	

	xbmcgui.Dialog().ok(addonname, line1, line2, line3)
	#xbmcgui.ControlButton(350, 500, 80, 30, "HELLO")
	#xbmcgui.ControlLabel(100, 120, 200, 200, '', 'font13', '0xFFFF00FF')

	#url = "plugin://plugin.video.1channel"
    #li = xbmcgui.ListItem('1Channel', iconImage='DefaultFolder.png')
    #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
    #                            listitem=li, isFolder=True)

    #xbmcplugin.endOfDirectory(addon_handle)


