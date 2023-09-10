#Hamd Khan 30143419 # Mohamed Sobair 30162987

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import random
pd.options.mode.chained_assignment = None #kept recieving an error which said 'cacher needs updating' had nothing to do with the code, with online research was able to bypass error with this.

class Country: # creates a class Country which can be instantaneously called to create one instance of such class
    '''
    A class which creates a Country object

    Attributes:
        country (string): string that represents the countries name 
        un_region (string): string that represents the countries UN region
        sub_region (string): string that represents the countries sub_region
        sq_km (string): string that represents the countries square kilometers 
    '''
    def __init__(self,country,un_region,sub_region,sq_km):
        self.country = country
        self.un_region = un_region
        self.sub_region = sub_region
        self.sq_km = sq_km
        
        
    def print_geo_stats(self): #  an instance method of the class which is used later on to format data by calling on the list at certain indices
        '''
        Function that creates a list of the of the instance of country when user inputs a country

        Parameters:
            none
        Returns:
            stats_list: this is a list of all stats regarding the country geographically during such instance
        '''
        stats_list= [f'{self.country}',f'{self.un_region}',f'{self.sub_region}',f'{self.sq_km}'] # list of stats
        return stats_list

def list_maker_country(complete_list): # makes a list of all countries
    '''
    This function creates a list of just contry names based off being given a multidimential list of data containing contry names,un region, sub region and square kms
    Parameters: 
        complete_list: this is a multidimentional list that contains the data of Country_Data.csv
    returns:
        reutrns the a list of all country names in the csv data file
    '''
    list_countries = [] # empty list is defined which is then appended with elements
    count = 0
    for i in range(len(complete_list)): # loops through every country in the multidimential list which is the parameter and only adds country names to the list
        list_countries.append(complete_list[count][0])
        count += 1
    return list_countries

def choice_geo(complete_list, index):
    '''
    This function essentially takes in a multidimentional list and the index of the country based off the list of countries and thus with this information a 1 dimensional list is created with the country name, un region, sub region and square kms.
    Then the function calls upon the class Country at the instance of the Country name, Un region, Sub region and Square KM. With this the instance method print_geo_stats is assigned to geo_stats which thus creates its own new list just for that one instance in of the chosen country, which is usefull later on in the program.

    Parameters:
        complete_list: this is a multidimentional list that contains all the data of Country_Data.csv
        index: the index of the country in the list created in the list_maker_country function
    
    Returns:
        geo_stats is returned which is the an instance list of the chosen country and corresponding data in the Country_Data.csv file


    '''
    stat = complete_list[index]
    region = stat[0] # gets the country name
    un_region_input = stat[1] # gets UN region of of chosen country
    sub_region_input = stat[2] # gets sub region of chosen country
    sq_km_input = int(stat[3]) # gets the square km of chosen country then converts it to an integer
    
    country_inst = Country(region,un_region_input,sub_region_input,sq_km_input) # creates an instance of the class and passes each stat or geographical data into the class
    geo_stats = country_inst.print_geo_stats() # calls on the instance method in the class to return a list of all related geographical data
    return geo_stats
def formating_stats(stats):
    '''
    Function: formating_stats, responsible for formatting the stats into a neat table/format. This formatting is based off of right and left allignment values which are specified in the function 

    Parameters: 
        stats is taken in as a parameter which it is the list of geographical data relating to the users inputed country.
    returns
        none
    '''
    format_string_one = '{country:20}{un_reg:20}{sub_reg:20}{sq_kmss:20}' # specifies the allignment of each title text
    print(format_string_one.format(country = 'Country',un_reg = 'UN Region',sub_reg = 'Sub Region',sq_kmss = 'Sqaure KM' )) # gives and prints a title to the table 
    print('-'*64)
    format_string= '{chosen_country:20}{chosen_un_regions:20}{chosen_sub_regions:20}{chosen_square_kms:20}' # specifies the allignment of each geographical data variable
    print(format_string.format(chosen_country = f'{stats[0]}',chosen_un_regions = f'{stats[1]}',chosen_sub_regions = f'{stats[2]}',chosen_square_kms = f'{stats[3]}')) # calls on stats to print each corresponding data information relating to geography
    
def comp_list_maker_geo():
    '''
    Function: starts off as an empty list which is filled with data from Country_Data.csv the first row in the csv file is skipped and all other rows are appended to the empty list, this is the main function which imports the csv file.

    Parameters: 
        none
    Returns
        the previously empty list which is now filled with raw data from the csv file, this data icludes all country names, regions and kms
    '''
    empty_list_geo = [] # creates an empty list that is to be appended with geographical data
    with open('Country_Data.csv') as csvgeodata: # data is imported from csv file
        rows = csv.reader(csvgeodata, delimiter=',') # seperated by ','
        
        first_row = True 
        for row in rows: # skips first row
            if first_row:
                first_row = False
                continue
            empty_list_geo.append(row) # adds all data in Country_Data.csv into the list 
    return empty_list_geo
