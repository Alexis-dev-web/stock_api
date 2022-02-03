from itertools import product
from app.stock.model.ProductRepository import Product, ProductRepository


class ProductService:

  def __init__(self) -> None:
    self.productRepository = ProductRepository()

  def create_product(self, json_body):
    product = Product()
    product.name = json_body.get('name')
    product.description = json_body.get('description')
    product.quantity = json_body.get('quantity')
    product.price = json_body.get('price')
    product.category_id = json_body.get('category_id')

    return self.productRepository.save(product)

  def delete_product(self, product):
    return self.productRepository.delete(product)

  def update(self, json_body, product):
    product.name = json_body.get('name')
    product.description = json_body.get('description')
    product.quantity = json_body.get('quantity')
    product.price = json_body.get('price')
    product.category_id = json_body.get('category_id')

    return self.productRepository.update(product)

  def get_all(self):
    products = self.productRepository.get_all()

    return [product.serialize() for product in products or []]
