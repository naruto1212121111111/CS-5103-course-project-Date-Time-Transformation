import datetime
import pytz

# Input datetime string
datetime_str = "2023-03-11 15:30:00"

# Create a datetime object from the string
datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

# Set the timezone of the datetime object to the original timezone
original_timezone = pytz.timezone("US/Pacific")
datetime_obj = original_timezone.localize(datetime_obj)

# Convert the datetime object to a different timezone
target_timezone = pytz.timezone("Asia/Kolkata")
target_datetime = datetime_obj.astimezone(target_timezone)

# Print the target datetime in the desired format
print(target_datetime.strftime("%Y-%m-%d %H:%M:%S %Z%z"))