from datetime import datetime
import pytz

# Define your team locations - customize these with your actual team locations
timezones = {
    'US_Eastern': 'America/New_York',
    'India': 'Asia/Kolkata',
    'UK': 'Europe/London',
    'Singapore': 'Asia/Singapore'
}

def show_meeting_times(meeting_time, source_tz):
    """Convert a meeting time to all team timezones"""
    source = pytz.timezone(timezones[source_tz])
    local_time = source.localize(meeting_time)
    
    print(f"\n{'='*60}")
    print(f"Meeting scheduled for: {meeting_time.strftime('%B %d, %Y at %I:%M %p')} {source_tz}")
    print('='*60)
    
    for location, tz_name in timezones.items():
        tz = pytz.timezone(tz_name)
        converted = local_time.astimezone(tz)
        print(f"{location:15} {converted.strftime('%B %d, %Y - %I:%M %p %Z')}")
    print()

def main():
    """Main function to run the timezone converter"""
    print("\n*** Meeting Time Zone Converter ***\n")
    
    # Get meeting details from user
    year = int(input("Enter year (e.g., 2026): "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))
    hour = int(input("Enter hour in 24-hour format (0-23, where 14 = 2 PM): "))
    minute = int(input("Enter minute (0-59): "))
    
    # Show available timezones
    print("\nAvailable timezones:")
    for i, tz in enumerate(timezones.keys(), 1):
        print(f"  {i}. {tz}")
    
    # Get source timezone
    source_tz = input("\nEnter the timezone for this meeting time (e.g., US_Eastern): ")
    
    # Validate timezone
    if source_tz not in timezones:
        print(f"Error: '{source_tz}' not found. Using US_Eastern as default.")
        source_tz = 'US_Eastern'
    
    # Create meeting time and show conversions
    meeting = datetime(year, month, day, hour, minute)
    show_meeting_times(meeting, source_tz)
    
    # Ask if user wants to check another time
    again = input("Check another meeting time? (y/n): ")
    if again.lower() == 'y':
        main()
    else:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()

