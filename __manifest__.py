# -*- coding: utf-8 -*-
{
    'name': 'ChatWhisperer Website Integeration',
    'version': '17.0.1.0',
    'summary': """ChatWhisperer Website Integeration
    Get your chatbot Iframe from https://bot.chatwhisperer.ai/dashboard/chatbot and add it in Chatbot settings for smooth chatbot integeration
    """,
    'author': 'sandbox',
    'website': 'sandbox.mu',
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