def score_checker_geo(comp_list_two,user_guess1):
    '''
    Function: checks to see if the users input was correct to the actual raw data in the csv file. This is done by splitting the users guesses based of ',' then the guesses are iterated through and if there is a match between the index of the correct answer in the csv file and the users guess then score is incremented by 1. 
    When a match is not found between the users guess and the corresponding item in the list then no score is added. 

    Parameter: 
        comp_list_two: this parameter is a list of the chosen contries data which contains all of its geographical data present for the certain country in Country_Data.csv, the indices of this list each represent the Un Region, Sub region and Square Kms of the country. These indices are looped through for each split of the users guess inorder to find a match
        user_guess1: this is a list of the users guesses which have been split by ','. Each guess is compared to a seperate index of the actual data and when the guesses match as a string then the value of score is increased

    Returns:
        The function returns the total score of the user after making all guesses
    '''
    user_guess = str(user_guess1) # converts the users geuss into a string
    split_guess = user_guess.split(',') # splits the string based on ',' and creates a list of each element that it is split between
    score = 0 # a way to keep track of users score
    count = 0 # a way to keep incrementing the index of each piece of geographical data
    for guess in split_guess:
        if guess ==str(comp_list_two[count+1]).lower(): # compares users input or guess to each element in a list containing the correct geographical data, ignores casing
            score+=1 # if answers match then score is incremented by 1
            print('Your answer  {} was correct.'.format(guess))
        else: 
            print(f'Your answer  {guess} was incorrect.')
        count += 1 # increments to the next index to compare next guess after each loop iteration
    return score
def lowercase_list_for_comparison(entire_cont_list): # lowercases all strings in the list of countries which is very useful later on
    '''
    Function: This function creates a lower case list of every country, this becomes usefull on in the program for if the user inputs a contry name without capitalizing it, there can still be a matching index.

    Parameters:
        entire_cont_list: this is a list of every country in Country_Data.csv, this list does not include geographical data

    Returns:
        The same list of elements  is returned but this time each element is entirely lowercased
    '''
    contry_list_lower = [] # empty list
    for string in entire_cont_list: # for each string in the list of contries each contry is lowered and appended to the country_list_lower
       lower_cont = string.lower()
       contry_list_lower.append(lower_cont)
    return contry_list_lower

def pop_data_import():
    '''
    Function: functions reads the csv file using the pandas module, the data within the module is seperated by ','. 
    A dataframe is also created for the imported data so that later on this function can be imported so that certain indices can later be called upon.
    Parameters:
        none
    Returns:
        returns the dataframe that has been created which is a callable type of data with searchable indexes which are used later on in the function.
    '''
    pop_data_func = pd.read_csv('Population_Data.csv', sep = ',',skiprows=0) # imports the data using pandas and skips no rows
   
    data_frame = pd.DataFrame(pop_data_func) # creates a dataframe which is very usefull throughout program in order to call such raw data at certain indexes
    

    return data_frame
    
    
    
def input_check(country_input,list_contrys):
    '''
    Function: function essentially has the role to validate the the users input of the country. If the country is valid and inside of the list of countries than and only then will the program continue

    Parameters:
        country_input: the users input choice for a country lowercased
        list_contrys: is the list of contries all lowercased
    Returns:
        function can return True if the user input of country is valid (in list of contries)
        function can return False if the user input of country is not in the list of contries
    '''
    if country_input in list_contrys: # checks to see if the users country input at the begining of program is valid or not
        return True
    else:
        return False



def input_to_data_match(user_cont_list_index,cont_pd):
    '''
    Function: Purpose of this function is to match the index of the chosen contry to the data in the dataframe made in the pop_data_import function. This dataframe is now specified at a certain index to return the matching countries name which is later used in the program but needed to first be matched. 

    Parameter:
        user_cont_list_index: This is the index of the users country in the list of contries it is a numeric value
        cont_pd: cont_pd is the dataframe created with the information of all contries and population data
    Returns:
        function returns the same country name but inside the dataframe of all contries and populations across years
    '''
    return cont_pd.loc[user_cont_list_index][0] # returns the same country name but within the data frame

def year_chosen_pop_list(index_of_chosen_cont,cont_pd):
    '''
    Function: 
        Function creates a list of populations for each year from 2000 to 2020 based off of the country the user inputs

    Parameters:
        index_of_chosen_cont: This parameter is the index in the list of contries of the users inputted contry.
        cont_pd: cont_pd is the dataframe created with the information of all contries and population data
    Returns
        returns list_pop_years which is a list of the population for each year for the users country
    '''
    list_pop_years=[] # creates an empty list which is appeneded with all population data for the specified country
   
    for year in cont_pd.loc[index_of_chosen_cont][1:]: # loops through each year at the index of the country and returns the corresponding population data as an integer and adds to previously empty list
        intyear = int(year)
        list_pop_years.append(intyear)
    
    return list_pop_years
