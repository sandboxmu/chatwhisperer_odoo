# -*- coding: utf-8 -*-
{
    'name': 'Chat Whisperer - Website Ai Chatbot',
    'version': '16.0.1.1',
    'summary': """ChatWhisperer Website Integeration
    Get your chatbot Iframe from https://bot.chatwhisperer.ai/dashboard/chatbot and add it in Chatbot settings for smooth chatbot integeration
    """,
    'author': 'sandbox',
    'website': 'https://chatwhisperer.ai/',
    'category': 'Technical',
    'depends': ['base', 'website'],
    "data": [
        "views/res_config_settings_views.xml",
        "views/web_layout_views.xml"
    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}