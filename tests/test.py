from jss28_bayesian.variable_selection import Model
from jss28_bayesian.regression import RegressionModel

reg_model = RegressionModel(shape=(100, 30))
print(reg_model.datax)
var_selection_model = Model()
var_selection_model.createModel(reg_model.datax)
print(var_selection_model.trace)