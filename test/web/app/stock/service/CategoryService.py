from app.stock.model.CategoryRepository import Category, CategoryRepository
from app.stock.model.ProductRepository import ProductRepository


class CategoryService:
  
  def __init__(self) -> None:
    self.categoryRepository = CategoryRepository()
    self.productRepository = ProductRepository()
  
  def create_category(self, json_body):
    category = Category()
    category.name = json_body.get('name')
    category.description = json_body.get('description')

    return self.categoryRepository.save(category)

  def update_category(self, json_body, category):
    category.name = json_body.get('name')
    category.description = json_body.get('description')

    return self.categoryRepository.update(category)

  def get_all(self):
    categories = self.categoryRepository.get_all()

    return [category.serialize() for category in categories or []]

  def delete_category(self, category):
    success = False
    products = self.productRepository.get_active_by_category_id(category.id)

    if len(products) > 0:
      for product in products:
        product.active = False
        self.productRepository.update(product)
  
      category.active = False
      self.categoryRepository.update(category)

      success = True
    else:
      success = self.categoryRepository.delete(category)
    
    return success

  def activate_category(self, category, activate_products=False):
    category.active = True

    if activate_products:
      products = self.productRepository.get_by_category_id(category.id)
      
      for product in products:
        product.active = True
        self.productRepository.update(product)
    
    return self.categoryRepository.update(category)
