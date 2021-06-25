import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city_df = pd.read_csv(CITY_DATA[city])
    city_df['Start Time']=pd.to_datetime(city_df['Start Time'])
    city_df['Month']=city_df['Start Time'].dt.month
    city_df['Day of Week']=city_df['Start Time'].dt.weekday_name
    
    
       
    return city_df

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        city=input("please choose one city of these cities:Chicago, New York City and Washington to analyze: ").lower()
        if city not in CITY_DATA:
            print("Please choose a correct city name")
            
        else:
            break
            
    while True:
        month=input("please choose the month you want to filter the data by(January, February, March, April, May or June) or type 'all' to apply no month filter: ").lower()
        months=['january', 'february','march','april','may','june']
        if month != 'all' and month not in months:
            print("Please enter a full valid month name")
        else:
            break
   
    while True:
        day=input("please choose the day you want to filter the data by(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) or type 'all' to apply no day filter: ").lower()
        days=['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if day != 'all' and day not in days:
            print("Please enter a full valid day name")
        else:
            break
                
    print('-'*40)
    return city, month, day
       
def time_stats(city_df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    popular_month=city_df['Month'].mode()[0]
    print("The most common month is: ",popular_month)
    
    popular_day=city_df['Day of Week'].mode()[0]
    print("The most common day of week is: ",popular_day)
    
    city_df['Start Hour']=city_df['Start Time'].dt.hour
    popular_hour=city_df['Start Hour'].mode()[0]
    print("The most common start hour is: ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(city_df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    popular_startstation=city_df['Start Station'].mode()[0]
    print("The most commonly used start station is: ",popular_startstation)
    
    popular_endstation=city_df['End Station'].mode()[0]
    print("The most commonly used end station is: ",popular_endstation)
    
    city_df['Combination of Start & End station trip']=city_df['Start Station'] + city_df['End Station']
    popular_combination=city_df['Combination of Start & End station trip'].mode()[0]
    print("The most frequent combination of start & end station is:",popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(city_df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    city_df['End Time']=pd.to_datetime(city_df['End Time'])
    city_df['End Hour']=city_df['End Time'].dt.hour
    city_df['Total Trip Time']=city_df['End Hour'] - city_df['Start Hour']
    print("The total travel time is: ",city_df['Total Trip Time'].sum())
    
    print("The travel time mean is: ",city_df['Total Trip Time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city_df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    
    count_of_user_types=city_df['User Type'].value_counts()
    print("The count of user types is: ",count_of_user_types)
    if 'Gender' in city_df:
        count_of_gender=city_df['Gender'].value_counts()
        print("The count of gender is: ",count_of_gender)
    else:
        print("The data in the washington file does not include column for Gender, so there is no user for them")
        
        
        
    if 'Birth Year' in city_df:
        sorted_year=np.sort(city_df['Birth Year'])
        print("The earliest year of birth is: ",sorted_year[0])
        print("The recent year of birth is: ",sorted_year[-1])
        popular_year=city_df['Birth Year'].mode()[0]
        print("Most common year is: ",popular_year)
    else:
        print("The data in the washington file does not include column for and Birth Year, so there is no user for them")
        
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(city_df):
    i=0
    answer = input("Would you like to display the first 5 rows of the data ? yes/no: ").lower()
    while True:
        if answer == 'no':
            break
        print(city_df[i:i+5])
        answer=input("Would you like to display the next 5 rows of data? yes/no: ").lower()
        i+=5


def main():
    while True:
        city, month, day = get_filters()
        city_df = load_data(city, month, day)
        
        time_stats(city_df)
        station_stats(city_df)
        trip_duration_stats(city_df)
        user_stats(city_df)
        display_raw_data(city_df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
