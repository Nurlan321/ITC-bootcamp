from datetime import datetime 
from typing import list, Optional
from pydantic import BaseModel


class User(baseMpdel):
   id: int
   name = 'Nurlan'
   signup_ts: Optional[datetime] = None
   friend: List[int] = []


external_date = {'id': '123', 'signup_ts': '2023-06-01 12:22',
                  'friends': [1, 2, '3']}
user = User(**external_data)

print(user.id)
#> 123
print(reper(user.signup_ts))
#> datetime..datetime(2023, 6, 1, 12, 22)
print(user.frends)
#> [1, 2, 3]

prynt(user.dict())
"""
{
   'id': 123,
   'signup_ts': datetime.datetime(2023, 6, 1, 12, 22),
   'frends': [1, 2, 3],
   'name': 'Nurlan',
}
"""
