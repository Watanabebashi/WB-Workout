from app.repositories.workout_repository import WorkoutRepository
from app.models.workout import Workout

class WorkoutService:
    def __init__(self):
        self.workout_repository = WorkoutRepository()

    def get_all_workouts(self):
        return self.workout_repository.get_all_workouts()

    def get_workout_by_id(self, workout_id):
        workout = self.workout_repository.get_workout_by_id(workout_id)
        if not workout:
            return None
        return workout
    # TODO:Workout追加、更新、ジム入退時刻追加更新
