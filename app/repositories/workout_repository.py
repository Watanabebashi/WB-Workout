from app.models.workout import Workout

class WorkoutRepository:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout: Workout):
        self.workouts.append(workout)

    def get_all_workouts(self):
        return self.workouts

    def get_workout_by_id(self, workout_id: int):
        for workout in self.workouts:
            if workout.id == workout_id:
                return workout
        return None

    def update_workout(self, workout_id: int, updated_workout: Workout):
        for i, workout in enumerate(self.workouts):
            if workout.id == workout_id:
                self.workouts[i] = updated_workout
                return True
        return False

    def delete_workout(self, workout_id: int):
        for i, workout in enumerate(self.workouts):
            if workout.id == workout_id:
                del self.workouts[i]
                return True
        return False