# -*- coding: utf-8 -*-

from openerp import models, fields, api

class students(models.Model):
    """
    This class will create an new table in DB with the same name of the object,
    but using '_' ==> the table name will be 'students_students'
    """
    _name = 'students.students'

    name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    gender = fields.Selection([('m', 'Male'), ('f', 'Female')], string='Gender')
    is_active = fields.Boolean(string='Active')
    birth_date = fields.Date(string='Birth Date')
