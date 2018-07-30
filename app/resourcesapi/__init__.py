from flask import Blueprint
from flask_restplus  import Api,Resource
from app.resourcesapi.Person_resource import PersonRes,SinglePersonRes
from app.resourcesapi.ExpType_resource import ExpTypeRes,SingleExpTypeRes
from app.resourcesapi.InvestType_resource import InvestTypeRes,SingleInvestTypeRes
from app.resourcesapi.Add_Expense_resource import ExpenseRes,SingleExpenseRes
api_bp = Blueprint('apiV2', __name__)
api = Api(api_bp)

# Route

api.add_resource(PersonRes, '/PersonRes')
api.add_resource(SinglePersonRes, '/SinglePerRes/<int:idx>')
api.add_resource(ExpTypeRes,'/ExptypeRes')
api.add_resource(SingleExpTypeRes,'/SingleExptypeRes/<int:idx>')
api.add_resource(InvestTypeRes,'/InvestTypeRes')
api.add_resource(SingleInvestTypeRes,'/SingleInvestTypeRes/<int:idx>')
api.add_resource(ExpenseRes,'/ExpenseRes')
api.add_resource(SingleExpenseRes,'/SingleExpenseRes/<int:idx>')