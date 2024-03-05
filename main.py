# https://github.com/cyberjunky/python-garminconnect/blob/master/example.py

from datetime import date
from datetime import timedelta
from config import BaseConfig
from garminconnect import Garmin


def init_api():
    garmin = Garmin(BaseConfig.USERNAME, BaseConfig.PASSWORD)
    garmin.login()
    return garmin


if __name__ == '__main__':
    today = date.today()
    start_date = today - timedelta(days=7)
    activity_type = 'walking'  # cycling, running, swimming, multi_sport, fitness_equipment, hiking, walking, other
    api = init_api()
    if api:
        print("api.get_full_name():", api.get_full_name())
        print(f"api.get_heart_rates('{today.isoformat()}'):", api.get_heart_rates(today.isoformat()))
        print("api.get_last_activity():", api.get_last_activity())
        activities = api.get_activities_by_date(start_date.isoformat(), today.isoformat(), activity_type)
        for activity in activities:
            print(activity)
            activity_id = activity["activityId"]
            activity_name = activity["activityName"]
            gpx_data = api.download_activity(activity_id, dl_fmt=api.ActivityDownloadFormat.GPX)
            print(gpx_data)
