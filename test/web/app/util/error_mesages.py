from email import message

messages = {
  # General errors
  'missing_json': 'Missing JSON request',
  'cradentials_not_exist': 'Credentials do not exits',
  'credentials_not_match': 'Credentials do not match',
  'password_required': 'Password required',
  'verify_email': 'Please verify your email',

  # Messagges to module user
  'email_required': 'Email required',
  'email_take': 'The email was taken',
  'name_required': 'Name required',
  'last_name_required': 'Last name required',
  'gender_required': 'Gender required',
  'gender_invalid': 'Invalid gender type',
  'profile_invalid': 'Invalid profile',
  'user_id_required': 'User id required',
  'user_not_exist': 'User does not exist',

  # Messagges to module stock
  'product_id_required': 'Product id required',
  'price_required': 'Price required',
  'quantity_required': 'Quantity required',
  'price_invalid': 'Invalid price',
  'quantity_invalid': 'Invalid quantity',
  'category_id_required': 'Category id required',
  'category_not_exist': 'Category does not exist',
  'category_exist': 'Category already exist',
  'product_exist': 'Product already exist',
  'product_not_exist': 'Product does not exist'
}