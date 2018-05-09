from flask_table import Table,Col,LinkCol

class PersonResults(Table):
    id = Col("PersonID", column_html_attrs={'class': '.table'})
    u_id = Col("UserID",column_html_attrs={'class': '.table'})
    per_name = Col("Person Name",column_html_attrs={'class': '.table'})
    per_sex = Col("Sex",column_html_attrs={'class': '.table'})
    per_bdate = Col("BirthDate",column_html_attrs={'class': '.table'})
    per_cdate = Col("CreatedDate",column_html_attrs={'class': '.table'})