def array_creator_pop(cont_pd):
    '''
    Function: The function creates an array of all the population data in the csvfile for population.This is done by looping through each population in each year of each contry in the csv file then appending the population data to a list, which is then added as a seperate elemtent to an array.

    Parameters: cont_pd is the dataframe created with the information of all conties and population data

    Returns
        returns array_data_pop which is an array consisting of multiple elements each element being a list containing each contries population from 2000 - 2021

    '''
    array_list_years= [] # creates an empty list which is appened with every population data for every country
        
    count_cont =0
    array = np.array([array_list_years]) # an array is created for every population data of each country
       
    while count_cont <= 193: # sets it so that the loop only stops when the final country index is reached 
        _years_list =[]
       
        for year in cont_pd.loc[count_cont][1:]: # for each year the population data is added into a list 
            intyear = int(year)
            _years_list.append(intyear)
        count_cont = count_cont + 1
        array_list_years.append(_years_list) # each list is then added as its own element into an even larger list
    array_data_pop = np.array([array_list_years]) # each list is its own element now in an array type 
               
    return array_data_pop
                

def min_max_mean(array_of_data,index_of_chosen_cont):
    '''
    Function: The role of this function is to calculate the minimum, maximum and mean population for the users imported country and print it out. 

    Parameters:
        array_data_pop: This is the array of every contries population data created in array_creator_pop
        index_of_chosen_cont: This is the index of the country in the list of countries
    Returns:
        the function returns a print statement which includes the maximum, minimum and mean data for the users chosen country
    '''
    max = array_of_data[0][index_of_chosen_cont][:].max() # calculates the highest population during of the users country 
    min = array_of_data[0][index_of_chosen_cont][:].min() # calculates the lowest population during of the users country 
    mean_calc = np.mean(array_of_data[0][index_of_chosen_cont][:]) #calculates the mean population during of the users country 
    mean = int(f'{mean_calc:.0f}') #formats the mean population too zero decimals 
    list_pop_of_country = year_chosen_pop_list(index_of_chosen_cont,pop_data_import()) # calls on a previous function which returns the corresponding population data for the chosen country
    
    index_pop_max= list_pop_of_country.index(max) # finds the index of the max population in the list
    index_pop_min = list_pop_of_country.index(min)# finds the index of the min population in the list
    

    index_year_min = list_of_years()[index_pop_min] # finds the corresponding year to the list of years function
    index_year_max = list_of_years()[index_pop_max] # finds the corresponding year to the list of years function

    return print(f'The lowest population for {input_to_data_match(index_of_chosen_cont,pop_data_import())} was in {index_year_min} with a population of {min} individuals.\nThe highest population {input_to_data_match(index_of_chosen_cont,pop_data_import())} was in {index_year_max} with a population of {max} individuals.\nThe average population from 2000 - 2021 for {input_to_data_match(index_of_chosen_cont,pop_data_import())} was {mean} individuals.') # prints all calculations into a sentence
def list_of_years():
    '''
    Function: function creates a list that is used later on in the program, this list is a list of years from 2000 - 2021, essentially contains every year from 2000  to 2021
    Parameters:
        none
    Returns:
        function returns a list of years from 2000 to 2020
    '''
    list_years = [] # empty list which is then appened with every year from 2000 to 2020
    dummy_year = 1999 # set as 1 year under as it is incremented by 1 so this was done to include the year 2000
    for year in range(21): # range of 21 which gets every year into the list from 2000 to 2020
        dummy_year = dummy_year + 1
        list_years.append(dummy_year)
    return list_years

def change_in_pop(array_of_data, index_of_chosen_cont, inputted_year_one,inputted_year_two):
    '''
    Function: the function calculates the change in population between two years that the user has imputted

    Parameters:
        array_of_data: This is the array of every contries population data created in array_creator_pop
        index_of_chosen_cont: This is the index of the country in the list of countries
        inputted_year_one: the smaller year the user inputs
        inputted_year_two: the seccond year or larger year
    Returns:
        function returns the calculation of the seccond year population - the first year inputted population which is the difference and the change in population
    '''
    index_of_year_one = list_of_years().index(int(inputted_year_one)) # finds the index the chosen year
    index_of_year_two = list_of_years().index(int(inputted_year_two))
    change_in_pop = array_of_data[0][index_of_chosen_cont][index_of_year_two] - array_of_data[0][index_of_chosen_cont][index_of_year_one] # subtracts each population at the respective indices
    return change_in_pop
def pop_density_calc(array_of_data, index_of_chosen_cont,inputed_year,stats):
    '''
    Function: function calculated the population density of the country inputted during a specific year. This funtion does this by dividing the population by the square km of such country.
    Parameters:
        array_of_data: This is the array of every contries population data created in array_creator_pop
        index_of_chosen_cont: This is the index of the country in the list of countries
        inputted_year: is the users input year they are trying to find the density of
        stats: is a list of data containing the users country, un region, sub region and square kms, it is created in an above function and called into this one
    
    Returns:
        function returns a numerical value which is the total population during a certain year / by the sq km of the country which is the density

    '''
    index_of_year = list_of_years().index(int(inputed_year)) # finds the index of the chosen year
    population = int(array_of_data[0][index_of_chosen_cont][index_of_year] ) / int(stats[3]) # finds the density by calling on the list of geographical data at the 3 index which is square kms and by calling on the population at the respective index
    return population
