def next_day(day):
  days_dict = {
      "Monday": "Tuesday",
      "Tuesday": "Wednesday",
      "Wednesday": "Thursday",
      "Thursday": "Friday",
      "Friday": "Saturday",
      "Saturday": "Sunday",
      "Sunday": "Monday"
  }
  return days_dict[day]


def add_time(start, duration, day=""):
  # Split start into hours, minutes, and meridiem.
  start_split = start.split(":")  # hours and minutes + meridiem
  start_hrs = int(start_split[0])
  start_mins = int(start_split[1].split(" ")[0])
  start_mer = start_split[1].split(" ")[1]

  # Split duration into hours and minutes.
  duration_split = duration.split(":")
  dur_hrs = int(duration_split[0])
  dur_mins = int(duration_split[1])

  # Set a new day variable with all lowercase letters except the first.
  start_day = day
  if day:
    start_day = day.lower().capitalize()
  else:
    start_day = "Monday"  # used as a placeholder, will not be showed in new_time

  # Convert into 24 hour time to make it easier to work with.
  if start_hrs == 12 and start_mer == "AM":
    start_hrs = 0
  elif start_hrs == 12 and start_mer == "PM":
    start_hrs = 12
  elif start_mer == "PM":
    start_hrs += 12

  # Set results variables
  final_hrs = start_hrs
  final_mins = start_mins
  final_mer = ""
  final_day = start_day
  days_later_count = 0

  # Loop through the duration minutes and add them to the final minutes.
  while dur_mins > 0:
    final_mins += 1
    dur_mins -= 1

    # If mins is 60, add an hour. If hours is 24, add a day.
    if final_mins == 60:
      final_mins = 0
      final_hrs += 1
      if final_hrs == 24:
        final_hrs = 0
        days_later_count += 1
        final_day = next_day(final_day)

  # Loop through the duration hours and add them to the final hours.
  while dur_hrs > 0:
    final_hrs += 1
    dur_hrs -= 1

    # If hrs is 24, reset and add a day.
    if final_hrs == 24:
      final_hrs = 0
      days_later_count += 1
      final_day = next_day(final_day)

  # Convert back into 12 hour time for the output.
  if final_hrs == 0:
    final_hrs = 12
    final_mer = "AM"
  elif final_hrs == 12:
    final_mer = "PM"
  elif final_hrs > 12:
    final_hrs -= 12
    final_mer = "PM"
  else:
    final_mer = "AM"

  # Add 0s to the beginning of 1 digit minute numbers
  if final_mins < 10:
    final_mins = "0" + str(final_mins)

  # Create and return new_time
  new_time = str(final_hrs) + ":" + str(final_mins) + " " + final_mer

  if day:
    new_time += ", " + final_day

  if days_later_count > 1:
    new_time += " (" + str(days_later_count) + " days later)"

  if days_later_count == 1:
    new_time += " (next day)"

  return new_time
