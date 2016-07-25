#
# BusinessModel.py
#
# sets up a class (or classes) to calculate how well a business
# will succeed based on analytics (i.e. viriality coefficient,
# cohort analysis, etc.)
# 
# Insight Remote Group, July 2016
#
# imports
import numpy as np
#
# set up class structure
class Probability(object):
    # define random probability  
    def __init__(self):
        #
        # assign a probality to this class
        self.prob= np.random.rand(1)[0]
        
class BusinessModel(object):
#
# this class contains the business model
#
# inputs
# initialCusts = a starting base of customers
# churn = number of customers lost each cycle
# viral = number of customers gained per invite rate each cycle
# happiness = 0 to 1 scale of overall customer satisfication 
#
# Class self's 
# noCusts = the number of customers 

#
  def calculateNewCusts(self,viral,churn,invites):
      #
      # determine the number of invites based on the viral coefficient
      #
      # inputs:
      # viral = number of accepted invites/number of invites issued
      # churn = customer loss/ customer total
      # invites = number of invites person
      #
      newCusts=viral*self.noCusts*invites
      lossCusts=churn*self.noCusts
      self.noCusts=int(newCusts-lossCusts)
      
      
  def __init__(self, Probability, initialCusts, churn, viral,
               invites=5, cycles=10):
  #
  # churn = churn rate (customer loss/customer total)
  # viral = number of accepted invites/number of invites issued
  # Probability = class structure that determines random probability
  # invites = a set number of invites per person, can be modified
  #
  # these are expected inputs into our class structure
  # so we set them as class objects, which can easily be
  # accessed by all the functions we build
  #
    self.noCusts=initialCusts
    for icycle in range(cycles):
       # call the function calculateNewCusts withing the class
       # this updates noCusts
       self.calculateNewCusts(viral,churn,invites)
       invites=int(Probability.prob*100.0)
    print(self.noCusts) 

BusinessModel(Probability(), 10, .03, .03)

