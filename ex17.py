# Create a mapping of state to abbreviation
# Add Oklahoma and Texas to the end of the list of States.
states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI',
          'Oklahoma': 'OK',
          'Texas': 'TX'}
cities = {'CA': 'San Francisco',
          'MI': 'Detroit', 
          'FL': 'Jacksonville',
          'OK': 'Oklahoma City',
          'TX': 'Austin',
          'OR': 'Portland',
          'NY': 'New York City'}
#add the rest of the cities here including Oklahoma and Texas

cities ['NY'] = 'New York City'
cities ['OR'] = 'Portland'
cities ['CA'] = 'San Francisco'
cities ['MI'] = 'Detroit'
cities ['TX'] = 'Austin'
cities ['OK'] = 'Oklahoma City'
cities ['FL'] = 'Jacksonville'

# Print out all the cities
print ('-' * 20)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])
print ("OK State has: ", cities['OK'])
print ("CA State has: ", cities['CA'])
print ("TX State has: ", cities['TX'])
print ("FL State has: ", cities['FL'])
print ("MI State has: ", cities['MI'])

# Print out all the states
print ('-' * 20)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("New Yorks's abbreviation is: ", states['New York'])
print ("Texas's abbreviation is: ", states['Texas'])
print ("Oklahoma's abbreviation is: ", states['Oklahoma'])
print ("Oregon's abbreviation is: ", states['Oregon'])
print ("California's abbreviation is: ", states['California'])
print ("Florida's abbreviation is: ", states['Florida'])
print ('-' * 20)

