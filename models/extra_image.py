from odoo import models, fields, api
from random import randint


class ImageCategory(models.Model):
    _name = 'sale_burguer.image_category'

    def _get_default_color(self):
        return randint(1, 11)

    rand_color = fields.Integer(
        string='Color Index', default=_get_default_color)
    name = fields.Char(string='Name')

    # Exists the possibilty of create a custom widget than depends of this fields and show custom colors.
    # color = fields.Char(String="Color")


class ExtraImage(models.Model):
    ######################
    # Private Attributes #
    #######################
    _name = 'sale_burguer.extra_image'

    ###################
    # Default methods #
    ###################

    ######################
    # Fields declaration #
    ######################
    original_image = fields.Image(
        "Original Image", max_width=1920, max_height=1920, required=True)
    medium_image = fields.Image(
        "Medium Image", related="original_image", max_width=1024, max_height=1024, store=True)
    small_image = fields.Image(
        "Small Image", related="original_image", max_width=512, max_height=512, store=True)
    icon_image = fields.Image(
        "Image", related="original_image", max_width=52, max_height=52, store=True)
    category_ids = fields.Many2many(
        'sale_burguer.image_category',
        string='Categories',
    )
    title = fields.Char(string="Title", required=True)
    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    ####################º#####
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
