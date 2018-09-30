from jss28_bayesian.variable_selection import Model
from jss28_bayesian.regression import RegressionModel
from jss28_bayesian.visualization import *

reg_model = RegressionModel(shape=(100, 30))
print(reg_model.datax)
var_selection_model = Model()
trace_len = 200
var_selection_model.createModel(reg_model.datax, reg_model.datay, trace_len=trace_len)
#print(var_selection_model.trace)
plot_params(trace_len, var_selection_model.trace[0][trace_len:, None], var_selection_model.trace[1][trace_len:, None])