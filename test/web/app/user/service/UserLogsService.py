from app.user.model.LogsRepository import Logs, LogsRepository


class UserLogsService:

  def __init__(self) -> None:
    self.logsRepository = LogsRepository()

  def create_log(self, product_id):
    log = Logs()
    log.product_id = product_id

    return log
