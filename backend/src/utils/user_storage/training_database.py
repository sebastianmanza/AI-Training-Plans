import backend.src.utils.user_storage.day_plan as day_plan
import backend.src.utils.user_storage.month_plan as month_plan
import backend.src.utils.user_storage.week_plan as week_plan
from backend.src.utils.user_storage.storage_stacks_and_queues import storage_stacks_and_queues


class training_database:
    _instance_ = None

    def __new__(cls):
        """Create or return the singleton instance.

        Returns:
            training_database: The shared training database instance.
        """
        if cls._instance_ is None:
            cls._instance_ = super(training_database, cls).__new__(cls)
            # Initialize the instance
            cls._instance_._initialize()
        return cls._instance_

    def _initialize(self):
        """Initialize the training database with default values."""

        # create static instance
        self.storage = storage_stacks_and_queues()

        self.day = self.storage.day_future
        self.week = self.storage.week_future
        self.month = self.storage.month_future

    @classmethod
    def get_instance(cls):
        """Access the singleton instance."""
        if cls._instance_ is None:
            cls._instance_ = cls()
        return cls._instance_
