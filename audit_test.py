"""Independent Python time-zone audit for the PWA's anchor events."""
from datetime import datetime
from zoneinfo import ZoneInfo
BKK=ZoneInfo('Asia/Bangkok')
CASES=[('2026-03-10','Europe/London',8,0,'15:00'),('2026-03-30','Europe/London',8,0,'14:00'),('2026-11-03','Europe/London',8,0,'15:00'),('2027-03-16','Europe/London',8,0,'15:00'),('2027-03-30','Europe/London',8,0,'14:00'),('2026-03-10','America/New_York',8,30,'19:30'),('2026-11-03','America/New_York',8,30,'20:30'),('2026-03-10','America/New_York',9,30,'20:30'),('2026-11-03','America/New_York',9,30,'21:30'),('2026-03-30','Europe/London',15,0,'21:00'),('2026-11-03','Europe/London',15,0,'22:00')]
for date,z,h,m,expected in CASES:
    t=datetime.fromisoformat(date).replace(hour=h,minute=m,tzinfo=ZoneInfo(z)).astimezone(BKK).strftime('%H:%M')
    assert t==expected,(date,z,t,expected)
print(f'PASS {len(CASES)} Python timezone reference tests')
