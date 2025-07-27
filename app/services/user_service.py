# ログイン処理書きかけ
from app.models.workout import User
from app.repositories.workout_repository import WorkoutRepository

class UserService:
    def __init__(self):
        # self.users = []
        self.workout_repository = WorkoutRepository()

    def login(self, username: str, password: str) -> User:
        # TODO:入力されたパスワードをハッシュ化して比較する処理を追加する
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None