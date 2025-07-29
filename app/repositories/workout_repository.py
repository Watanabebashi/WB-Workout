from app.models import db
from app.models.workout import Workout
from typing import List

class WorkoutRepository:
    def add_workout(self, workout: Workout) -> Workout:
        db.session.add(workout)
        db.session.commit()
        return workout

    def get_all_workouts(self) -> List[Workout]:
        return Workout.query.all()

    def get_workout_by_id(self, workout_id: int) -> Workout | None:
        return Workout.query.get(workout_id)

    def update_workout(self, workout: Workout) -> Workout:
        db.session.commit()
        return workout

    def delete_workout(self, workout_id: int) -> bool:
        workout = self.get_by_id(workout_id)
        if workout:
            db.session.delete(workout)
            db.session.commit()
            return True
        return False
    
    # TODO:ジム入退時刻追加更新