#!/bin/bash

# Download the content from the URL and save it to a temporary file
curl -s https://www.amfiindia.com/spages/NAVAll.txt > temp.txt

# Extract Scheme Name and Asset Value fields and save them in a TSV file
awk -F ';' '{ print $4 "\t" $5 }' temp.txt > Scheme_AssetValue.tsv

# Clean up: Remove the temporary file
rm temp.txt

# Display a message
echo "Scheme Name and Asset Value extracted and saved in Scheme_AssetValue.tsv"
