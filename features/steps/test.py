from behave import *

use_step_matcher("re")


@given("Fail successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Fail successfully')

@given("another step")
def step_impl(ctx):
    print("lorem ipsum")