from numpy.testing import assert_allclose
exp = 2
obs = 2.01
err = 0.5
assert_allclose(obs,exp, atol=err)
print "within tolerance"
