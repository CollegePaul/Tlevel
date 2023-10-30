'''
This is the maths T Level library
'''

class MathTL():
    '''The MathTL libray developed by T level students
       This will provide a range of commonly used algorithems
       and helper utilities for computer science
    '''

    @staticmethod
    def add(n1:float,n2:float) -> float:
        '''
        This is a demonstration method only, adding 2 numbers
        Behaviour for other datatypes is not implimented

        Parameters
        ----------
        n1 : float
            The first addend
        n2: float
            The second addend

        Returns
        -------
        float
            The Sum of the addends
        '''

        try:
            n1 = float(n1)
        except ValueError:
            n1 = 0
       
        return n1 + n2

    @staticmethod
    def sub(n1:float,n2:float) -> float:
        '''
        This is a demonstration method only, subtracting 2 numbers
        Behaviour for other datatypes is not implimented
        Submitted by Paul Smith

        Parameters
        ----------
        n1 : float
            The minuend
        n2: float
            The subtrahend

        Returns
        -------
        float
            The Sum of the addends
        '''

        try:
            n1 = float(n1)
        except ValueError:
            n1 = 0

        return n1 - n2
    


  
