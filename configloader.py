#!/usr/bin/python
# -*- coding: UTF-8 -*-
import importloader

g_config = None
m_config = None


def load_config():
    global g_config
    g_config = importloader.loads(['userapiconfig', 'apiconfig'])
    m_config = importloader.loads(['config',])


def get_config():
    return g_config

def get_mconfig():
    return m_config

load_config()
