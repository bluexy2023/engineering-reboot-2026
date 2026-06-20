</Markdown>

# Day 15 Notes

# Concepts Learned
- Collection of dictionaries processing
- Creation of a list from a collection for summary
  and aggregation
- Creation of key-value(dictionary) to summarize
  data within a collection of dictionaries
- Traversing a collection and conditional counting
# Key Commands
- print
- for loop
- if, else
- use of append() in list
# Key Observations
- dictionaries can be created at runtime 
  by using the variable[varibale] assignment
# Lessons Learned
## What is a dictionary?
- similar to a hash table
- allows for creation of objects with attributes
- uses the {} convention for its contents
- access to attribute thru dictionary_var["attib name"]
## How do lists and dictionaries work together?
- used as a collection of dictionaries
- an array of hash tables
- traversed as an array element individual dictionaries
## How are structured records represented?
- structured records are represented exactly as a series of similar objects, an array of hash tables, or in python terms, a list of dictionaries
## How can collections of records be traversed?
- collection records can be traversed similar to how you do a list of values, but values are of type dictionaries, which could be analyzed in more detail through their attributes. for python, use a for loop or use incremting indeces to access individual records
## How can statistical information be extracted from collections?
- can be extracted by going through attributes of each item from the collection by traversal.  then, use temporary placeholders to isolate information being analyzed, then use aggregation on the newly created temporary variable
## How can aggregation techniques be applied to structured data?
- aggegation can be applied to structured data or distilled information from a collection, similar to what I described above
## How are category counts calculated?
- category counts can be implemented in multiple ways, but using a hash table and check if category already exists in the dictionary, increment if it does, assign 1 if it is a new entry is an efficient algorithm to apply to approaching similar problems.
## Where do data-analysis techniques appear in real-world software systems?
- banking, finance, retail, contruction -- anything that requires statistical data
# Questions For Future Study
- none