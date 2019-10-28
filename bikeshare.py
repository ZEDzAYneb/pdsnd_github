import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
        invalid_inputs = "Sorry, Invalid input. Please try again" 
    
    print('Hello! Let\'s explore some US bikeshare data!')
   
    # TO DO: get user raw_input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("\nWhich city would you like to filter by: New York, Chicago or Washington?\n").lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print(invalid_inputs)
    
    # TO DO: get user raw_input for month (all, january, february, ... , june)
    while True :
        month = input("\nWhich month would you like to filter by: January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print(invalid_inputs)

    # TO DO: get user raw_input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("\nWhich day would you like to filter by: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n").lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print(invalid_inputs)


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
    file_name = CITY_DATA[city]
    print ("Accessing data from: " + file_name)
    df = pd.read_csv(file_name)
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # filter by month if applicable
    if month != 'all':
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month]

    # filter by day if applicable
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        
        # filter by day of week to create the new dataframe
        df = df[df['Start Time'].dt.weekday_name == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nThis took %s seconds." % (time.time() - start_time))    
    print('-'*40)
  

def main():
    while 1 == 1 :
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()