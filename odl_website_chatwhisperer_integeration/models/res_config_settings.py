# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    
    chatbot_iframe = fields.Char(string="Enter ChatBot Iframe", config_parameter='odl_website_chatwhisperer_integeration.chatbot_iframe', 
                                 help="""Thanks for the install! Glad to have you in the Chat Whisperer community!
                                 You’re just a hop and a skip away from converting your site visitors into customers.
                                 To get Chat Whisperer Chat bot on your WordPress site, you’ll just do a quick and easy “copy and paste” to install the site snippet.
                                 Here’s how:
                                 1. Log in or sign up to www.chatwhisperer.ai
                                 2. Create your chatbot
                                 3. Copy the chat ID top right
                                 Now, your site snippet will be saved and ready to paste into WordPress directly, down below!""")
    
