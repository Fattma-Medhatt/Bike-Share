import time
import calendar
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose a city from chicago, new york city, washington: ').lower()
        if city not in CITY_DATA:
            print('Invalid choice! Please choose a correct city name')
        else:
            break 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please choose a month from january to june, or type "all" to display all months: ').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != 'all' and month not in months:
            print('Invalid choice! Please enter a full valid month name')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose a day of the weeek or type "all" to display all days: ').lower()
        days = ['saturday','sunday', 'monday', 'tuseday', 'wednsday', 'thursday', 'friday']
        if day != 'all' and day not in days:
            print('Invalid choice! Please enter a full valid day name')
        else:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df ['month'].mode()[0]                   
    print('Most Common Month:', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
                                       
    print('Most Common Day:', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
                                       
    common_hour = df['hour'].mode()[0]
                                       
    print('Most Common Start Hour:', common_hour)                                   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0] 
    print('Most Commonly Used Start Station:', common_start)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]                                   
    print('Most Commonly Used End Station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + ' ' + ['End Station']).mode()[0]
    print('Most Frequent Combination of Start Station and End Station Trip:', common_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_time, 'Sec')      

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average Travel Time:', mean_time, 'Sec')      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_counts = df['User Type'].value_counts()
    print('Counts of User Types:\n', type_counts)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nCounts Of Gender:\n', df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\n Earliest Year of Birth:\n', earliest_birth_year)
        recent_birth_year = int(df['Birth Year'].max())
        print('\n Most Recent Year of Birth:\n', recent_birth_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\n Most Common Year Of Birth:\n', common_birth_year)
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    i = 0
    user_input = input('Would you like to display 5 row of raw data? yes/no:').lower()
    pd.set_option('display.max_columns',None)
    while True:
        if user_input == 'no':
            break
        print(df[i:i+5])
        user_input = input('Would you like to display more 5 rows of raw data? yes/no: ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
              

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()