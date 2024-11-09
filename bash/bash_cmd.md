#### Usefuell bash cmds for working with ETL/ELT pipelines

extract the first four characters.
```bash
echo "database" | cut -c1-4
```

We can extract a specific column/field from a delimited text file, by mentioning the delimiter using the -d option, or the field number using the -f option.
```bash
cut -d":" -f1 /etc/passwd
```

extract multiple fields 1st, 3rd, and 6th
```bash
cut -d":" -f1,3,6 /etc/passwd
```

extract a range of fields 3rd to 6th
```bash
cut -d":" -f3-6 /etc/passwd
```

translate all lower case alphabets to upper case.
```bash
echo "Shell Scripting" | tr "[a-z]" "[A-Z]"
```

You could also use the pre-defined character sets also for this purpose:
```bash
echo "Shell Scripting" | tr "[:lower:]" "[:upper:]"
```

translate all upper case alphabets to lower case.
```bash
echo "Shell Scripting" | tr  "[A-Z]" "[a-z]"
```

replace repeat occurrences of ‘space’ in the output of ps command with one ‘space’.
```bash
ps | tr -s " "
```

delete all digits.
```bash
echo "My login pin is 5634" | tr -d "[:digit:]"
```

Transform phase

read the extracted data and replace the colons with commas (for csv)
```bash
tr ":" "," < extracted-data.txt  > transformed-data.csv
```