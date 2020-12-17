education_dictionary = {} # Make an empty dictionary
education_dictionary['Bachelors'] = education_dictionary.get('Bachelors', 0) + 1 # Use get to manage if there is no value corresponding to the key 'Bachelors'.  In such a case, set it to 1
print(education_dictionary)
education_dictionary['Bachelors'] = education_dictionary.get('Bachelors', 0) + 1 # This should update 'Bachelors' to 2
print(education_dictionary)