def plot_data_across_years(array_of_data,index_of_chosen_cont,list_contrys):
    '''
    Function: The functions role is to plot the population increase over time for the users inputted country.

    Parameters:
        array_of_data: This is the array of every contries population data created in array_creator_pop
        index_of_chosen_cont: This is the index of the country in the list of countries
        list_contrys: list of all contries
    Returns:
        none
    '''
    years = list(range(2000,2021)) # creates a cariable that can be called into the x axis for plotting
    plt.title(f'Population by Year for {list_contrys[index_of_chosen_cont].capitalize()}') # title
    plt.xlabel('Year') # x axis label
    plt.ylabel('Population') # y axis label
    plt.xticks(years, fontsize = 6) # formats to each element is a tick on x axis and sets the font size of each element
    
    plt.plot(years,array_of_data[0][index_of_chosen_cont][:],'g-', label = 'Population Increase Over Time') # plots the population increase of chosen country through out years with a green line
    plt.legend(shadow =True , loc = 'upper left')
    plt.show()
def import_cont_data_pd():
    '''
    Function: this function creates a data frame which is usable to find and call upon certain indices of the population data. The dataframe consists of every country name and all the data in the Population_Data.csv file.

    Parameters:
        none
    Returns:
        function returns the dataframe created which is all the data presented in the Population_Data.csv file
    '''
    pop_data_func_two = pd.read_csv('Country_Data.csv', sep = ',',skiprows=0) # reads and imports geographical file in a different way
   
    data_frame_two = pd.DataFrame(pop_data_func_two) # creates a dataframe which allows for callable values later on in the program
    

    return data_frame_two
def sub_region_puller(data_frame_two_data,index_their_country):
    '''
    Function: this function compares the sub region of the users country by searching for the index of that country at the sub region and compares it to the every subregion in the dataframe created in the function import_cont_data_pd.
    This is done by looping through and incrementing every index up by 1 which allows for a comparison every countries sub region to the users sub region. If a match is found the loop adds the corresponding country to a new list 
    
    Parameters:
        data_frame_two_data: This is the dataframe of all the data in Country_Data.csv file which consists of every country, un region, sub region and sq km
        index_their_country: This is the index of the country in the list of countries
    Returns
        the function returns a list of every country that has the matching sub region as the users inputted country
    '''
    list_cont= [] # creates an empty list which is appened with each country in the same sub region as the users country
    
        
    count = 0
    
    count = 0
    while count <=193: # ensures all indices are looped through by setting to 193
        for data_frame_two_data.loc[count][2] in data_frame_two_data.loc[:]: # for each country in the entire data set of countries
           if data_frame_two_data.loc[count][2] == data_frame_two_data.loc[index_their_country][2]: # if the sub region of the users country is the same as any contry it is added to the list
               list_cont.append(data_frame_two_data.loc[count][0])
               
        count +=1 # increments to go through entire data set
    list_cont_1 = [] # a new list is defined as duplicates for seen in the previous list
    count_two =0
    for contry in list_cont: #removes dups in list
        if list_cont.index(contry) == count_two:
            list_cont_1.append(contry)
        count_two += 1
        
    
    
    return list_cont_1
def formating_stats_sub_region(array_data_pop_two,list_of_cont_in_sub, input_year_user,multidimensional_list,data_frame_two_data,stats):
    '''
    Function: Formats and calculates the density of every country in the same subregion as the users input and out puts it neatly into a table using right and left allignment methods
    Parameters:
        array_data_pop_two: Which is an array consisting of multiple elements each element being a list containing each contries population from 2000 - 2021
        list_of_cont_in_sub: this is a list of every country in the matching sub region
        input_year_user: is the users input year to compare the densities of 
        multidimension_list: his is a multidimentional list that contains all the data of Country_Data.csv for each country at its own index
        data_frame_two_data: This is the dataframe of all the data in Country_Data.csv file which consists of every country, un region, sub region and sq km
        stats: is a list of data containing the users country, un region, sub region and square kms, it is created in a previous function and called into this one
    
    Returns:
        none

    '''
    format_string_three= '{contry_in_sub:40}{sub_region_of_contry:40}{population_density_of_contry:40}' # sets the title and allignment of title
    print(format_string_three.format(contry_in_sub = 'Country',sub_region_of_contry = 'Sub Region',population_density_of_contry = 'Population Density' ))
    print('-'*100)
    index_of_year = list_of_years().index(int(input_year_user)) # calls on previous function tor return the specific index of the users requested year
    
   
    
    for country in list_of_cont_in_sub: # for each contry in the list of contries with matching sub regions
        index_of_contry = lowercase_list_for_comparison(list_maker_country(multidimensional_list)).index(country.lower()) # finds the index of the country by comparing it to the lower case list of all contries this helps to ignore users input capitalization
        population = array_data_pop_two[0][index_of_contry][index_of_year] # finds the population at each country at the users requested year
        sq_km_of_region = int(stats[3]) # calls on the list of the geographical data to find the square km of the country 
        pop_density = population / sq_km_of_region # preforms the mathimatical operation
        sub_region_contry =  data_frame_two_data.loc[index_of_contry][2] # finds the sub region of each country
        format_string_four= '{contry_sub:40}{sub_of_contry:40}{pop_density_of_cont_in_sub:40}' # formats each country with allignment factors
        print(format_string_four.format(contry_sub = f'{country}',sub_of_contry= f'{sub_region_contry}',pop_density_of_cont_in_sub = f'{pop_density:.2f}')) # prints out the neatly formatted table rounding all density calculations to 2 decimals
        
