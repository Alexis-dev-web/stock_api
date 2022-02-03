from app.stock.controller.AdminCategoriesController import AdminCategoriesController
from app.stock.controller.AdminCategoryController import AdminCategoryController
from app.stock.controller.AdminProductController import AdminProductController
from app.stock.controller.AdminProductsController import AdminProductsController
from app.stock.controller.ProductController import ProductController
from app.stock.controller.ProductsControler import ProductsController
from app.user.controller.AdminUserController import AdminUserController
from app.auth.controller.AuthController import AuthController


def create_routes(api):
  """
      Admin routes
  """
  api.add_resource(AdminProductsController, '/admin/products')
  api.add_resource(AdminProductController, '/admin/product')
  api.add_resource(AdminCategoriesController, '/admin/categories')
  api.add_resource(AdminCategoryController, '/admin/category')
  api.add_resource(AdminUserController, '/admin/user')
  api.add_resource(AuthController, '/admin/auth')

  """
      Public routes
  """
  api.add_resource(ProductsController, '/apiv1/products')
  api.add_resource(ProductController, '/apiv1/product')