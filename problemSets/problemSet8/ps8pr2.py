#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        
        return new_date

#### Put your code for problem 2 below. ####

    def advance_one(self):
        """advances the date by one day"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[2] = 29
        if self.day == days_in_month[self.month]:
            if self.month==12:
                self.year+=1
                self.month=1
            else:
                self.month+=1
            self.day =1
        else:
            self.day+=1
            
    def advance_n(self,n):
        """advances the date by n days by using the advance one method multiple times"""
        print(self)
        for i in range(n):
            self.advance_one()
            print(self)
            
    def __eq__(self, other):
        """overides the normal eq method and returns true if the day month and year are the same
        for two dates"""
        if self.month == other.month:
            if self.day == other.day:
                if self.year ==other.year:
                    return True
        return False
    
    def is_before(self, other):
        """checks to see if the self date is before other
        if it is, returns true, else returns false"""
        if self.year > other.year:
            return False
        if self.year == other.year:
            if self.month > other.month:
                return False
        if self.year == other.year:
            if self.month == other.month:
                if self.day >= other.day:
                    return False
        return True
    
    def is_after(self, other):
        """checks to see if the self date is after other
        returns true if it is, else returns false"""
        if self.is_before(other) == False:
            if self != other:
                return True
        return False
    
    def days_between(self, other):
        """checks to see how many days are between the self day and other"""
        new_self = self.copy()
        new_other = other.copy()
        count=0
        if self.is_before(other):
            while(True):
                if new_self == new_other:
                    break
                count-=1
                new_self.advance_one()
        elif self.is_after(other):
            while(True):
                if new_self==new_other:
                    break
                count+=1
                new_other.advance_one()

        return count
    
    
    def day_name(self):
            """checks on what day of the week, the date lies on using a reference date"""
            ref = Date(11, 11, 2019)
            day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
            days = self.days_between(ref)
            self_day = day_names[days%7]
            return self_day