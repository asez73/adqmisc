# -*- coding: utf-8 -*-
import struct

class EFrameRSS:
    """File formatter for the binary RSS feed files used by the eframe."""
    
    def __init__(self):
	self.__feeds = ()

    def AddFeed(self, title, rss_url, original_url):
	self.__feeds += ((title, rss_url, original_url), )

    def Encode(self):
	raw = struct.pack('4sBB', "RSS ", 2, 0)

	for feed in self.__feeds:
	    raw += struct.pack('64s', feed[0][:64])
	    raw += struct.pack('256s', feed[1][:256])
	    raw += struct.pack('256s', feed[2][:256])

	return raw
