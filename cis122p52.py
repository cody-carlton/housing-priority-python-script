'''
Title: Project 5-2 – Housing Priority project
Author: Cody Carlton
Credits: Based on project by prof. Evan Peck, Bucknell University
Description: Collect user attributes and calculate a housing priority score
based on this input.
'''
def is_housing_eligible(year):
    '''
    function to determine if student is eligible for student housing
    depending on year and returns boolean to housing_main function

    >>> is_housing_eligible(3)
    returns true
    '''
    if year < 4:
        return True 

    elif year >= 4:
        year = input('are you close to finishing? (y or n)?')

    if year == 'y': # if student answers 'y' returns false and prints "you are no longer eligible for student housing'
        return False

    else:
        return True
    
def collect_info():
    '''
    function that asks user to input a collection of data and returns intergers or
    boolean values to housing priority function in order to calculate score

    >>> collect_info()
    'what year are you?'
    'are you currently on full-time, off-campus program credit?'
    'are you currently on academic probation?'
    'are you currently on academic suspension'?
    'were you on disciplinary probation at any point during the academic year?'
    '''
    year = int(input('please re-enter your year'))
    age = int(input('how old are you'))
    off_campus = input('are you currently on full-time, off-campus program credit? (y or n)?')
    
    if off_campus == 'y': # if statement that changes string into boolean value 
        off_campus = True 
    else:
        off_campus = False
        
    acad_prob = input('are you currently on academic probation? (y or n)?')
    if acad_prob == 'y':
        acad_prob = True
    else:
        acad_prob = False
        
    acad_suspend = input('are you currently on academic suspension? (y or n)')
    if acad_suspend == 'y':
        acad_suspend = True
    else:
        acad_suspend = False
        
    disc_prob = input('were you on disciplinary probation at any point during the academic year? (y or n)?')
    if disc_prob == 'y':
        disc_prob = True
    else:
        disc_prob = False
        
    return year, age, off_campus, acad_suspend, acad_prob, disc_prob # returns info to housing priority funciton

def housing_priority(year, age, off_campus, acad_suspend, acad_prob, disc_prob):
    '''
    fucntion that uses information from function: collect_info to determine score based on
    users input

    >>>housing_priority
    [takes parameters from collect info and returns integer score to report_priority]
    '''
    score = 0 # score adds up each local variable and assigns it a value
    if year == 1:
        score = score + 1
        
    if year == 2:
        score = score + 2
        
    if year == 3:
        score = score + 3
        
    if year == 4:
        score = score + 4
        
    if age >= 23:
        score = score + 1
        
    if off_campus == True:
        score = score + 1
        
    if acad_prob == True:
        score = score - 1
        
    if acad_suspend == True:
        score = score - 2
        
    if disc_prob == True:
        score = score - 3

    return score #returns total score to report_priority function

def report_priority(score):
    '''
    funciton that prints score from housing_priority function

    >>>report_priority
    you have 4 housing points
    '''
    print('you have', score, 'housing points') 
    

def housing_main():
    '''
    driver for housing priority program
    '''

    # set up
    print('Welcome to the U Housing Information Center.')
    print('Please respond to the following questions: ')
    print()

    # determine eligibility for housing
    year = int(input('What year are you? (1 for 1st year, 2 for 2nd, etc.): '))
    
    housing_eligible = is_housing_eligible(year)

    if housing_eligible:
        year, age, off_campus, acad_suspend, acad_prob, disc_prob = collect_info()
        priority = housing_priority(year, age, off_campus, acad_suspend, acad_prob, disc_prob)

        report_priority(priority)
        
    else:
        print('You are no longer eligible for student housing.')

    return

housing_main()
