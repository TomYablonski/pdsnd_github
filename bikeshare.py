import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    CRED = '\033[91m'
    CGREEN = '\033[92m'
    CEND = '\033[0m'
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            print(CGREEN + "\n To see the bikeshare data for a selected city")
            print("Please enter one of these cities")
            print("Chicago, New York, or Washington \n" +CEND)
            city = input().lower()
            if city == "new york":
                city = "new york city"
            if city != "chicago" and \
                city != "new york city" and \
                city != "washington":
                print(CRED + "Invalid city name entered. Please try again." + CEND)
            if city == "chicago" or \
                city == "new york city" or \
                city == "washington":    
                break
        except:
            print(CRED + "Unexpected Error occurred getting the City" +CEND)
       # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            print("\n Which month would you like to see the data for ?")
            print("January, February, March, April, May or June. To see all enter All \n")
            month = input().lower()
            if month != "january" and \
                month != "february" and \
                month != "march" and \
                month != "april" and \
                month != "may" and \
                month != "june" and \
                month != "all":
                print(CRED + "Invalid month entered. Please try again." + CEND)
            if month == "january" or \
                month == "february" or \
                month == "march" or \
                month == "april" or \
                month == "may" or \
                month == "june" or \
                month == "all":
                break
        except:
            print(CRED + "Unexpected Error occurred getting the Month" + CEND)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            print("\n Which day would you like to see the data for ?")
            print("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday. To see all enter All \n")
            day = input().lower()

            if day != "monday" and \
                day != "tuesday" and \
                day != "wednesday" and \
                day != "thursday" and \
                day != "friday" and \
                day != "saturday" and \
                day != "sunday" and \
                day != "all":
                print(CRED + "Invalid day entered. Please try again." + CEND)
            if day == "monday" or \
                day == "tuesday" or \
                day == "wednesday" or \
                day == "thursday" or \
                day == "friday" or \
                day == "saturday" or \
                day == "sunday" or \
                day == "all":
                break
        except:
            print(CRED + "Unexpected Error occurred getting the Day" + CEND)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('Most common Month:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]

    print('Most common Start Hour:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station is:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most common End Station is:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_stop_station = (df['Start Station'] + '  -  ' + df['End Station']).mode()[0]
    print('\nMost frequent combination of start station and end station is:')
    print(start_stop_station)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    holdtime = int(total_travel_time) 
    days = holdtime // (24 * 3600)
    holdtime = holdtime % (24 * 3600)
    hours = holdtime // 3600
    holdtime %= 3600
    minutes = holdtime // 60
    holdtime %= 60
    seconds = holdtime
    
    print("Total travel time : {} days, {} hours, {} minutes, {} seconds"\
            .format(days, hours, minutes, seconds))       

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    holdtime = int(mean_travel_time) 
    days = holdtime // (24 * 3600)
    holdtime = holdtime % (24 * 3600)
    hours = holdtime // 3600
    holdtime %= 3600
    minutes = holdtime // 60
    holdtime %= 60
    seconds = holdtime
    
    print("The mean travel time : {} days, {} hours, {} minutes, {} seconds"\
            .format(days, hours, minutes, seconds))       

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    CRED = '\033[91m'
    CEND = '\033[0m'

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type Data :")
    for index, user_type in enumerate(user_types):
        print("{}: {}".format(user_types.index[index], user_type))
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\nGender Data :")
        genders = df['Gender'].value_counts()
        for index, gender in enumerate(genders):
            print("Gender \n  {}: {}".format(genders.index[index], gender))
    else:
         print(CRED + "Gender data in not found in ths cities data" + CEND)
            
    # TO DO: Display earliest, most recent, and most common year of birth
    print("\n\n Birth Year Data")
    if 'Birth Year' in df.columns:
        early_birth_year = df['Birth Year'].min()
        print("The earliest year of birth is : ", early_birth_year)
        recent_birth_year = df['Birth Year'].max()
        print("The most recent year of birth is : ", recent_birth_year)
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        print("The most common year of birth is : ", common_birth_year)
    else:
         print(CRED + "Birth Year data in not found in ths selection of data" + CEND)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays statistics on bikeshare users."""
    CRED = '\033[91m'
    CEND = '\033[0m'

    rowcnt = 0
    print('\nDisplay the data...\n')
    print("\nWould you like to see the raw data ?")
    print("Please entter 'yes' or 'no' \n")
    displaydata = input().lower()
           
    while True:
        if displaydata != "yes" and displaydata != "no":
            print(CRED + "Invalid answer entered. Please enter 'yes' or 'no'\n" + CEND) 
            displaydata = input("\nPlease enter either 'yes or 'no'\n")
        if displaydata == "no":
            return
        
        if displaydata == "yes":
            print(df[rowcnt: rowcnt + 5])
            rowcnt = rowcnt + 5
            displaydata = input("\nWould you like to see 5 more rows of data ? Enter 'yes' or 'no'\n")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
