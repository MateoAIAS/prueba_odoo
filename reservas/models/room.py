# -*- coding: utf-8 -*-
from odoo import models, fields, api

STATES = [
    ("reserved", "Reserved"),
    ("occupied", "Occupied"),
    ("enabled", "Enabled"),
]


class Room(models.Model):
    _name = "reservas.room"

    name = fields.Char(string="Room Name", required=True)
    states = fields.Selection(STATES, string="State", default="enabled", readonly=True)
    reservation_ids = fields.One2many("reservas.reservation", "room_id", string="Reservations")
