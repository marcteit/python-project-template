from domain.sample_business_logic import sample_business_logic
from infrastructure.data_access.sample_data_access import sample_data_access

def lambda1():
    _sample_data_access = sample_data_access()
    _sample_business_logic = sample_business_logic(_sample_data_access)
    print(_sample_business_logic.execute())

def lambda2():
    print("foo")