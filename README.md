# due date calculator
A solution needed that implements a due date calculator in an issue tracking system, the task is to implement the CalculateDueDate method
- input: Takes the submit date/time and turnaround time.
- output: Returns the date/time when the issue is resolved.
## rules
- working hours are 9:00-17:00 from monday to friday
- holidays are ignored
- turnaround time is in hours
- submit date can only be between working hours
- dont use thirdparty libraries
## Usage
### Parameters
- submit_datetime - datetime object, when does the ticket got submitted
- turnaround_hours - integer, how much working hour does the ticket take
### Test
- $ python3 -m unittest