def sub_region_comparison_quiz(requested_sub_region,data_frame_two_data):
    '''
    Function: This function has the roll of finding all the contries withing the users requested subregion and than adding them to a list with all sub regions lowercased and no duplicates
    Parameters:
        requested_sub_region: This parameter is the users input of the sub region they wish to use
        data_frame_two_data: data_frame_two_data: This is the dataframe of all the data in Country_Data.csv file which consists of every country, un region, sub region and sq km
    Returns
        returns dups_and_lower_contry_in_sub: a list off all contries with matching sub region all lowercased
    '''
    list_cont_for_sub_comparision= [] # empty list is created which is then appended with each contry in the users requested sub region to be tested on
    
    
    
    
    count = 0
    while count <=193:
        for data_frame_two_data.loc[count][2] in data_frame_two_data.loc[:]: # loops through all data in the country data
           if data_frame_two_data.loc[count][2].lower() == requested_sub_region.lower(): # when the subregion of a country  matches the requested subregion then it is added to the list above
               list_cont_for_sub_comparision.append(data_frame_two_data.loc[count][0])
               

               
        count +=1
    list_cont_comparison_sub_dup_removed = [] # a new list is created to help remove duplicates
    
    count_two =0
    for contry in list_cont_for_sub_comparision: #removes dups in list
        if list_cont_for_sub_comparision.index(contry) == count_two: # dups are removed by comparing the index of the first occurance to the index of any occurance if they match then it is added to the dups removed list
            list_cont_comparison_sub_dup_removed.append(contry)
        count_two += 1
    dups_and_lower_contry_in_sub =[] # new list is defined to lower case all countries which helps when comparing later on in the program
    for country_cap in list_cont_comparison_sub_dup_removed:
        country_lower = country_cap.lower()
        dups_and_lower_contry_in_sub.append(country_lower)

    return dups_and_lower_contry_in_sub

def array_endangered_import():
    '''
    Function: This function imports the endangered species csv file and organizes it all into a datatype of an array

    Parameters:
        none
    Returns
        returns an array of all data housed in the endangered species csv file
    '''
    species_data = pd.read_csv('Threatened_Species.csv',sep=',') # imports and reads the threatened species csv file seperating it with ','
    species_data_dataframe = pd.DataFrame(species_data) # creates a dataframe which is extreamely useful later on in the program when calling on data at certain indices
    array_species_data = np.array([species_data_dataframe.loc[:][:]]) # creates an array of all data
    return array_species_data


def country_q_maker(array_of_species_data,list_of_contry_in_req_sub,list_of_contries_all):
    ''' 
    Function: Function essentially creates the base for questions, by randomly selecting country from the list of contries with matching subregions as the users requested sub region. Then assigns values to the endangered species of such chosen country

    Parameters:
        array_of_species_data: is an array of all the data housed in the endangered species csv file
        list_of_country_in_req_sub: is a list of all countries in the same sub region as the users request
        list_of_contries_all: is a list of all contries in the entire csv file Country_Data.csv this was used to help index 
    Returns:
        returns a list of usefull data which is used to format questions and answers, this data contains endangered species of each kind and the countries name
    '''
    length_list = len(list_of_contry_in_req_sub)
    
    random_index_for_in_list_sub = list_of_contry_in_req_sub.index(random.choice(list_of_contry_in_req_sub))
    
    
    country_name = list_of_contry_in_req_sub[random_index_for_in_list_sub].lower()
    real_index_in_file = list_of_contries_all.index(country_name)
    question_for_plants = array_of_species_data[0][real_index_in_file][1]
    
    question_for_fish = array_of_species_data[0][real_index_in_file][2]
    question_for_birds = array_of_species_data[0][real_index_in_file][3]
    question_for_mammals = array_of_species_data[0][real_index_in_file][4]
    
    return [country_name,question_for_plants,question_for_fish,question_for_birds,question_for_mammals]

def list_maker_without_chosen_cont(list_of_cont_subregion,country_name_for_quiz):
    '''
    Function: Function has the roll to make another list without the randomly selected country in order to format the distractor answers in the multiple choice quiz. This is done by picking random contries from the same sub region but these random contries do not have the same number of endangered species as the correct answer

    Parameters:
        country_name_for_quiz: This is the randomly selected country that was selected to generate the question
        list_of_cont_subregion: This is the list of all the contries in the same subregion
    
    Returns:
        function returns a list of  2 fake answers which are placed as distractors in the multiple choice.

    '''
    
    index_of_cont_list_of_cont_in_sub = list_of_cont_subregion.index(country_name_for_quiz)
    new_list_to_remove_chosen_cont = list_of_cont_subregion
    new_list_to_remove_chosen_cont.pop(index_of_cont_list_of_cont_in_sub)
    length_new_list = len(new_list_to_remove_chosen_cont)
    list_of_fake_ans =[]
    for fakeanswer in range(2):
        fake_ans_index = new_list_to_remove_chosen_cont.index(random.choice(new_list_to_remove_chosen_cont))
        fake_ans = new_list_to_remove_chosen_cont[fake_ans_index]
        list_of_fake_ans.append(fake_ans)

    return [list_of_fake_ans[0],list_of_fake_ans[1]]


