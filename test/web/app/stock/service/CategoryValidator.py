from unicodedata import category
from app.util.RequestExceptions import ValueRequiredException
from app.util.error_mesages import messages

from app.user.service.UserValidator import UserValidator
from app.stock.model.CategoryRepository import CategoryRepository
from app.stock.model.ProductRepository import ProductRepository


class CategoryValidator:

  def __init__(self) -> None:
    self.userValidator = UserValidator()
    self.categoryRepository = CategoryRepository()
    self.productRepository = ProductRepository()

  def validate_create_category(self, json_body):
    name = json_body.get('name', None)

    if not name:
      raise ValueRequiredException(messages['name_required'])

    category = self.categoryRepository.get_by_name(name)
    if category:
      raise AssertionError(messages['category_exist'])

  def validate_category_exist(self, json_body):
    category_id = json_body.get('category_id', None)

    if not category_id:
      raise ValueRequiredException(messages['category_id_required'])
    
    category = self.categoryRepository.get_by_id(category_id)
    if not category:
      raise AssertionError(messages['category_not_exist'])
  
    return category

  def validate_update_category(self, json_body):
    name = json_body.get('name', None)
    category = self.validate_category_exist(json_body)
    if not name:
      raise ValueRequiredException(messages['name_required'])

    if self.categoryRepository.get_by_name_and_diferent_id(name, category.id):
      raise AssertionError(messages['category_exist'])

    return category
