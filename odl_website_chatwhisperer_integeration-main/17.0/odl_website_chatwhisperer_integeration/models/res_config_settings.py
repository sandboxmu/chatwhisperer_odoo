# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    
    chatbot_iframe = fields.Char(string="Enter ChatBot Iframe", config_parameter='odl_website_chatwhisperer_integeration.chatbot_iframe', help="Add your Chatbot Iframe Or get one from https://bot.chatwhisperer.ai/dashboard/chatbot")
    
