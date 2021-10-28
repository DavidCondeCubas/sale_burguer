from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import UserError, ValidationError


class ProductBurguer(models.Model):
    ######################
    # Private Attributes #
    #######################
    _inherit = 'product.template'

    ###################
    # Default methods #
    ###################

    ######################
    # Fields declaration #
    ######################
    is_a_burguer = fields.Boolean(string="Is a burguer?")
    size = fields.Selection(
        [("sm", "SM"), ("m", "M"), ("l", "L"), ("xl", "XL")], string='Size')
    meat = fields.Selection([("beef", "Beef"), ("pig", "Pig"), ("chicken",
                            "Chiken"), ("peas", "Peas"), ("soya", "Soya")], string='Meat', default="beef")
    limited_edition = fields.Boolean("Limited Edition")
    is_vegan = fields.Boolean("Is Vegan?")
    gluten_free = fields.Boolean("Gluten Free?")
    author = fields.Many2one(
        'res.partner',
        string='Author', domain="[('supplier_rank','=',1)]"
    )
    slogan = fields.Char(string="Slogan", translate=True)
    rating = fields.Integer(string="Rating")
    popularity = fields.Selection(
        selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], compute='_compute_popularity', store=True)

    extra_images_ids = fields.Many2many('sale_burguer.extra_image')
    ##############################
    # Compute and search methods #
    ##############################
    @api.depends('rating')
    def _compute_popularity(self):
        for product in self:
            product.popularity = 'low' if product.rating <= 4000 else 'high' if product.rating > 10000 else 'medium'

    ############################
    # Constrains and onchanges #
    ############################
    @api.onchange('rating')
    def _onchange_rating(self):
        if self.rating < 0:
            self.rating = 0
            return {'warning': {
                    'title': _("Check the rating."),
                    'message': 'The rating has to be upper than 0.'}}

    @api.onchange('is_vegan', 'meat')
    def _onchange_check_vegan(self):
        vegetarian_meat = ["peas", "soya"]
        if self.is_vegan and self.meat not in vegetarian_meat:
            self.meat = False
            return {'warning': {
                    'title': _("Type of Meat."),
                    'message':  _('You need select a vegetarian meat: %s' % ','.join(vegetarian_meat))
                    }}

    @api.constrains('rating')
    def _validate_rating(self):
        for record in self:
            if record.rating < 0:
                raise ValidationError(
                    _("The upper cant be negative!."))
    ####################º#####
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
