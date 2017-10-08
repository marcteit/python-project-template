class sample_business_logic:
    def __init__(self, sample_data_access):
        self._sample_data_access = sample_data_access

    def execute(self):
        return [self._sample_data_access.execute()]