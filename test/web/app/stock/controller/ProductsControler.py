# from app.auth.middleware.SecuredSystemMiddleware import SecuredSystemMiddleware
from flask import request
from flask.json import jsonify
from flask_restful import Resource, abort
from app import app

from app.util.RequestExceptions import ValueRequiredException
from app.stock.service.ProductService import ProductService


class ProductsController(Resource):

    def __init__(self):
        self.productService = ProductService()

    def get(self):
        app.logger.info(f"ProductsController#get START - Request received - userAgent={request.user_agent.string}")

        products = self.productService.get_all()

        app.logger.info(f"ProductsController#get SUCCESS - Produucts retrieved - countProducts={len(products)}")

        return jsonify(data=products)

