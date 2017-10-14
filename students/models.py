# -*- coding: utf-8 -*-

from openerp import models, fields, api

class students(models.Model):
    """
    This class will create an new table in DB with the same name of the object,
    but using '_' ==> the table name will be 'students_students'
    """
    def _set_is_active(self):
        # Write your own method
        return True

    _name = 'students.students'

    name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    gender = fields.Selection([('m', 'Male'), ('f', 'Female')], string='Gender', default='m')
    is_active = fields.Boolean(string='Active', default=_set_is_active)
    birth_date = fields.Date(string='Birth Date', default=fields.Date.today(), )
    room_id = fields.Many2one(comodel_name="study.room", string="Study Room", )

    _sql_constraints = [('unique_email', 'unique(email)', 'This email is used for another student!')]
