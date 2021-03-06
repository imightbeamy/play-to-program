'''
 Represents a generic list combinator.
 
 Contains an abstract class and several child classes which use various
 methods to determine a single value representing all elements in a given
 list. Refer to individual child classes for more detailed explanations.
'''

class ProbMap:
    ''' Abstract parent class.
    
    NOTE: DO NOT IMPLEMENT THIS CLASS! ONLY USE ONE OF ITS CHILD CLASSES.
    '''
    def process(self, li):
        return 0


class MultMap(ProbMap):
    ''' Multiplier probability mapper (Bayesian).
    
    Combines probabilities by computing a product across all probabilities.
    '''
    
    def process(self, li):
        result = 1.0
        for i in li:
            result *= li.get(i)
            #print result
        return result
        
        
class MinMap(ProbMap):
    ''' Returns the smallest (numerically) number in the list
    
    Returns the smallest possibility
    '''
    
    def process(self, li):
    
        if len(li.keys())==0:
            return 1.0
        result = 1.0
        for i in li:
            if li.get(i) < result:
                result = li.get(i)
        return result


class MeanMap(ProbMap):
    ''' Uses the mean/average to ascertain probability
    
    Calculates the simple arithmetic mean of the list values.
    '''
    
    def process(self, li):
        
        if len(li.keys())==0:
            return 1.0
        result = 0.0
        for i in li:
            result += li.get(i)
        return result/len(li.keys())
        
        
#unit testing
def main():
    li = {'IA': .1, 'IB': .2, 'IC':.3}
    print MultMap().process(li)
    print MinMap().process(li)
    print MeanMap().process(li)
    
if __name__ == "__main__":
    main()
