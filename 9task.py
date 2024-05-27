from datetime import datetime, timedelta

# Function to get time input from the user in HH:MM:SS format
def get_time_input(prompt):
    while True:  # Loop until a valid time is entered
        try:
            time_str = input(prompt)  # Prompt the user for input
            return datetime.strptime(time_str, '%H:%M:%S')  # Parse and return the time
        except ValueError:  # Handle invalid time format
            print("Invalid time format. Please enter time in HH:MM:SS format.")

# Function to increase a given time by specified hours, minutes, and seconds
def increase_time(time, seconds=0, minutes=0, hours=0):
    delta = timedelta(seconds=seconds, minutes=minutes, hours=hours)  # Create a timedelta object
    return time + delta  # Add the timedelta to the given time

# Function to add two times together
def add_times(time1, time2):
    # Convert times to timedelta objects
    delta1 = timedelta(hours=time1.hour, minutes=time1.minute, seconds=time1.second)
    delta2 = timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
    total_delta = delta1 + delta2  # Add the two timedelta objects
    return (datetime.min + total_delta).time()  # Return the result as a time object

# Function to calculate the difference between two times
def difference_times(time1, time2):
    # Convert times to timedelta objects
    delta1 = timedelta(hours=time1.hour, minutes=time1.minute, seconds=time1.second)
    delta2 = timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
    diff = abs(delta1 - delta2)  # Calculate the absolute difference
    return diff  # Return the difference as a timedelta object

# Main part of the program
if __name__ == "__main__":
    print("Enter the first time:")
    time1 = get_time_input("Time (HH:MM:SS): ")  # Get the first time from the user
    
    print("Enter the second time:")
    time2 = get_time_input("Time (HH:MM:SS): ")  # Get the second time from the user

    # Add the two times and display the result
    added_time = add_times(time1, time2)
    print(f"Addition of two times: {added_time}")

    # Calculate the difference between the two times and display the result
    time_difference = difference_times(time1, time2)
    print(f"Difference of two times: {time_difference}")

    # Loop to repeatedly increase the time based on user input
    while True:
        increase = input("Do you want to increase the time? (y/n): ").strip().lower()  # Prompt user to increase time
        if increase == 'y':  # If the user wants to increase the time
            hours = int(input("Enter hours to increase: "))  # Get the number of hours to increase
            minutes = int(input("Enter minutes to increase: "))  # Get the number of minutes to increase
            seconds = int(input("Enter seconds to increase: "))  # Get the number of seconds to increase
            increased_time = increase_time(time1, seconds=seconds, minutes=minutes, hours=hours)  # Increase the time
            print(f"Time after increasing: {increased_time.time()}")  # Display the increased time
            time1 = increased_time  # Update time1 to the new increased time for further increments
        elif increase == 'n':  # If the user does not want to increase the time
            print("Stop Execution of programe.")  # Print a message indicating the end of the program
            break  # Exit the loop
        else:  # If the user input is invalid
            print("Invalid input, please enter 'y' or 'n'.")  # Prompt the user to enter a valid response
