## Bikeshare project

### Date created
28.07.2020.

### Description
*Bikeshare project* allows for exploring data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington. The data is provided by *Motivate*, a bike share system provider for many major cities in the United States. The project aim is to uncover bike share usage patterns through interactive querying of the databases and providing selected statistics.

* #### Interactive queries
  The program will ask the user to choose query parameters by asking the following questions:
  1. Would you like to see data for Chicago, New York, or Washington?
  2. Would you like to filter the data by month, day, both or not at all?
  3. *(If they chose month or both)* Which month - January, February, March, April, May, or June?
  4. *(If they chose day or both)* Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

  Additionally, it will be offered to user to display the raw data selected with above described filters.

* #### Statistics Computed
  *Bikeshare project* will run and display the following statistical information about the filtered dataset:

  1. Popular times of travel (i.e., occurs most often in the start time)
    * most common month
    * most common day of week
    * most common hour of day
  2. Popular stations and trip
    * most common start station
    * most common end station
    * most common trip from start to end (i.e., most frequent combination of start station and end station)
  3. Trip duration
    * total travel time
    * average travel time
  4. User info
    * counts of each user type
    * counts of each gender (only available for NYC and Chicago)
    * earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files used
* **bikeshare.py** - the single source code file used for delivering this project.
* Data files *(used by the program but not uploaded to GitHub repository due to the size of the files)*:
  * **chicago.csv**
  * **new_york_city.csv**
  * **washington.csv**

  ### Credits
  Resources used for the *Bikeshare project*:
  - [Pandas documentation](https://pandas.pydata.org/docs/user_guide/index.html)
  - [Python 3.7.6. documentation](https://docs.python.org/release/3.7.6/)
