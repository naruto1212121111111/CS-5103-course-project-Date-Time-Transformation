import datetime
import pytz


def transform_datetime(datetime_str, original_tz, target_tz, apply_dst=True):
    datetime_obj = datetime.datetime.strptime(datetime_str,
                                              "%Y-%m-%d %H:%M:%S")
    original_timezone = pytz.timezone(original_tz)
    datetime_obj = original_timezone.localize(datetime_obj, is_dst=apply_dst)
    target_timezone = pytz.timezone(target_tz)
    target_datetime = datetime_obj.astimezone(target_timezone)

    if apply_dst:
        target_datetime = target_datetime - target_timezone.dst(
            datetime_obj.replace(tzinfo=None))
    target_datetime = target_timezone.normalize(target_datetime)
    updated_datetime = target_datetime.strftime("%m/%d/%Y %A %H:%M")
    print(updated_datetime)
    return updated_datetime


transform_datetime("2023-11-01 16:30:00", "US/Pacific", "Asia/Kolkata")
