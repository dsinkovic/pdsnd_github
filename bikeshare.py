import time
import pandas as pd
import numpy as np
from datetime import timedelta

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_user_input(question, result_set):
    """
    Asks user for input with a specific question. Expected user response should be within result_set.
    Repeats input question until an appropriate response is given.

    Args:
        (str) question - Text of the question to user
        (list) result_set - a list containing possible user responses

    Returns:
        (str) response - valid user response
    """

    response = input(question).title()
    while response not in result_set:
        response = input('\nI\'m sorry, I don\'t understand your answer, please respond with: \'' \
            + '\', \''.join(result_set[:-1]) + '\' or \'' + result_set[-1] + '\'\n').title()

    return response

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_user_input('Would you like to see data for Chicago, New York City or Washington?\n', \
        ['Chicago', 'New York City', 'Washington'])

    # set inital values to no filters
    month = day = 'All'

    # get user input for filtering criteria
    response = get_user_input('\nWould you like to filter the data by month, day, both or not at all? Please type \'No\' for no time filter.\n', \
        ['Month', 'Day', 'Both', 'No'])

    # get user input for month (January, February, ... , June)
    if response in {'Month', 'Both'}:
        month = get_user_input('\nWhich month - January, February, March, April, May, or June?\n', \
            ['January', 'February', 'March', 'April', 'May', 'June'])

    # get user input for day of week (Monday, Tuesday, ... Sunday)
    if response in {'Day', 'Both'}:
        day = get_user_input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n', \
            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    print('Your selected filters: {}, {}, {}\n'.format(city, month, day))
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

    df = pd.read_csv(city.replace(' ', '_').lower() + '.csv')
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Start Month'] = df['Start Time'].dt.month_name()
    df['Start Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    if (month != 'All') and (day != 'All'):
        df = df[(df['Start Month'] == month) & (df['Start Day']==day)]
    elif (month != 'All') and (day == 'All'):
        df = df[df['Start Month'] == month]
    elif (month == 'All') and (day != 'All'):
        df = df[df['Start Day']==day]

    print('\nData was successfully loaded and filtered based on given criteria.')
    print('-'*40)

    return df

def display_raw_data(df):
    """
    Asks the user whether they want to display the raw data or not. If yes, 5 rows od data is printed at a time and the user is asked to confirm to print next 5 rows.

    Args:
        df - Pandas DataFrame containing filtered city data
    """

    response = get_user_input('\nWould you like to display raw data of the filtered dataset?\n', ['Yes', 'No'])

    if response == 'Yes':
        pos, row_count = 0, len(df)

        response2 = get_user_input('\nWould you like to display all columns or to fit the number of columns to screen width? Please answer with \'All\' or \'Fit\':\n', ['All', 'Fit'])
        if response2 == 'All':
            pd.set_option('display.max_columns', None)
        else:
            pd.reset_option('display.max_columns')

        while (response == 'Yes') and (pos < row_count):
            print(df[pos:min(pos + 5, row_count)])
            pos += 5
            response = get_user_input('\nWould you like to print next 5 rows?\n', ['Yes', 'No'])

        print('\nPrinted {} rows out of {}'.format(min(pos, row_count), row_count))

        if response == 'No':
            print('Printing dataset ended on your request.')
        else:
            print('Printing dataset completed.')

    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: {}\n'.format(df['Start Month'].mode()[0]))

    # display the most common day of week
    print('Most common day of week: {}\n'.format(df['Start Day'].mode()[0]))

    # display the most common start hour
    print('Most common start hour: {}\n'.format(df['Start Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station: {}\n'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most commonly used end station: {}\n'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station
    # concatenate names of start and end station and calculating Mode on the resulting column
    print('Most frequent combination of start station and end station: {}\n'.format((df['Start Station'] + ' - ' + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal travel time: {}'.format(timedelta(seconds = float(df['Trip Duration'].sum()))))

    # display mean travel time
    print('\nMean trip duration: {}'.format(timedelta(seconds = float(df['Trip Duration'].mean()))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print('\nUser type counts:\n')
        print(df['User Type'].value_counts())
        nan_no = df['User Type'].isnull().sum()
        if nan_no > 0:
            print('{} records have no User Type assignment.'.format(nan_no))
    except:
        print('No User Type data available.')

    # Display counts of gender
    print('\nGender counts:')
    try:
        print(df['Gender'].value_counts())
        nan_no = df['Gender'].isnull().sum()
        if nan_no > 0:
            print('{} records have no Gender assignment.'.format(nan_no))
    except:
        print('No Gender data available.')

    # Display earliest, most recent, and most common year of birth
    try:
        print('\nThe earliest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('The most common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))
        nan_no = df['Birth Year'].isnull().sum()
        if nan_no > 0:
            print('{} records have no Birth Year assignment.'.format(nan_no))
    except:
        print('\nNo Birth Year data available.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)

        time_stats(df)
        input("Press Enter to continue...\n")
        station_stats(df)
        input("Press Enter to continue...\n")
        trip_duration_stats(df)
        input("Press Enter to continue...\n")
        user_stats(df)

        restart = get_user_input('\nWould you like to restart? Enter yes or no.\n', ['Yes', 'No'])
        if restart != 'Yes':
            break


if __name__ == "__main__":
	main()