def answer_checker(user_answer,correct_answer):
    '''
    Function: This function checks the users input to the multiple choice, if the user gets the answer correct then a correct answer statement is printed, if the user gets the answer incorrect then the correct answer and an incorrect answer statement is printed

    Parameters:
        user_answer: this is the users answer inputted to the question
        correct_answer: this is the actual answer to the question
    Returns
        function returns score which is the users score
    '''
    score = 0
    
    if user_answer.lower() == correct_answer.lower():
        print(f'Your answer {user_answer} was correct!!')
        score += 1
    else:
        print(f'Your answer {user_answer} was incorrect')
        print(f'The correct answer is {correct_answer}')
    
    return score


def sub_region_checker(data_frame_two_data): 
    '''
    Function: Function creates a list of subregions which are then checked and compared to in the main program, this is done by iterating through every subregion and adding it to a list then dups are removed and lowercased

    Parameters: 
        data_frame_two_data : data_frame_two_data:  This is the dataframe of all the data in Country_Data.csv file which consists of every country, un region, sub region and sq km
    Returns:
        returns sub_region_list_dups_removed: this is a list of all sub regions
    '''
    sub_region_list=[]
    count = 0 
   
    while count <=193: 
        for data_frame_two_data.loc[count][2] in data_frame_two_data:
            sub_region_list.append(data_frame_two_data.loc[count][2].lower())
        
        count +=1 
    count_two =0
    sub_region_list_dups_removed =[]
    for sub in sub_region_list: #removes dups in list
        if sub_region_list.index(sub) == count_two: # dups are removed by comparing the index of the first occurance to the index of any occurance if they match then it is added to the dups removed list
            sub_region_list_dups_removed.append(sub)
        count_two += 1
    
    return sub_region_list_dups_removed
    


#2
def plot_endangered(list_of_cont_in_sub,multidimensional_list,data_frame_two_data, species_data_array):
    '''
    Function: This function essentially plots the total number of endangered species in each country of the same subregion the user has chosen

    Parameters: 
        list_of_cont_in_sub: this is a list of every country in the matching sub region
        multidimension_list: his is a multidimentional list that contains all the data of Country_Data.csv for each country at its own index
        data_frame_two_data: This is the dataframe of all the data in Country_Data.csv file which consists of every country, un region, sub region and sq km
        species_data_array: This is the array of data of every species that is endangered in every country , this parameter is called on at specific indices in order to add to achieve total number of species endangered
    Returns:
        none
    '''
    dictionary = {}
    
    for country in list_of_cont_in_sub:
        index_of_contry = lowercase_list_for_comparison(list_maker_country(multidimensional_list)).index(country.lower()) 
        dictionary[country] = species_data_array[0][index_of_contry][1] + species_data_array[0][index_of_contry][2] +species_data_array[0][index_of_contry][3]+species_data_array[0][index_of_contry][4] # adds the endangered data per species for a country together to get total endangered species
   
    countries = list(dictionary.keys()) # all contries in sub region
  
    total_endangered = list(dictionary.values()) # total endangered in the sub region
    plt.bar(countries, total_endangered, color = 'red', label = 'Total number of endangered species')
    plt.xlabel("Contries in Sub region")
    plt.ylabel('Number of total endangered species')
    plt.xticks(countries,)
    plt.legend(shadow =True , loc = 'upper left')
    plt.title(f'Comparison of total endangered species in {data_frame_two_data.loc[index_of_contry][2]}')
    plt.show()
    

    
   

    

 


   

 
 
