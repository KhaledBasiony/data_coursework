import time
import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = {'all':0, 'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
DAYS = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}



def input_string(field, check, inpt):
    """
    Prints a message, asking for user input for a specific field, several times until the input is correct.

    Parameters
    ----------
    field : str
        the field of data which the program should filter by.
    check : set or dict
        a data structure in which to check wether the value collected is in or not.
    inpt : str
        the printed message clarifying the user's input.

    Returns
    -------
    value : string
        a stripped lowercase copy of the user's input.

    """

    #Get input from user correctly
    while True:
        try:
            print("Which {}'s data would you like to see ?".format(field))

            #make sure that the input is in lowercase and without any whitespaces on the beginning or the end
            value= input(inpt).lower().strip()
            if(value == '000'):
                sys.exit(0)
            assert value in check
            break
        except AssertionError:
            print("Looks like there was something wrong with your input, please try again\n")

    print('\n\n===============\n\n')
    return value

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('\n***PLEASE NOTE: if and when you\'d like to exit the program, please type in 000 as input.***\n')


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    inpt_msg = "Please type in one of the following without the quotes ('chicago', 'new york city', 'washington') : "
    city = input_string('city', CITY_DATA, inpt_msg)


    # get user input for month (all, january, february, ... , june)
    inpt_msg = "Please type in a full month name from 'january' up to 'june' or 'all' for no filtering by month : "
    month = input_string('month', MONTHS, inpt_msg)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    inpt_msg = "Please type in a full day name or 'all' for no filtering by day : "
    day = input_string('day', DAYS, inpt_msg)


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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], format="%Y-%m-%d %H:%M")


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS[month]

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df, month, day):

    """
    Displays statistics on the most frequent times of travel.


    Parameters
    ----------
    df : A Pandas DataFrame
        The DataFrame to make the processing on.

    month : str
        The user chosen choice for months,
        to know whether the provided DataFrame is filtered by month or not.

    day : str
        The user chosen choice for day of the week,
        to know whether the provided DataFrame is filtered by day or not.


    Returns
    -------
    None.

    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    if month == 'all':
        months = pd.to_datetime(df['Start Time']).dt.month_name().value_counts()
        print("The most common month is: {}\nwith a count of: {}\n".format(months.idxmax(), months.max()))
        plt.figure(1)
        months.plot(kind='pie', label='', title='Months', autopct='%1.1f%%', startangle=90, shadow=True, explode=(0.1,0,0,0,0,0))
    else:
        print("You Chose to filter by month! which is {}\n".format(month))

    # display the most common day of week
    if day == 'all':
        days = pd.to_datetime(df['Start Time']).dt.day_name().value_counts()
        print("The most common day is: {}\nwith a count of: {}\n".format(days.idxmax(), days.max()))
        plt.figure(2)
        days.plot(kind='pie', label='', title='Days', autopct='%1.1f%%', startangle=90, shadow=True, explode=(0.1,0,0,0,0,0,0))
    else:
        print("You Chose to filter by day! which is {}\n".format(day))

    # display the most common start hour
    hours = pd.to_datetime(df['Start Time']).dt.hour.value_counts()
    print("The most common Hour is: {}\nwith a count of: {}\n".format(hours.idxmax(), hours.max()))
    plt.figure(3)
    hours.plot(kind='bar', label='', title='Hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\nCalculating The Most Popular Stations and Trip...\n\n')
    start_time = time.time()

    # display most commonly used start station
    st_stations = df['Start Station'].value_counts()
    print("The most frequent start station is: {}\nwith the count of: {}\n".format(st_stations.idxmax(), st_stations.max()))

    # display most commonly used end station
    end_stations = df['End Station'].value_counts()
    print("The most frequent end station is: {}\nwith the count of: {}\n".format(end_stations.idxmax(), end_stations.max()))

    # display most frequent combination of start station and end station trip
    comb = pd.Series(df['Start Station'] + '  --  ' + df['End Station']).value_counts()
    print('The most frequent combination is: {}\nwith the count of: {}\n'.format(comb.idxmax(), comb.max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total trip duration is: {} seconds\n".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("The average trip duration is: {} seconds\n".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The count of user types is:\n{}\n".format(df['User Type'].value_counts().to_string()))
    plt.figure(4)
    df['User Type'].value_counts().plot(kind='pie', shadow=True, autopct='%1.1f%%', label='', title='User Types')

    # Display counts of gender
    try:
        print("The count of genders is:\n{}\n".format(df['Gender'].value_counts().to_string()))
        plt.figure(5)
        df['Gender'].value_counts().plot(kind='pie', shadow=True, autopct='%1.1f%%', label='', title='Genders')
    except KeyError:
        print("Oops, Looks like there is no data regarding the Gender.\n")

    # Display earliest, most recent, and most common year of birth
    try:
        birth = df['Birth Year']
        print("The Earliest birth year: {}\nThe Most Recent birth year: {}\nThe Most Common birth year: {}\n".format(int(birth.min()), int(birth.max()), int(birth.mode()[0])))
    except KeyError:
        print("Oops, Looks like there is no data regarding the Year OF Birth.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df, city):
    """

    Display the DataFrame upon user request

    Parameters
    ----------
    df : Pandas DataFrame
        The DataFrame to display.

    city: str
        The name of the chosen city, as washington's data is different.

    Returns
    -------
    None.

    """

    #check whether the user wants to see the data
    req = input("\n\n{}\nWould you like to see the raw data ?\nEnter yes to do so: ".format('-'*40)).lower().strip()
    index = 0

    #applying exit code for the program
    if(req=='000'):
        sys.exit(0)

    #filling null values and dropping garbage data
    df.drop(df.columns[[0, -1, -2]], axis=1, inplace=True)
    df.reset_index(drop=True, inplace=True)
    if (city!='washington' and req=='yes'):
        fill_null = input("\nPlease note that the data contains a few missing values in both the gender and the birth year columns, Would you like for them to be filled automatically?\nEnter yes to do so: ").lower().strip()
        if fill_null=='000':
            sys.exit(0)
        if fill_null=='yes':
            df.fillna(method = 'ffill', inplace=True)


    #loop to know when to exit
    while req=='yes':
        print("\n{}\n".format('-'*40))
        rows = input("How many rows would you like to see ? Enter 0 to stop\n").lower().strip()

        #apply exit conditions
        if(rows=='000'):
            sys.exit(0)
        elif(rows == '0'):
            return

        #check whether the input was a valid number
        try:
            rows = int(rows)
            assert rows > 0
        except:
            print("Looks like something is wrong with your input.\nPlease try again with a positive integer number.")
            continue

        #print selected number of rows
        print(df.iloc[index:index+rows].to_string())
        index += rows
    else:
        print("\nNo data will be shown.\n{}".format('-'*40))




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df, city)

        show_graphs = input("Would you Like to see some Graphs? if not, type no\n").lower().strip()
        if(show_graphs == '000'):
            sys.exit(0)
        if(show_graphs != 'no'):
            plt.show()
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        plt.close('all')
        if restart.lower().strip() != 'yes':
            break


if __name__ == "__main__":
	main()
