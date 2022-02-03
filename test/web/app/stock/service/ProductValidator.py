from app.util.RequestExceptions import ValueRequiredException
from app.util.error_mesages import messages

from app.user.service.UserValidator import UserValidator
from app.stock.model.CategoryRepository import CategoryRepository
from app.stock.model.ProductRepository import ProductRepository


class ProductValidator:

  def __init__(self) -> None:
    self.userValidator = UserValidator()
    self.categoryRepository = CategoryRepository()
    self.productRepository = ProductRepository()

  def validate_create_product(self, json_body):
    name = json_body.get('name', None)

    self.validate_general_product(json_body)

    product = self.productRepository.get_by_name(name)
    if product:
      raise AssertionError(messages['product_exist'])

  def validate_general_product(self, json_body):
    name = json_body.get('name', None)
    quantity = json_body.get('quantity', None)
    price = json_body.get('price', None)
    category_id = json_body.get('category_id', None)

    if not name:
      raise ValueRequiredException(messages['name_required'])
    
    if not category_id:
      raise ValueRequiredException(messages['category_id_required'])

    category = self.categoryRepository.get_by_id(category_id)
    if not category:
      raise AssertionError(messages['category_not_exist'])

    if quantity and not int(quantity):
      raise AssertionError(messages['quantity_invalid'])
    
    if not price:
      raise ValueRequiredException(messages['price_required'])

    if not float(price):
      raise AssertionError(messages['price_invalid'])

  def validate_product_exist(self, product_id):
    if not product_id:
      raise ValueRequiredException(messages['product_id_required'])
    
    product = self.productRepository.get_by_id(product_id)
    if not product:
      raise AssertionError(messages['product_not_exist'])
  
    return product

  def validate_update_product(self, json_body):
    name = json_body.get('name', None)
    product_id = json_body.get('product_id', None)

    product = self.validate_product_exist(product_id)

    self.validate_general_product(json_body)

    if self.productRepository.get_by_name_and_diferent_id(name, product.id):
      raise AssertionError(messages['product_exist'])

    return product