def main():
    '''
    Function: Main function all code is called into this function
    Parameters: 
        none
    Returns :
        none
    '''
   
    print()
    print('*' *24,'Welcome to the program presented by Hamd and Mohammed','*'*24)
    multi_list = comp_list_maker_geo() # makes list multidimensional list of all geo data
    
    
    list_country = (lowercase_list_for_comparison(list_maker_country(multi_list))) # calls on function to create of all contries in lower case
    

    main_loop_var = 0 # sets a variable that allows entire main program to loop
    while main_loop_var == 0:
        
                
            
        
            
        print()
        user_choice_1 = input(f'Please enter what game you would like to do next\n1:Geograpical Trivia\n2:Population Fun Facts\n3:Endangered Species Quiz\n') # asks user for next choice in program
        
        
        if user_choice_1 == '1': # if user chooses geographical option then geographical trivia is played
            input_loop_check_var = 0
            while input_loop_check_var == 0: # loop that validates users input country
                user_country_input = input('Please enter a country name to continue: ').lower()
                if input_check(user_country_input,list_country) == True:
                    input_loop_check_var +=10
                
                else:
                    print('You have not provided a valid country please re-enter:')
                    input_loop_check_var = 0
            index_country = list_country.index(user_country_input) # finds the index of the country
            chosen_count_list = multi_list[index_country] # finds the corresponding list of geographical data by using the index of the contry in the list of contries 
            print("You must take a guess in 4 categories:\n\nUn region selected country belongs to\nSub Region country belongs to\nSquare KM of such country") 
            print()
            user_guess = input('Please enter your guesses seperated by a \',\' ').lower() # tells user to input guesses
            print()
            print('You accumulated a score of {}'.format(score_checker_geo(chosen_count_list,user_guess))) # checks answers and validates them and returns total score
            print()
            print('The correct answers are')
            print()
            formating_stats(choice_geo(multi_list,index_country)) # calls on geo funct to which finds all stats of chosen country in a neat tabel
            print()
            user_continue_game_choice = input('Would you like to continue with the program?: (Yes/No) ').lower() # ends or continues loop depending on user choice
            if user_continue_game_choice == 'yes':
                main_loop_var = 0
            elif user_continue_game_choice == 'no':
                print('Thanks for playing!!')
                main_loop_var += 10
            else:
                print('A valid response was not provided:')
            
                    
        elif user_choice_1 == '2': # if user chooses to learn fun facts in terms of population
            input_loop_check_var_two = 0
            while input_loop_check_var_two == 0: # validates users country input
                user_country_input = input('Please enter a country name to continue: ').lower()
                if input_check(user_country_input,list_country) == True:
                    input_loop_check_var_two +=10
                
                else:
                    print('You have not provided a valid country please re-enter:')
                    input_loop_check_var_two = 0
            index_country = list_country.index(user_country_input) 
            loop_var_two = 0
            while loop_var_two == 0: # validates if user enters yes or no
                user_choice_pop = input('Would you like to know the max, min and mean values in terms of population for your country; (Yes/No) ')
                if user_choice_pop.lower() == 'yes':
                    
                    print()
                    print('Making the calculations.......')
                    print()
                    min_max_mean(array_creator_pop(pop_data_import()),index_country) # calls on the min max mean function with the array of population data and the index of the users contry and prints out corressponding data
                    print()
                    loop_var_two += 10
                elif user_choice_pop.lower() != 'yes' and  user_choice_pop.lower() != 'no':
                    print('You have not provided a valid response')
                elif user_choice_pop.lower() == 'no':
                    loop_var_two += 10
            while loop_var_two == 10: # loop for validation of input
                user_choice_stat_pop = input('Would you like to view a graph of statistical data in terms of population for your country?: (Yes/No) ') # asks user if they would like to see a plot of the population increase over time for said country
                if user_choice_stat_pop.lower() =='yes':
                    print()
                    #plot_data_across_years(array_creator_pop(pop_data_import()),index_country,list_country) # calls to plot such data
                    print('Your plot will be displayed at the ending of the program.')
                    print()
                    loop_var_two += 10
                elif user_choice_stat_pop.lower() == 'no':
                    loop_var_two += 10
                else:
                    print('You have no provided a valid respnse please re-enter')

            while loop_var_two == 20: # loop for validation
                user_choice_max_pop_cont = input('Would you like to know the change in population between years?: (Yes/No) ') # user next fun fact change in population
                if user_choice_max_pop_cont.lower() == 'yes':
                    print()
                    year_choice_number_one = int(input('Please type the first year starting from the smaller year from 2000 - 2020: ')) # asks for the first year
                    year_choice_number_two = int(input(f'Please type the seccond year inbetween {year_choice_number_one} - 2020: ')) # asks for the next year
                    print()
                    print('Making the calculations.......')
                    print()
                    loop_var_two += 10
                    print(f'The change in population from {year_choice_number_one} to {year_choice_number_two} was {change_in_pop(array_creator_pop(pop_data_import()), index_country, year_choice_number_one,year_choice_number_two)}') # calls on the change in pop function to return the corresponding values
                    print()
                elif user_choice_max_pop_cont.lower() == 'no':
                    loop_var_two += 10
                else: 
                    print('A valid response was not provided')
            while loop_var_two == 30: # loop for input validation
                user_choice_density = input('Would you like to know population density during a specific year for your country?: (Yes/No) ')
                if user_choice_density.lower() == 'yes':
                    print()
                    year_input = int(input('What year in between 2000 - 2021 would you like to know the population density of?: ')) # asks user what year density they would like to know
                    print()
                    print('Making the calculations.......')
                    print()
                    print(f'The population density in {year_input} for your chosen country was {pop_density_calc(array_creator_pop(pop_data_import()),index_country,year_input, choice_geo(multi_list,index_country)):.2f} individuals per square km.') #calls on density calculator function 
                    print()
                    loop_var_two += 10
                elif user_choice_density.lower() == 'no':
                    loop_var_two += 10
                else:
                    print('You have not provided a valid response')
                user_density_comp_choice = input('Would you like to see a comparison of population density of different contries in your subregion?: (Yes/No) ') # asks users if they would like to compare population densities in different sub regions

                if user_density_comp_choice.lower() == 'yes':
                    print()
                    year_choice_user = int(input('Please enter a year in between 2000 - 2021: ')) # user enters a year for selection
                    print()
                    print('Making the calculations.......')
                    print()
                    formating_stats_sub_region(array_creator_pop(pop_data_import()),sub_region_puller(import_cont_data_pd(),index_country),year_choice_user,multi_list,import_cont_data_pd(),choice_geo(multi_list,index_country)) # calls on formating function and multiple other functions to print out a neat tabel of all countrues with same sub region and prints out their sub region and population densities
                elif user_density_comp_choice.lower() == 'no':
                    loop_var_two+=10
                else:
                    print('You have not provided a valid response')
           
            user_choice_continue = input('Would you like to continue the program?: (Yes/No) ').lower() # asks if main program loop should terminate or continue
            if user_choice_continue.lower() == 'yes':
                main_loop_var = 0
                if user_choice_stat_pop.lower() =='yes':
                    plot_data_across_years(array_creator_pop(pop_data_import()),index_country,list_country)
            elif user_choice_continue.lower() == 'no':
                main_loop_var += 10
                print('Thank you for playing!!!')
                if user_choice_stat_pop.lower() =='yes':
                    plot_data_across_years(array_creator_pop(pop_data_import()),index_country,list_country)
            else: 
                print('You have not provided a valid response and are being redirected:')
                main_loop_var = 0

            
        elif user_choice_1 =='3': # if user chooses to play the endangered species quiz
            loop_var_quiz = 1
            print('Welcome to the endangered species quiz!')
            while loop_var_quiz<=3: # number of questions user can play
                loop_var_validate = 0
                while loop_var_validate == 0:
                    
                    req_sub = input('Enter a subregion to be tested on: ') # enters a new sub region for each question
                    list_of_sub_regionns = sub_region_checker(import_cont_data_pd())
                    if req_sub.lower() in list_of_sub_regionns:
                        print()
                        print(f'Question {loop_var_quiz}:') # prints question number
                        function_list_ans = country_q_maker(array_endangered_import(),sub_region_comparison_quiz(req_sub,import_cont_data_pd()),list_country) # calls on function which allows us to create questions based off the function returning a list of valuable information
           

                        print(f'What country has {function_list_ans[1]} endangered plants, {function_list_ans[2]} endangered fish, {function_list_ans[3]} endangered birds, {function_list_ans[4]} endangered mammals.') # formats the question
                        print(f'1.{function_list_ans[0]}\n2.{list_maker_without_chosen_cont(sub_region_comparison_quiz(req_sub,import_cont_data_pd()),country_q_maker(array_endangered_import(),sub_region_comparison_quiz(req_sub,import_cont_data_pd()),list_country)[0])[0]}\n3.{list_maker_without_chosen_cont(sub_region_comparison_quiz(req_sub,import_cont_data_pd()),country_q_maker(array_endangered_import(),sub_region_comparison_quiz(req_sub,import_cont_data_pd()),list_country)[0])[1]}')# prints the correct answer and a bunch of incorrect random answers of contries
                        print()
                        user_answer_to_quiz = input('Please enter the name of the country as your guess:')
                        print()
                        answer_checker(user_answer_to_quiz,function_list_ans[0]) # checks the users input by calling on answer checker function
                        loop_var_quiz +=1
                        loop_var_validate+= 1
                    else:
                        print('You have not provided a valid response')
            user_endangered_bar = input('You made it this far, would you like to see a visual comparison of total endangered species in contries of the same sub region?: (Yes/No) ')
            bar_plot_loop_var = 0
            while bar_plot_loop_var ==0:
                if user_endangered_bar.lower() == 'yes':
                    print()
                    input_checking_var = 0
                    while input_checking_var ==0:
                        user_country_choice = input('Please enter a country: ')
                        if input_check(user_country_choice,list_country):
                            index_country_one = list_country.index(user_country_choice)
                            plot_endangered(sub_region_puller(import_cont_data_pd(),index_country_one),multi_list,import_cont_data_pd(), array_endangered_import())
                            bar_plot_loop_var += 10
                        else:
                            print('A valid response was not provided')
                elif user_endangered_bar == 'no':
                    print()
                    print('Thank you for playing!!')
                    bar_plot_loop_var+= 10

                else:
                    print('A valid response was not recieved.')

            user_choice_to_continue_or_not = input('Would you like to continue the program?: (Yes/No)') # asks user to input a if they would like to continue or not
            if user_choice_to_continue_or_not.lower() == 'yes':
                main_loop_var = 0
            elif user_choice_to_continue_or_not.lower() =='no':
                main_loop_var += 10
                plot_data_across_years(array_creator_pop(pop_data_import()),index_country)
                print('Thank you for playing!!!')
            else: 
                print('You have not provided a valid response and are being redirected:')
                main_loop_var = 0
       

        elif user_choice_1 != 1 or user_choice_1 != 2 or user_choice_1 != 3: # if user does not input a valid choice on what game to play
            print('You have not provided a valid option for what to do and are being redirected')
            main_looop_var = 0
      
if __name__ == '__main__':
     main()




   