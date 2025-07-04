import backend.src.utils.user_storage.day_plan as day_plan
import backend.src.utils.user_storage.month_plan as month_plan
import backend.src.utils.user_storage.week_plan as week_plan


class training:
    __slots__ = ("daily", "weekly", "monthly")

    def __init__(self, daily: day_plan, weekly: week_plan, monthly: month_plan):
        self.daily = daily
        self.weekly = weekly
        self.monthly = monthly
