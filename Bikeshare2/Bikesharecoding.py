{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import data\n",
    "\n",
    "CITY_DATA = { 'chicago': 'chicago.csv',\n",
    "              'new york city': 'new_york_city.csv',\n",
    "              'washington': 'washington.csv' }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def get_filters():\n",
    "    \"\"\"\n",
    "    Asks user to specify a city, month, and day to analyze.\n",
    "\n",
    "    Returns:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    \"\"\"\n",
    "    print('Hello! Let\\'s explore some US bikeshare data!')\n",
    "    \n",
    "    \n",
    "    \n",
    "    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs\n",
    "    city= input('Please enter the city name: ')\n",
    "    while city not in ['new york city', 'washington', 'chicago']:\n",
    "            print('Sorry, Your input is not in the database')\n",
    "         \n",
    "\n",
    "    month = input('Which month are you looking for:')\n",
    "    while month not in ('January', 'Februray', 'March', 'April', 'May', 'June','other'):\n",
    "            print('Invalid Input')\n",
    "            \n",
    "            \n",
    "\n",
    "    # get user input for day of week (all, monday, tuesday, ... sunday)\n",
    "    day =input('Please enter the date, Monday, Tuesday, etc: ')\n",
    "    day_dict= {'Monday': Mon, 'Tuesday': Tue, 'Wednesday': Wed, 'Thursday': Thurs, 'Friday': Fri, 'Saturday': Sat,\n",
    "                    'Sunday': Sun}\n",
    "    while day.lower() not in day_dict.keys():\n",
    "                print('Please input valid date: Mon')\n",
    "\n",
    "    print('-'*40)\n",
    "    return city, month, day\n",
    "\n",
    "\n",
    "\n",
    "def load_data(city, month, day):\n",
    "    \"\"\"\n",
    "    Loads data for the specified city and filters by month and day if applicable.\n",
    "\n",
    "    Args:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    Returns:\n",
    "        df - Pandas DataFrame containing city data filtered by month and day\n",
    "    \"\"\"\n",
    "    df = pd.read_csv(\"{}.csv\".format(city.replace(\" \", \"_\")))\n",
    "    df['Start Time'] = pd.to_datetime(df['Start Time'])\n",
    "    df['End Time'] = pd.to_datetime(df['End Time'])\n",
    "    df['month'] = pd.to_datetime(df['Start Time']).dt.month\n",
    "    if day != 'all':\n",
    "        df = df[df['day_of_week'] == day]\n",
    "    if month != 'all':\n",
    "        df = df[df['month'] == month]\n",
    "    df.drop('day_of_week', axis=1, inplace=True)\n",
    "    df.drop('month', axis=1, inplace=True)\n",
    "    return df\n",
    "\n",
    "\n",
    "\n",
    "def time_stats (df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "    \n",
    "    pop_month = df['month'].mode()[0]\n",
    "    print('Popular Month:', pop_month)\n",
    "    \n",
    "    pop_day = df['day_of_week'].mode()[0]\n",
    "    print('Popular day:', pop_day)\n",
    "    \n",
    "    \n",
    "    \n",
    "    df['hour'] = df['Start Time'].dt.hour\n",
    "    \n",
    "    # the hour\n",
    "    pop_hour = df['hour'].mode()[0]\n",
    "    print('Popular Hour', Pop_hour)\n",
    "    \n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "    \n",
    "\n",
    "def station_stats(df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # display most commonly used start station\n",
    "    Print('The commonly Start station is:{}'.format(df['Start Station'].mode()[0]))\n",
    "    \n",
    "\n",
    "    # display most commonly used end station\n",
    "    Print('The commonly End station is:{}'.format(df['End Station'].mode()[0]))\n",
    "\n",
    "\n",
    "    # display most frequent combination of start station and end station trip\n",
    "    comb= df['Start Station']+' '+ df['End Station']\n",
    "    print('most frequent combination of start station and end station trip is{}'.format(comb.mode()[0]))\n",
    "\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "    \n",
    "    \n",
    "def trip_duration_stats(df):\n",
    "    \"\"\"Displays statistics on the total and average trip duration.\"\"\"\n",
    "\n",
    "    print('\\nCalculating Trip Duration...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    \n",
    "    # display total travel time\n",
    "    total_travel= df['Trip Duration'].sum()\n",
    "    print('Total Travel Time is:', total_travel)\n",
    "\n",
    "    # display mean travel time\n",
    "    \n",
    "    mean_travel= df['Trip Duration'].mean()\n",
    "    print('The mean travel time is:',mean_travel/60,\"(Min)\")\n",
    "\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "    \n",
    "\n",
    "\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "def user_stats(df):\n",
    "    \"\"\"Displays statistics on bikeshare users.\"\"\"\n",
    "\n",
    "    print('\\nCalculating User Stats...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # Display counts of user types\n",
    "    \n",
    "    User_type = df['User Type'].value_counts()\n",
    "    print('User Type:', User_type)\n",
    "\n",
    "\n",
    "    # Display counts of gender\n",
    "    \n",
    "    if city not in 'washington':\n",
    "        print('Count of Gener: ', df['Gender'].value_counts())\n",
    "\n",
    "    # Display earliest, most recent, and most common year of birth\n",
    "    \n",
    "    Earliest = int(df['birth_year'].min())\n",
    "    print('The earliest birth year:{}'.format(Earliest))\n",
    "    \n",
    "    latest = int(df['birth_year'].max())\n",
    "    print('The recent birth year:{}'.format(latest))\n",
    "    \n",
    "    common = int(df['birth_year'].mode())\n",
    "    print('The common birth year:{}'.format(common))\n",
    "    \n",
    "\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "def main():\n",
    "    while True:\n",
    "        city, month, day = get_filters()\n",
    "        df = load_data(city, month, day)\n",
    "\n",
    "        time_stats(df)\n",
    "        station_stats(df)\n",
    "        trip_duration_stats(df)\n",
    "        user_stats(df)\n",
    "\n",
    "        restart = input('\\nWould you like to restart? Enter yes or no.\\n')\n",
    "        if restart.lower() != 'yes':\n",
    "            break\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\tmain()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}