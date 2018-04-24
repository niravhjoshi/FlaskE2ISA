from flask_table import Table,Col,LinkCol

class PersonResults(Table):
    id = Col("PersonID")
    u_id = Col("UserID")
    per_name = Col("Person Name")
    per_sex = Col("Sex")
    per_bdate = Col("BirthDate")
    per_cdate = Col("CreatedDate")