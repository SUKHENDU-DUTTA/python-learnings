import pywhatkit as kit

txt = """A SQL database table: SQL databases are designed to store structured data with a well-defined schema, 
where each row represents a record and each column represents a field or attribute of that record."""
kit.text_to_handwriting(txt)
print("End")
