# design a feature flag system for an application
# list of features
# part 2: 

# let's say we're doing an A/B test, so we need to make sure that half of all users get experience A while the other half gets experience B.

#check if A/B cookie/session object doesn't exist
#   if isEven(userId):



class FEATURE_CONSTANTS:
    COOL_SEARCH = 'COOL_SEARCH'
    THRESHOLDS = {
        COOL_SEARCH: 500
    }

def getThreshhold(feature):
    return FEATURE_CONSTANTS.THRESHOLDS[feature]


class User:
    def __init__(self, userId):
        self.userId = userId

#Should we display the link / enable the feature?
# if isEven(user.userId) and user.hasFeature(FEATURE_CONSTANTS.SOME_NEW_FEATURE):
#    showFeature()

# This assumes user IDs are numeric and evenly distributed
def hasFeatureEven(feature, user):
    return isEven(user.userId)

# assume ID is not numeric or in some predictable pattern
import random
# random.random() -> a float between 0.00000 and .99999
# threshold



# O(1)
def hasFeatureRandom(feature, user):
    return random() < getThreshhold(FEATURE_CONSTANTS.SOME_NEW_FEATURE)

# part 2: this implementation can lead to an inconsistent experience for your users
# they will potentially see something different every time they log in or visit a particular feature.
# without increasing complexity, solve this issue.
# keep this evaluation server-side

def hasFeatureEncode(feature, user):
    roll = abs(hash(user)) % (10 ** 3)
    print(roll)
    print(getThreshhold(feature))
    return roll > getThreshhold(feature)
    #return abs(hash(user)) % (10 ** 8) < getThreshhold(feature)

def main():
    user = User('tralf')
    print(user.userId)
    print(hasFeatureEncode(FEATURE_CONSTANTS.COOL_SEARCH, user))
    return

if __name__ == "__main__":
    main()
