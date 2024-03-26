#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

__author__ = "federico"
__date__ = "$Feb 27, 2024 2:28:51 PM$"


class Transcoder(object):
    """Transcoder"""

    def __init__(self, trans_map_fn):
        """Init"""
        self.trans_map = None
        self.max_span_len = None
        self.populate_trans_map(trans_map_fn)

    def populate_trans_map(self, trans_file_name):
        """Populate the transcoding map"""
        self.max_span_len = 0
        self.trans_map = {}
        with open(trans_file_name, encoding='UTF-8') as trans_file:
            for line in trans_file:
                if line.startswith('//'): continue
                try:
                    chunk1, chunk2 = line.split('\t')
                    if len(chunk1) > self.max_span_len:
                        self.max_span_len = len(chunk1)
                    self.trans_map[chunk1] = chunk2[:-1]
                except:
                    pass

    def transcode(self, str):
        """Transcode a string"""
        in_str = [str[:]]
        out_str = []
        if in_str[0] == '':
            return out_str
        for i in range(0, self.max_span_len):
            in_str.append(' ')
        in_str = ''.join(in_str)
        in_str_len = len(in_str)
        i_left = 0
        i_right = self.max_span_len
        while i_right <= in_str_len:
            while i_right > i_left:
                try:
                    frag = in_str[i_left:i_right]
                    code = self.trans_map[frag]
                    code =re.sub(r'_',' ',code)
                    if code != '#*#':
                        out_str.append(code)
                    break
                except:
                    #pass
                    if i_right-i_left == 1:
                        out_str.append(frag)
                i_right -= 1
            if i_right == i_left:
                i_right += 1
            i_left = i_right
            i_right += self.max_span_len
        out_str = ''.join(out_str)
        return out_str


