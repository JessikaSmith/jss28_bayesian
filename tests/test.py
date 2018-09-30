from jss28_bayesian.variable_selection import Model
from jss28_bayesian.regression import RegressionModel
from jss28_bayesian.visualization import *

reg_model = RegressionModel(shape=(100, 30))
print(reg_model.datax)
var_selection_model = Model()
trace_len = 50000
var_selection_model.createModel(reg_model.datax, reg_model.datay, trace_len=trace_len)
#print(var_selection_model.trace)
# print(var_selection_model.trace)
#plot_params(trace_len, var_selection_model.trace['alpha'], var_selection_model.trace['e'][-1])
#plot_trace(var_selection_model.trace['alpha'], var_selection_model.trace['theta'][-1])
