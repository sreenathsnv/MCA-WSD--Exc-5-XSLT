import xmlschema as xml


XML_SCHEMA = xml.XMLSchema("Lab_Exe5\employee_schema.xsd")

if XML_SCHEMA.is_valid("Lab_Exe5\employee.xml"):
    print("The xml is vaild")
else:
    print("Sorry, xml is not well formed or valid")
