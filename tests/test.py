from jss28_bayesian.variable_selection import Model
from jss28_bayesian.regression import RegressionModel
from jss28_bayesian.visualization import *

reg_model = RegressionModel(shape=(100, 30))
print(reg_model.datax)
var_selection_model = Model()
var_selection_model.createModel(reg_model.datax, reg_model.datay)
#print(var_selection_model.trace)
plot_params(5000, var_selection_model.trace[0][5000:, None], var_selection_model.trace[1][5000:, None])