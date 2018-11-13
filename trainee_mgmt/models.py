# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class Trainee(models.Model):
    _name = "hr.trainee"
    name = fields.Char(string='Name')
    trainer = fields.Many2one("hr.employee", string='Trainer')
    trainer_id = fields.Char()
    hrbp = fields.Char(string='HRBP')
    training_start_date = fields.Date(string='Training Start')
    training_end_date = fields.Date(string='Training End')
    position = fields.Char(string='Position')
    department_id = fields.Many2one("hr.dempartment", string='Dept')
    graduation_date = fields.Date(string='Graduation Date')
    idcard_type = fields.Selection(selection='_idcard_type_selection', string="IDCard Type")
    idcard_number = fields.Char(string='IDCard Number')
    education = fields.Selection(selection='_education_selection', string="Education")
    university = fields.Char(string='University')
    mobile_phone = fields.Char(string="Mobile Phone")
    bank_account_id = fields.Many2one("res.partner.bank", string='Bank Account')
    upload_file = fields.Binary(string="Upload File")
    file_name = fields.Char(string="File Name")
    country_id = fields.Many2one("res.country", string='Country')
    bankcard_img = fields.Binary("Image", attachment=True)
    # user_id = fields.Many2one('res.users', compute='_get_current_user')
    user_id = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user.id)
    state = fields.Selection([
        ('draft', "Draft"),
        ('confirmed', "Confirmed"),
        ('done', "Done"),
    ], default='draft')

    # @api.depends()
    # def _get_current_user(self):
    #     for rec in self:
    #         rec.user_id = self.env.user
    #     self.update({'user_id': self.env.user.id})

    @api.onchange('trainer')
    def onchange_trainer(self):
        _logger.info("-----------"+str(self.trainer.id))
        if self.trainer.id:
            self.trainer_id = self.trainer.user_id.id


    def _idcard_type_selection(self):
        return [(1, _('ID Card')), (2, _('Passport'))]


    def _education_selection(self):
        return [(1, _("bachelor's degree")), (2, _('college'))]

    @api.model
    def create(self, vals):
        _logger.info("-------workflow start--------")

        return super(Trainee, self).create(vals)

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'

    @api.multi
    def action_done(self):
        self.state = 'done'


    @api.model
    def hello(self):
        _logger.info("-------hello start--------")
        return "hello"


class UploadFile(models.Model):
    _name = "trainee_mgmt.uploadfile"

    name = fields.Char(string='文件名')