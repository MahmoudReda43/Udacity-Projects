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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city name (chicago, new york city, washington): ").lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
        print("Invalid type or city name")
        city = input("Enter city name (chicago, new york city, washington): ").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month (all, january, february, ... , june): ").lower()
    
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("Invalid type or month name")
        month = input("Enter month (all, january, february, ... , june): ").lower()
         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day (all, monday, tuesday, ... sunday): ").lower()

    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("Invalid type or month name")
        day = input("Enter month (all, january, february, ... , june): ").lower()
         

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
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week: ", df['day_of_week'].mode()[0])
    
    # TO DO: display the most common start hour
    print("The most common start hour: ", df['Start Time'].dt.hour.mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    
    # way 1 to get the most frequent combination of start station and end station trip
#     most_freq = (df['Start Station'] + '$merg$' + df['End Station']).mode()[0].split('$merg$')
    
    # way 2 to get the most frequent combination of start station and end station trip
    most_freq = df.groupby(['Start Station','End Station']).size().idxmax()
    
    # I got that way 2 more faster than way 1 so I used way 2 
    print(f"The most frequent combination of start station and station trip: \nStart Station: {most_freq[0]}\nEnd Station: {most_freq[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"The total travel time is {df['Trip Duration'].sum()} sec")

    # TO DO: display mean travel time
    print(f"The total travel time is {df['Trip Duration'].mean()} sec")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"Counts of user types:\n{df['User Type'].value_counts()}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(f"Counts of user types:\n{df['Gender'].value_counts()}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f"The earliest year of birth: {int(df['Birth Year'].min())}")
        print(f"The most recent year of birth: {int(df['Birth Year'].max())}")
        print(f"The most common year of birth: {int(df['Birth Year'].mode())}")
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# display_data for displaying 5 rows of the returned dataset
def display_data(df):
    # Ask the user if he wants to display  rows of the data
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower() 
    start_loc = 0
    
    while (view_data == 'yes'):
        # check if the next 5 rows will exceed the dataset total number of rows
        if start_loc + 5 > df.shape[0]:
            print(df.iloc[start_loc : ])
            print(f'You have printed the whole data which contains {df.shape[0]} rows')
            break
            
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5   
        
        view_display = input("Do you wish to continue displaying the next 5 rows of individual trip data?: ").lower()
        if view_display != 'yes':
            break

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
