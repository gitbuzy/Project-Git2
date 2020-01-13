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

    cities = CITY_DATA.keys()
    months = ('all', 'january', 'february','march', 'april', 'may', 'june')
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city would you like to view: chicago, new york city, washington?\n').lower()
        if city not in cities:
            print('Invalid response, please try again.')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to view: all, january, february, march, april, may, june?\n').lower()
        if month not in months:
            print('Invalid response, please try again.')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day of the week would you like to view: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday?\n').lower()
        if day not in days:
            print('Invalid response, please try again.')
            continue
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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['DOW'] = df['Start Time'].dt.weekday
    df['month'] = df['Start Time'].dt.month

    if month != 'all':
        months = ['january','february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df= df[df['DOW'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month for travel:', most_common_month)

    # TO DO: display the most common day of week
    most_common_DOW = df['day_of_week'].mode()[0]
    print('The most common day of the week for travel:', most_common_DOW)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_sthr = df['hour'].mode()[0]
    print('The most common start hour of the day:', most_common_sthr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_ststation = df['Start Station'].mode()[0]
    print('The most common starting destination:', most_common_ststation)

    # TO DO: display most commonly used end station
    most_common_estation = df['End Station'].mode()[0]
    print('The most common ending destination:', most_common_estation)

    # TO DO: display most frequent combination of start station and end station trip
    cmb_station = (df ['Start Station'] + '&' + df['End Station']).mode()[0]
    print('Most frequently used stations combined:', cmb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    AVG_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', AVG_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Types'].value_counts()
    print('User Type:', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Gender Types:', gender)
    except KeyError:
        print('No data available at this time')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        year_birth_max = df['Birth Year'].max()
        print('The earliest birth year recorded:', year_birth_max)
    except KeyError:
        print('No data available at this time')

    try:
        year_birth_min = df['Birth Year'].min()
        print('The latest year recorded:', year_birth_min)
    except KeyError:
        print('No data avaiable at this time')

    try:
        year_birth_common = df['Birth Year'].mode()[0]
        print('The common year recorded:', year_birth_common)
    except KeyError:
        print('No data available at this time')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #TO DO: Prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes',
    #and continue these prompts and displays until the user says 'no'.

def raw_data(df):
        """Display raw data upon user's request
        If the answer is Yes ask the user if you want to see 5 more rows of data.
        Continue to ask until the answer is No. If No print Thank you. Goodbye"""

        rows = 0
        data_view = input('Would you like to see 5 rows of raw data? Yes or No\n').lower()

        while data_view == 'Yes':
              print(df[rows:rows +5])
              rows = rows +5
              data_view =input('Would you like to see 5 more rows of raw data? Yes or No\n').lower()

        print('Thank you. Goodbye:-)')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # added function
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
