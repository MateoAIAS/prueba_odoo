# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reservation(models.Model):
    _name = "reservas.reservation"

    name = fields.Char(string="Reservation Name", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner")
    user_id = fields.Many2one("res.users", string="Assigned to")
    room_id = fields.Many2one("reservas.reservation", string="Room")
    chair_amount = fields.Integer(string="Chair Amount")
    table_amount = fields.Integer(string="Table Amount")
    start_hour = fields.Float(string="Start Hours")
    end_hour = fields.Float(string="End Hours")
    have_catering = fields.Boolean(string="Catering service")
    states = fields.Selection([("draft", "Draft"), ("confirmed", "Confirmed")], string="State", default="draft")
    room_states = fields.Selection(
        [("reserved", "Reserved"), ("occupied", "Occupied"), ("enabled", "Enabled")],
        string="Room State",
        related="room_id.states",
        readonly=True,
    )
    room_name = fields.Char(string="Room Name", related="room_id.name", readonly=True)
